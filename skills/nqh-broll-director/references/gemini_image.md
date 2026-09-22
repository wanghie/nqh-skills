# Gemini Image — Prompt frame đầu (Nano Banana)

Frame đầu là điểm xuất phát của clip image-to-video. Nó khoá toàn bộ look. Làm tốt frame này = nửa cái clip đã thắng.

## Chọn model

- **Nano Banana Pro (Gemini 3 Pro Image):** mặc định cho B-roll cinematic — suy luận bố cục tốt, render chi tiết/ánh sáng cao, nhận tới ~14 ảnh tham chiếu, render chữ chuẩn (hữu ích khi cần text trong khung). Bật "Thinking" mode cho cảnh phức tạp.
- **Nano Banana (Gemini 2.5 Flash Image):** nhanh, hợp khi chỉ cần *chỉnh nhẹ* một ảnh đã gần đúng hoặc style-transfer nhanh.
- Edit-first: nếu ảnh ra 80% đúng, **đừng regenerate từ đầu** — bảo Gemini "keep the composition, change only the lighting to golden hour".

## Khung prompt (thứ tự này đọc rõ nhất)

```
[Subject — cụ thể] , [Composition/framing] , [Setting/environment] ,
[Lighting] , [STYLE DNA block] , [Lens & camera] , [Aspect ratio]
```

Viết bằng **tiếng Anh**, câu mô tả tự nhiên (Gemini đọc văn xuôi tốt, không cần nhồi tag kiểu Midjourney). Một prompt 40-120 từ thường đủ.

### Các thành phần

1. **Subject** — ai/cái gì, đặc tả cụ thể. *"a steaming cup of black coffee beside an open laptop"* hơn *"coffee"*. Với B-roll faceless: tay + vật + môi trường.
2. **Composition** — `extreme close-up / medium shot / wide establishing / low angle / top-down / over-the-shoulder`, kèm vị trí chủ thể (`off-center, rule of thirds`).
3. **Setting** — không gian + thời điểm. *"a quiet café at late evening, rain on the window"*.
4. **Lighting** — lấy thẳng từ Style DNA trục 2.
5. **STYLE DNA** — dán grade + texture + mood từ thẻ. **Đây là thứ giữ cả bộ đồng nhất** — đừng bỏ.
6. **Lens & camera** — `shot on 35mm lens, f/2, shallow depth of field, cinematic`. Có thể thêm thân máy: `shot on Arri Alexa` để đẩy chất điện ảnh.
7. **Aspect ratio** — ghi rõ `16:9` (hoặc `9:16`). Sai tỷ lệ = phải làm lại, đốt credit.

## QUY TẮC RIÊNG CHO FRAME ĐẦU (vì sẽ đưa vào video)

Đây là điểm sống còn — frame này phải **có chỗ để động**:

- **Chừa negative space** về hướng máy/chủ thể sẽ di chuyển vào. Frame chật cứng = clip đứng hình.
- **Có lớp tiền cảnh/hậu cảnh** để tạo parallax khi máy push-in (vd: vật mờ ở tiền cảnh, đèn bokeh ở hậu cảnh).
- **Compose ở trạng thái "trước khi xảy ra".** Nếu clip là "rót cà phê", frame đầu là *bình nghiêng sắp rót*, chưa rót. Để chuyển động có chỗ diễn.
- **Frame sạch, sáng tốt, một chủ thể rõ.** Higgsfield/Kling warp mạnh nhất ở ảnh bẩn/rối/tối thui. Garbage in = garbage out.
- **Né mặt người cận + tay nhiều ngón** nếu không cần — vùng AI hay hỏng khi animate.

## Dùng ảnh tham chiếu (giữ nhân vật/sản phẩm/style)

Nano Banana Pro nhận nhiều ảnh. Chỉ định vai từng ảnh:
```
Use Image 1 as the character reference — maintain this exact person, face and outfit.
Use Image 2 as the style reference — match its color grade and lighting.
Place the subject in: [setting mới]. Cinematic, shot at 35mm, 16:9.
```
Hữu ích khi Hiếu muốn chính mình/sản phẩm Buyyouraccount xuất hiện nhất quán qua nhiều cảnh.

## Ví dụ hoàn chỉnh

**Ý:** "làm việc khuya một mình" (faceless, default cinematic DNA)
```
An extreme close-up of hands typing on a laptop keyboard in a dim home office at
midnight, the screen's glow lighting the fingers from the front, a half-empty cup of
coffee softly out of focus in the foreground. Warm amber shadows, low saturation,
slight crushed blacks, fine 35mm film grain, gentle halation on the screen highlights.
Contemplative late-night mood, generous negative space on the right of the frame.
Shot on 35mm lens, f/2, shallow depth of field, cinematic. 16:9.
```
Vì sao hợp frame đầu: tay chưa cần di chuyển nhiều, có foreground (cốc mờ) để parallax, có negative space bên phải cho máy drift vào.
