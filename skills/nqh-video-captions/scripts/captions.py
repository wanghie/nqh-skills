#!/usr/bin/env python3
"""nqh-video-captions - word-by-word burned captions, styled per audience.

Builds an .ass file with one event per word (the whole line stays on screen,
the spoken word is highlighted), then burns it. Word-level highlight is the
single biggest retention lever in short-form and it costs nothing to render.

Usage:
  python3 captions.py INPUT.mp4 -t transcript.json [-o out.mp4]
          [--audience vi|en] [--style bold|clean] [--font NAME]
          [--position 0.22] [--ass-only]
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "lib"))
import sfcore as sf  # noqa: E402


def ts(t: float) -> str:
    t = max(t, 0)
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def pick_font(candidates: list) -> str:
    """First font actually installed wins; otherwise let libass substitute."""
    if shutil.which("fc-match"):
        installed = subprocess.run(
            ["fc-list", ":", "family"], capture_output=True, text=True
        ).stdout.lower()
        for name in candidates:
            if name.lower() in installed:
                return name
    return candidates[0]


def group_words(words: list, per_line: int, max_chars: int,
                max_gap: float = 0.8) -> list:
    """Chunk words into caption lines. A long pause always breaks a line -
    a caption that spans a pause is a caption that lies about the rhythm."""
    lines, cur, chars = [], [], 0
    for i, w in enumerate(words):
        gap = w["start"] - words[i - 1]["end"] if i else 0
        too_long = len(cur) >= per_line or chars + len(w["word"]) > max_chars
        if cur and (too_long or gap > max_gap):
            lines.append(cur)
            cur, chars = [], 0
        cur.append(w)
        chars += len(w["word"]) + 1
    if cur:
        lines.append(cur)
    return lines


def build_ass(words, cap, width, height, style_name, position) -> str:
    font = pick_font([cap["font"]] + cap.get("font_fallback", []))
    # Size from BOTH dimensions. Height alone overflows a 9:16 frame: a
    # 22-char Vietnamese line at 6.5% of 1920 is 124px tall and ~1500px wide
    # on a 1080-wide canvas. The width term is what keeps the line inside.
    usable_w = width * (1 - 2 * 0.06)          # matches MarginL/R below
    by_height = height * cap["font_size_pct"] / 100
    by_width = usable_w / (cap["max_chars_per_line"] * 0.60)
    size = max(int(min(by_height, by_width)), 16)
    margin_v = int(height * (position if position is not None
                             else cap["margin_v_pct"] / 100))
    outline = cap["outline"] if style_name == "bold" else max(cap["outline"] - 2, 1)
    shadow = cap["shadow"] if style_name == "bold" else 0
    prim, hl = cap["primary_color"], cap["highlight_color"]

    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {width}
PlayResY: {height}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: SF,{font},{size},{prim},{prim},&H00101010,&H80000000,-1,0,0,0,100,100,0,0,1,{outline},{shadow},2,{int(width*0.06)},{int(width*0.06)},{margin_v},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    up_all = cap.get("uppercase", False)
    up_hl = cap.get("uppercase_highlight", False)
    lines = group_words(words, cap["words_per_line"], cap["max_chars_per_line"])

    events = []
    for grp in lines:
        for j, active in enumerate(grp):
            start = active["start"] if j else grp[0]["start"]
            end = active["end"] if j < len(grp) - 1 else grp[-1]["end"] + 0.08
            if end <= start:
                end = start + 0.05
            parts = []
            for k, w in enumerate(grp):
                txt = w["word"].replace("{", "(").replace("}", ")")
                if up_all:
                    txt = txt.upper()
                if k == j:
                    if up_hl and not up_all:
                        txt = txt.upper()
                    parts.append(f"{{\\c{hl}\\fscx108\\fscy108}}{txt}{{\\c{prim}\\fscx100\\fscy100}}")
                else:
                    parts.append(txt)
            events.append(
                f"Dialogue: 0,{ts(start)},{ts(end)},SF,,0,0,0,,{' '.join(parts)}"
            )
    return head + "\n".join(events) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("-t", "--transcript", required=True)
    ap.add_argument("-o", "--output", default=None)
    ap.add_argument("--audience", default=None)
    ap.add_argument("--style", default="bold", choices=["bold", "clean"])
    ap.add_argument("--font", default=None)
    ap.add_argument("--position", type=float, default=None,
                    help="vertical margin as fraction of height, e.g. 0.22")
    ap.add_argument("--ass-only", action="store_true")
    args = ap.parse_args()

    sf.require("ffmpeg", "ffprobe")
    tr = sf.load_transcript(args.transcript)
    audience = args.audience or tr.get("audience", "en")
    cap = dict(sf.load_preset(audience)["captions"])
    if args.font:
        cap["font"] = args.font

    src = Path(args.input)
    meta = sf.probe(str(src))
    ass_text = build_ass(tr["words"], cap, meta["width"], meta["height"],
                         args.style, args.position)

    out = Path(args.output or src.with_name(src.stem + ".captioned.mp4"))
    ass_path = out.with_suffix(".ass")
    ass_path.write_text(ass_text, encoding="utf-8")
    sf.info(f"audience={audience} font={pick_font([cap['font']] + cap.get('font_fallback', []))} "
            f"upper={cap.get('uppercase')} words/line={cap['words_per_line']}")
    if args.ass_only:
        print(ass_path)
        return

    esc = str(ass_path).replace("\\", "/").replace(":", r"\:").replace("'", r"\'")
    sf.run(["ffmpeg", "-y", "-v", "error", "-i", str(src),
            "-vf", f"subtitles='{esc}'"] + sf.encode_args() + [str(out)])
    print(out)


if __name__ == "__main__":
    main()
