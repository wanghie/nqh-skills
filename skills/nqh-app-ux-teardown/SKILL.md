---
name: nqh-app-ux-teardown
description: Bóc UX app đối thủ thành quyết định sản phẩm — bóc 3 app một lượt để tách quy ước ngành khỏi lựa chọn riêng, kiểm điều kiện chuyển giao trước khi mượn cơ chế, đếm friction và vị trí paywall, gắn cờ cơ chế ĐỘC, số motion chỉ lấy từ video đo bằng ffmpeg. Kích hoạt khi nói "bóc UX app", "teardown UX", "bóc hiệu ứng của", "app này UX thế nào", "nghiên cứu app đối thủ". KHÁC nqh-app-landing (kia dựng trang bán app) và nqh-research-teardown (kia bóc ruột kỹ thuật để build lại).
---

# /nqh-app-ux-teardown

Bóc một app không phải là kể lại nó có màn nào. Việc của skill này là biến một
app đã thắng thành **quyết định cho app mình** — và chặn đúng cái bẫy đắt nhất
của nghề: bê nguyên cơ chế của họ về mà không hỏi cơ chế đó sống nhờ điều kiện
gì.

Ba nguyên tắc chi phối cả file:

1. **Bóc ba app, không bóc một.** Một app cho một điểm dữ liệu, không phân biệt
   được quy ước ngành với lựa chọn riêng.
2. **Cơ chế nào cũng có điều kiện sống.** Không kiểm điều kiện thì đang cargo-cult.
3. **Số nào cũng phải truy được về nguồn.** Cấu trúc từ ảnh, chuyển động từ
   video, còn lại gắn nhãn `[SUY ĐOÁN]`.

Nền phương pháp đầy đủ (10 heuristic Nielsen, walkthrough, Hooked, B=MAP, bảng
số Material/Apple, nguyên lý Growth.Design) nằm ở artifact **Sổ tay bóc UX**.

## Dùng khi nào

- Sắp dựng app, muốn biết ngách này ai đã giải xong cái gì
- Thích cảm giác của một app nhưng chưa gọi được tên thứ mình thích
- Cần quyết định một luồng khó: onboarding, xin quyền, đặt paywall
- Cần bộ số motion đưa cho Claude Design dựng

**Không dùng khi:** cần biết thị trường có ai và giá bao nhiêu
(`nqh-research-creator-product`) · đã biết muốn gì, chỉ cần dựng màn
(`nqh-app-designer`) · app không có trên Mobbin và không quay được — không
nguồn thì không bóc, nói thẳng thay vì đoán.

---

## Bước 0 — Chặn đầu: viết một câu "bóc để làm gì"

> Bóc `<app>` để mượn `<cơ chế cụ thể>` cho `<màn nào của app mình>`.

Đạt: "Bóc Opal để mượn cơ chế viên đá làm gương phản chiếu hành vi, áp cho màn
Home của The System."  Trượt: "Bóc Opal xem nó hay chỗ nào."

Chưa có câu này thì hỏi đúng một câu rồi chạy tiếp. Hiếu vắng mặt thì tự điền,
in vào mục giả định ở cuối.

---

## Bước 1 — Ba app, và đếm friction ngay từ ảnh

> **Luật ba app** — Chọn app dẫn đầu, một app cùng hạng, một app làm khác kiểu.
> Chỗ **cả ba giống nhau** là quy ước ngành: làm khác là bắt người dùng học lại,
> thường thua. Chỗ **mỗi app một kiểu** là chưa ai đúng — sân chơi của mình.
> Chỗ **chỉ app thắng có** là ứng viên số một để mượn.

`mcp__Mobbin_apps__search_flows` rồi `search_screens`, `platform: "ios"`. Tìm
flow trước (flow giữ THỨ TỰ, mà thứ tự chính là UX), tên app đưa thẳng vào
query. Có nhiều phiên bản flow cùng tên thì lấy hết. **Phải mở ảnh ra xem** —
cấm mô tả màn hình bằng metadata.

Rồi đếm ngay bảng này, chỉ từ ảnh, không cần video. Đây là số rẻ nhất và nói
nhiều về ý đồ sản phẩm hơn cả trang motion token:

