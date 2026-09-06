#!/usr/bin/env python3
"""nqh-video-transcribe - word-level transcript, audience-aware.

Every other skill in this repo reads the JSON this produces. Run it once
per source file; the rest of the chain is then pure arithmetic on text.

Usage:
  python3 transcribe.py INPUT.mp4 [-o transcript.json] [--audience vi|en|auto]
                        [--model large-v3] [--device auto|cpu|cuda]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "lib"))
import sfcore as sf  # noqa: E402


def extract_audio(src: str, dst: Path) -> None:
    sf.run([
        "ffmpeg", "-y", "-v", "error", "-i", src,
        "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", str(dst),
    ])


def transcribe(wav: Path, language: str | None, model_size: str,
               device: str, initial_prompt: str | None) -> dict:
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        sf.die(
            "faster-whisper is not installed.\n"
            "  pip install faster-whisper        (CPU or CUDA)\n"
            "  On Apple Silicon this runs fine on CPU with compute_type=int8."
        )

    if device == "auto":
        try:
            import torch  # noqa
            device = "cuda" if torch.cuda.is_available() else "cpu"
        except Exception:
            device = "cpu"
    compute_type = "float16" if device == "cuda" else "int8"

    sf.info(f"whisper {model_size} on {device} ({compute_type})")
    model = WhisperModel(model_size, device=device, compute_type=compute_type)
    segments, meta = model.transcribe(
        str(wav),
        language=language,
        initial_prompt=initial_prompt,
        word_timestamps=True,
        vad_filter=True,
        vad_parameters={"min_silence_duration_ms": 250},
        beam_size=5,
    )

    words, segs = [], []
    for s in segments:
        segs.append({"start": round(s.start, 3), "end": round(s.end, 3),
                     "text": s.text.strip()})
        for w in (s.words or []):
            words.append({
                "start": round(w.start, 3),
                "end": round(w.end, 3),
                "word": w.word.strip(),
                "prob": round(float(w.probability or 0), 3),
            })
    return {"words": words, "segments": segs,
            "detected_language": meta.language}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("-o", "--output", default=None)
    ap.add_argument("--audience", default="auto", help="vi | en | auto")
    ap.add_argument("--model", default=None)
    ap.add_argument("--device", default="auto")
    args = ap.parse_args()

    sf.require("ffmpeg", "ffprobe")
    src = Path(args.input)
    if not src.exists():
        sf.die(f"No such file: {src}")

    out = Path(args.output or src.with_suffix(".transcript.json"))
    work = out.parent / f".sf-{src.stem}"
    work.mkdir(parents=True, exist_ok=True)
    wav = work / "audio.wav"
    extract_audio(str(src), wav)

    # Audience decides the ASR language hint. 'auto' means: let Whisper
    # detect, then classify the result — safer than guessing from a filename.
    if args.audience in ("vi", "en"):
        preset = sf.load_preset(args.audience)
        lang = preset["asr"]["language"]
        prompt = preset["asr"].get("initial_prompt")
        model_size = args.model or preset["asr"].get("model", "large-v3")
    else:
        lang, prompt, model_size = None, None, (args.model or "large-v3")

    res = transcribe(wav, lang, model_size, args.device, prompt)
    audience = args.audience if args.audience in ("vi", "en") else sf.detect_audience(res)

    meta = sf.probe(str(src))
    payload = {
        "source": str(src.resolve()),
        "audience": audience,
        "detected_language": res["detected_language"],
        "duration": meta["duration"],
        "fps": meta["fps"],
        "width": meta["width"],
        "height": meta["height"],
        "words": res["words"],
        "segments": res["segments"],
    }
    sf.save_json(payload, str(out))
    print(f"{out}  ({len(payload['words'])} words, audience={audience})")


if __name__ == "__main__":
    main()
