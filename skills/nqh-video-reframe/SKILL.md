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

## SỔ LỖI ĐÃ BỊ NHẮC

Đọc hết mục này TRƯỚC khi xuất chữ đầu tiên. Mỗi dòng là một lỗi đã bị nhắc; lặp
lại nó lần nữa là lỗi nặng hơn lần đầu. Bảng rỗng = skill này chưa từng bị nhắc.
**Bảng rỗng là trung thực — cấm bịa dòng mẫu cho có.**

- **Nhận ra feedback:** "sai rồi", "không phải thế", "đừng…", "bỏ… đi", "lần sau…",
  "từ giờ…", "tôi đã bảo rồi", "vẫn còn…", "nói bao nhiêu lần rồi", hoặc Hiếu tự
  tay sửa output vừa nhận rồi gửi ngược lại.
- **Ghi gì:** sửa output và quét sửa hết chỗ cùng loại — việc này LUÔN LUÔN làm.
  Ghi sổ thì CÓ ĐIỀU KIỆN: chỉ khi lỗi thuộc loại THÀNH LUẬT, tức sẽ lặp lại với
  một input khác. Lỗi MỘT LẦN (sai tên, sai số, sai link, đổi ý muốn) thì sửa
  output rồi dừng, không ghi sổ. Ghi thì thêm ĐÚNG MỘT dòng vào bảng dưới, trong
  chính file này, rồi nói ra `Đã ghi vào SỔ LỖI của nqh-video-reframe: SAI … → ĐÚNG …`.
  Cột **Nguồn** bắt buộc, đúng ba giá trị: `Hiếu` (Hiếu nói thật) · `review` (bộ
  máy review bắt được) · `tự đo` (tự gọi tool ra kết quả). Cấm trình bày kết luận
  của agent như thể Hiếu đã nói — bịa nguồn tệ hơn không ghi. Cột SAI tả hành vi
  quan sát được, không tả cảm giác.
- **Trần sổ: 10 dòng** — không phải số chọn bừa. Luật mẹ là `SKILL.md < 300 dòng`;
  khối này chiếm 27 dòng khung, cộng dòng trắng ngăn cách và 10 dòng sổ là 38, nên
  thân skill phải dừng dưới 262 dòng. Sổ đủ 10 dòng mà có dòng mới → nâng dòng bị
  lặp nhiều nhất thành luật cứng có tên ở thân skill rồi xoá khỏi sổ; không xoá
  một dòng chỉ vì nó cũ. Hai luật chọi nhau thì `< 300 dòng` THẮNG. Kiểm bằng
  `wc -l SKILL.md` (< 300) và `grep -c '^| 20' SKILL.md` (<= 10).

| Ngày | Nguồn | SAI | ĐÚNG |
|---|---|---|---|