| Chỉ số | App A | App B | App C |
|---|---|---|---|
| Số bước tới **giá trị đầu tiên** (khoảnh khắc thấy app có ích) | | | |
| Số trường bắt buộc phải điền | | | |
| Số màn skip được / tổng số màn | | | |
| **Paywall ở bước thứ mấy** — trước hay sau giá trị đầu tiên | | | |
| Xin quyền ở đâu — có giải thích lý do trước không | | | |
| Có chặn cứng đăng nhập không | | | |

Timing paywall là quyết định kinh tế lớn nhất của app. Đừng để nó nằm trong một
dấu ngoặc.

**Xong khi:** có bảng luồng theo thứ tự cho từng app, cộng bảng friction ba cột.

---

## Bước 2 — Đọc lịch sử, vì app thắng không có nghĩa mọi thứ trong app đều đúng

App thắng có thể sống nhờ ASO và PR, còn thứ mình đang mê chỉ là hành khách.
Bằng chứng gần nhân quả nhất lại lấy được miễn phí:

- **App Store → Version History**, 3-5 bản gần nhất
- **Review 1-2 sao**, sắp "Most Recent", đọc 20 cái

Ba câu phải trả lời:

| Đọc thấy gì | Nghĩa là |
|---|---|
| Họ sửa gì liên tục qua nhiều bản | Chỗ đau chưa giải xong |
| Họ ÂM THẦM BỎ gì (so hai bản flow Mobbin cũng ra) | Họ đã đo được là không hiệu quả |
| Người ghét app ghét ở đâu | Khoảng trống của mình |

---

## Bước 3 — Bóc cơ chế, bốn lớp, chạy đúng thứ tự

### Lớp 0 — Điều kiện chuyển giao (chạy TRƯỚC mọi lớp khác)

Cho mỗi cơ chế định mượn, viết ba ô:

1. Người dùng app đó bước vào với **trạng thái** nào — tội lỗi, tò mò, gấp gáp,
   chán, sợ bỏ lỡ?
2. Cơ chế này ăn vào trạng thái đó ở chỗ nào?
3. Người dùng app MÌNH có trạng thái đó không? Không có thì cơ chế phải đổi gì?

> **Luật điều kiện chuyển giao** — Không trả lời được ô số 3 thì cơ chế đó ghi
> vào cột BỎ, không phải cột LẤY. Cú sốc dữ liệu của Opal hiệu quả vì người tải
> Opal đã mang sẵn cảm giác tội lỗi trước khi mở app. Bê nguyên sang một app
> không có cảm giác tội lỗi nền thì nó thành xúc phạm người dùng.

### Lớp A — Ba câu cơ chế, cho mỗi màn lõi

| Câu hỏi | Ví dụ đạt (Opal) |
|---|---|
| Nó làm gì với **cảm xúc**? | Bắt tự đoán số giờ dùng máy, rồi nối Screen Time thật để đập vào mặt con số lớn hơn — cú sốc bằng dữ liệu CỦA CHÍNH HỌ |
| Nó biến **dữ liệu khô** thành cái gì? | Viên đá đẹp/xấu theo hành vi. Nhìn hòn đá là biết hôm nay mình sống thế nào |
| Nó tạo **lý do quay lại ngày mai** bằng gì? | Điểm reset theo ngày + streak + so với người khác |

### Lớp B — Cognitive walkthrough, cho mỗi BƯỚC trong luồng

Đóng vai người dùng lần đầu, hỏi bốn câu. Ghi lại bước nào trượt câu nào — mỗi
câu ứng với một loại thuốc chữa khác nhau:

| # | Câu hỏi | Trượt = lỗi |
|---|---|---|
| 1 | Họ có đang cố đạt kết quả đúng không? | Sai mục tiêu |
| 2 | Họ có NHÌN THẤY hành động đúng đang sẵn có không? | Hiển thị |
| 3 | Họ có nối được hành động đó với kết quả họ muốn? | Chữ nghĩa |
| 4 | Sau khi làm, họ có thấy mình tiến gần mục tiêu hơn? | Phản hồi — chữa bằng motion, không phải thêm chữ |

### Lớp C — Bốn nhịp Hooked, cho cả app

**Trigger** (ngoài hay trong) → **Action** (hành động tối thiểu đổi lấy thưởng)
→ **Variable Reward** (thưởng có bất định không) → **Investment** (bỏ gì vào
khiến khó rời). Nhịp nào viết không ra là nhịp app đó THIẾU THẬT — ghi vào cột
KHOẢNG TRỐNG.

