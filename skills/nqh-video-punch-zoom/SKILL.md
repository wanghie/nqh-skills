---
name: nqh-video-punch-zoom
description: Thêm nhịp cho video talking head bằng punch-zoom vào từ nhấn mạnh và Ken Burns push chậm ở đoạn dài, tự dò điểm nhấn từ transcript theo bộ từ khoá riêng cho tiếng Việt và tiếng Anh. Dùng khi user nói "video nhìn tĩnh quá", "thêm zoom", "punch zoom", "làm cho đỡ chán", "thêm nhịp cho video". Cần transcript từ nqh-video-transcribe.
---

# nqh-video-punch-zoom

Talking head một góc máy đứng yên là lý do số một khiến người xem lướt qua. Skill này thêm hai kiểu chuyển động, cả hai đều bám vào lời nói chứ không rải ngẫu nhiên.

- **punch** — zoom cứng ngay lập tức vào từ được nhấn, giữ đến hết vế câu
- **push** — Ken Burns đẩy chậm dưới đoạn nói dài, để khung không bao giờ đứng im quá lâu

## Chạy

```bash
python3 skills/nqh-video-punch-zoom/scripts/zoom.py INPUT.mp4 \
  -t work/INPUT.transcript.json \
  --density 0.12 \
  -o work/INPUT.zoom.mp4
```

`--density` = số cú zoom mỗi giây. `0.12` ≈ một cú mỗi 8 giây (mặc định, hợp short 30-60s). Video 15s nên tăng lên `0.2`.
`--dry-run` in ra danh sách điểm zoom kèm từ được chọn, chưa render — luôn chạy cái này trước.
`--map file.json` dùng kế hoạch tự viết tay thay vì auto.

## Cách chấm điểm từ

Mỗi từ được cộng điểm theo 4 tín hiệu:

| Tín hiệu | Điểm | Vì sao |
|---|---|---|
| Nằm trong danh sách từ khoá của preset | +3 | "bí quyết", "sự thật", "đừng" / "never", "secret" |
| Có số hoặc % | +2 | Con số luôn là điểm nhấn |
| Có khoảng nghỉ ngay trước | +2 đến +3 | Người nói dừng trước một từ là đang tự đánh dấu từ đó |
| Dài bất thường so với trung vị | +1.5 | Kéo dài âm = nhấn giọng |

Sau đó lọc theo khoảng cách tối thiểu 2.2s giữa hai cú zoom. Không có bước này video sẽ giật liên hồi.

## Khác biệt VI / EN

- Biên độ zoom: VI `x1.18`, EN `x1.22`. Short tiếng Anh chuộng zoom gắt hơn; khán giả Việt phản ứng tốt hơn với biên độ vừa.
- Bộ từ khoá hoàn toàn khác nhau, xem `presets/audience.*.json` mục `zoom.emphasis_keywords`. Bạn nên tự thêm từ khoá theo niche của mình — đây là chỗ chỉnh cho ra chất riêng.

## Chi tiết kỹ thuật

Punch crop lệch lên trên (40% thay vì 50% chiều cao) để mặt không bị đẩy ra khỏi khung khi zoom. Với video đã reframe 9:16, chạy skill này SAU nqh-video-reframe.
