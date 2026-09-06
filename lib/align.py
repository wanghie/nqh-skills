#!/usr/bin/env python3
"""Syllable-nuclei alignment - word timings from audio + plain text.

Why this exists: not every ASR gives word timestamps (sherpa-onnx Whisper,
most cloud APIs' cheap tiers, and any transcript a human typed by hand give
you text only). This recovers timing from the audio itself.

It works especially well for Vietnamese. Vietnamese is monosyllabic and
syllable-timed: every syllable carries a vowel nucleus with a clear energy
peak, and syllables occupy roughly equal time. So peaks in the smoothed
energy envelope map almost one-to-one onto syllables, and syllables map
one-to-one onto words. English is stress-timed and this is rougher there -
treat it as a fallback, not a replacement for real word timestamps.

Usage:
  python3 align.py audio.wav --text "..." -o transcript.json [--audience vi]
"""
from __future__ import annotations

import argparse
import re
import sys
import wave
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sfcore as sf  # noqa: E402

VOWELS = "aàáảãạăằắẳẵặâầấẩẫậeèéẻẽẹêềếểễệiìíỉĩịoòóỏõọôồốổỗộơờớởỡợuùúủũụưừứửữựyỳýỷỹỵ"


def read_wav(path: str):
    import numpy as np
    with wave.open(path) as w:
        if w.getsampwidth() != 2 or w.getnchannels() != 1:
            sf.die("align.py needs 16-bit mono WAV (ffmpeg -ac 1 -c:a pcm_s16le)")
        sr = w.getframerate()
        a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16)
    return a.astype(np.float32) / 32768.0, sr


