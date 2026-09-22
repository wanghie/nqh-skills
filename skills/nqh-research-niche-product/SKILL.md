---
name: nqh-research-niche-product
description: "Quét CẢ MỘT NGÁCH trên TikTok/Instagram/YouTube cho tới khi bão hoà, lọc creator bán sản phẩm của chính họ, ra bảng vật lý/digital/dịch vụ × giá × tính năng × chân dung khách, matrix định vị, TAM/SAM/SOM, và khoảng trống đã kiểm bằng xu hướng xã hội. Khác research-product-via-channel: cái kia bóc MỘT kênh, cái này quét CẢ NGÁCH nhiều kênh. Kích hoạt khi nói \"tìm sản phẩm ngách\", \"find niche product\", \"cả ngách này ai đang bán gì\", \"quét cả ngách\"."
---

# /nqh-research-niche-product

Một ngách không phải một từ khoá. Nó là một đám người đang trả tiền cho ai đó,
và một đám khác đang muốn trả mà chưa tìm được ai nhận. Skill này đi tìm đám thứ
hai.

Đầu ra là một tấm bản đồ, không phải một bài viết. Người đọc phải nhìn ra chỗ
trống bằng mắt trước khi đọc một chữ nào.

**Năm câu phải trả lời được, đúng thứ tự:**

```
1. Thị trường này lớn bao nhiêu?            → Hình 1
2. Có tổng bao nhiêu đối thủ?               → Hình 2, đã lọc miễn phí, đã bão hoà
3. Họ đang đứng ở những vị trí nào?         → Hình 3 + 4 + 5
4. Bạn chiếm mảnh nào, bao nhiêu phần?      → ô trống Hình 3 + SOM + Bước 10
5. Chiến lược đi vào của bạn là gì?         → USP một câu + nhóm khách Bước 9
```

## Dùng khi nào

- Đã chọn ngách, chưa biết trong đó có ai, bán gì, giá bao nhiêu
- Cần bản đồ đối thủ để quyết định đứng ở đâu, không cần một danh sách
- Muốn tìm nhóm khách bị bỏ rơi trong ngách đã đông
- Cần con số để chọn giữa ngách này và ngách khác

**Không dùng khi:** chỉ có một kênh và muốn bóc kênh đó — dùng
`research-product-via-channel`. Chỉ cần ý tưởng content. Đã build xong, chỉ cần
theo dõi đối thủ — cái đó là monitor.

**File tra cứu, đọc trước khi chạy bước tương ứng:**
- `references/nhan-dien-san-pham.md` — sở hữu vs affiliate · ba tầng sản phẩm ·
  bóc giá · tính năng vs điểm nổi bật · thang giá 12 loại · schema CSV
- `references/mau-bang-bieu.md` — mẫu vẽ sẵn tám hình bắt buộc + bảng độ phủ

---

## Bước 0 — Chốt ngách và ngưỡng dừng trước khi gọi tool

Điền năm dòng ra màn hình. Thiếu thì hỏi **gộp tối đa 3 câu một lượt**.

```
NGÁCH:         <một câu người thật nói, không phải từ khoá SEO>
SEED:          2-3 kênh/tài khoản đã biết trong ngách
THỊ TRƯỜNG:    toàn cầu | tiếng Việt | <khu vực>     ← quyết định SAM
TRỤC QUAN TÂM: để trống, chốt ở Bước 7 sau khi đọc comment
NGƯỠNG DỪNG:   SOM năm 1 dưới <số tiền> thì KHÔNG VÀO
```

> **Luật seed, không luật từ khoá.** Vào bằng kênh mẫu, đừng vào bằng từ khoá.
> Không có seed thì chạy MỘT lượt từ khoá lấy seed rồi quay lại luật này.

Người dùng bảo "cứ chạy đi" thì tự điền, chạy luôn, in mục
`## Giả định tôi đã tự điền` ở cuối. KHÔNG VÀO là kết quả tốt — tiết kiệm ba
tháng.

