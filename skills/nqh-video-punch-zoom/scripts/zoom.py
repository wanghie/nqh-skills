#!/usr/bin/env python3
"""nqh-video-punch-zoom - add rhythm to a static talking head.

Two moves, both driven by the transcript:
  punch  - instant hard-cut zoom on an emphasised word, held to end of clause
  push   - slow Ken Burns creep under a long statement

Auto-detection scores each word on: emphasis keyword, a pause right before it
(a speaker pausing before a word is telling you it matters), unusual word
duration, and numbers. Highest scores win, spaced out so the video does not
pulse like a strobe.

Usage:
  python3 zoom.py INPUT.mp4 -t transcript.json [-o out.mp4]
          [--audience vi|en] [--density 0.12] [--map zoommap.json] [--dry-run]
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "lib"))
import sfcore as sf  # noqa: E402

NUM = re.compile(r"\d")


def score_words(words: list, keywords: set) -> list:
    if not words:
        return []
    durs = sorted(w["end"] - w["start"] for w in words)
    med = durs[len(durs) // 2] or 0.2
    scored = []
    for i, w in enumerate(words):
        n = sf.norm_word(w["word"])
        if len(n) < 2 and not NUM.search(n):
            continue
        s = 0.0
        if n in keywords:
            s += 3.0
        if NUM.search(n) or "%" in w["word"]:
            s += 2.0
        gap = w["start"] - words[i - 1]["end"] if i else 1.0
        if gap > 0.35:
            s += 2.0 + min(gap, 1.0)
        d = w["end"] - w["start"]
        if d > med * 1.8:
            s += 1.5
        if s > 0:
            scored.append((s, i, w))
    return sorted(scored, key=lambda x: -x[0])


def plan_moves(words, preset, duration, density, min_spacing=2.2):
    z = preset["zoom"]
    keywords = {sf.norm_word(k) for k in z["emphasis_keywords"]}
    budget = max(1, int(duration * density))
    picked, taken = [], []
    for s, i, w in score_words(words, keywords):
        if len(picked) >= budget:
            break
        if any(abs(w["start"] - t) < min_spacing for t in taken):
            continue
        # hold the zoom to the end of the clause, not just the word
        end = w["end"]
        for nxt in words[i + 1:]:
            if nxt["start"] - end > 0.45:
                break
            end = nxt["end"]
            if end - w["start"] > 3.0:
                break
        picked.append({"type": "punch", "start": round(w["start"], 3),
                       "end": round(min(end + 0.15, duration), 3),
                       "scale": z["punch_scale"], "word": w["word"],
                       "score": round(s, 2)})
        taken.append(w["start"])
    picked.sort(key=lambda m: m["start"])

    # merge overlaps, then fill long quiet stretches with a slow push
    merged = []
    for m in picked:
        if merged and m["start"] < merged[-1]["end"]:
            merged[-1]["end"] = max(merged[-1]["end"], m["end"])
        else:
            merged.append(m)

    out, cursor = [], 0.0
    for m in merged:
        gap = m["start"] - cursor
        if gap >= z["kenburns_min_sec"] * 2:
            out.append({"type": "push", "start": round(cursor, 3),
                        "end": round(m["start"], 3), "scale": z["kenburns_scale"]})
        elif gap > 0:
            out.append({"type": "hold", "start": round(cursor, 3),
                        "end": round(m["start"], 3), "scale": 1.0})
        out.append(m)
        cursor = m["end"]
    if duration - cursor > 0.1:
        kind = "push" if duration - cursor >= z["kenburns_min_sec"] * 2 else "hold"
        out.append({"type": kind, "start": round(cursor, 3),
                    "end": round(duration, 3),
                    "scale": z["kenburns_scale"] if kind == "push" else 1.0})
    return [m for m in out if m["end"] - m["start"] > 0.12]


def render(src: str, moves: list, out: Path, work: Path, meta: dict) -> None:
    W, H, fps = meta["width"], meta["height"], meta["fps"]
    parts = []
    for i, m in enumerate(moves):
        p = work / f"z{i:04d}.mp4"
        dur = m["end"] - m["start"]
        if m["type"] == "push":
            inc = (m["scale"] - 1.0) / max(dur * fps, 1)
            vf = (f"zoompan=z='min(zoom+{inc:.6f},{m['scale']})'"
                  f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
                  f":d=1:s={W}x{H}:fps={fps},setsar=1")
        elif m["scale"] > 1.001:
            zw, zh = int(W * m["scale"]) // 2 * 2, int(H * m["scale"]) // 2 * 2
            vf = (f"scale={zw}:{zh}:flags=lanczos,"
                  f"crop={W}:{H}:{(zw - W) // 2}:{int((zh - H) * 0.40)},setsar=1")
        else:
            vf = "setsar=1"
        sf.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{m['start']:.3f}",
                "-i", src, "-t", f"{dur:.3f}", "-vf", vf] +
               sf.encode_args() + ["-r", str(fps), str(p)])
        parts.append(p)
    sf.concat(parts, str(out), work)
    for p in parts:
        p.unlink(missing_ok=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("-t", "--transcript", default=None)
    ap.add_argument("-o", "--output", default=None)
    ap.add_argument("--audience", default=None)
    ap.add_argument("--density", type=float, default=0.12,
                    help="zoom events per second (0.12 ~ one per 8s)")
    ap.add_argument("--map", default=None, help="hand-written zoom map JSON")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    sf.require("ffmpeg", "ffprobe")
    src = Path(args.input)
    meta = sf.probe(str(src))
    out = Path(args.output or src.with_name(src.stem + ".zoom.mp4"))

    if args.map:
        import json
        moves = json.loads(Path(args.map).read_text(encoding="utf-8"))["moves"]
    else:
        if not args.transcript:
            sf.die("Need --transcript for auto mode, or --map for a manual plan.")
        tr = sf.load_transcript(args.transcript)
        audience = args.audience or tr.get("audience", "en")
        preset = sf.load_preset(audience)
        moves = plan_moves(tr["words"], preset, meta["duration"], args.density)
        sf.info(f"audience={audience} "
                f"{sum(1 for m in moves if m['type'] == 'punch')} punch, "
                f"{sum(1 for m in moves if m['type'] == 'push')} push")

    sf.save_json({"source": str(src.resolve()), "moves": moves},
                 str(out.with_suffix(".zoommap.json")))
    if args.dry_run:
        for m in moves:
            if m["type"] == "punch":
                sf.info(f"  {m['start']:6.2f}s punch x{m['scale']}  \"{m.get('word','')}\"")
        print(out.with_suffix(".zoommap.json"))
        return

    work = out.parent / f".sf-{src.stem}"
    work.mkdir(parents=True, exist_ok=True)
    render(str(src), moves, out, work, meta)
    print(out)


if __name__ == "__main__":
    main()
