---
name: nqh-app-landing
description: "Dùng khi Hiếu muốn dựng LANDING PAGE cho một app điện thoại và/hoặc bộ ẢNH APP STORE, bắt đầu bằng việc nghiên cứu đối thủ cùng ngách rồi bóc DNA trang của họ. Kích hoạt: 'làm landing cho app', 'trang giới thiệu app', 'landing page app', 'ảnh app store', 'screenshot app store', 'dựng trang bán app'."
---

# NQH App Landing

Một câu ý tưởng app → trang landing dựng được + bộ ảnh App Store đúng chuẩn Apple.
Nền của mọi thứ là RESEARCH ĐỐI THỦ, không phải cảm hứng.

## Luật số 1: LANDING BÁN APP, KHÔNG PHẢI TRANG GIỚI THIỆU CÔNG TY

Sai lầm hay gặp: dựng ra trang SaaS B2B đầy tính năng rồi gắn nút tải app.

- Chuyển đổi duy nhất = **bấm nút tải app** (App Store / Google Play badge). Mọi thứ khác là phụ.
- Ảnh chủ đạo phải là **màn hình app trong khung điện thoại**, không phải ảnh stock người cười.
- Trang đọc trên điện thoại là chính, không phải desktop. Thiết kế 390px trước, mở rộng sau.
- Nếu một section không đẩy người ta gần hơn tới nút tải, cắt.

## Quy trình 6 bước

### Bước 0 — Chốt brief bằng đúng 3 câu hỏi (AskUserQuestion)

- **App làm gì, cho ai** (một câu)
- **Cần gì**: chỉ landing / chỉ ảnh App Store / cả hai
- **Cảm giác**: chọn 1 — tối & game-y · sáng & sạch (Apple, Linear) · ấm & thân thiện (Finch, Duolingo) · nghiêm & dữ liệu

Nếu Hiếu không có mặt: tự chốt, ghi giả định một dòng ở cuối, làm tiếp. Không dừng chờ.

### Bước 1 — Nghiên cứu đối thủ (BẮT BUỘC, không được bỏ)

Skill hỗ trợ: `competitor-alternatives` — **chỉ dùng phần research, KHÔNG viết trang so sánh SEO**.

Tìm **5-8 app cùng ngách** đã có landing thật. Với mỗi cái, mở trang và bóc đúng 7 thứ:

| Bóc gì | Ghi lại cụ thể |
|---|---|
| Headline hero | Chép nguyên văn, đếm số chữ |
| Sub-headline | Nó xử lý phản đối nào |
| Ảnh hero | Mấy khung điện thoại, góc nghiêng hay thẳng, có tay người không |
| Thứ tự section | Liệt kê từ trên xuống, đúng thứ tự |
| Social proof | Loại gì (số lượt tải / rating / logo báo / testimonial), đặt ở đâu |
| Nút CTA | Chữ trên nút, badge store, lặp lại mấy lần |
| Cái họ KHÔNG có | Section nào cả ngành đều thiếu |

Nguồn ưu tiên: trang chủ app, App Store / Google Play listing, Product Hunt. Ghi rõ **fact có nguồn** vs **suy đoán của tôi**.
Nếu container bị chặn: dùng Chrome trên máy Hiếu (`mcp__claude-in-chrome__*`) hoặc trình duyệt trong app để tự soi.

**Đầu ra bước 1** — một bảng DNA gọn + 3 dòng kết luận:
- Cái gì cả ngành đều làm → mình phải có, không sáng tạo lại.
- Cái gì chỉ 1-2 app làm mà hiệu quả → mình lấy.
- Khoảng trống chưa ai lấp → chỗ mình khác biệt.

Không có bảng DNA thì KHÔNG được sang bước 2.

### Bước 2 — Chốt cấu trúc trang

Skill hỗ trợ: `landing-page`.

Khung mặc định cho landing app (đổi được theo DNA bước 1):

1. **Hero** — headline + sub + khung điện thoại + 2 badge store
2. **Nỗi đau** — 1 câu người dùng tự nói trong đầu
3. **3 lợi ích lõi** — mỗi cái 1 ảnh màn hình thật, không icon chung chung
4. **Cách hoạt động** — 3 bước, không quá 3
5. **Bằng chứng** — rating, lượt tải, review thật có tên
6. **FAQ** — 4-6 câu, xử lý đúng phản đối tìm được ở bước 1
7. **CTA cuối** — lặp lại badge store, không có gì khác trên màn

Bỏ navigation nhiều mục. Landing app không cần menu 7 tab.

### Bước 3 — Viết copy theo công thức

Skill hỗ trợ: `landing-page-design`.

- Headline **6-12 chữ**, nêu KẾT QUẢ chứ không nêu tính năng.
  Sai: "Ứng dụng quản lý thói quen với AI". Đúng: "Giữ được thói quen sang tuần thứ ba".
- Sub-headline xử lý phản đối lớn nhất, không lặp lại headline.
- Chữ trên nút nói giá trị: "Tải miễn phí" > "Tải xuống"; "Dùng thử 7 ngày" > "Bắt đầu".
- Above-the-fold trên 390px phải nhìn thấy: headline + 1 khung điện thoại + 1 badge store. Không cần cuộn.
- Ba cách viết headline, chọn 1 rồi giữ nhất quán: **vẽ một khoảnh khắc** · **nêu kết quả** · **giết một nỗi đau**.

Skill `landing-page-design` có phần gen ảnh hero qua CLI `belt` của inference.sh (cần login riêng). **Nếu chưa có `belt`, bỏ phần đó**, chỉ dùng khung + công thức copy. Vẫn chạy bình thường.

