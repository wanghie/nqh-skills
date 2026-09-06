"""Shared helpers for the sf-* short-form video skills.

Every script imports this. It owns three things and nothing else:
preset loading (the VI/EN audience profiles), ffmpeg/ffprobe wrappers,
and the transcript JSON contract that the skills pass between each other.

Transcript contract (one JSON file, produced by sf-transcribe):
{
  "audience": "vi",
  "duration": 61.4,
  "words": [{"start": 0.12, "end": 0.41, "word": "chào", "prob": 0.98}, ...],
  "segments": [{"start": 0.1, "end": 4.2, "text": "..."}, ...]
}
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PRESET_DIR = REPO_ROOT / "presets"


# --------------------------------------------------------------------------
# presets
# --------------------------------------------------------------------------
def load_preset(audience: str) -> dict:
    """Load an audience preset by id ('vi', 'en') or by explicit path."""
    p = Path(audience)
    if p.suffix == ".json" and p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    f = PRESET_DIR / f"audience.{audience}.json"
    if not f.exists():
        avail = sorted(x.stem.split(".")[-1] for x in PRESET_DIR.glob("audience.*.json"))
        die(f"Unknown audience '{audience}'. Available: {', '.join(avail)}")
    return json.loads(f.read_text(encoding="utf-8"))


def detect_audience(transcript_or_text) -> str:
    """Guess 'vi' vs 'en' from text. Vietnamese is unmistakable: it is the
    only one of the two that carries combining diacritics on vowels."""
    if isinstance(transcript_or_text, dict):
        text = " ".join(w["word"] for w in transcript_or_text.get("words", []))
    else:
        text = str(transcript_or_text)
    if not text.strip():
        return "en"
    marked = sum(
        1
        for ch in unicodedata.normalize("NFD", text)
        if unicodedata.combining(ch)
    )
    return "vi" if marked / max(len(text), 1) > 0.03 else "en"


# --------------------------------------------------------------------------
# text
# --------------------------------------------------------------------------
def norm_word(w: str) -> str:
    """Lowercase, strip punctuation. Keeps Vietnamese diacritics intact."""
    return "".join(
        ch for ch in w.lower().strip() if ch.isalnum() or ch in "%'’-"
    ).strip("-'’")


# --------------------------------------------------------------------------
# ffmpeg
# --------------------------------------------------------------------------
def require(*bins: str) -> None:
    missing = [b for b in bins if shutil.which(b) is None]
    if missing:
        die(f"Missing required tool(s): {', '.join(missing)}. Install them first.")


def run(cmd: list, quiet: bool = True) -> subprocess.CompletedProcess:
    res = subprocess.run(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        errors="replace",
    )
    if res.returncode != 0:
        sys.stderr.write("\n".join(res.stderr.strip().splitlines()[-25:]) + "\n")
        die(f"Command failed: {' '.join(str(c) for c in cmd[:6])} ...")
    if not quiet and res.stdout:
        print(res.stdout)
    return res


def probe(path: str) -> dict:
    out = run([
        "ffprobe", "-v", "error", "-print_format", "json",
        "-show_format", "-show_streams", str(path),
    ]).stdout
    info = json.loads(out)
    v = next((s for s in info["streams"] if s["codec_type"] == "video"), None)
    a = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
    if v is None:
        die(f"No video stream in {path}")
    num, den = (v.get("r_frame_rate") or "30/1").split("/")
    fps = float(num) / float(den or 1)
    return {
        "width": int(v["width"]),
        "height": int(v["height"]),
        "fps": round(fps, 4),
        "duration": float(info["format"].get("duration") or v.get("duration") or 0),
        "has_audio": a is not None,
    }


def encode_args(crf: int = 18, preset: str = "medium") -> list:
    """One place for encode settings, so every skill in the chain matches
    and concat never has to re-encode twice for mismatched params."""
    return [
        "-c:v", "libx264", "-preset", preset, "-crf", str(crf),
        "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.2",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart",
    ]


def concat(parts: list, out_path: str, workdir: Path) -> None:
    """Stream-copy concat of already-encoded parts."""
    listfile = workdir / "concat.txt"
    listfile.write_text(
        "".join(f"file '{Path(p).resolve()}'\n" for p in parts), encoding="utf-8"
    )
    run([
        "ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0",
        "-i", str(listfile), "-c", "copy", str(out_path),
    ])


# --------------------------------------------------------------------------
# transcript io
# --------------------------------------------------------------------------
def load_transcript(path: str) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if "words" not in data:
        die(f"{path} is not a valid transcript (no 'words' key). Run sf-transcribe first.")
    return data


def save_json(obj: dict, path: str) -> None:
    Path(path).write_text(
        json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8"
    )


def die(msg: str) -> None:
    sys.stderr.write(f"error: {msg}\n")
    sys.exit(1)


def info(msg: str) -> None:
    sys.stderr.write(f"  {msg}\n")