**Xong khi:** năm dòng đã hiện ra và người dùng không phản đối.

---

## Bước 1 — Gom creator: TikTok trước, YouTube sau cùng

```
mcp__govrl__find_outlier_videos { keyword: <ngách>, platform: "tiktok" }
mcp__govrl__find_outlier_videos { keyword: <ngách>, platform: "instagram" }
mcp__govrl__find_outlier_videos { keyword: <ngách>, platform: "youtube" }  ← CUỐI
```

> **Luật TikTok trước.** YouTube đốt ~100 đơn vị hạn mức mỗi lượt tìm và hay trả
> `HTTP 429 quota exceeded`; cháy hạn mức là mất cả ngày. TikTok/Instagram không
> đụng vào hạn mức đó, và trường `title` của chúng chứa **nguyên văn caption** —
> nơi creator viết tên chương trình, lời mời, đôi khi cả giá. YouTube chỉ trả
> tiêu đề, không có mô tả.

*Chuyện thật 12.09.2026: lượt tìm YouTube thứ hai trong ngày trả 429, cháy hạn
mức trước khi quét xong một ngách. TikTok cùng từ khoá vẫn chạy, cho nhiều tài
khoản hơn hẳn.*

> **Luật sàn quy mô.** Bỏ tài khoản dưới 1.000 người theo dõi. Outlier Score kéo
> kênh nhỏ lên là đúng về nội dung, nhưng kênh 18 subscriber không có sản phẩm
> để nghiên cứu.

**Xong khi:** ≥40 tài khoản đã khử trùng, mỗi dòng có nền tảng, quy mô, link bài
outlier.

---

## Bước 2 — Mở rộng cho tới khi BÃO HOÀ, không dừng ở vài kênh

```
mcp__govrl__find_similar_channels { url: <mỗi kênh>, platform: <plat>, k: 30 }
mcp__govrl__niche_overview        { url: <seed> }
```

Chạy similar cho **mọi kênh trong danh sách**, không chỉ seed. Kênh mới tìm được
lại thành seed cho vòng sau.

> **Luật quét tới bão hoà.** Không dừng theo số kênh, dừng theo độ mới. Quét
> thêm 10 tài khoản mà **không ra thêm creator SỞ HỮU nào mới** thì mới được
> dừng. Chưa chạm mốc đó mà dừng là báo cáo thiếu, và mọi con số phía sau đều
> nhỏ hơn sự thật.

In bảng độ phủ sau mỗi vòng — mẫu ở Hình 2b của file bảng biểu.

> **Luật kiểm ba dòng đầu.** Đọc ba dòng đầu của `find_similar_channels` trước
> khi dùng bất cứ gì. Nếu chúng không cùng ngách với seed, **vứt toàn bộ kết
> quả**. Dấu hiệu hỏng nhìn thấy được: cột `format_sim` giống hệt nhau ở nhiều
> dòng liên tiếp — đó là giá trị mặc định, không phải phép đo.

| | |
|---|---|
| HỎNG | seed fitness đàn ông 40+ → khoa học 21M · công nghệ 21M · giải trí 503M |
| DÙNG ĐƯỢC | seed fitness → ba dòng đầu đều fitness, cùng tầm quy mô |

*Chuyện thật 12.09.2026: đúng bảng HỎNG ở trên, kèm `format_sim` bằng đúng 0.605
ở 10 dòng liền.*

Similar hỏng thì vẫn phải chạy tới bão hoà bằng ba đường thay thế: **đồng xuất
hiện** (tài khoản lọt vào từ hai lượt tìm khác nhau) · **kênh được giới thiệu**
(featured/collab) · **hashtag và từ khoá kề** trên TikTok/IG.

**Xong khi:** bảng độ phủ có một vòng `SỞ HỮU MỚI = 0`, và ghi rõ "similar dùng
được" hay "similar hỏng, đã mở rộng bằng cách khác".

---

