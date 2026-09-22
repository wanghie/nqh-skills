# Mẫu bảng biểu — tám hình bắt buộc

Vẽ theo đúng mẫu dưới. Số trong ví dụ là số giả để thấy hình dạng — thay bằng số
thật khi chạy.

Hai luật áp cho mọi hình:

- **Ô sáu chữ.** Mỗi ô tối đa sáu chữ. Dài hơn thì xuống chú thích dưới bảng.
- **Số thay chữ.** Có số thì in số. Không có thì ghi "chưa đo được", không thay
  bằng tính từ.

Ký hiệu dùng chung: `●` có · `○` không · `◐` một phần · `↑` tăng · `↓` giảm ·
`→` đứng yên · `▓` ô trống đáng chú ý.

---

## Hình 1 — TAM / SAM / SOM

Thanh xếp chồng, không vẽ vòng tròn lồng nhau. Terminal đọc thanh dễ hơn.

```
                                                NGƯỜI        TIỀN/NĂM
TAM  ████████████████████████████████████████  2.400.000     $120M
SAM  ██████████                                  740.000      $37M
SOM  █                                             5.200     $780K

Kịch bản        THẤP        CƠ SỞ        CAO
SOM người        2.100       5.200      11.400
SOM tiền         $315K       $780K       $1,7M
```

Dưới hình, in đúng công thức và nhãn từng thừa số. Không có công thức thì hình
này vô nghĩa.

---

## Hình 2 — Đếm đối thủ theo tầng và loại

Tách tầng trước, loại sau. Cột `SỐ` không nói lên gì nếu không biết tầng.

```
TẦNG       LOẠI              SỐ   CÓ GIÁ   GIÁ GIỮA
DIGITAL    Khoá quay sẵn     14      11      $180
           Cộng đồng          9       7    $39/th
           Template           5       5       $29
           Micro-SaaS         2       2    $19/th
           ─────────────     ──      ──
           cộng              30      25

DỊCH VỤ    Coaching 1:1       6       3    $250/h
           Khoá cohort        3       2    $1.400
           Done-for-you       1       0    giá ẩn
           ─────────────     ──      ──
           cộng              10       5

VẬT LÝ     Supplement         2       2       $59
           ─────────────     ──      ──
           cộng               2       2

TỔNG                         42      32

Đã bỏ: 12 cộng đồng miễn phí · 4 chưa xác minh
```

Hai dòng bắt buộc dưới hình:

- **"Đã bỏ"** — không lọc nhóm miễn phí thì số đối thủ phồng lên nhiều lần.
- **Độ lệch tầng** — ví dụ `DIGITAL 71% · DỊCH VỤ 24% · VẬT LÝ 5%`. Tầng nào
  dưới 10% là ứng viên khoảng trống tầng, đem sang Bước 10 kiểm.

---

## Hình 2b — Bảng độ phủ

In trước mọi hình khác. Nó chứng minh báo cáo đã quét tới bão hoà.

```
VÒNG   QUÉT   MỚI   SỞ HỮU MỚI   SP MỚI
1        40    40        14        19
2        73    33         9        12
3       104    31         3         4
4       131    27         0         0   ← bão hoà, dừng
```

Không có vòng `SỞ HỮU MỚI = 0` thì báo cáo chưa xong. Mọi con số phía sau đều
nhỏ hơn sự thật.

---

## Hình 3 — Lưới matrix định vị

```
                    GIÁ CAO
                       │
                       │
      ● Kênh D         │         ● Kênh A
        $1.900         │           $2.400
                       │
      ● Kênh F         │    ▓ TRỐNG
        $890           │      $600-1.200
  ─────────────────────┼─────────────────────
      TỰ HỌC           │              KÈM 1:1
                       │
      ● Kênh B  ● Kênh C         ● Kênh E
        $49      $99               $290/th
                       │
                    GIÁ THẤP

▓  Ô trống · $600-1.200 · kèm 1:1   [CÓ BẰNG CHỨNG]
   "I'd pay for someone to check my form weekly but can't do $2k"
   — comment video abc123, 2026-08
```