### Lớp D — Gắn cờ ĐỘC

Một nửa kỹ thuật trong Hooked là dark pattern khi dùng sai. App cải thiện bản
thân mà mượn nhầm thì thành app phạt người dùng. Năm dòng nhận diện:

- Mất streak có bị phạt nặng hơn phần thưởng khi giữ được không?
- Nút từ chối có viết theo lối tự sỉ nhục không ("Không, tôi thích lãng phí đời mình")?
- Huỷ đăng ký có khó hơn đăng ký không?
- Thông báo có tạo lo âu thay vì tạo động lực không?
- Số liệu có so sánh với người khác theo hướng hạ thấp không?

Cơ chế dính bất kỳ dòng nào: giữ chân được, nhưng bằng cách làm người dùng thấy
tệ về bản thân. Ghi cột ĐỘC, không ghi cột LẤY.

> **Luật "bóc cơ chế, không bóc da"** — Mô tả cấu trúc và cơ chế thì được. Vẽ
> lại logo, wordmark, nhân vật, tranh minh hoạ của họ thì không, kể cả đổi màu.
> Ranh giới: đưa người ngoài xem, họ có nhận ra app kia không.

---

## Bước 4 — Accessibility, năm dòng, kiểm được từ ảnh

Không có mục này thì không phải teardown UX. Kiểm từ ảnh Mobbin cộng một phút
bật máy:

| Kiểm | Ngưỡng |
|---|---|
| Vùng chạm | ≥ 44×44pt (Apple HIG) |
| Tương phản chữ | ≥ 4.5:1 (WCAG AA) — đo được từ ảnh |
| Dynamic Type | Bật cỡ chữ lớn nhất, layout có vỡ không |
| **Reduce Motion** | App có tôn trọng không |
| VoiceOver | Nút chỉ có icon đã có nhãn chưa |

Dòng Reduce Motion nối thẳng vào phần motion: mượn token về mà không kèm bản
fallback thì app mình vi phạm.

---

## Bước 5 — Motion: nguồn, phép đo, và chấm theo MỤC ĐÍCH

> **Luật "không có video thì không có số"** — Mobbin là ẢNH TĨNH. Mọi con số
> duration/easing rút từ ảnh tĩnh đều là bịa, kể cả khi nghe rất hợp lý.

Nguồn hợp lệ chỉ hai: **video quay màn hình thật**, và **tài liệu chính chủ**
(Apple HIG, WWDC, blog engineering của app đó). Ngoài ra phải gắn `[SUY ĐOÁN]`
ngay tại dòng, không gom vào disclaimer cuối bài.

**Claude không tự chạy được app iPhone.** Điều khiển được app trên macOS và
Chrome, không chạm được vào iPhone. Đừng hứa tự soi rồi im lặng bịa.

Yêu cầu quay — copy nguyên khối gửi Hiếu:

> Anh quay màn hình iPhone giúp tôi, Control Center → Record. Ba đoạn: (1) mở
> app vào Home, để yên 10 giây; (2) chạy hết luồng `<tên>`, mỗi màn dừng 2 giây;
> (3) bấm `<phần tử có hiệu ứng>` rồi thoát, làm 2 lần.
> Nhớ nói giúp tôi **máy anh là model nào**. Bật 60fps ở Settings → Camera →
> Record Video trước khi quay. Xong AirDrop sang MacBook, để trong Downloads.

### Đo

Chạy trên máy Hiếu bằng `device_bash`, file ở Downloads, đừng stage lên cloud.
Khối này đã chạy thật, dán nguyên:

```bash
V=~/Downloads/quay.mov
ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate \
  -show_entries format=duration -of default=nw=1 "$V"

ffmpeg -i "$V" -vf \
  "tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG" \
  -f null - 2>&1 \
| grep -oE "pts_time:[0-9.]+|YAVG=[0-9.]+" | paste - - \
| sed 's/pts_time://; s/YAVG=//' \
| awk '{n=int($2*4); s=""; while(n-->0) s=s"#"; printf "%8.3fs %6.2f %s\n", $1, $2, s}'
```

Dãy số nằm im ở 0, vọt lên, tắt về 0. `duration = (giây cuối khác 0 − giây đầu
khác 0) × 1000`. Đo một phần tử thì chèn `crop=w:h:x:y,` ngay trước `tblend`.

