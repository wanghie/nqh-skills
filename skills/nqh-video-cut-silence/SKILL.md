---
name: nqh-video-cut-silence
description: Cắt im lặng, khoảng chết và từ đệm (ừ, à, kiểu như / um, uh, you know) khỏi video talking head, dùng bộ từ đệm riêng cho khán giả Việt và khán giả Anh. Dùng khi user nói "cắt im lặng", "bỏ ừ à", "làm gọn video", "cut dead air", "video nói lê thê quá", hoặc là bước 2 trong pipeline nqh-video-shorts. Cần transcript từ nqh-video-transcribe trước.
---

# nqh-video-cut-silence

Cắt dựa trên transcript, không chỉ dựa trên biên độ âm thanh. Lý do: đo âm lượng chỉ biết chỗ *không ai nói*; transcript biết thêm chỗ *có nói nhưng nói thừa*. Cả hai đều bị cắt.

## Chạy

```bash
python3 skills/nqh-video-cut-silence/scripts/cut.py INPUT.mp4 \
  -t work/INPUT.transcript.json \
  --mode balanced \
  -o work/INPUT.cut.mp4
```

`--mode`:
| mode | ngưỡng khoảng nghỉ | dùng khi |
|---|---|---|
| `aggressive` | x0.7 | short/reels, cần nhịp gắt |
| `balanced` | x1.0 | mặc định |
| `gentle` | x1.5 | podcast, video cần giữ nhịp thở tự nhiên |

`--keep-fillers` giữ nguyên từ đệm, chỉ cắt im lặng.
`--dry-run` chỉ xuất file `.edl.json` để bạn xem trước danh sách đoạn giữ, không render.

## Khác biệt VI / EN

Đây là điểm mà các skill nước ngoài làm sai với tiếng Việt:

- **Ngưỡng im lặng**: preset VI dùng `-34dB / 380ms`, EN dùng `-30dB / 300ms`. Người Việt nói liền mạch hơn, ngưỡng EN sẽ cắt vào giữa câu.
- **Từ đệm**: VI có `kiểu như là, thì là, nói chung là, tức là, đại loại`. Đây là những cụm 2-3 từ, phải khớp theo cụm chứ không theo từ đơn — cắt riêng từ "là" sẽ phá câu.
- **Giữ từ mở câu**: "So," hay "Thì" đứng đầu câu là dấu hiệu diễn đạt, không phải rác. Script giữ lại nếu trước nó có khoảng nghỉ > 450ms.

## Đầu ra

- `INPUT.cut.mp4` — video đã cắt
- `INPUT.cut.edl.json` — danh sách đoạn giữ, để skill sau (nqh-video-captions, nqh-video-punch-zoom) tính lại timestamp

## Lưu ý

Sau khi cắt, timestamp trong transcript gốc KHÔNG còn đúng. Chạy lại `nqh-video-transcribe` trên file đã cắt trước khi làm caption, hoặc để `nqh-video-shorts` lo việc đó.

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
  chính file này, rồi nói ra `Đã ghi vào SỔ LỖI của nqh-video-cut-silence: SAI … → ĐÚNG …`.
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
