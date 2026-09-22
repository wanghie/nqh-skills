# Video Motion — Prompt image-to-video (Kling 3.0 / Higgsfield)

Đã có frame đầu từ Gemini. Bây giờ chỉ thổi **chuyển động** vào. Luật vàng của image-to-video: **ảnh đã mã hoá ngoại hình/ánh sáng/màu — prompt video CHỈ nói chuyển động.** Mô tả lại ngoại hình = model bỏ frame, clip morph.

## Chọn tool

| Cảnh kiểu... | Dùng | Vì sao |
|---|---|---|
| Cú máy preset sạch trên cảnh tĩnh/1 chủ thể (dolly, orbit, crane, push-in) | **Higgsfield** | Mạnh nhất ở thư viện preset cú máy điện ảnh; "một move một clip" là sân nhà |
| Chuyển động chủ thể/môi trường tinh tế (khói bay, tóc lay, đèn nhấp nháy, chất lỏng), hoặc nhiều beat hành động | **Kling 3.0** | Vật lý & chi tiết chuyển động tốt hơn, nhận prompt nhiều beat |
| Không chắc | Đưa **cả hai** biến thể cho user thử | Mỗi tool ăn ảnh khác nhau |

Cả hai đều làm tốt clip ngắn 3-5s chậm — đúng nhu cầu B-roll.

---

## KLING 3.0 — image-to-video (motion-only)

Cấu trúc:
```
[Camera move] . [Beat hành động có timecode] . [Mood gọn 1 cụm] .
Negative: ...
```

Quy tắc:
- **Chỉ chuyển động.** Không màu, không lens, không "a man wearing..." (ảnh có rồi).
- **Beat có timecode** cho clip 3-5s, thường 2-3 beat: `0-2s: ...` `2-4s: ...` `4-5s: ...`. Kling tiêu "ngân sách chuyển động" cho beat nào động mạnh nhất → đặt beat quan trọng trước.
- **Mô tả trạng thái kết thúc** (end-state) để tránh treo: nói rõ cảnh kết ở đâu.
- **Spatial language** ("from left to right", "toward the camera") cho vật lý ổn định.
- **Một cú máy.** Đừng orbit + zoom cùng lúc.
- Chậm: thêm `slow, steady, smooth, no abrupt motion`.

Từ vựng cú máy Kling: `slow push-in / slow dolly-in / gentle drift left / subtle parallax / rack focus from foreground to subject / slight handheld sway / tilt up`.

Ví dụ (frame "tay gõ laptop khuya"):
```
Slow push-in toward the laptop screen. 0-2s: fingers continue typing softly,
the coffee steam drifts upward in the foreground. 2-5s: camera settles, screen glow
pulses gently. Slow, steady, intimate late-night mood.
Negative: warping, morphing, distorted hands, extra fingers, jittery, bending lines, flickering, sudden zoom
```

## HIGGSFIELD — image-to-video (preset-driven)

Higgsfield xoay quanh **preset cú máy**. Cấu trúc:
```
[Tên preset/cú máy] on [chủ thể trong ảnh] , [hướng & tốc độ] , [mood] .
Negative: ...
```

Thư viện preset hay dùng (chọn ĐÚNG MỘT):
`Dolly In / Dolly Out / Push-in / Orbit (360 hoặc bán nguyệt) / Crane Up / Crane Down / Tracking / Tilt Up / Boom / Rack Focus / Slow Zoom / Parallax`.
(Né Whip Pan / Bullet Time / FPV cho B-roll chậm — đó là cho cảnh hành động.)

Quy tắc:
- **Một preset/clip.** Higgsfield khuyến nghị không trộn move.
- Mô tả chủ thể ngắn gọn để neo (vd "the laptop and hands") nhưng KHÔNG tả lại ngoại hình chi tiết.
- Thêm tốc độ: `at a slow, steady creep` / `constant slow radius` (cho orbit).
- Pro tip: ghép **dolly-in + chủ thể tĩnh/biểu cảm giữ yên** → chính chuyển động máy tạo kịch tính.
- Clip 3-5s là ngọt; dài hơn dễ drift.

Ví dụ (cùng frame):
```
Slow dolly-in on the laptop and typing hands, camera glides forward at a steady creep,
coffee steam rising in the foreground, intimate contemplative late-night mood.
Negative: warping, morphing, distorted hands, extra fingers, jittery, flickering, sudden zoom
```

---

## Negative prompt chuẩn (luôn kèm)

Cơ bản:
```
warping, morphing, distorted face, extra fingers, deformed hands, jittery, bending lines, flickering, sudden zoom, abrupt motion
```
Thêm theo cảnh:
- Có kiến trúc/đường thẳng: `+ warping structure, bending walls, distorted windows`
- Có chữ trong khung: `+ garbled text, changing letters`
- Có chất lỏng: `+ floating liquid, unnatural splashes`

## Định nhịp 3-5s chậm (gợi ý)

- **3s:** một cú máy đơn, một beat (push-in dứt khoát). Cảnh chuyển nhanh trong video.
- **4s:** một cú máy + một chuyển động chủ thể nhẹ (steam, tóc, ánh sáng).
- **5s:** một cú máy + 2 beat (vd push-in rồi settle + rack focus). Cảnh "thở" — hợp lúc Hiếu nói câu nặng ký, cần khán giả lắng.

## Lỗi hay gặp → cách sửa

- **Clip morph/biến dạng** → prompt video đang tả ngoại hình. Xoá hết, chỉ để chuyển động.
- **Treo / không động** → frame đầu chật, không có chỗ động; hoặc thiếu end-state. Sửa frame ở Gemini hoặc thêm "ends with...".
- **Chuyển động giật/nhanh** → thêm `slow, steady, smooth`; giảm số beat.
- **Mặt/tay hỏng** → giảm độ hở của mặt/tay trong frame đầu, hoặc đẩy negative mạnh hơn.
- **Nhiều move loạn** → tách thành nhiều clip, mỗi clip một move.
