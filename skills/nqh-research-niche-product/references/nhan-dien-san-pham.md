# Nhận diện sản phẩm — sở hữu, phân loại, giá, tính năng

## 1. Sở hữu hay đi bán hộ

Chấm điểm mỗi link. Chỉ dòng `SỞ HỮU` mới được vào bảng thống kê.

| Cộng điểm — SỞ HỮU | Trừ điểm — LOẠI RA |
|---|---|
| Tên miền khớp tên kênh | `?ref=` `?aff=` `?a=` `/r/` `tag=` |
| Cùng domain ở ≥60% bài, 90 ngày | `utm_source=affiliate` |
| Slug riêng trên nền tảng bán | `impact.com` `shareasale` `cj.com` |
| Trang đích có mặt/tên creator | `partnerize` `amzn.to` `clickbank` |
| Có nút thanh toán thật | "use code" · "my discount" |
| Đang chạy ads cho chính domain đó | `#ad` · "sponsored by" · "thanks to" |
| | Xuất hiện <20% bài, dồn một cửa sổ ngắn |

**Slug riêng tính là sở hữu:**

```
*.kajabi.com      *.teachable.com     *.thinkific.com    *.podia.com
skool.com/<slug>  circle.so/<slug>    whop.com/<slug>    patreon.com/<slug>
gumroad.com/<slug>  stan.store/<slug>  lemonsqueezy.com/<slug>
calendly.com/<slug>  acuityscheduling.com/<slug>
*.substack.com    *.beehiiv.com       *.myshopify.com
```

> **Ngoại lệ phải nhớ.** Rất nhiều creator gắn tham số theo dõi vào link sản
> phẩm của CHÍNH HỌ để đếm đơn. Tham số chỉ trừ điểm khi **tên miền đích không
> khớp thương hiệu kênh**. Khớp thương hiệu luôn thắng tham số.

Bung mọi link rút gọn về URL cuối trước khi chấm: `bit.ly` `lnk.to` `rb.gy`
`tinyurl` `linktr.ee` `beacons.ai` `komi.io` `pillar.io` `stan.store`.

---

## 2. Ba tầng loại sản phẩm

Phân tầng trước, phân loại sau. Ba tầng này quyết định trần công suất và biên
lợi nhuận — hai thứ khác nhau hoàn toàn giữa các tầng.

```
VẬT LÝ     giao hàng thật, có tồn kho, biên thấp, nhân bản bằng tiền
DIGITAL    làm một lần bán nhiều lần, biên cao, trần công suất gần như vô hạn
DỊCH VỤ    đổi thời gian lấy tiền, biên cao nhưng trần công suất cứng
```

| Tầng | Loại con | Đơn vị giá |
|---|---|---|
| VẬT LÝ | `hang_vat_ly` merch, sách in, dụng cụ | một lần |
| | `thuc_pham_bo_sung` | một lần / định kỳ |
| DIGITAL | `khoa_quay_san` | một lần |
| | `template` preset, notion, prompt pack | một lần |
| | `ebook` guide, PDF | một lần |
| | `saas` app, tool, extension | tháng / năm |
| | `cong_dong` membership | tháng / năm |
| | `newsletter` bản trả phí | tháng / năm |
| DỊCH VỤ | `coaching_1_1` | giờ / gói |
| | `group_mastermind` | tháng / khoá |
| | `khoa_cohort` có lịch, có người dạy | khoá |
| | `dich_vu` done-for-you, agency | retainer / dự án |
| | `chung_chi` certification | khoá |

> **Luật ghi tầng trước.** Mỗi dòng sản phẩm ghi tầng rồi mới ghi loại. Ngách
> toàn DỊCH VỤ và ngách toàn DIGITAL là hai thị trường khác nhau, dù số đối thủ
> bằng nhau: một bên trần công suất cứng nên luôn còn chỗ, một bên người dẫn đầu
> nuốt hết.

---

## 3. Bóc giá

Bốn cách, dừng ở cách đầu tiên thành công:

1. JSON-LD `Product` / `Offer` trong đầu trang — chính xác tuyệt đối
2. Embed thanh toán Stripe / Paddle / Lemon Squeezy — có cả chu kỳ
3. Con số quanh nút mua: `$X` · `/mo` · `one-time` · `VNĐ`
4. Không thấy → ghi **"giá ẩn — phải đăng ký"**. Không đoán, không nội suy

Ghi đủ: `so_tien · don_vi_tien · chu_ky · ten_bac · url · ngay_kiem · do_tin`

