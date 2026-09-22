---
name: nqh-app-designer
description: "Dùng khi Hiếu chỉ nói MỘT Ý TƯỞNG APP và muốn ra màn hình UI đẹp, bấm/sửa được — skill tự nghiên cứu đối thủ, chốt hướng thẩm mỹ, rồi dựng màn hình trên canvas. Kích hoạt khi nói 'thiết kế app', 'làm UI cho', 'dựng màn hình', 'mockup app', 'design lại app này'."
---

# NQH App Designer

Biến một câu ý tưởng thành bộ màn hình app đẹp, bấm được, sửa được trên canvas.
Hiếu nói ý — skill lo research, lo thẩm mỹ, lo dựng.

## Luật số 1: ĐÂY LÀ MÀN HÌNH APP, KHÔNG PHẢI SLIDE

Sai lầm hay gặp nhất: dựng ra deck đầy chữ rồi gọi đó là design.

- Mỗi artboard = MỘT MÀN HÌNH ĐIỆN THOẠI 390×844 (hoặc 1440×900 nếu là web).
- Chữ trên màn hình chỉ là chữ THẬT trong app: nhãn nút, tên mục, con số. Không phân tích, không giải thích, không bullet.
- Mọi ghi chú/lý do thiết kế đi vào **sticky note** (`annotations` trong canvas.json), KHÔNG nằm trong artboard.
- Nếu một artboard có trên ~40 từ, gần như chắc chắn đang làm sai.

## Quy trình 5 bước

### 1. Chốt brief bằng đúng 3 câu hỏi (AskUserQuestion)
Không hỏi lan man. Chỉ 3 thứ quyết định mọi thứ còn lại:
- **Ai dùng & để làm gì** (một câu)
- **Nền tảng**: app điện thoại / web / cả hai
- **Cảm giác**: chọn 1 — tối & game-y (Solo Leveling, neon) · sáng & sạch (Apple, Notion) · ấm & thân thiện (Finch, Duolingo) · nghiêm & dữ liệu (Linear, Bloomberg)

Nếu Hiếu không có mặt để trả lời: tự chốt, ghi rõ giả định một dòng ở cuối, làm tiếp — không dừng chờ.

### 2. Nghiên cứu trước khi vẽ (BẮT BUỘC, không bỏ qua)
- WebSearch 3-5 app cùng ngách. Với mỗi app lấy: các tab chính, màn hình lõi, cơ chế giữ chân, điểm bị chê nhiều nhất trong review thật.
- Ưu tiên nguồn: App Store / Google Play / tài liệu chính chủ / help center. Ghi rõ **fact có nguồn** vs **suy đoán**.
- Nếu container bị chặn ra store: dùng Chrome trên máy Hiếu (`mcp__claude-in-chrome__*`) để tự soi.
- Chốt lại 1 đoạn ngắn: cái gì LẤY, cái gì BỎ, khoảng trống nào chưa ai lấp. Đây là nền của thiết kế, không phải trang trí.

### 3. Chốt hướng thẩm mỹ trước khi dựng hi-fi
Dựng 2-3 artboard low-fi cùng MỘT màn hình, mỗi cái một hướng khác nhau thật sự (không phải 3 sắc độ của một hướng). Đặt tên hướng bằng tiếng Việt dễ nhớ. Cho Hiếu chọn.
Hiếu chọn rồi mới dựng full — và giữ nguyên tên hướng đó về sau.

### 4. Dựng bộ màn hình bằng skill `design`
Gọi skill `design`, tuân thủ format `.dc.html` + `canvas.json` của nó. Ngoài ra:
- **Số lượng**: 5-8 màn hình cho luồng chính. Không dựng 24 artboard rồi để rỗng ruột.
- **Thứ tự trên canvas**: theo đúng luồng người dùng đi (onboarding → màn chính → hành động → phần thưởng → cài đặt).
- **Trang (`pages`)**: 1 trang cho luồng chính, 1 trang cho variation/component. Không tách trang bừa.
- Đặt `"is_interactive": true` cho artboard có nút bấm chạy thật.

### 5. Bàn giao ngắn
Một hai câu: dựng gì, giả định gì, chỗ nào cần Hiếu xem lại. Không hướng dẫn cách sửa canvas — canvas tự nói.

## Luật thẩm mỹ (cái làm nên chữ "đẹp")

**Chữ**
- Tối đa 2 font. Tránh Inter/Roboto/Arial — đã quá nhàm. Ưu tiên font có cá tính cho tiêu đề (vd Space Grotesk, Sora, Bricolage Grotesque, Instrument Serif) + một font thân sạch.
- Font phải hiển thị tốt TIẾNG VIỆT có dấu — kiểm tra chữ "ữ ằ ộ" không bị vỡ. Nếu font không đủ dấu, đổi font.
- Thang cỡ chữ rõ ràng: 28-32 tiêu đề màn / 17-20 tiêu đề mục / 15-16 thân / 12-13 phụ. Không có 7 cỡ chữ na ná nhau.

**Màu**
- 1 màu nền chủ đạo + 1 accent + tối đa 1 accent phụ. Định nghĩa bằng oklch, cùng chroma/lightness, chỉ đổi hue.
- Trắng và đen phải có tông (ám ấm hoặc ám lạnh), không dùng #fff / #000 thuần.
- Kiểm tra tương phản chữ trên nền ở mức đọc được ngoài nắng.

**Bố cục**
- Luôn dùng flex/grid + `gap`. Không dùng margin lẻ từng phần tử — sẽ vỡ khi Hiếu kéo thả trong canvas.
- Vùng bấm không dưới 44px.
- KHÔNG vẽ thanh trạng thái iOS giả (9:41, pin, wifi) và KHÔNG vẽ bàn phím ảo giả. Chừa chỗ trống.
- Icon: vẽ SVG nét, lưới 20/24px, cùng độ dày nét. TUYỆT ĐỐI không dùng emoji làm icon.

**Tránh (AI slop)**
- Gradient tím-xanh vô cớ, thẻ bo góc kèm viền trái màu, emoji rải khắp, số liệu giả cho đầy chỗ.
- Không bịa số thật (giá, ngày, tên). Chỗ chưa có dữ liệu thì để `[GIÁ]`, `[NGÀY]` cho Hiếu điền. Riêng prototype bấm được thì dùng số mẫu và nói rõ là số mẫu.

## Bản quyền
Khi tham chiếu app đối thủ: mô tả CẤU TRÚC và CƠ CHẾ, không vẽ lại logo, nhân vật, wordmark hay tranh minh hoạ của họ. Nghiên cứu đối thủ thì được; sao chép giao diện có thương hiệu của họ thì không.

## Ngôn ngữ
Toàn bộ chữ trong app và ghi chú viết tiếng Việt tự nhiên, đúng cách người Việt nói. Không dịch máy từ tiếng Anh. Tên riêng và thuật ngữ kỹ thuật giữ nguyên.