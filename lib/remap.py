#!/usr/bin/env python3
"""Re-time a transcript onto a cut video, using the EDL from sf-cut-silence.

Saves a second Whisper pass (minutes on large-v3). Words that fell inside a
removed region are dropped; the rest are shifted by how much was cut before
them.

Usage: python3 remap.py transcript.json cut.edl.json -o cut.transcript.json
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import sfcore as sf  # noqa: E402


def remap(tr: dict, keeps: list) -> dict:
    offsets, acc = [], 0.0
    for s, e in keeps:
        offsets.append((s, e, acc))
        acc += e - s

    def conv(t):
        for s, e, off in offsets:
            if s <= t <= e:
                return off + (t - s)
        return None

    words = []
    for w in tr["words"]:
        a, b = conv(w["start"]), conv(w["end"])
        if a is None or b is None or b <= a:
            continue
        words.append({**w, "start": round(a, 3), "end": round(b, 3)})

    segs = []
    for s in tr.get("segments", []):
        a, b = conv(s["start"]), conv(s["end"])
        if a is not None and b is not None and b > a:
            segs.append({**s, "start": round(a, 3), "end": round(b, 3)})

    return {**tr, "words": words, "segments": segs, "duration": round(acc, 3),
            "remapped_from": tr.get("source")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript")
    ap.add_argument("edl")
    ap.add_argument("-o", "--output", required=True)
    a = ap.parse_args()
    tr = sf.load_transcript(a.transcript)
    keeps = json.loads(Path(a.edl).read_text(encoding="utf-8"))["keeps"]
    out = remap(tr, keeps)
    sf.save_json(out, a.output)
    print(f"{a.output}  ({len(out['words'])} words, {out['duration']}s)")


if __name__ == "__main__":
    main()