Mỗi ô trống phải có ba dòng: toạ độ, nhãn bằng chứng, và một câu trích nguyên
văn có link. Không có trích dẫn thì nhãn là `[GIẢ THUYẾT CẦN KIỂM]`.

**Trục thường gặp — đưa 5-6 cái này cho người dùng chọn 2:**

| Trục | Đầu thấp | Đầu cao |
|---|---|---|
| Giá | vài chục đô | vài nghìn đô |
| Mức cầm tay | tự học một mình | kèm 1:1 hàng tuần |
| Phạm vi | dạy cho mọi người | chuyên một nhóm |
| Tốc độ kết quả | vài tháng | 7 ngày |
| Mức làm hộ | dạy để tự làm | làm hộ luôn |
| Trình độ người mua | mới hoàn toàn | đã có nền |
| Định dạng | nội dung | phần mềm |

---

## Hình 4 — Histogram phân bổ giá

```
$0-29      ████████████████████  23
$30-99     ██████████████        14
$100-299   ▒▒                     2   ← lõm
$300-999   ▒                      1   ← lõm
$1.000+    ████████               9

Median $150 · n=49 sản phẩm có giá thật · 2026-09-12
```

`▒` đánh dấu bậc dưới ngưỡng. Cần ≥12 sản phẩm có giá thật mới được vẽ hình này;
dưới ngưỡng thì bỏ hình, ghi "chưa đủ dữ liệu".

Một cái lõm **chưa phải cơ hội** — có thể chỗ đó không ai mua. Đặt thẳng câu hỏi
đó dưới hình.

---

## Hình 5 — Ma trận tính năng × sản phẩm

```
TÍNH NĂNG           A    B    C    D    E     CÓ
Kèm 1:1             ●    ○    ●    ○    ●    3/5
Cộng đồng riêng     ●    ●    ○    ●    ●    4/5
Giáo án in được     ●    ●    ●    ●    ●    5/5
App theo dõi        ○    ○    ○    ●    ○    1/5
Hoàn tiền           ●    ○    ●    ○    ○    2/5
Tiếng Việt          ○    ○    ○    ○    ○    0/5   ← trống

GIÁ              $297 $49 $1.9K $19/th $290/th
```

Dòng `CÓ` ở cuối cho thấy tính năng nào ai cũng có (không phải lợi thế) và tính
năng nào chưa ai làm. Hàng `0/5` là ứng viên khác biệt — nhưng vẫn phải qua luật
ô trống ở Hình 3.

---

## Hình 6 — Chân dung khách hàng

Bốn trục. Thiếu trục nào thì ghi "chưa đo được", không bỏ dòng.

```
TUỔI       18-24  ████████          22%
           25-34  █████████         24%
           35-44  ████████          21%
           45-54  █████             14%
           55+    █████             15%

GIỚI       Nam    ███████████████   75%
           Nữ     ████              23%

QUỐC GIA   Mỹ     ██████████        48%
           Anh    ████              18%
           Úc     ███               12%
           Khác   █████             22%

SỞ THÍCH   gym tại nhà      ██████████   31 kênh
           ăn kiêng ít carb ███████      22
           chạy bộ          █████        16
           bóng đá          ███           9
           làm vườn         ██            6

TỰ KHAI    "for busy dads over 40 who travel for work"
           fitfatherproject.com · 2026-09-12

NHÃN       tuổi · giới : [ƯỚC TÍNH]  demographics, estimated=true, nguồn=topic
           quốc gia    : [ƯỚC TÍNH]  country của 42 kênh
           sở thích    : [ƯỚC TÍNH]  videoTags lặp ở ≥5 kênh khác nhau
           tự khai     : [FACT]      câu nguyên văn trên trang bán
```

Hai luật cho hình này:

- **Khối NHÃN bắt buộc.** `demographics` suy từ chủ đề kênh, **không đo người
  xem** — vẽ hình thì được, kết luận thì không. Một câu tự khai trên trang bán
  đáng tin hơn cả bảng demographics.
- **Sở thích đếm theo số KÊNH, không theo số bài.** Tag lặp ở ≥5 kênh khác nhau
  mới là sở thích chung của nhóm; lặp trong một kênh chỉ là thói quen của
  creator đó.

