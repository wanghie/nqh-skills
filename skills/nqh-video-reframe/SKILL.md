---
name: nqh-video-reframe
description: Chuyển video ngang 16:9 sang dọc 9:16 (hoặc 4:5, 1:1) bám theo mặt người nói bằng MediaPipe, dùng kiểu cắt cảnh cứng thay vì pan trôi. Dùng khi user nói "chuyển sang dọc", "làm 9:16", "crop cho TikTok/Reels/Shorts", "video ngang muốn đăng short", "reframe". Không cần transcript.
---

# nqh-video-reframe

## Chạy

```bash
python3 skills/nqh-video-reframe/scripts/reframe.py INPUT.mp4 \
  --aspect 9:16 --mode face \
  -o work/INPUT.vertical.mp4
```

`--mode`:
- `face` (mặc định) — MediaPipe dò mặt, chọn khuôn mặt to nhất (người đang nói với camera)
- `center` — crop giữa, dùng khi video đã canh sẵn
- `top` — crop giữa theo chiều ngang nhưng bám mép trên, dùng cho screen recording

`--dry-run` xuất `.reframe.json` để xem kế hoạch cắt trước khi render.

## Vì sao cắt cứng chứ không pan mượt

Crop di chuyển từng frame theo mặt trông như cầm máy rung. Script này giữ khung đứng yên, chỉ nhảy sang vị trí mới khi người nói đã dịch chuyển **và giữ vị trí đó** đủ lâu (`--min-hold`, mặc định 1.2s) với biên độ đủ lớn (`--jump`, mặc định 6% chiều rộng). Kết quả nhìn như có người bấm cut, không như camera bị đẩy.

Chỉnh 2 tham số này là chỉnh toàn bộ cảm giác:
- Talking head ngồi yên: tăng `--jump 0.10` để gần như không nhảy khung
- Người đi lại, nhiều máy: giảm `--min-hold 0.6`

## Giới hạn thật

- Nhiều người trong khung: script chọn mặt TO nhất, không phải người ĐANG NÓI. Với video phỏng vấn 2 người ngồi cạnh nhau, nó sẽ bám nhầm. Cần active-speaker detection mới xử lý đúng — chưa có trong repo này.
- Nếu MediaPipe không cài, script tự động lùi về crop giữa và báo rõ, không fail.

## Yêu cầu

`ffmpeg`, `pip install mediapipe opencv-python` (tuỳ chọn — thiếu thì chạy chế độ center)
