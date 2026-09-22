---
name: nqh-appstore-shots
description: "Dựng bộ ảnh App Store (iOS) chuẩn spec Apple và đẹp để duyệt — research đối thủ, chốt kịch bản 6 khung, viết caption, render PNG đúng pixel, QC luật review. Dùng khi cần bộ ảnh mới lên store, hoặc bộ ảnh cũ bị Apple từ chối. Kích hoạt khi nói 'làm ảnh App Store', 'screenshot app store', 'ảnh lên store', 'bị reject ảnh'."
---

# nqh-appstore-shots — Bộ ảnh App Store chuẩn duyệt, đẹp, và bán được

Mục tiêu: ra một bộ 5–7 ảnh App Store (iOS) **đúng pixel Apple yêu cầu**, **không dính luật review**, và **chuyển đổi tốt** (2 ảnh đầu quyết định phần lớn lượt cài).

Mặc định dựng bằng **HTML + Playwright → PNG**. Chỉ chuyển sang Figma khi Hiếu nói muốn chỉnh tay (xem Phụ lục C).

---

## 5 luật bất di bất dịch

Vi phạm 1 trong 5 = ảnh bị từ chối hoặc app bị reject. Kiểm tra trước khi làm bất cứ việc gì khác.

1. **Chỉ dùng màn hình THẬT của app.** Không vẽ UI tưởng tượng, không ghép tính năng chưa có. Nếu chưa có ảnh chụp thật → dừng lại, hỏi xin, không tự bịa. (Guideline 2.3.1, 2.3.3)
2. **Không dùng splash screen, màn login, logo art làm ảnh đầu.** Ảnh phải cho thấy app đang được dùng. (2.3.3)
3. **Không có giá, khuyến mãi, "Free", "Sale 50%", "Download now" trong ảnh.** (2.3.7)
4. **Không có tên/icon/khung máy Android, Google Play, hay nền tảng khác.** (2.3.10)
5. **Không có nội dung placeholder, "Lorem ipsum", "Beta", dữ liệu cá nhân thật.** Dữ liệu trong ảnh phải là tài khoản hư cấu nhưng trông thật. (2.1, 2.2)

---

## Bước 0 — Thu input (hỏi gọn, tối đa 1 lượt)

Cần đủ 5 thứ, thiếu thì hỏi:

| Input | Ghi chú |
|---|---|
| Tên app + 1 câu app làm gì cho ai | Dùng để viết caption |
| 6–10 ảnh chụp màn hình THẬT | PNG từ Simulator hoặc máy thật, đúng độ phân giải gốc |
| Màu brand + font | Nếu không có, lấy từ icon app |
| 3 đối thủ cùng ngách | Tên app hoặc link App Store |
| Ngôn ngữ ảnh | Tiếng Việt / tiếng Anh / cả hai |

Ảnh chụp chuẩn từ Simulator (đúng pixel, không có thanh trạng thái lỗi):

```bash
xcrun simctl io booted screenshot ~/Desktop/shot-01.png
# Chỉnh status bar cho đẹp và nhất quán:
xcrun simctl status_bar booted override --time "9:41" --batteryState charged --batteryLevel 100 --cellularBars 4 --wifiBars 3
```

---

## Bước 1 — Research đối thủ (bắt buộc, đừng bỏ)

Mở App Store 3 đối thủ, bóc đúng 4 thứ cho mỗi app:

1. Ảnh 1 của họ nói **kết quả** gì (outcome) hay chỉ khoe **tính năng**?
2. Caption dài bao nhiêu từ, đặt trên hay dưới?
3. Có khung máy (device frame) không? Nền đặc, gradient, hay ảnh?
4. Ảnh nào bị lặp ý — đó là chỗ mình thắng.

Ghi thành bảng 3 cột rồi **chọn hướng khác biệt**, không copy. Nếu cả 3 đối thủ đều nền tối gradient tím → mình đi nền sáng hoặc màu đặc.

---

## Bước 2 — Chốt kịch bản 6 khung

Mỗi khung = 1 ý, không nhồi. Khung 1–2 làm kỹ nhất vì trang App Store chỉ hiện 2–3 ảnh đầu khi chưa vuốt.

| # | Vai trò | Nội dung |
|---|---|---|
| 1 | **Kết quả** | Người dùng ĐƯỢC GÌ sau khi dùng app. Không phải "app có tính năng X" |
| 2 | **Cách làm** | Màn hình lõi giải thích app hoạt động thế nào |
| 3 | **Tính năng mạnh nhất** | Thứ đối thủ không có |
| 4 | **Chiều sâu** | Cho thấy app không hời hợt (dữ liệu, lịch sử, tuỳ chỉnh) |
| 5 | **Bằng chứng** | Số liệu thật, review thật có nguồn, hoặc trước–sau. KHÔNG bịa rating |
| 6 | **Mở rộng** | Widget, Apple Watch, đồng bộ, offline — tuỳ app |

5 ảnh chắc chắn hơn 10 ảnh lặp ý. Apple cho 1–10 ảnh mỗi cỡ máy.

---

## Bước 3 — Viết caption

Luật:

