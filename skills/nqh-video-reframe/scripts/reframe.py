#!/usr/bin/env python3
"""nqh-video-reframe - 16:9 -> 9:16 with the speaker's face kept in frame.

Strategy is hard-cut pans, not continuous tracking: the crop window holds
still and only jumps when the subject has genuinely moved and stayed moved.
A crop that drifts every frame reads as a shaky camera; a crop that cuts
reads as an edit.

Usage:
  python3 reframe.py INPUT.mp4 [-o out.mp4] [--aspect 9:16]
          [--mode face|center|top] [--sample 0.4] [--smooth 5] [--dry-run]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "lib"))
import sfcore as sf  # noqa: E402


def _make_detector():
    """Return (detect_fn, name) or (None, reason).

    Three backends, tried in order. MediaPipe ships two incompatible APIs
    depending on version, and some wheels ship neither - so OpenCV's Haar
    cascade is kept as the always-available floor. It is less accurate but
    it never leaves the skill dead.
    """
    import cv2

    try:  # mediapipe <= 0.10.x classic solutions API
        import mediapipe as mp
        det = mp.solutions.face_detection.FaceDetection(
            model_selection=1, min_detection_confidence=0.4)

        def f(frame):
            res = det.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            if not res.detections:
                return None
            best = max(res.detections,
                       key=lambda d: d.location_data.relative_bounding_box.width)
            bb = best.location_data.relative_bounding_box
            return (bb.xmin + bb.width / 2) * frame.shape[1]

        return f, "mediapipe.solutions"
    except Exception:
        pass

    try:  # mediapipe tasks API - needs a local .tflite model
        import os
        import mediapipe as mp
        from mediapipe.tasks.python import vision, BaseOptions
        model = os.environ.get("SF_FACE_MODEL", "")
        if model and Path(model).exists():
            opts = vision.FaceDetectorOptions(
                base_options=BaseOptions(model_asset_path=model),
                min_detection_confidence=0.4)
            det = vision.FaceDetector.create_from_options(opts)

            def f(frame):
                img = mp.Image(image_format=mp.ImageFormat.SRGB,
                               data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                res = det.detect(img)
                if not res.detections:
                    return None
                best = max(res.detections, key=lambda d: d.bounding_box.width)
                bb = best.bounding_box
                return bb.origin_x + bb.width / 2

            return f, "mediapipe.tasks"
    except Exception:
        pass

    try:  # opencv haar - bundled with opencv-python, no download
        cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        if cascade.empty():
            raise RuntimeError("cascade did not load")

        def f(frame):
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = cascade.detectMultiScale(gray, 1.15, 5, minSize=(60, 60))
            if len(faces) == 0:
                return None
            x, y, w, h = max(faces, key=lambda r: r[2])
            return x + w / 2

        return f, "opencv.haar"
    except Exception as e:
        return None, f"no face backend ({e})"


def sample_face_centers(src: str, step: float, crop_w: int, width: int):
    """Return [(t, cx_pixels)] sampled every `step` seconds. cx is None where
    no face was found - callers hold the last known position."""
    try:
        import cv2
    except ImportError:
        sf.info("opencv not installed - falling back to centre crop")
        return None

    detect, name = _make_detector()
    if detect is None:
        sf.info(f"{name} - falling back to centre crop")
        return None
    sf.info(f"face backend: {name}")

    cap = cv2.VideoCapture(src)
    if not cap.isOpened():
        sf.die(f"OpenCV cannot open {src}")
    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    stride = max(int(round(fps * step)), 1)

    out, idx = [], 0
    while True:
        if not cap.grab():
            break
        if idx % stride == 0:
            ok, frame = cap.retrieve()
            if ok:
                try:
                    cx = detect(frame)
                except Exception:
                    cx = None
                out.append((idx / fps, cx))
        idx += 1
    cap.release()
    found = sum(1 for _, c in out if c is not None)
    sf.info(f"sampled {len(out)} frames, face found in {found}")
    if found == 0:
        sf.info("no face anywhere - using centre crop")
        return None
    return out


def to_shots(samples, width: int, crop_w: int, smooth: int,
             jump_px: float, min_hold: float, duration: float):
    """Fill gaps, moving-average, then quantise into hold-and-jump shots."""
    if not samples:
        return [(0.0, duration, (width - crop_w) / 2)]

    xs, last = [], width / 2
    for t, c in samples:
        if c is None:
            c = last
        last = c
        xs.append((t, c))

    k = max(smooth, 1)
    sm = []
    for i, (t, _) in enumerate(xs):
        lo, hi = max(0, i - k // 2), min(len(xs), i - k // 2 + k)
        sm.append((t, sum(v for _, v in xs[lo:hi]) / (hi - lo)))

    def clamp(cx):
        return max(0.0, min(width - crop_w, cx - crop_w / 2))

    shots = [[sm[0][0], clamp(sm[0][1])]]
    pending = None
    for t, cx in sm[1:]:
        x = clamp(cx)
        if abs(x - shots[-1][1]) < jump_px:
            pending = None
            continue
        if pending is None:
            pending = (t, x)
        elif t - pending[0] >= min_hold:
            # only commit a jump the subject actually sustained
            shots.append([pending[0], x])
            pending = None
    out = []
    for i, (t, x) in enumerate(shots):
        end = shots[i + 1][0] if i + 1 < len(shots) else duration
        if end - t > 0.25:
            out.append((t, end, x))
        elif out:
            out[-1] = (out[-1][0], end, out[-1][2])
    return out or [(0.0, duration, (width - crop_w) / 2)]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ap.add_argument("-o", "--output", default=None)
    ap.add_argument("--aspect", default="9:16")
    ap.add_argument("--mode", default="face", choices=["face", "center", "top"])
    ap.add_argument("--sample", type=float, default=0.4, help="seconds between samples")
    ap.add_argument("--smooth", type=int, default=5)
    ap.add_argument("--jump", type=float, default=0.06,
                    help="min move as fraction of width before a re-cut")
    ap.add_argument("--min-hold", type=float, default=1.2)
    ap.add_argument("--out-height", type=int, default=1920)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    sf.require("ffmpeg", "ffprobe")
    src = Path(args.input)
    meta = sf.probe(str(src))
    W, H, dur = meta["width"], meta["height"], meta["duration"]

    aw, ah = (int(v) for v in args.aspect.split(":"))
    crop_w = min(W, int(round(H * aw / ah)))
    crop_h = min(H, int(round(crop_w * ah / aw)))
    crop_w -= crop_w % 2
    crop_h -= crop_h % 2

    if crop_w >= W:
        sf.info("source is already at or narrower than target aspect - "
                "cropping height instead")

    if args.mode == "face":
        samples = sample_face_centers(str(src), args.sample, crop_w, W)
    else:
        samples = None
    shots = to_shots(samples or [], W, crop_w, args.smooth,
                     args.jump * W, args.min_hold, dur)
    y = 0 if args.mode == "top" else max(0, (H - crop_h) // 2)

    out = Path(args.output or src.with_name(src.stem + ".vertical.mp4"))
    plan = {"source": str(src.resolve()), "aspect": args.aspect,
            "crop": [crop_w, crop_h], "shots": [
                {"start": round(s, 3), "end": round(e, 3), "x": int(x)}
                for s, e, x in shots]}
    sf.save_json(plan, str(out.with_suffix(".reframe.json")))
    sf.info(f"{W}x{H} -> {crop_w}x{crop_h}, {len(shots)} shot(s)")
    if args.dry_run:
        print(out.with_suffix(".reframe.json"))
        return

    work = out.parent / f".sf-{src.stem}"
    work.mkdir(parents=True, exist_ok=True)
    out_h = args.out_height
    out_w = int(round(out_h * aw / ah))
    out_w -= out_w % 2

    parts = []
    for i, (s, e, x) in enumerate(shots):
        p = work / f"rf{i:04d}.mp4"
        vf = (f"crop={crop_w}:{crop_h}:{int(x)}:{y},"
              f"scale={out_w}:{out_h}:flags=lanczos")
        sf.run(["ffmpeg", "-y", "-v", "error", "-ss", f"{s:.3f}", "-i", str(src),
                "-t", f"{e - s:.3f}", "-vf", vf] + sf.encode_args() +
               ["-r", str(meta["fps"]), str(p)])
        parts.append(p)
    sf.concat(parts, str(out), work)
    for p in parts:
        p.unlink(missing_ok=True)
    print(out)


if __name__ == "__main__":
    main()