## Bước 3 — Lọc sản phẩm SỞ HỮU khỏi hàng đi bán hộ

Đọc `references/nhan-dien-san-pham.md` mục 1 trước khi chấm.

Lấy link từ bốn chỗ, rẻ trước: caption TikTok/IG (đã có sẵn) → mô tả video +
comment ghim → link-in-bio → trang About. Bung link rút gọn về URL thật.

> **Luật ba bằng chứng.** Mỗi sản phẩm vào bảng phải có đủ: URL gốc · xuất hiện
> ở bao nhiêu bài trên bao nhiêu bài kiểm · lần đầu thấy khi nào. Thiếu một
> trong ba thì xếp `CHƯA XÁC MINH` — không xoá, không tính vào thống kê.

> **Luật chỉ nhận link thật.** `deep_channel_report` có khối
> `monetization.products[]` rất tiện nhưng nó **suy đoán**. Dòng mở đầu bằng
> "suggests potential for", "strongly indicates", "implied through" là AI đoán
> từ giọng văn. Chỉ nhận dòng có URL.

*Chuyện thật 12.09.2026: khối này trả 4 sản phẩm cho @fitfatherproject — 2 cái
suy đoán thuần, 3/4 không có giá. Bê nguyên vào bảng là ngách tự dưng có thêm 4
đối thủ không tồn tại.*

`channel_analytics` và `video_stats` **không trả link ngoài nào**. Đừng chờ.

**Xong khi:** mỗi creator gắn nhãn `SỞ HỮU` / `AFFILIATE` / `TÀI TRỢ` /
`CHƯA XÁC MINH`, mọi dòng `SỞ HỮU` có URL.

---

## Bước 4 — Dựng bảng sản phẩm: tầng · giá · tính năng · điểm nổi bật

Sáu cột bắt buộc: `tên · tầng · loại · giá · tính năng · điểm nổi bật`. Thiếu
cột nào ghi lý do (`giá ẩn — phải đăng ký`, `trang không liệt kê`), không bỏ
trống. Cách bóc từng cột ở file tra cứu, mục 2-4.

> **Luật ghi tầng trước.** `VAT_LY` / `DIGITAL` / `DICH_VU`. Ngách toàn DỊCH VỤ
> và ngách toàn DIGITAL là hai thị trường khác nhau dù số đối thủ bằng nhau:
> dịch vụ có trần công suất cứng nên luôn còn chỗ, digital thì người dẫn đầu
> nuốt hết. Đếm đối thủ mà không tách tầng là đếm sai.

> **Luật giá phải có ngày.** Mọi giá kèm URL và ngày kiểm. Giá không có ngày là
> giá sai — bảng giá đổi vài tháng một lần.

| | |
|---|---|
| SAI | Khoá loại này thường 200-500$ |
| ĐÚNG | $297 một lần · example.com/pricing · 2026-09-12 |

Tính năng trả lời *họ giao cái gì*. Điểm nổi bật trả lời *vì sao khách tin*. Hai
sản phẩm cùng tính năng mà khác điểm nổi bật là hai đối thủ khác nhau.

**Xong khi:** ≥15 dòng sản phẩm, mọi dòng có tầng, không dòng nào trống `url` và
`ngay_kiem`.

---

## Bước 5 — Dựng chân dung khách: tuổi · giới · quốc gia · sở thích

Bốn trục bắt buộc, mỗi trục một nhãn độ tin. Thiếu trục nào ghi "chưa đo được",
không bỏ dòng.

| Trục | Nguồn | Nhãn |
|---|---|---|
| Tự khai | câu trên trang bán: "for busy dads over 40" | `[FACT]` |
| Nỗi đau | `audienceInsights`, trích nguyên văn + link | `[FACT]` |
| Tuổi · giới | `demographics` trong `channel_analytics` | `[ƯỚC TÍNH]` |
| Quốc gia | `country` của N kênh + ngôn ngữ trang bán | `[ƯỚC TÍNH]` |
| Sở thích | `videoTags` lặp ở ≥5 kênh khác nhau | `[ƯỚC TÍNH]` |
| Khả năng chi trả | suy từ bậc giá họ đang mua | `[ƯỚC TÍNH]` |