- **Tối đa 6 từ** cho dòng tiêu đề, 2 dòng là kịch trần.
- Nói **kết quả cụ thể**, cấm từ mơ hồ: "all-in-one", "tối ưu trải nghiệm", "giải pháp toàn diện", "nâng tầm".
- Động từ đứng đầu câu khi được: "Theo dõi chi tiêu trong 5 giây" > "Tính năng theo dõi chi tiêu".
- Không dấu chấm cuối câu tiêu đề.
- Không viết hoa toàn bộ trừ khi brand yêu cầu.
- Nếu có dòng phụ: tối đa 10 từ, cỡ chữ bằng 45–50% dòng chính.

Test nhanh: thu ảnh về chiều rộng 140px (kích thước thumbnail trên App Store). Nếu không đọc được caption → chữ quá nhỏ hoặc quá nhiều chữ.

---

## Bước 4 — Dựng HTML

Canvas mặc định **1320 × 2868** (iPhone 6.9", cỡ duy nhất Apple bắt buộc). Render 1 file HTML chứa toàn bộ các khung, mỗi khung là một `<section class="shot">`.

Lưới an toàn cho canvas 1320×2868:

| Vùng | Giá trị |
|---|---|
| Lề trái/phải | 96px |
| Caption block | y = 150 → 640px |
| Cỡ chữ tiêu đề | 96–120px, weight 700–800, line-height 1.08 |
| Cỡ chữ dòng phụ | 48–56px, weight 400–500, opacity .75 |
| Ảnh máy | bắt đầu y ≈ 720px, rộng 1060px, bo góc 88px |
| Khoảng chừa dưới | ≥ 80px (tránh bị crop) |

Template gốc:

```html
<!doctype html>
<meta charset="utf-8">
<style>
  :root{
    --bg:#0B0B0F; --ink:#FFFFFF; --accent:#7C5CFF; --sub:rgba(255,255,255,.72);
    --W:1320px; --H:2868px;
  }
  *{margin:0;padding:0;box-sizing:border-box}
  body{background:#333}
  .shot{
    width:var(--W); height:var(--H); position:relative; overflow:hidden;
    background:var(--bg);
    font-family:"SF Pro Display",-apple-system,"Inter","Helvetica Neue",sans-serif;
    color:var(--ink); display:flex; flex-direction:column; align-items:center;
  }
  .glow{position:absolute;width:1400px;height:1400px;border-radius:50%;
        background:radial-gradient(circle,var(--accent) 0%,transparent 62%);
        opacity:.32;top:-420px;left:-260px;filter:blur(40px)}
  .cap{position:relative;z-index:2;padding:150px 96px 0;text-align:center;width:100%}
  .cap h1{font-size:108px;font-weight:800;line-height:1.08;letter-spacing:-.02em}
  .cap p{margin-top:28px;font-size:52px;font-weight:450;color:var(--sub);line-height:1.3}
  .device{position:relative;z-index:2;margin-top:auto;width:1060px;
          border-radius:88px;overflow:hidden;
          box-shadow:0 60px 140px rgba(0,0,0,.55);
          border:10px solid rgba(255,255,255,.10);
          transform:translateY(120px)}
  .device img{display:block;width:100%}
</style>

<section class="shot">
  <div class="glow"></div>
  <div class="cap">
    <h1>Biến kỷ luật thành<br>điểm kinh nghiệm</h1>
    <p>Mỗi thói quen hoàn thành là một lần lên cấp</p>
  </div>
  <div class="device"><img src="shots/shot-01.png"></div>
</section>
<!-- lặp lại section cho từng khung -->
```

Quy tắc thẩm mỹ:

- **Một hệ màu xuyên suốt cả bộ.** Đổi accent giữa các khung = trông rời rạc.
- Nền: màu đặc hoặc gradient 2 điểm. Tránh ảnh stock làm nền.
- Ảnh máy: cắt tràn đáy (`translateY`) tạo cảm giác chiều sâu, hoặc bo tròn full nếu UI là trọng tâm.
- Khung máy (device frame) là **tuỳ chọn**, không bắt buộc. Dùng khi cần bối cảnh phần cứng; bỏ khi UI tự nó là câu chuyện.
- Đừng nghiêng máy 3D ở khung 1. Thẳng, rõ, dễ đọc.

---

## Bước 5 — Render PNG đúng pixel

```bash
npm i -D playwright  # container đã có chromium, KHÔNG chạy playwright install
```

```js
// render.mjs
import { chromium } from 'playwright';
const W = 1320, H = 2868;
const b = await chromium.launch({ executablePath: process.env.CHROME_PATH || undefined });
const p = await b.newPage({ viewport:{width:W,height:H}, deviceScaleFactor:1 });
await p.goto('file://' + process.cwd() + '/shots.html');
const n = await p.locator('.shot').count();
for (let i = 0; i < n; i++) {
  await p.locator('.shot').nth(i).screenshot({
    path: `out/appstore-${String(i+1).padStart(2,'0')}.png`,
    scale: 'css'
  });
}
await b.close();
```

**Bắt buộc làm phẳng alpha** — Apple từ chối PNG có kênh alpha:

```bash
python3 - <<'PY'
from PIL import Image; import glob
for f in glob.glob('out/*.png'):
    Image.open(f).convert('RGB').save(f)
PY
```

Kiểm tra lại:

```bash
python3 -c "from PIL import Image;import glob;[print(f, Image.open(f).size, Image.open(f).mode) for f in sorted(glob.glob('out/*.png'))]"
# Phải ra: (1320, 2868) RGB — sai 1 pixel là App Store Connect chặn upload
```

---

## Bước 6 — QC checklist (chạy trước khi giao)

**Kỹ thuật**

- [ ] Đúng 1320×2868 (hoặc cỡ 6.9" khác: 1290×2796, 1260×2736) — tất cả ảnh cùng một cỡ
- [ ] Mode `RGB`, không alpha, không ICC lạ
- [ ] Định dạng .png hoặc .jpg, 1–10 ảnh
- [ ] Nếu app chạy iPad: có thêm bộ 13" (2064×2752)

**Nội dung**

- [ ] Mọi UI trong ảnh đều là màn hình thật của app
- [ ] Ảnh 1 không phải splash/login
- [ ] Không có giá, "Free", "Sale", "Download"
- [ ] Không có Android / Google Play / nền tảng khác
- [ ] Không dữ liệu cá nhân thật, không placeholder
- [ ] Rating/review (nếu có) là thật và ghi được nguồn
- [ ] Status bar nhất quán (9:41, pin đầy) ở mọi ảnh

**Chuyển đổi**

- [ ] Thu về 140px vẫn đọc được caption khung 1 và 2
- [ ] Mỗi khung một ý, không lặp
- [ ] Caption nói kết quả, không nói tính năng suông
- [ ] Cả bộ nhìn như một hệ thống, không rời rạc

---

## Bước 7 — Bàn giao

Giao đúng 3 thứ:

1. Thư mục `out/` chứa PNG đã đặt tên theo thứ tự upload
2. Bảng caption (để Hiếu sửa chữ mà không cần dựng lại)
3. 1 dòng ghi chú: cỡ nào bắt buộc, cỡ nào Apple tự scale

Gợi ý A/B: App Store có **Product Page Optimization**, test tối đa 3 phương án trong 90 ngày. Test có giả thuyết rõ (ảnh 1 nói kết quả vs nói tính năng), không test bừa.

---

## Phụ lục A — Spec kích thước Apple (bản rút gọn)

**iPhone — bắt buộc cỡ 6.9"**, các cỡ khác Apple tự scale:

| Cỡ | Dọc | Ngang |
|---|---|---|
| 6.9" | 1320×2868 · 1290×2796 · 1260×2736 | đảo ngược |
| 6.5" | 1284×2778 · 1242×2688 | đảo ngược |
| 6.3" | 1206×2622 · 1179×2556 | đảo ngược |

**iPad — bắt buộc cỡ 13"** nếu app chạy iPad:

| Cỡ | Dọc | Ngang |
|---|---|---|
| 13" | 2064×2752 · 2048×2732 | đảo ngược |
| 11" | 1488×2266 · 1668×2388 | đảo ngược |

Chung: 1–10 ảnh, .png/.jpg/.jpeg, **không alpha, không trong suốt**. Mac 16:10 (1280×800…2880×1800), Apple Watch phải dùng cùng một cỡ cho mọi ngôn ngữ.

---

## Phụ lục B — Điều luật hay dính

| Guideline | Nội dung |
|---|---|
| 2.3.1 | Quảng bá sai — khoe tính năng app không có |
| 2.3.3 | Ảnh không cho thấy app đang được dùng (splash, login, title art) |
| 2.3.7 | Giá, điều khoản, mô tả không thuộc loại metadata đó |
| 2.3.10 | Nhắc nền tảng khác (Android, Google Play) |
| 2.1 | Nội dung placeholder, web rỗng |
| 2.2 | Bản beta/demo/trial |

Bị reject ảnh thì **không cần build mới** — sửa ảnh rồi submit lại metadata là đủ.

---

## Phụ lục C — Nhánh Figma (khi Hiếu muốn chỉnh tay)

Chỉ dùng khi được yêu cầu. Quy trình:

1. Làm xong Bước 1–3 như bình thường (research, kịch bản, caption).
2. Dùng Figma MCP tạo file mới, mỗi khung 1 frame đúng 1320×2868, đặt tên `01 — Outcome`, `02 — How it works`…
3. Tạo component cho caption block và device mask để sửa một chỗ ăn cả bộ.
4. Upload ảnh chụp thật vào frame bằng `upload_assets`.
5. Export ra PNG 1x, rồi vẫn chạy bước làm phẳng alpha ở Bước 5 trước khi upload.

---

## Liên quan

- `nqh-app-landing` — landing page cho app, dùng chung nghiên cứu đối thủ và copy
- `nqh-app-designer` — dựng UI màn hình app (dùng TRƯỚC skill này nếu app chưa có màn hình)

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
  chính file này, rồi nói ra `Đã ghi vào SỔ LỖI của nqh-appstore-shots: SAI … → ĐÚNG …`.
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
