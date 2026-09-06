---
name: nqh-video-shorts
description: Chạy full pipeline biến 1 video talking head thô thành short 9:16 hoàn chỉnh — bóc transcript, cắt im lặng và từ đệm, reframe bám mặt, punch zoom, burn caption — theo đúng tệp khán giả Việt hoặc Anh. Dùng khi user đưa 1 file video và nói "dựng thành short", "làm reels từ video này", "biến video này thành TikTok", "chạy full pipeline", "edit video này giúp tôi".
---

# nqh-video-shorts

Skill điều phối. Gọi 5 skill còn lại theo đúng thứ tự và tự chuyển timestamp giữa các bước.

## Chạy

```bash
bash skills/nqh-video-shorts/scripts/pipeline.sh INPUT.mp4 --audience vi
```

Tuỳ chọn:

| Flag | Mặc định | Ghi chú |
|---|---|---|
| `--audience` | `auto` | `vi`, `en`, hoặc `auto` (tự nhận từ transcript) |
| `--outdir` | `<thư mục input>/sf-out` | |
| `--mode` | `balanced` | độ gắt khi cắt: `aggressive` / `balanced` / `gentle` |
| `--aspect` | `9:16` | `4:5` cho Facebook/LinkedIn, `1:1` cho feed vuông |
| `--density` | `0.12` | số cú zoom mỗi giây |
| `--skip` | — | ví dụ `--skip zoom,reframe` |
| `--dry-run` | — | chỉ xuất file kế hoạch (edl/reframe/zoommap/ass), không render |

## Thứ tự và lý do

```
1  transcribe   → transcript.json (word-level)
2  cut-silence  → cut.mp4 + edl.json
   remap        → cut.transcript.json   (KHÔNG chạy Whisper lần 2)
3  reframe      → vertical.mp4          (9:16 bám mặt)
4  punch-zoom   → zoom.mp4              (chạy sau reframe, để zoom trên khung dọc)
5  captions     → final.mp4             (chạy cuối, để chữ không bị crop mất)
```

Bước `remap` là chỗ tiết kiệm nhất: sau khi cắt, mọi timestamp trong transcript đều sai. Thay vì chạy lại Whisper large-v3 (vài phút), script dịch timestamp cũ sang trục thời gian mới bằng EDL, mất chưa tới một giây.

## Quy trình khuyên dùng

Chạy `--dry-run` trước, xem 3 file kế hoạch, sửa preset nếu cần, rồi mới render thật:

```bash
bash skills/nqh-video-shorts/scripts/pipeline.sh raw.mp4 --audience vi --dry-run
# xem sf-out/raw.cut.edl.json, raw.reframe.json, raw.zoommap.json
bash skills/nqh-video-shorts/scripts/pipeline.sh raw.mp4 --audience vi
```

Transcript đã có sẽ được dùng lại, không transcribe lại — nên lần chạy thứ hai nhanh hơn nhiều.

## Giới hạn

- Một người nói, một góc máy. Phỏng vấn 2 người cần active-speaker detection, chưa có.
- Không tự chọn đoạn hay nhất trong video dài. Skill này dựng nguyên video bạn đưa vào; muốn cắt highlight từ video 30 phút thì cắt thô trước rồi mới đưa vào đây.