> **Luật demographics không phải số đo.** Trường này trả kèm `estimated: true`
> và `ageSource: "topic"` — nó suy từ chủ đề kênh, **không đo người xem**. Vẽ
> hình thì được, kết luận thì không. Một câu tự khai trên trang bán đáng tin hơn
> cả bảng demographics.

> **Luật sở thích đếm theo kênh.** Tag lặp ở ≥5 kênh khác nhau mới là sở thích
> chung của nhóm. Lặp trong một kênh chỉ là thói quen của creator đó.

**Xong khi:** đủ bốn trục, mỗi trục có nhãn, ít nhất một dòng `[FACT]` trích
nguyên văn có link.

---

## Bước 6 — Đo độ hot bằng năm chỉ số, để riêng

```
1. Reach 90 ngày    Σ lượt xem của ngách theo tháng, ba tháng gần nhất
2. Mật độ outlier   % bài có Outlier Score ≥ 3 trên tổng bài quét
3. Kênh mới         số tài khoản lập trong 12 tháng, vẫn đang đăng
4. Sản phẩm mới     số sản phẩm SỞ HỮU ra mắt trong 12 tháng
5. Bão hoà          saturation.pct của 3-5 kênh lớn nhất
```

> **Luật không gộp điểm.** Cấm cộng năm chỉ số thành một "điểm độ hot". Số tổng
> hợp che mất chuyện ngách đang tăng reach rất nhanh mà không ai ra sản phẩm mới
> — đó mới là chỗ tốt nhất, và nó biến mất ngay khi bạn cộng lại.

| Reach | Sản phẩm mới | Nghĩa là |
|---|---|---|
| ↑ | ↑ | Nóng thật, vào phải nhanh |
| ↑ | → | Cầu lên, cung chưa theo — chỗ tốt nhất |
| → | ↑ | Chen nhau chia lại bánh cũ |
| ↓ | ↓ | Đang tắt, đừng vào |

**Xong khi:** năm số có cửa sổ thời gian và cỡ mẫu đi kèm.

---

## Bước 7 — Chấm matrix định vị, SWOT làm sau

```
Hai trục là hai thứ KHÁCH quan tâm
Chấm hết đối thủ đếm được lên đó
Khoảng trống hiện ra bằng mắt
SWOT làm sau, khi đã có bản đồ để so
```

> **Luật trục do khách chọn.** Trục phải là thứ khách cân nhắc khi móc ví, không
> phải thứ bạn tự hào. "Công nghệ hiện đại" không phải trục. "Bao lâu thì tôi
> thấy kết quả" mới là trục.

```
mcp__govrl__comment_analysis { videoId: <id>, title: <title> }   # 8-12 bài outlier
```

Thứ người xem khen và chê nhiều nhất chính là trục. Đưa 5-6 trục ứng viên cho
người dùng **chọn 2**, không tự chọn thay họ. Danh sách trục ở file bảng biểu.

> **Luật ô trống chưa phải cơ hội.** Ô trống có thể vì chỗ đó không ai mua. Mỗi
> ô trống trả lời một câu: *có bằng chứng nào cho thấy có người muốn mua ở đây
> không?* Không có thì ghi `[GIẢ THUYẾT CẦN KIỂM]`.

Bằng chứng đủ mạnh: có người hỏi thẳng trong comment (trích nguyên văn, có link)
· ngách kề đang bán đúng kiểu đó và sống được · có người đang trả tiền cho giải
pháp chắp vá.

SWOT làm **sau**, chỉ cho vị trí bạn định đứng — không SWOT cả ngách.

**Xong khi:** lưới hai trục đã chấm hết đối thủ, mỗi ô trống có nhãn bằng chứng.

---

## Bước 8 — Tính TAM/SAM/SOM bottom-up

