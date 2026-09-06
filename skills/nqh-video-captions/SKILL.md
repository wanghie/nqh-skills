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