`chu_ky` chọn trong: `mot_lan` · `thang` · `nam` · `gio` · `nop_don`

> **Luật giá phải có ngày.** Giá không có ngày là giá sai. SaaS và khoá học đổi
> bảng giá vài tháng một lần.

| | |
|---|---|
| SAI | Khoá loại này thường 200-500$ |
| ĐÚNG | $297 một lần · example.com/pricing · 2026-09-12 |

---

## 4. Tính năng và điểm nổi bật — hai thứ khác nhau

| | Lấy ở đâu | Dùng để |
|---|---|---|
| **Tính năng** | gạch đầu dòng trên trang bán, dòng trong bảng giá | dựng ma trận có/không |
| **Điểm nổi bật** | headline, câu trên nút mua, bảo chứng, cam kết | hiểu họ bán bằng lý do gì |

Tính năng trả lời *họ giao cái gì*. Điểm nổi bật trả lời *vì sao khách tin*.
Hai sản phẩm cùng tính năng mà khác điểm nổi bật là hai đối thủ khác nhau.

Điểm nổi bật thường gặp — gom về các nhóm này:

```
BẢO CHỨNG      bằng cấp, số năm, kết quả cá nhân, được báo nhắc tên
SỐ ĐÔNG        "12.000 học viên", ảnh trước-sau, đánh giá sao
GIẢM RỦI RO    hoàn tiền, học thử, trả góp, cam kết kết quả
TỐC ĐỘ         "7 ngày", "kết quả tuần đầu"
ĐỘC QUYỀN      giới hạn suất, xét duyệt đầu vào, chỉ mở theo đợt
CÁ NHÂN HOÁ    "thiết kế riêng cho bạn", kèm 1:1
```

Gom các cách gọi tính năng khác nhau về một tên chuẩn trước khi dựng ma trận,
nếu không ma trận sẽ toàn ô trống giả.

---

## 5. Thang giá thị trường — để đối chiếu, không phải để kết luận

| Loại | Khoảng | Median | Nguồn · cỡ mẫu |
|---|---|---|---|
| Khoá quay sẵn | $49–357 | $150 | Ruzuku, 11.691 khoá |
| Khoá cohort | $399–4.999 | $1.898 | Ruzuku, 408 chương trình |
| Cộng đồng | $10–49/th | $29–147 theo ngách | Skool, 2.629 nhóm, 05/2026 |
| Coaching 1:1 | $193–270/h | $234/h | ICF 2025, n=8.916 coach |
| Template | $9–47 | $27–40 | Gumroad, 146.271 sp |
| Ebook | $29–49 | ~$50/đơn | Gumroad, 1.049 ebook |
| Micro-SaaS | $8–29/th | $25/th | Outmano, 651 trang giá |
| Dịch vụ DFY | retainer $500–1K | $2.917/th | Ahrefs, n=439 |
| Newsletter | $10/th | $96/năm | Substack, 20.000 bản |
| Supplement | AOV $45–120 | — | Eightx, 35+ brand |
| Chứng chỉ | — | — | không có nguồn có cỡ mẫu |

**Hai cái bẫy khi đọc bảng này:**

- Median khoá quay sẵn là **$150**, không phải $997. Ngách của bạn toàn $997 thì
  hoặc ngách đó đặc biệt, hoặc mẫu bị lệch — kiểm lại trước khi neo giá.
- Khoảng **70% cộng đồng trên Skool miễn phí**. Đếm cung mà không lọc nhóm miễn
  phí sẽ thổi phồng số đối thủ lên gấp ba.

Số trong bảng lấy từ khảo sát và scrape công khai, kiểm 09/2026. Quá vài tháng
thì kiểm lại từ nguồn gốc.

---

## 6. Schema CSV xuất ra

```csv
creator,platform,quy_mo,ten_san_pham,tang,loai,gia,don_vi_tien,chu_ky,
tinh_nang_loi,diem_noi_bat,doi_tuong_khach,do_tuoi,quoc_gia,so_thich,
url,so_bai_xuat_hien,tong_bai_kiem,lan_dau_thay,ngay_kiem,nhan_so_huu,do_tin
```

- `tang` = `VAT_LY` / `DIGITAL` / `DICH_VU`
- `nhan_so_huu` = `SO_HUU` / `AFFILIATE` / `TAI_TRO` / `CHUA_XAC_MINH`
- `do_tin` = `FACT` / `UOC_TINH` / `GIA_DINH`
- `url` và `ngay_kiem` không được để trống ở bất kỳ dòng `SO_HUU` nào