---

## Hình 7 — Năm chỉ số độ hot

```
CHỈ SỐ              XU HƯỚNG   SỐ            CỬA SỔ / MẪU
Reach                  ↑       12,4M→16,6M   90 ngày, 37 kênh
Mật độ outlier         —       18%           142/790 bài
Kênh mới               ↑       11            12 tháng
Sản phẩm mới           →       2             12 tháng
Bão hoà                —       54%           4 kênh lớn

ĐỌC: reach ↑ + sản phẩm mới → = cầu lên, cung chưa theo
```

Năm dòng để riêng. Cấm cộng thành một điểm — gộp lại là mất đúng tín hiệu đáng
giá nhất.

Cột `CỬA SỔ / MẪU` bắt buộc. Con số không có cỡ mẫu là con số không kiểm được.

---

## Hình 8 — Đường cong xu hướng 24 tháng

Một khoảng trống đúng mà đi ngược gió thì vẫn chết. Hình này để **loại bớt**,
không để thêm vào.

```
REACH NGÁCH THEO THÁNG (triệu lượt xem)

 20 │                                        ▁▃▅
 15 │                            ▁▂▄▅▆▇██████████
 10 │            ▁▂▃▄▅▆▇████████████
  5 │  ▁▂▃▄▅▆▇███████
  0 └──────────────────────────────────────────────
    2024-10        2025-04        2025-10     2026-09

    Nguồn: Σ views30d, 42 kênh, tính lùi 24 tháng   [FACT]
    Dạng:  lên đều, không đỉnh nhọn → CHUYỂN DỊCH DÀI
```

Ba dạng đường cong, ba quyết định khác nhau:

| Dạng | Dấu hiệu | Làm gì |
|---|---|---|
| **Chuyển dịch dài** | lên đều 3-5 năm, không đỉnh nhọn | Vào được, xây dài |
| **Sóng ngắn** | dựng đứng dưới 12 tháng, có đỉnh | Vào nhanh, thu nhanh, đừng xây nền |
| **Câu chuyện** | không vẽ được đường nào | Bỏ qua, đừng dựa vào |

Bảng khớp khoảng trống với xu hướng — mỗi khoảng trống một dòng:

```
KHOẢNG TRỐNG              XU HƯỚNG ĐẨY          DẠNG          CÒN SAU 24TH?
Kèm 1:1 tầm $600-1.2K     giá coaching tăng     dài            Còn
Bản tiếng Việt            chưa có đường cong    câu chuyện     Chưa rõ
App theo dõi tự động      AI rẻ đi              dài            Còn
Gói 7 ngày                sóng "75 hard"        ngắn           Có thể hết
```

> **Luật xu hướng phải có đường cong.** Xu hướng không vẽ được đường tăng theo
> thời gian thì là câu chuyện kể, không phải xu hướng. Ghi `[CÂU CHUYỆN]` và
> không dùng nó để biện minh cho quyết định vào.

Ba nguồn đường cong, theo thứ tự tin: reach ngách theo tháng tính từ dữ liệu đã
quét · `mcp__govrl__trending_formats` · Google Trends 3-5 từ khoá lõi, 5 năm.
Bài báo và báo cáo ngành **không** phải đường cong.

---

## Bảng nhóm khách × ai đang phục vụ

Không tính vào bảy hình bắt buộc, nhưng nên có ở Bước 8.

```
NHÓM KHÁCH            AI PHỤC VỤ   TỐT (1-5)   HỌ TRẢ      TRỐNG
Mới, ít tiền          B, C              4       $49-99       ○
Mới, ít thời gian     —                 —       —            ●
Đang làm dở           A, D              3       $297-1.9K    ○
Đã có nền, muốn nâng  A                 2       $2.4K        ◐
Nói tiếng Việt        —                 —       —            ●

● trống hẳn   ◐ phục vụ yếu   ○ đã có người
```

Ô `●` có giá trị khi nhóm đó **đã đang trả tiền cho thứ gần giống**. Nhóm chưa
từng trả tiền cho gì không phải cơ hội, là sở thích.