> **Luật bottom-up.** Cấm chép TAM từ báo cáo thị trường. Tính ngược từ số đã
> đếm được ở Bước 1-5.

> **Luật dùng reach, không dùng subscriber.** Subscriber trùng nặng giữa các
> kênh và lạm phát theo thời gian.

```
NGƯỜI TRONG NGÁCH = (Σ lượt xem 30 ngày mọi kênh đã quét)
                    ÷ (số bài một người xem mỗi tháng)
                    × (1 − tỷ lệ trùng giữa các kênh)

TAM = NGƯỜI TRONG NGÁCH × ARPU năm
SAM = TAM × (% ngôn ngữ bạn phục vụ) × (% ở nền tảng bạn có mặt)
SOM = SAM × (% thị phần năm 1)

  Σ lượt xem 30 ngày   [FACT]       views30d, N kênh
  bài/người/tháng      [GIẢ ĐỊNH]   ghi con số bạn đặt và vì sao
  tỷ lệ trùng          [GIẢ ĐỊNH]   cùng ngách thường 30-50%
  ARPU năm             [ƯỚC TÍNH]   giá trung vị Bước 4 × số lần mua/năm
  % ngôn ngữ/nền tảng  [ƯỚC TÍNH]   từ quốc gia ở Bước 5
  % thị phần năm 1     [GIẢ ĐỊNH]   neo bằng đối thủ mới nhất mất bao lâu đạt X khách
```

> **Luật không lấy 1% của TAM.** "SOM = 1% TAM" là con số bịa quen thuộc nhất.
> SOM tính từ dưới lên: bao nhiêu người bạn thật sự chạm được trong 12 tháng ×
> tỷ lệ mua × giá.

In cả ba kịch bản thấp / cơ sở / cao. Một con số duy nhất là một con số bịa.

**Xong khi:** ba số có công thức, mọi thừa số có nhãn, đã in ba kịch bản.

---

## Bước 9 — Tìm khoảng trống theo NHÓM KHÁCH, không theo tính năng

Đừng tìm tính năng chưa ai làm. Tìm **nhóm người chưa ai chịu nhận**.

| Trục tách nhóm | Các nhóm |
|---|---|
| Trình độ | mới hoàn toàn · đang làm dở · muốn nâng |
| Hoàn cảnh | ít thời gian · ít tiền · thiếu cả hai |
| Động cơ | nghề chính · làm thêm · làm cho vui |
| Quốc gia / ngôn ngữ | nhóm bị bỏ rơi rõ nhất, dễ chiếm nhất |
| Tầng sản phẩm | muốn DỊCH VỤ trong ngách toàn DIGITAL, và ngược lại |

Ô đáng vào: nhóm **đau rõ + chưa ai phục vụ riêng + đã đang trả tiền cho thứ gần
giống**. Đau rõ mà chưa từng trả tiền cho gì thì không phải cơ hội, là sở thích.

**Xong khi:** tối đa 3 nhóm khách xếp hạng, mỗi nhóm có số người và giá họ đang
trả.

---

## Bước 10 — Kiểm khoảng trống bằng xu hướng xã hội

Một khoảng trống đúng mà đi ngược gió thì vẫn chết. Bước này để **loại bớt**,
không để thêm vào. Với mỗi khoảng trống ở Bước 9, trả lời ba câu:

```
1. Xu hướng nào đang đẩy nhóm khách này lớn lên hoặc nhỏ đi?
2. Xu hướng đó có ĐƯỜNG CONG không, hay chỉ là một câu chuyện hay?
3. Nếu xu hướng tắt trong 24 tháng, khoảng trống này còn không?
```

> **Luật xu hướng phải có đường cong.** Xu hướng không vẽ được đường tăng theo
> thời gian thì là câu chuyện kể, không phải xu hướng. Ghi `[CÂU CHUYỆN]` và
> không dùng nó để biện minh cho quyết định vào.