**Bốn giới hạn phải ghi vào file, không được lờ:**

- **YAVG đo lượng pixel đổi, không đo vị trí** → không phân biệt fade với move.
  Muốn đọc easing của chuyển động vị trí thì bắt buộc crop chặt vào phần tử.
- **ProMotion 120Hz**: iPhone Pro chạy UI 120Hz nhưng screen recording ra 60fps,
  nên mọi thứ dưới 16ms không nhìn thấy. Ghi model máy vào file.
- **Drop frame khi máy nóng**: kiểm khoảng cách timestamp thật giữa các frame
  trước khi tin, đừng giả định đều.
- **Quay 30fps**: sai số ±33ms, ghi vào `tolerance`.

### Chấm hai tầng

**Tầng 1 — hiệu ứng này phục vụ việc gì?** Đây mới là kết luận đáng đưa cho
người dựng:

| Mục đích | Giữ |
|---|---|
| Che độ trễ mạng | Có |
| Giữ liên tục không gian (người dùng biết đi từ đâu tới đâu) | Có |
| Hướng mắt tới thứ vừa đổi | Có |
| Xác nhận hành động | Có |
| Thuần trang trí | **Cắt** |

**Tầng 2 — nhanh hay chậm so với chuẩn:**

| Loại | Chuẩn | Nguồn |
|---|---|---|
| Phản hồi khi chạm | ≤100ms là "tức thì"; >1s mất mạch nghĩ | Nielsen |
| Chuyển màn | short 50-200 · medium 250-400 · long 450-600ms | Material 3 |
| Spring dừng hẳn | ~0.5s (`.smooth/.snappy/.bouncy` SwiftUI) | Apple |
| Bám ngón tay | response ~0.15s (`.interactiveSpring`) | Apple |
| Nút / tooltip / dropdown / modal | 100-160 · 125-200 · 150-250 · 200-500ms | Kowalski — **chuẩn WEB, không phải iOS native. Ghi rõ khi trích** |
| Stagger | ≤20ms (Material 1) · tổng chuỗi ≤500ms | M1 / Carbon |
| Frame rate | ≤16ms/frame để đạt 60fps | Google RAIL |

Apple HIG **không công bố con số duration nào** — chỉ nói định tính. Đừng trích
HIG cho một con số; trích tài liệu API SwiftUI.

**Haptic không đo được từ video.** Ghi `[KHÔNG ĐO ĐƯỢC]`.

---

## Bước 6 — Xuất ba thứ, kết thúc bằng thí nghiệm

**`<app>-TEARDOWN.md`** — mở đầu bằng 5 điều rút ra, mỗi điều một dòng. Bắt
buộc có ở đầu file: **tên app, số hiệu bản, ngày bóc, model máy quay.** Không có
bốn thứ đó thì ba tháng sau file thành lời đồn.

Các mục: bảng luồng ba app · bảng friction · bốn lớp cơ chế · **bảng các bước
trượt walkthrough, ghi rõ trượt câu số mấy** · accessibility · motion.

Bảng chốt có **năm cột**, không phải ba:

| Cơ chế | LẤY / BỎ / KHOẢNG TRỐNG / ĐỘC | Chi phí dựng (giờ) | Kiểm chứng bằng cách nào |
|---|---|---|---|

Kết thúc bằng **ba giả thuyết kiểm được, xếp theo tỉ lệ tác động trên chi phí** —
không phải mười hai ý tưởng hay ngang nhau.

> **Luật "không kết luận ai thắng"** — Mục tiêu không phải chấm điểm đối thủ.
> Bản kết thúc bằng "app họ tốt hơn" là bản vô dụng. Kết thúc bằng khoảng trống
> mình lấp được. Bóc thiết kế thì chỉ bóc thiết kế, không lạc sang phán xét công
> ty đó tốt xấu.

**`MOTION-TOKENS.json`** — cho Claude Design đọc thẳng:

