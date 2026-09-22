# Style DNA — Bóc phong cách từ mẫu

Mục tiêu: biến mẫu user đưa (ảnh/video/link/mô tả) thành một **thẻ Style DNA** gồm các cụm từ tiếng Anh dùng được luôn trong prompt ảnh. Thẻ này khoá một lần, áp cho cả bộ B-roll để đồng nhất.

## Quy tắc nền

- **Nhìn trước, nói sau.** Có ảnh thì `view` nó. Có video thì xem/đọc mô tả frame. KHÔNG bịa.
- **Bóc cái lặp lại, bỏ cái ngẫu nhiên.** Nếu cả 3 mẫu đều tối + đèn vàng + máy chậm → đó là DNA. Một mẫu lẻ màu xanh → bỏ qua.
- **Diễn đạt bằng từ khoá kỹ thuật**, không phải tính từ mơ hồ. "Đẹp" vô dụng; "warm-amber grade, crushed blacks, soft window key" dùng được.
- Khi mẫu mâu thuẫn nhau → hỏi user mẫu nào ưu tiên, hoặc chọn mẫu user nói "thích nhất".

## 9 trục cần bóc

### 1. Màu / Grade
Tông màu chủ đạo, độ bão hoà, vùng tối/sáng được đẩy về đâu.
Từ vựng: `warm amber / teal-orange / desaturated / muted earth tones / high contrast / crushed blacks / lifted shadows / filmic LUT / monochrome / pastel`.

### 2. Ánh sáng
Nguồn sáng, hướng, độ mềm, tỷ lệ tương phản.
Từ vựng: `soft single key light / hard directional light / window light / golden hour / blue hour / practical lamps / rim light / low-key (tối, ít sáng) / high-key (sáng, đều) / volumetric god rays / neon glow / candlelit`.

### 3. Lens & Depth of Field
Tiêu cự cảm giác và độ nông sâu.
Từ vựng: `35mm / 50mm / 85mm / wide 24mm / anamorphic / f/1.8 shallow depth of field / deep focus / bokeh / focus breathing / lens flare`.

### 4. Texture / Grain / "độ thật"
Bề mặt hình ảnh.
Từ vựng: `fine 35mm film grain / clean digital / halation on highlights / soft haze / sharp 4K clarity / vintage VHS texture / matte finish`.

### 5. Kiểu chuyển động máy (đọc từ mẫu video)
Mẫu di chuyển thế nào — để bước 5 chọn cú máy khớp.
Từ vựng: `slow push-in / drift / handheld sway / locked-off static / orbit / crane up / whip pan / parallax`. Với B-roll của Hiếu, ưu tiên **slow & deliberate**.

### 6. Không khí / Mood
Cảm giác cảnh để lại.
Từ vựng: `contemplative / premium / energetic / moody / nostalgic / clinical-minimal / warm intimate / epic`.

### 7. Bố cục & Tỷ lệ khung
Cách đặt chủ thể, không gian âm, khung hình.
Từ vựng: `rule of thirds / centered symmetry / negative space / tight close-up / wide establishing / low angle / top-down / over-the-shoulder`.
Tỷ lệ: `16:9` (YouTube ngang, mặc định cho Hiếu), `9:16` (Shorts/Reels), `4:5` (feed), `2.39:1` (anamorphic điện ảnh).

### 8. Cách xử lý chủ thể
Có người không? Cận hay xa? Có mặt không (Hiếu hay làm faceless ở một số kênh)? Vật/sản phẩm/cảnh vật?
Vd: `faceless — hands and objects only / silhouette / back of subject / product hero shot / empty environment`.

### 9. Tham chiếu thẩm mỹ
Một mỏ neo văn hoá giúp model bắt nhanh.
Vd: `A24 film look / Apple product ad / founder-documentary YouTube style / Kinfolk minimal / cyberpunk`.

## Mẫu thẻ output

```
STYLE DNA — [tên bộ video]
- Grade: [trục 1]
- Light: [trục 2]
- Lens: [trục 3]
- Texture: [trục 4]
- Motion: [trục 5 — ưu tiên slow]
- Mood: [trục 6]
- Frame: [trục 7]
- Subject: [trục 8]
- Aesthetic ref: [trục 9]
- Aspect: [16:9 / 9:16 ...]
```

## Default khi không có mẫu (cinematic founder look)

```
STYLE DNA — default cinematic
- Grade: warm amber shadows, low saturation, slight crushed blacks
- Light: soft single key from window-left, deep falloff, practical lamp glow
- Lens: 35mm, f/2, shallow depth of field
- Texture: fine 35mm film grain, gentle halation
- Motion: slow push-in / drift / parallax only
- Mood: contemplative, premium, late-evening calm
- Frame: rule of thirds, generous negative space
- Subject: hands + objects + environment (faceless-friendly)
- Aesthetic ref: founder-documentary / A24
- Aspect: 16:9
```
Nói rõ với user đây là default và đưa mẫu sẽ chuẩn hơn.