Ba nguồn đường cong, theo thứ tự tin: reach ngách theo tháng tính từ dữ liệu đã
quét · `mcp__govrl__trending_formats` · Google Trends 3-5 từ khoá lõi, 5 năm.
Bài báo và báo cáo ngành **không** phải đường cong.

Ba dạng, ba quyết định: **chuyển dịch dài** (lên đều 3-5 năm) vào được, xây dài
· **sóng ngắn** (dựng đứng dưới 12 tháng) vào nhanh thu nhanh, đừng xây nền ·
**câu chuyện** bỏ qua. Bảng khớp mẫu ở Hình 8.

**Đầu ra bắt buộc — USP một câu:**

```
<Sản phẩm> cho <nhóm khách cụ thể>, khác <đối thủ gần nhất> ở chỗ <một điểm duy nhất>.
```

Câu này phải trả lời được: vì sao khách chọn bạn mà không chọn cái chấm bên cạnh
trên lưới ở Bước 7. Viết không nổi một câu nghĩa là chưa tìm ra chỗ đứng.

**Xong khi:** mỗi khoảng trống gắn một trong ba dạng, kèm nguồn đường cong; và
có một câu USP không có chữ "và", không có chữ "cũng".

---

## Bước 11 — Xuất báo cáo dạng bảng và hình, không dạng bài viết

> **Luật ô sáu chữ.** Mỗi ô trong bảng tối đa sáu chữ. Cần dài hơn thì đưa xuống
> chú thích dưới bảng. Bảng chữ dày không ai đọc, và nó là cách nhanh nhất để
> giấu một con số yếu.

> **Luật số thay chữ.** Có số thì in số. "Nhiều đối thủ" → `31 đối thủ`. "Giá
> cao" → `$1.200`. "Đang tăng" → `↑ +34%`. Không có số thì ghi "chưa đo được",
> đừng thay bằng tính từ.

Tám hình bắt buộc, mẫu vẽ sẵn ở `references/mau-bang-bieu.md`:

```
1  Thanh xếp chồng TAM/SAM/SOM        5  Ma trận tính năng × sản phẩm (● ○)
2  Đếm đối thủ theo tầng và loại      6  Chân dung khách: tuổi·giới·quốc gia·sở thích
2b Bảng độ phủ                        7  Năm chỉ số độ hot, có mũi tên
3  Lưới matrix hai trục, có ô trống   8  Đường cong xu hướng 24 tháng
4  Histogram phân bổ giá
```

**Thứ tự file `niche-<ngach>-<YYYYMMDD>.md`:**

```
1. Năm câu trả lời            — mỗi câu một dòng, có số
2. VÀO / KHÔNG VÀO            — gắn với ngưỡng dừng Bước 0
3. USP một câu
4. Bảng độ phủ                — chứng minh đã quét tới bão hoà
5. Tám hình theo thứ tự trên
6. Bảng sản phẩm đầy đủ
7. Giả định tôi đã tự điền    ← bắt buộc, không được rỗng
8. Nguồn
```

Kèm `products-<ngach>-<YYYYMMDD>.csv` theo schema ở file tra cứu mục 6. Gửi cả
hai bằng SendUserFile.

**Xong khi:** đủ tám hình, bảng độ phủ có vòng bão hoà, năm câu đều có số hoặc
chữ "chưa trả lời được, vì…", mục Giả định không rỗng.

---

## Checklist trước khi giao

