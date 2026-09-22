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
  chính file này, rồi nói ra `Đã ghi vào SỔ LỖI của nqh-video-punch-zoom: SAI … → ĐÚNG …`.
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