### Bước 4 — Dựng code

Skill hỗ trợ: `frontend-design`.

- Ra file HTML/React chạy được thật, không phải mockup ảnh.
- Mobile-first: viết 390px trước, thêm breakpoint sau.
- Khung điện thoại vẽ bằng CSS hoặc SVG, không chèn ảnh mockup nặng.
- Badge App Store / Google Play: dùng đúng asset chính chủ Apple/Google, không tự vẽ lại.

### Bước 5 — Ảnh App Store

Skill hỗ trợ: `app-store-screenshots` (dựng app Next.js xuất ảnh).

- **Nguyên tắc lõi: screenshot là QUẢNG CÁO, không phải tài liệu.** Mỗi slide bán MỘT ý.
- Mạch 5-8 slide: lợi ích lớn nhất → điểm khác biệt → tính năng lõi (2-3 slide) → bằng chứng tin cậy.
- Caption ngắn, đọc được ở cỡ thumbnail trên điện thoại.
- Độ phân giải bắt buộc: iPhone 1320×2868 và 1125×2436; iPad 2064×2752 và 2048×2732.
- Xuất bằng `html-to-image` `toPng()` với **mẹo gọi 2 lần** (lần 1 nạp asset, lần 2 mới ra ảnh sạch).

### Bước 6 — Rà lại trước khi bàn giao

Skill hỗ trợ: `page-cro`.

Checklist bắt buộc, tự rà rồi báo cáo:

- [ ] Người lạ hiểu app này làm gì trong 5 giây?
- [ ] Badge store nhìn thấy được ở 390px mà không cần cuộn?
- [ ] Vùng bấm ≥ 44px?
- [ ] Headline đúng 6-12 chữ, nêu kết quả?
- [ ] Mọi số liệu là số thật hay đã đánh dấu `[SỐ]`?
- [ ] Có section nào không đẩy tới nút tải không? Cắt chưa?
- [ ] Chữ tiếng Việt có dấu hiển thị đúng, không vỡ font?

Ra 3 nhóm: **Sửa ngay** · **Sửa lớn, ưu tiên** · **Nên A/B test**.

## Luật thẩm mỹ

**Chữ**
- Tối đa 2 font. Tránh Inter/Roboto/Arial. Ưu tiên font có cá tính cho tiêu đề (Space Grotesk, Sora, Bricolage Grotesque, Instrument Serif) + một font thân sạch.
- Font phải đủ dấu tiếng Việt — kiểm tra "ữ ằ ộ" không vỡ. Vỡ thì đổi font.
- Thang cỡ rõ: 40-56 headline hero / 28-32 tiêu đề section / 16-18 thân / 13-14 phụ.

**Màu**
- 1 nền chủ đạo + 1 accent + tối đa 1 accent phụ. Định nghĩa bằng oklch, cùng chroma/lightness, chỉ đổi hue.
- Trắng và đen phải có tông (ám ấm hoặc ám lạnh), không dùng #fff / #000 thuần.

**Bố cục**
- Flex/grid + `gap`. Không margin lẻ từng phần tử.
- Icon: SVG nét, lưới 20/24px, cùng độ dày. TUYỆT ĐỐI không dùng emoji làm icon.

**Tránh (AI slop)**
- Gradient tím-xanh vô cớ, thẻ bo góc kèm viền trái màu, emoji rải khắp, ảnh stock người cười, số liệu giả cho đầy chỗ.
- Không bịa số thật (lượt tải, rating, giá, tên người review). Chưa có thì để `[LƯỢT TẢI]`, `[RATING]` cho Hiếu điền.

## Bản quyền

Nghiên cứu đối thủ thì được. Vẽ lại logo, wordmark, nhân vật hay tranh minh hoạ của họ thì không.
Bóc **cấu trúc và cơ chế**, không bóc **tài sản thương hiệu**.
Không lấy testimonial, rating hay logo báo của đối thủ gắn lên trang của mình.

## Ngôn ngữ

Toàn bộ copy viết tiếng Việt tự nhiên, đúng cách người Việt nói. Không dịch máy từ tiếng Anh.
Tên riêng và thuật ngữ kỹ thuật giữ nguyên. Nếu landing hướng thị trường quốc tế thì viết tiếng Anh native, không phải tiếng Anh dịch từ tiếng Việt.

## Nếu chưa cài các skill hỗ trợ

Sáu skill trên nằm ở `~/.claude/skills`. Cài:

```bash
mkdir -p ~/Vibe-Code/_khac && cd ~/Vibe-Code/_khac
git clone https://github.com/boraoztunc/skills.git bora-skills
mkdir -p ~/.claude/skills
for s in competitor-alternatives landing-page page-cro app-store-screenshots frontend-design; do
  ln -sfn ~/Vibe-Code/_khac/bora-skills/$s ~/.claude/skills/$s
done
npx skills add https://github.com/inference-sh/skills --skill landing-page-design
```

Chưa cài thì vẫn chạy được 6 bước trên bằng checklist nhúng sẵn trong file này — chỉ mất phần chi tiết sâu của từng skill.

## Bàn giao

Một hai câu: dựng gì, dựa trên đối thủ nào, giả định gì, chỗ nào cần Hiếu xem lại.
Kèm bảng DNA bước 1 để Hiếu kiểm chứng — đó là phần dễ sai nhất.

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
  chính file này, rồi nói ra `Đã ghi vào SỔ LỖI của nqh-app-landing: SAI … → ĐÚNG …`.
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