- [ ] Bảng độ phủ có một vòng `SỞ HỮU MỚI = 0` — đã quét tới bão hoà
- [ ] Đã kiểm ba dòng đầu `find_similar_channels`, ghi rõ dùng được hay hỏng
- [ ] Mọi sản phẩm trong bảng là `SỞ HỮU`, đủ ba bằng chứng
- [ ] Không dòng nào lấy từ `monetization.products[]` mà thiếu URL thật
- [ ] Mọi sản phẩm có tầng `VAT_LY` / `DIGITAL` / `DICH_VU`
- [ ] Mọi giá có URL và ngày kiểm
- [ ] Mỗi sản phẩm đủ: giá · tính năng · điểm nổi bật
- [ ] Chân dung khách đủ bốn trục: tuổi · giới · quốc gia · sở thích, có nhãn
- [ ] Đã lọc bỏ cộng đồng miễn phí khỏi số đếm đối thủ
- [ ] Năm chỉ số độ hot in riêng, không gộp thành một điểm
- [ ] TAM/SAM/SOM tính từ reach; ba kịch bản; mọi thừa số có nhãn
- [ ] SOM không phải một phần trăm nào đó của TAM
- [ ] Hai trục matrix do người dùng chọn từ 5-6 ứng viên rút từ comment
- [ ] Mỗi ô trống gắn `[CÓ BẰNG CHỨNG]` hoặc `[GIẢ THUYẾT CẦN KIỂM]`
- [ ] Mỗi khoảng trống có đường cong xu hướng, hoặc bị ghi `[CÂU CHUYỆN]`
- [ ] Đủ tám hình, không ô nào quá sáu chữ
- [ ] USP viết được trong một câu
- [ ] Kết luận là VÀO hoặc KHÔNG VÀO, không phải "tuỳ"
- [ ] Bạn đã đọc hết và sửa ít nhất một chỗ agent nói sai. Chưa tìm thấy chỗ sai
      nào thì gần như chắc chắn là chưa đọc kỹ

---

## Bảng tra nhanh

| Tình huống | Làm gì |
|---|---|
| YouTube trả `HTTP 429` | Chạy hết TikTok + Instagram, quay lại YouTube hôm sau |
| `find_similar_channels` trả kênh lệch ngách | Vứt kết quả, mở rộng bằng đồng xuất hiện |
| Vòng quét vẫn ra creator mới | Chưa bão hoà. Chạy tiếp, đừng viết báo cáo |
| Dưới 15 sản phẩm có giá | Không vẽ Hình 3, 4. Ghi "chưa đủ dữ liệu", mở rộng seed |
| Đa số ghi "giá ẩn" | Tín hiệu bán qua tư vấn, giá cao. Ghi nhận, đừng đoán |
| Ngách toàn cộng đồng miễn phí | Ý muốn trả tiền thấp. Cân nhắc KHÔNG VÀO |
| Ngách toàn DIGITAL, không ai làm DỊCH VỤ | Ứng viên khoảng trống tầng. Kiểm bằng Bước 10 |
| Đã có 30 sản phẩm tương tự | Xem 30 cái đó cùng bỏ rơi nhóm khách nào |
| Xu hướng chỉ có bài báo, không đường cong | `[CÂU CHUYỆN]`. Hạ khoảng trống đó xuống cuối |
| Không tách được nhóm khách nào trống | Đây là kết quả. Ghi KHÔNG VÀO và nêu lý do |
| Người dùng bảo "cứ chạy đi" | Tự điền, chạy, in mục giả định ở cuối |

## Nhớ một câu

Khoảng trống không nằm ở tính năng chưa ai làm. Nó nằm ở nhóm người chưa ai chịu
nhận.

## Skill này phải tự tốt lên

1. **Eval sau mỗi lần chạy.** Xong việc thì tự chấm ngắn theo checklist của
   skill: thiếu bước nào, chỗ nào người dùng phải sửa tay. Có chỗ đáng sửa thì
   đề xuất người dùng cập nhật thẳng vào file SKILL.md này.
2. **Thi thoảng lookup để update.** Giá, công cụ và cách các trang tổ chức dữ
   liệu đổi liên tục. Con số hay tên tool nào trong file đã vài tháng tuổi thì
   kiểm lại từ nguồn gốc trước khi tin.
3. **Không biết thì hỏi người.** Cái gì ngoài tầm thì nói thẳng và chỉ người
   dùng đi hỏi ai. Người thật là một nguồn trợ giúp, không phải chỉ có tài liệu.
