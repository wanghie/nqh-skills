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