```json
{
  "source": "opal-home.mov", "device": "iPhone 15 Pro", "refreshRate": 120,
  "capturedFps": 60, "tolerance": "±16ms", "measuredOn": "2026-09-06",
  "platform": "ios-native",
  "duration": { "tap": 120, "reveal": 320, "screen": 400 },
  "easing": { "standard": "cubic-bezier(0.2, 0, 0, 1)",
              "hero": "spring(response=0.5, damping=0.825)" },
  "stagger": { "list": 40 },
  "appliesTo": { "reveal": "thẻ chỉ số màn Home", "screen": "chuyển tab" },
  "reducedMotion": { "reveal": "opacity only, 160ms", "screen": "cross-fade" },
  "measured": ["duration.reveal", "duration.screen"],
  "guessed": ["easing.hero", "stagger.list"]
}
```

`measured` / `guessed` là bắt buộc. `platform` bắt buộc vì spring SwiftUI khác
cubic-bezier CSS, mà Claude Design nhận đầu vào web. `reducedMotion` bắt buộc vì
không có nó thì token mượn về làm app mình vi phạm accessibility.

**Chứng cứ** — trích 3-5 frame mốc ra PNG, lưu cạnh file MD. Video ở Downloads
sẽ bị xoá; ảnh thì còn.

---

## Checklist trước khi giao

- [ ] Có câu "bóc để làm gì" ở đầu file
- [ ] Bóc đủ **ba app**, có chỉ rõ đâu là quy ước ngành, đâu là sân chơi
- [ ] Bảng friction đã điền, có vị trí paywall
- [ ] Đã đọc changelog + 20 review 1-2 sao
- [ ] **Lớp 0 chạy trước Lớp A**, mọi cơ chế cột LẤY đều qua được ô số 3
- [ ] Bảng các bước trượt walkthrough có mặt trong file, ghi rõ trượt câu mấy
- [ ] Cột ĐỘC đã soi đủ năm dòng dark pattern
- [ ] Năm dòng accessibility đã kiểm
- [ ] Mọi hiệu ứng đã chấm MỤC ĐÍCH trước khi chấm nhanh chậm
- [ ] Đã ghi model máy, fps, tolerance, ngày bóc, số hiệu bản app
- [ ] Dòng không đo được đã gắn `[SUY ĐOÁN]` tại chỗ
- [ ] Không vẽ lại logo/nhân vật/wordmark của app bị bóc
- [ ] Kết thúc bằng 3 giả thuyết có chi phí và cách kiểm chứng
- [ ] **Đã đánh dấu 3 kết luận có độ tin thấp nhất, ghi rõ cần bằng chứng gì để
      chắc** — để người đọc soi đúng chỗ thay vì soi mò

---

## Bảng tra nhanh

| Tình huống | Làm gì |
|---|---|
| App không có trên Mobbin | Bỏ phần ảnh, đi thẳng vào video. Nói rõ thiếu nguồn cấu trúc |
| Chưa có video | Xong Bước 1-4, giao trước, để trống motion. Không đoán cho đủ |
| Chỉ bóc được 1 app | Vẫn làm, nhưng ghi rõ: không tách được quy ước khỏi lựa chọn riêng |
| App có bản Mac | Chạy được bằng `computer_app_*`, NHƯNG Mac Catalyst có motion khác iOS — số đo trên Mac không dùng cho token iOS |
| Đối thủ do Apple viết | Tra HIG/WWDC trước — hiệu ứng chuẩn hệ thống có tên và số công khai |
| Bóc xong muốn dựng màn | Sang `nqh-app-designer`, đưa `MOTION-TOKENS.json` làm đầu vào |

## Nhớ một câu

Cơ chế nào cũng sống nhờ một điều kiện. Chép cơ chế mà bỏ điều kiện thì chép về
một cái xác.

## Skill này phải tự tốt lên

1. **Eval sau mỗi lần chạy.** Xong việc thì tự chấm ngắn theo checklist: thiếu
   bước nào, chỗ nào người dùng phải sửa tay. Có chỗ đáng sửa thì đề xuất cập
   nhật thẳng vào file SKILL.md này.
2. **Thi thoảng lookup để update.** Mobbin đổi cách tổ chức dữ liệu, cờ ffmpeg
   đổi theo phiên bản, iOS đổi hệ animation mỗi năm, WCAG có bản mới. Con số hay
   tên tool nào đã vài tháng tuổi thì kiểm lại từ nguồn gốc trước khi tin.
3. **Không biết thì hỏi người.** Cái gì ngoài tầm thì nói thẳng và chỉ người
   dùng đi hỏi ai. Người thật là một nguồn trợ giúp, không phải chỉ có tài liệu.
