---
name: nqh-video-transcribe
description: Tạo transcript word-level (JSON) cho video/audio bằng Whisper, tự nhận diện tệp khán giả Việt hay Anh. Dùng khi user muốn bóc lời video, lấy timestamp từng từ, hoặc trước khi chạy bất kỳ skill nqh-video-* nào khác (nqh-video-cut-silence, nqh-video-captions, nqh-video-punch-zoom đều cần file này). Kích hoạt khi user nói "bóc transcript", "lấy phụ đề", "transcribe video này", "chuẩn bị dựng short".
---

# nqh-video-transcribe

Bước 0 của mọi pipeline trong repo này. Các skill khác không đọc pixel — chúng đọc file JSON này.

## Chạy

```bash
python3 skills/nqh-video-transcribe/scripts/transcribe.py INPUT.mp4 \
  --audience auto \
  -o work/INPUT.transcript.json
```

`--audience`:
- `vi` — ép Whisper nhận tiếng Việt, nạp initial_prompt tiếng Việt (giảm lỗi tên riêng, thuật ngữ)
- `en` — ép tiếng Anh
- `auto` (mặc định) — để Whisper tự detect, sau đó phân loại lại bằng mật độ dấu thanh trong kết quả

## Đầu ra

```json
{
  "audience": "vi",
  "duration": 61.4,
  "fps": 30.0, "width": 1920, "height": 1080,
  "words": [{"start": 0.12, "end": 0.41, "word": "chào", "prob": 0.98}],
  "segments": [{"start": 0.1, "end": 4.2, "text": "..."}]
}
```

## Lưu ý thật

- Tiếng Việt: dùng `large-v3`. Model nhỏ hơn (`base`, `small`) sai timestamp từ khá nhiều với tiếng Việt vì âm tiết ngắn — caption sẽ lệch thấy rõ. Đây là chỗ KHÔNG nên tiết kiệm.
- Apple Silicon: chạy CPU với `compute_type=int8` vẫn nhanh chấp nhận được (~1/3 realtime với large-v3). Không cần CUDA.
- Nếu video có nhạc nền to, tách vocal trước sẽ tăng độ chính xác đáng kể.

## Yêu cầu

`ffmpeg`, `ffprobe`, `pip install faster-whisper`

## Khi ASR không trả timestamp từng từ

Một số đường ASR chỉ trả về CHỮ, không có timestamp: sherpa-onnx Whisper (ONNX, tải model từ GitHub thay vì Hugging Face), phần lớn API cloud gói rẻ, và mọi transcript do người gõ tay.

Dùng `lib/align.py` để dựng lại timestamp từ chính file âm thanh:

```bash
ffmpeg -y -i INPUT.mp4 -vn -ac 1 -ar 16000 -c:a pcm_s16le audio.wav
python3 lib/align.py audio.wav \
  --text "Google vừa tung ra 15 bộ công cụ AI" \
  --audience vi --source INPUT.mp4 -o transcript.json
```

Cách hoạt động: dò đỉnh năng lượng trong đường bao âm thanh — mỗi đỉnh là một nhân âm tiết — rồi gán âm tiết cho từ theo thứ tự.

**Cách này ăn tiếng Việt hơn hẳn tiếng Anh.** Tiếng Việt đơn âm và tính nhịp theo âm tiết: mỗi từ đúng một âm tiết, mỗi âm tiết một đỉnh năng lượng rõ, độ dài các âm tiết xấp xỉ nhau. Nên đỉnh ↔ âm tiết ↔ từ gần như một-đối-một. Tiếng Anh tính nhịp theo trọng âm, âm tiết không đều — ở EN đây chỉ là phương án chữa cháy.

Ba chi tiết khiến nó chạy được trên file thật:

- **Hai ngưỡng riêng.** Ngưỡng dò đỉnh lỏng (max−22dB) để âm tiết nhỏ vẫn được tính; ngưỡng xác định vùng nói chặt hơn (max−18dB) vì tiếng phòng và tiếng thở nằm ngay dưới ngưỡng lỏng.
- **Chỉ nhận vùng nói kéo dài ≥60ms.** Một frame lẻ vượt ngưỡng là tiếng click của codec ở đầu/cuối file — nhận nó làm biên sẽ kéo từ đầu và từ cuối trải dài cả clip.
- **Co giãn tuyến tính về đúng vùng nói.** Dò đỉnh hay bỏ sót phần đuôi của âm tiết cuối, làm caption cuối tắt sớm và bước cắt ăn vào chữ. Một phép co giãn sửa cả hai đầu.

Độ chính xác: đủ tốt cho caption và punch zoom. KHÔNG đủ để cắt gắt ở chế độ `aggressive` — dùng `--mode gentle` khi transcript đến từ đường này. Có Whisper word-level thật thì luôn ưu tiên.

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
  chính file này, rồi nói ra `Đã ghi vào SỔ LỖI của nqh-video-transcribe: SAI … → ĐÚNG …`.
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
