---
name: nqh-video-captions
description: Burn phụ đề word-by-word (highlight từng từ đang nói) lên video, style riêng cho khán giả Việt và khán giả Anh — xử lý đúng dấu tiếng Việt, số từ mỗi dòng, font hỗ trợ Unicode. Dùng khi user nói "gắn phụ đề", "làm caption", "sub kiểu Opus/Hormozi", "burn sub", "caption tiếng Việt bị lỗi dấu". Cần transcript từ nqh-video-transcribe.
---

# nqh-video-captions

Sinh file `.ass` một event mỗi từ (cả dòng đứng yên, từ đang nói đổi màu + phóng to 8%), rồi burn vào video.

## Chạy

```bash
python3 skills/nqh-video-captions/scripts/captions.py INPUT.mp4 \
  -t work/INPUT.transcript.json \
  --style bold \
  -o work/INPUT.captioned.mp4
```

`--style bold` (viền dày, có bóng) hoặc `--style clean` (viền mỏng, không bóng).
`--position 0.22` đẩy caption lên/xuống (tỷ lệ so với chiều cao).
`--ass-only` chỉ xuất file `.ass` để bạn kéo vào Premiere/CapCut chỉnh tay.

## Khác biệt VI / EN — phần quan trọng nhất của skill này

| | Khán giả Việt | Khán giả Anh |
|---|---|---|
| Viết hoa | **KHÔNG** viết hoa toàn bộ | CÓ, ALL CAPS |
| Từ / dòng | 4 | 2 |
| Ký tự tối đa / dòng | 22 | 16 |
| Font mặc định | Be Vietnam Pro | Montserrat |

Hai lý do đằng sau:

1. **Viết hoa tiếng Việt phá dấu.** Chữ hoa có dấu (Ế, Ữ, Ộ) đội dấu lên cao, nhiều font hiển thị chồng lấn hoặc cắt mất dấu ở viền trên. Đọc chậm hơn thấy rõ. Preset VI chỉ viết hoa **từ đang được highlight** để vẫn có điểm nhấn mà không hy sinh khả năng đọc.
2. **Từ tiếng Việt ngắn hơn.** Phần lớn là 1-2 âm tiết. Để 2 từ/dòng như chuẩn EN sẽ ra caption trống trải, phải nhảy dòng liên tục. 4 từ/dòng cho mật độ tương đương.

Script tự dò font đã cài trên máy theo thứ tự ưu tiên; thiếu font Việt sẽ tự lùi về font có Unicode đầy đủ thay vì render ra ô vuông.

## Ngắt dòng theo nhịp nói

Dòng caption luôn bị ngắt khi có khoảng nghỉ > 0.8s, kể cả chưa đủ số từ. Caption nối qua một quãng lặng là caption nói dối về nhịp — người xem thấy chữ đứng im trong khi không ai nói.

## Yêu cầu

`ffmpeg` build có `libass` (bản Homebrew mặc định đã có).
Font: `brew install --cask font-be-vietnam-pro font-montserrat`

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
  chính file này, rồi nói ra `Đã ghi vào SỔ LỖI của nqh-video-captions: SAI … → ĐÚNG …`.
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