def envelope(a, sr, hop_s=0.010, win_s=0.025, smooth=5):
    import numpy as np
    hop, win = int(sr * hop_s), int(sr * win_s)
    n = max((len(a) - win) // hop, 1)
    rms = np.empty(n, dtype=np.float32)
    for i in range(n):
        f = a[i * hop:i * hop + win]
        rms[i] = np.sqrt((f * f).mean())
    db = 20 * np.log10(rms + 1e-9)
    k = np.ones(smooth, dtype=np.float32) / smooth
    return np.convolve(db, k, mode="same"), hop_s


def find_nuclei(db, hop_s, floor_db=22.0, span_floor_db=18.0, min_gap_s=0.11):
    """Two thresholds on purpose. Peak picking wants a loose floor so quiet
    syllables still register. The speech SPAN wants a tighter one - room tone
    and breath sit just under the loose floor, and letting them into the span
    stretches the last word over a second of silence."""
    thr = db.max() - floor_db
    peaks = []
    for i in range(1, len(db) - 1):
        if db[i] >= db[i - 1] and db[i] > db[i + 1] and db[i] > thr:
            if peaks and (i - peaks[-1]) * hop_s < min_gap_s:
                if db[i] > db[peaks[-1]]:
                    peaks[-1] = i
                continue
            peaks.append(i)
    # Sustained runs only. A single frame over the threshold is a codec click
    # or a mouth noise at the file boundary; taking it as the edge of speech
    # stretches the first and last word across the whole clip.
    span_thr = db.max() - span_floor_db
    min_run = max(int(0.06 / hop_s), 3)
    runs, i = [], 0
    while i < len(db):
        if db[i] > span_thr:
            j = i
            while j < len(db) and db[j] > span_thr:
                j += 1
            if j - i >= min_run:
                runs.append((i, j - 1))
            i = j
        else:
            i += 1
    span = ((runs[0][0] * hop_s, runs[-1][1] * hop_s) if runs
            else (0.0, len(db) * hop_s))
    return [p * hop_s for p in peaks], span, thr


def syllables(word: str, audience: str) -> int:
    """Vietnamese words are one syllable each. Foreign words inside a
    Vietnamese sentence (Google, AI) are not, so those fall back to counting
    vowel groups. Digits are spelled out and cost more than they look."""
    w = word.lower()
    if re.fullmatch(r"[\d.,%]+", w):
        digits = re.sub(r"\D", "", w)
        return max(len(digits), 1)          # 15 -> "mười lăm" ~ 2
    core = "".join(c for c in w if c.isalpha())
    if not core:
        return 1
    if audience == "vi" and all(c in VOWELS or c.isalpha() and ord(c) > 127
                                or c in "bcdđghklmnpqrstvxaeiouy"
                                for c in core):
        # a native Vietnamese token: exactly one syllable
        if not re.search(r"[fjwz]", core) and len(core) <= 7:
            return 1
    groups = re.findall(rf"[{VOWELS}]+", core)
    return max(len(groups), 1)


def align(text: str, peaks: list, span: tuple, audience: str) -> list:
    words = [w for w in text.split() if w.strip()]
    if not words:
        return []
    counts = [syllables(w, audience) for w in words]
    total = sum(counts)
    start, end = span

    if len(peaks) >= total >= 1 and peaks:
        # Enough nuclei to hand out: give each word its share, in order.
        # Extra peaks at the edges are noise; drop from the end first.
        use = peaks[:total] if len(peaks) > total else peaks
        anchors, i = [], 0
        for c in counts:
            grp = use[i:i + c] or [use[-1]]
            anchors.append((grp[0], grp[-1]))
            i += c
    else:
        # Not enough nuclei (noisy audio, model missed): fall back to
        # proportional split across the voiced span.
        anchors, t = [], start
        step = (end - start) / total
        for c in counts:
            anchors.append((t, t + c * step))
            t += c * step

    out = []
    for i, (w, (a, b)) in enumerate(zip(words, anchors)):
        prev_b = anchors[i - 1][1] if i else start
        nxt_a = anchors[i + 1][0] if i + 1 < len(anchors) else end
        s = a - (a - prev_b) * 0.5 if i else max(start, a - 0.08)
        e = b + (nxt_a - b) * 0.5 if i + 1 < len(anchors) else min(end, b + 0.25)
        if e <= s:
            e = s + 0.08
        out.append({"start": s, "end": e, "word": w, "prob": 0.5})

    # Stretch the result onto the measured speech span. Peak picking usually
    # misses the release of the final syllable (energy is already falling),
    # which leaves the last caption ending early and the cutter trimming into
    # the word. One linear rescale fixes both ends at once.
    if out:
        a0, b0 = out[0]["start"], out[-1]["end"]
        if b0 > a0 and end > start:
            k = (end - start) / (b0 - a0)
            for w in out:
                w["start"] = round(start + (w["start"] - a0) * k, 3)
                w["end"] = round(start + (w["end"] - a0) * k, 3)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("audio", help="16-bit mono 16k WAV")
    ap.add_argument("--text", required=True)
    ap.add_argument("--audience", default="vi")
    ap.add_argument("--source", default="")
    ap.add_argument("-o", "--output", required=True)
    ap.add_argument("--floor-db", type=float, default=22.0)
    a = ap.parse_args()

    audio, sr = read_wav(a.audio)
    db, hop = envelope(audio, sr)
    peaks, span, _ = find_nuclei(db, hop, a.floor_db)
    words = align(a.text, peaks, span, a.audience)
    sf.info(f"{len(peaks)} nuclei, {len(words)} words, "
            f"speech {span[0]:.2f}-{span[1]:.2f}s")

    payload = {"source": a.source or a.audio, "audience": a.audience,
               "detected_language": a.audience, "duration": round(len(audio) / sr, 3),
               "alignment": "syllable-nuclei (approximate)",
               "words": words,
               "segments": [{"start": words[0]["start"], "end": words[-1]["end"],
                             "text": a.text}] if words else []}
    sf.save_json(payload, a.output)
    print(a.output)


if __name__ == "__main__":
    main()
