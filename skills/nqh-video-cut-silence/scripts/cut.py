#!/usr/bin/env python3
"""nqh-video-cut-silence - remove dead air and filler words, per audience profile.

Works off the word-level transcript, not audio RMS alone: silence detection
tells you where nobody speaks, the transcript tells you where someone speaks
but says nothing. Both get cut.

Usage:
  python3 cut.py INPUT.mp4 -t transcript.json [-o out.mp4]
                 [--audience vi|en] [--mode aggressive|balanced|gentle]
                 [--keep-fillers] [--dry-run]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "lib"))
import sfcore as sf  # noqa: E402

MODE_GAIN = {"aggressive": 0.7, "balanced": 1.0, "gentle": 1.5}


def filler_spans(words: list, preset: dict) -> list:
    """Indices of words to drop. Phrases are matched greedily and longest-first
    so 'kiểu như là' wins over 'kiểu như'."""
    fl = preset["fillers"]
    singles = {sf.norm_word(w) for w in fl["single"]}
    phrases = sorted(
        ([sf.norm_word(t) for t in p.split()] for p in fl["phrases"]),
        key=len, reverse=True,
    )
    norm = [sf.norm_word(w["word"]) for w in words]
    drop = set()
    i = 0
    while i < len(norm):
        if i in drop:
            i += 1
            continue
        hit = None
        for ph in phrases:
            n = len(ph)
            if norm[i:i + n] == ph:
                hit = n
                break
        if hit:
            drop.update(range(i, i + hit))
            i += hit
            continue
        if norm[i] in singles:
            # A filler that opens a sentence is often a real discourse marker
            # ("So, here is the thing"). Keeping it reads more human.
            prev_end = words[i - 1]["end"] if i else 0.0
            starts_sentence = (i == 0) or (words[i]["start"] - prev_end > 0.45)
            if not (fl.get("keep_if_sentence_start") and starts_sentence):
                drop.add(i)
        i += 1
    return sorted(drop)


def build_keeps(words: list, preset: dict, duration: float,
                mode: str, keep_fillers: bool) -> list:
    cut = preset["cut"]
    gain = MODE_GAIN[mode]
    min_gap = (cut["min_silence_ms"] / 1000.0) * gain
    pad_h = cut["pad_head_ms"] / 1000.0
    pad_t = cut["pad_tail_ms"] / 1000.0

    drop = set() if keep_fillers else set(filler_spans(words, preset))
    kept = [w for i, w in enumerate(words) if i not in drop]
    if not kept:
        sf.die("Nothing left after filtering - check the transcript.")

    runs = []
    cur = [kept[0]["start"], kept[0]["end"]]
    for w in kept[1:]:
        if w["start"] - cur[1] > min_gap:
            runs.append(cur)
            cur = [w["start"], w["end"]]
        else:
            cur[1] = w["end"]
    runs.append(cur)

    keeps = []
    for s, e in runs:
        s = max(0.0, s - pad_h)
        e = min(duration, e + pad_t)
        if keeps and s <= keeps[-1][1] + 0.02:
            keeps[-1][1] = max(keeps[-1][1], e)
        elif e - s > 0.12:
            keeps.append([s, e])
    return keeps


def render(src: str, keeps: list, out: Path, work: Path) -> None:
    meta = sf.probe(src)
    parts = []
    fade = 0.025  # kills the click at every cut boundary
    for i, (s, e) in enumerate(keeps):
        p = work / f"part{i:04d}.mp4"
        dur = e - s
        af = f"afade=t=in:st=0:d={fade},afade=t=out:st={max(dur - fade, 0):.3f}:d={fade}"
        cmd = ["ffmpeg", "-y", "-v", "error", "-ss", f"{s:.3f}", "-i", src,
               "-t", f"{dur:.3f}"]
        if meta["has_audio"]:
            cmd += ["-af", af]
        cmd += sf.encode_args() + ["-r", str(meta["fps"]), str(p)]
        sf.run(cmd)
        parts.append(p)
    sf.concat(parts, str(out), work)
    for p in parts:
        p.unlink(missing_ok=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("-t", "--transcript", required=True)
    ap.add_argument("-o", "--output", default=None)
    ap.add_argument("--audience", default=None)
    ap.add_argument("--mode", default="balanced", choices=list(MODE_GAIN))
    ap.add_argument("--keep-fillers", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    sf.require("ffmpeg", "ffprobe")
    tr = sf.load_transcript(args.transcript)
    audience = args.audience or tr.get("audience", "en")
    preset = sf.load_preset(audience)
    duration = tr.get("duration") or sf.probe(args.input)["duration"]

    keeps = build_keeps(tr["words"], preset, duration, args.mode, args.keep_fillers)
    kept_time = sum(e - s for s, e in keeps)
    sf.info(f"audience={audience} mode={args.mode}")
    sf.info(f"{duration:.1f}s -> {kept_time:.1f}s "
            f"({100 * (1 - kept_time / duration):.0f}% removed, {len(keeps)} cuts)")

    src = Path(args.input)
    out = Path(args.output or src.with_name(src.stem + ".cut.mp4"))
    work = out.parent / f".sf-{src.stem}"
    work.mkdir(parents=True, exist_ok=True)

    edl = {"audience": audience, "mode": args.mode, "source": str(src.resolve()),
           "keeps": [[round(s, 3), round(e, 3)] for s, e in keeps],
           "original_duration": duration, "output_duration": round(kept_time, 3)}
    sf.save_json(edl, str(out.with_suffix(".edl.json")))

    if args.dry_run:
        print(out.with_suffix(".edl.json"))
        return
    render(str(src), keeps, out, work)
    print(out)


if __name__ == "__main__":
    main()
