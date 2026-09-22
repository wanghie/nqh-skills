---
name: nqh-skill-forge
description: "Biến một quy trình hoặc kinh nghiệm thành file SKILL.md chuẩn — bạn kể thông tin, skill lo phần còn lại. Mọi skill, mới lẫn đã có, đều mang một SỔ LỖI ĐÃ BỊ NHẮC nằm trong chính SKILL.md để lỗi đã feedback không lặp lại. Kích hoạt khi nói \"viết skill\", \"làm skill cho việc này\", \"sửa skill\", \"skill không tự bật\", \"chuẩn hoá bộ skill\"."
---

# /nqh-skill-forge

Skill không phải một bài viết hay. Skill là tờ luật agent đọc GIỮA LÚC đang làm việc,
khi nó đang vội và đang muốn đi tắt. Viết cho lúc đó, không viết cho lúc người ta
ngồi đọc.

Ba thứ quyết định một skill sống hay chết: **description có làm agent tự bật đúng lúc
không**, **các bước có kiểm được không**, và **lỗi đã bị nhắc có được ghi lại trong
file không**. Thiếu thứ ba thì mỗi phiên agent lại sai đúng chỗ cũ.

## Dùng khi nào

- Có một quy trình đang lặp lại bằng tay, mỗi lần phải dán lại prompt
- Có một lần hỏng thật, muốn nó không hỏng lần thứ hai
- Có skill đã viết nhưng agent không tự bật, bật sai lúc, hoặc muốn chuẩn hoá cả bộ

**Không dùng khi:** việc chỉ làm một lần, hoặc luật thay đổi mỗi tuần. Skill là thứ
đọng lại, không phải chỗ ghi việc đang chạy.

## Bước 0 — Gom đủ 6 mẩu thông tin trước khi viết một chữ nào

Người dùng chỉ cần kể. Việc của agent là **soi đủ 6 mẩu**, thiếu mẩu nào hỏi mẩu đó.
| # | Mẩu | Câu hỏi nếu thiếu |
|---|---|---|
| 1 | Skill làm gì, một câu | "Skill này thay bạn làm việc gì, nói gọn một câu" |
| 2 | Từ khoá kích hoạt | "Bạn sẽ gõ gì cho agent lúc cần nó? Cho 3-5 câu THẬT" |
| 3 | Quy trình | "Kể tuần tự bạn đang làm tay ra sao, kể lộn xộn cũng được" |
| 4 | Luật cứng | "Cái gì tuyệt đối cấm? Đã có lần nào hỏng vì bỏ qua nó chưa?" |
| 5 | Đầu ra | "Xong thì ra cái gì: file gì, dạng gì, ai đọc?" |
| 6 | Không dùng khi nào | "Lúc nào thì KHÔNG nên dùng skill này?" |

Hỏi tối đa **3 câu một lượt**, gộp lại; **không hỏi lại thứ người dùng đã nói**. Họ
bảo "cứ làm đi" thì tự điền giả định, viết luôn, in mục `## Giả định tôi đã tự điền`
ở cuối để họ sửa — không đứng chờ. Mẩu 4 quan trọng nhất: luật rút từ chuyện thật thì
agent làm theo, luật lấy từ sách thì agent bỏ qua — không moi được thì hỏi thẳng
"lần gần nhất việc này hỏng là hỏng thế nào".

## Bước 1 — Viết frontmatter trước, và viết cho MÁY đọc

Đây là phần duy nhất luôn nằm sẵn trong context của agent. Body chỉ được đọc SAU
KHI đã bật. Description sai thì cả file vô nghĩa. Công thức ba mệnh đề:

> `[Làm gì, kèm ràng buộc cứng đặc trưng]. [Dùng khi <tình huống>]. [Kích hoạt khi nói "cụm 1", "cụm 2", "cụm 3"].`

- `name`: kebab-case, tiếng Anh, có tiền tố họ skill (`nqh-`, `bto-`), trùng đúng
  tên thư mục. Ngôi thứ ba, tả skill, không xưng "tôi"
- Nhét **đúng cụm từ người dùng thật sự gõ**, cả tiếng Việt lẫn tiếng Anh; giữ dưới
  ~500 ký tự, nhồi mọi thứ vào làm loãng tín hiệu
- Nêu cái làm nó KHÁC skill họ hàng. Cặp SAI/ĐÚNG mẫu: [`references/tra-cuu.md`](./references/tra-cuu.md)

## Bước 2 — Một câu luận đề ngay dưới tiêu đề

`# /ten-skill`, xuống dòng, rồi 2-3 câu nói cái nhìn cốt lõi — không phải tóm tắt,
mà là **câu làm agent hiểu tinh thần** để xử đúng cả tình huống file chưa liệt kê.

## Bước 3 — Bước 0 của skill luôn là "đặt mục tiêu" hoặc "có đáng làm không"

Mọi skill tốt đều chặn ở đầu, trước khi tốn công. Loại nghiên cứu, sản xuất thì bắt
viết mục tiêu một câu; loại build, cam kết dài thì bắt trả lời "có đáng làm không"
và cho phép kết luận **dừng lại** — dừng là kết quả tốt, không phải thất bại.

## Bước 4 — Chia bước, mỗi bước một hành động kiểm được

- Đánh số. Tiêu đề bắt đầu bằng **động từ mệnh lệnh**, tả kết quả chứ không tả chủ đề
- Mỗi bước có **điều kiện xong** nhìn là biết, và một khối **copy-dán được**: prompt
  cho agent con, lệnh bash, bảng, hoặc công thức
- Prompt giao cho agent con thì đóng khung `>` như một bản hợp đồng, viết sẵn cả
  yêu cầu định dạng trả về và cái nó KHÔNG được tự làm
- Nhiều việc độc lập thì nói thẳng "thả 2-3 agent chạy song song", chia việc rõ

## Bước 5 — Luật cứng: đặt tên nó, cặp SAI/ĐÚNG, gắn với chuyện thật

- Đặt tên cho luật để còn gọi lại: "Luật sạch phòng", "Luật 3 — quét trước khi
  push". Luật có tên thì được nhắc; luật không tên thì bị trôi
- Luật quan trọng viết dạng blockquote một dòng; ưu tiên **cặp SAI/ĐÚNG hai cột** hơn
  một đoạn văn giải thích. Mỗi luật nặng gắn một câu chuyện hỏng thật, một dòng là đủ
- Có đánh đổi thì **nói thẳng**: "cách này chậm hơn vì…; dự án nhỏ thì không cần".
  Skill giấu đánh đổi là skill bị bỏ giữa chừng. Phân biệt **rủi ro đo được** với
  **doạ chung chung**

## Bước 6 — Checklist tự kiểm, rồi một câu để nhớ

Checklist `- [ ]` đặt ngay trước lúc giao kết quả, mỗi dòng kiểm được bằng mắt, và
có ít nhất một dòng **bắt con người phải đọc**:

> - [ ] Bạn đã đọc hết và sửa ít nhất một chỗ agent nói sai. Chưa tìm thấy chỗ sai
>   nào thì gần như chắc chắn là chưa đọc kỹ

Skill trên ~200 dòng thì thêm bảng tra nhanh hai cột tình huống → làm gì, để ở file
cạnh bên nếu SKILL.md đã chật. Đóng file bằng `## Nhớ một câu` nếu có câu đáng nhớ.

## Bước 7 — Áp khối SỔ LỖI, cho skill MỚI lẫn skill ĐÃ CÓ

Skill xong thì kết thúc bằng hai khối: `## Skill này phải tự tốt lên` (bản 5 điều),
rồi `## SỔ LỖI ĐÃ BỊ NHẮC`. Khối 1 chỉ "đề xuất cập nhật" — hết phiên là feedback
bay mất; khối 2 là NƠI GHI, và phải nằm TRONG chính SKILL.md vì agent chỉ nạp
SKILL.md lúc kích hoạt. **Cơ chế này không tự bò sang skill khác**: không ai áp thì
skill cũ vĩnh viễn không có sổ. 7b nói rõ ai áp, khi nào.

### 7a — Một bản gốc duy nhất, copy chứ không chép tay

Bản gốc của khối sổ là [`references/khoi-so-loi.md`](./references/khoi-so-loi.md),
27 dòng, bảng rỗng. Copy nguyên văn, chỉ thay `<ten-skill>` bằng tên skill đích:

```bash
D=~/Projects/nqh-skills/skills/nqh-video-reframe   # thư mục skill đích
GOC=~/Projects/nqh-skills/skills/nqh-skill-forge/references/khoi-so-loi.md
printf '\n' >> "$D/SKILL.md" && sed "s/<ten-skill>/$(basename "$D")/" "$GOC" >> "$D/SKILL.md"
```

Không chép tay, không diễn đạt lại. Trong khối **cấm mọi tham chiếu ra ngoài file
đích** ("xem Bước 7", "luật ở skill-forge"): skill con không có Bước 7 nên tham chiếu
đó chết ngay lúc dán — khối phải tự chứa đủ 3 dòng luật và con số trần.

### 7b — Ai áp, khi nào

| Ai | Khi nào | Làm gì |
|---|---|---|
| Agent đang chạy skill này | Sinh skill MỚI | Dán khối rỗng + footer 5 điều lúc xuất file |
| Agent đang chạy skill BẤT KỲ | Vừa bị nhắc mà skill đó chưa có sổ | Dán khối RỖNG vào cuối SKILL.md của skill đó trong repo, rồi ghi dòng đầu tiên — ngay trong phiên đó, không hẹn lại |
| Agent đang chạy skill này | Được gọi "sửa skill", "chuẩn hoá bộ skill" | Quét cả hai kho, skill nào thiếu khối thì dán khối RỖNG. **Không** bịa dòng cho skill chưa từng bị nhắc |

Skill ĐÃ CÓ chỉ bắt buộc khối SỔ LỖI: 3 dòng luật trong khối đủ để nó sống một mình.
Footer 5 điều thêm ở lần sửa kế tiếp, nếu còn chỗ dưới 300 dòng. Dán xong chạy máy
kiểm ở CẢ HAI kho, đừng soi bằng mắt:

```bash
python3 tools/check_so_loi.py
```

Nó bắt: thiếu khối, bảng sai 4 cột `Ngày | Nguồn | SAI | ĐÚNG`, sổ quá 10 dòng, nguồn
lạ ngoài `Hiếu · review · tự đo`, khối lệch bản gốc, và file vượt 300 dòng. File vượt
300 thì **báo ra cho người dùng**, đừng cắt nội dung có sẵn để lấy chỗ.

### 7c — Ghi vào bản nào: FILE TRONG REPO

`~/.claude/skills/<ten-skill>` là **symlink** trỏ về repo — sửa file trong repo là có
hiệu lực ngay, không phải copy đi đâu:

```
~/Projects/nqh-skills/skills/<ten-skill>/SKILL.md          # kho public
~/Projects/nqh-skills-private/skills/<ten-skill>/SKILL.md  # kho private
```

- **Không phải mục nào trong `~/.claude/skills` cũng có repo.** Đo 2026-09-22: 23
  symlink (17 public, 4 private, 2 trỏ về kho cũ `Skill_nqh_agent`) và 4 thư mục
  thật, gồm `synced/`. `readlink` trước khi tin
- Không ghi vào `synced/` — Cloud đồng bộ sẽ ghi đè. Skill nằm ở thư mục thật thì
  chuyển về một trong hai kho rồi chạy lại `./setup`, đừng sửa tại chỗ
- Ghi xong, `git -C <repo> diff` phải thấy dòng mới. Không thấy là chưa ghi

### 7d — Hợp đồng ghi sổ: một bản duy nhất, nằm ở đây

> **Thứ tự ưu tiên.** Mục 7d này là bản thật. Footer điều 2, bảng tra nhanh và khối
> dán sang skill con đều chỉ nói lại 7d; chỗ nào nói khác thì **7d THẮNG** và chỗ
> đó phải sửa cho khớp, không phải sửa 7d.

Ba việc, làm NGAY trong phiên bị nhắc:

1. **Sửa output — LUÔN LUÔN, không điều kiện.** Sửa hết chỗ cùng loại, không chỉ
   chỗ bị chỉ tay: quét lại cả bài, cả file, cả phần đã gửi trong phiên này
2. **Ghi một dòng vào sổ — CÓ ĐIỀU KIỆN, chỉ khi lỗi thuộc loại THÀNH LUẬT.** Ghi
   vào sổ của skill đã sinh ra đoạn bị nhắc, không phải skill được gọi đầu tiên
3. **Nói ra**: `Đã ghi vào SỔ LỖI của <ten-skill>: SAI … → ĐÚNG …`

Lỗi MỘT LẦN thì dừng sau việc 1. Quyết loại nào bằng đúng một câu hỏi, không đoán:

> Lỗi này có lặp lại với một input khác không? Có → ghi sổ. Không → chỉ sửa output.

| Ghi sổ (THÀNH LUẬT) | Chỉ sửa output (MỘT LẦN) |
|---|---|
| Nói về CÁCH LÀM: giọng, đại từ, định dạng, thứ tự, thứ phải bỏ | Gắn với dữ liệu lần này: sai tên, sai số, sai link |
| Có chữ chỉ tương lai: "lần sau", "từ giờ", "luôn", "đừng bao giờ" | Đổi ý muốn chứ không phải sửa lỗi: "thôi làm bản ngắn hơn" |
| Đang bị nhắc lần thứ hai | Chọn giữa hai phương án ngang nhau |

Không xếp được cột nào thì hỏi "áp mọi lần sau, hay chỉ lần này?" — một câu hỏi rẻ hơn
một luật cứng ghi sai vào sổ.

### 7e — Viết một dòng sổ, và giữ sổ không phình

```
| YYYY-MM-DD | Hiếu · review · tự đo | SAI: hành vi cụ thể của agent | ĐÚNG: hành vi thay vào, làm ngay được |
```

**Cột NGUỒN bắt buộc**, đúng ba giá trị: `Hiếu` (Hiếu nói thật) · `review` (bộ máy
review bắt được) · `tự đo` (tự gọi tool ra kết quả). Cấm trình bày kết luận của agent
như thể Hiếu đã nói — bịa nguồn còn tệ hơn không ghi; không chắc thì ghi nguồn yếu
hơn. Cột SAI tả **hành vi quan sát được**: "viết nhạt" không ai kiểm được, "mở short
bằng câu hỏi tu từ" thì soi một giây là biết.

- Đọc sổ trước khi thêm. Có dòng gần giống = bị nhắc **lần thứ hai** → KHÔNG thêm
  dòng mới; nâng thành luật cứng có tên ở thân skill (Bước 5), xoá khỏi sổ
- Sổ đầy mà có dòng mới → gộp dòng cùng chủ đề, hoặc nâng dòng bị lặp nhiều nhất
  lên luật cứng. **Không xoá một dòng chỉ vì nó cũ**
- Dòng sổ chọi luật trong thân skill → thân skill sai, sửa thân skill
- Sắp cán 300 dòng thì tách phần tra cứu ra file cạnh bên, **không cắt sổ**

## Bước 8 — Xuất file, đặt đúng chỗ

Bản thật là bản trong repo, đường dẫn ở Bước 7c; `~/.claude/skills/<ten-skill>/SKILL.md`
chỉ là symlink trỏ về đó, và là chỗ Claude Code tự nạp.

- Một skill một thư mục, tên thư mục **trùng** `name` trong frontmatter. File phụ
  (template, ví dụ, script) để cạnh SKILL.md và **dẫn link từ trong SKILL.md**
- SKILL.md dưới 300 dòng VÀ còn chỗ cho sổ lên đủ trần 10 dòng, tức thân skill dừng
  dưới 262 dòng. Dài hơn thì tách phần tra cứu ra file riêng
- Skill giọng văn và chuyện đời tư về kho private; quy trình/kỹ thuật ở kho public
- Phiên Cowork không ghi thẳng vào tài khoản được: dựng file rồi dùng `propose_skills`
  để người dùng bấm lưu, đồng thời gửi kèm file cho họ

## Bước 9 — Test kích hoạt trước khi coi là xong

Mở **phiên agent mới**, thử ba câu: đúng từ khoá → phải bật; tả bằng lời khác → nên
bật; việc của skill họ hàng → **không** được bật. Cách xử khi trượt: mục "Test kích
hoạt" ở [`references/tra-cuu.md`](./references/tra-cuu.md).

## Luật viết, áp cho mọi skill sinh ra từ đây

- Tiếng Việt, câu ngắn, không emoji, không lời quảng cáo. Không câu nào chỉ để nối ý
- Không viết "hãy chuyên nghiệp", "hãy cẩn thận" — đó không phải chỉ dẫn. Ưu tiên
  bảng và khối lệnh hơn đoạn văn
- Xuống dòng quanh cột 80 cho dễ đọc trong terminal
- Skill nói với agent, không nói với độc giả. Câu lệnh, không phải bài giảng

## Trước khi giao: chạy checklist

Bốn dòng dưới là dòng trượt là hỏng. Checklist đầy đủ 13 dòng và bảng tra nhanh 12
tình huống ở [`references/tra-cuu.md`](./references/tra-cuu.md) — **mở và chạy hết**.

- [ ] `## SỔ LỖI ĐÃ BỊ NHẮC` copy từ `references/khoi-so-loi.md`, bảng 4 cột
      `Ngày | Nguồn | SAI | ĐÚNG`, rỗng nếu chưa có feedback thật
- [ ] `python3 tools/check_so_loi.py` sạch, `wc -l SKILL.md` dưới 300
- [ ] Đã chạy test 3 câu ở Bước 9 trong một phiên agent mới
- [ ] Đã in mục "Giả định tôi đã tự điền" nếu có chỗ tự điền

## Nhớ một câu

Skill làm agent nhớ luật và đi đúng quy trình. Nó không làm kết quả thành đúng. Ba
việc vẫn của con người: đặt mục tiêu trước khi giao, đọc kết quả rồi sửa chỗ sai
trước khi tin, và duyệt trước khi thứ gì đó rời khỏi máy.

## Skill này phải tự tốt lên

1. **Đọc SỔ LỖI trước khi làm.** Mục sổ ở cuối file này là luật cứng, không phải
   ghi chú. Đọc hết trước khi xuất chữ đầu tiên.
2. **Bị nhắc thì xử ngay trong phiên đó**, theo đúng hợp đồng ở Bước 7d và không
   diễn đạt lại: sửa output LUÔN LUÔN, ghi một dòng vào sổ CHỈ KHI lỗi thuộc loại
   THÀNH LUẬT, rồi nói ra là đã ghi. Không để đến cuối phiên, không dừng ở mức
   "đề xuất". Hai chỗ nói khác nhau thì Bước 7d thắng.
3. **Eval sau mỗi lần chạy.** Tự chấm ngắn theo checklist: thiếu bước nào, chỗ nào
   người dùng phải sửa tay. Chỗ đáng sửa mà không phải lỗi bị nhắc thì đề xuất
   người dùng cập nhật thẳng vào SKILL.md này.
4. **Thi thoảng lookup để update.** Nơi đặt skill, giới hạn độ dài và cách agent nạp
   skill đổi theo phiên bản công cụ. Chi tiết vài tháng tuổi thì kiểm lại từ gốc.
5. **Không biết thì hỏi người.** Cái gì ngoài tầm thì nói thẳng và chỉ người dùng đi
   hỏi ai. Người thật là một nguồn trợ giúp, không phải chỉ có tài liệu.

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
  chính file này, rồi nói ra `Đã ghi vào SỔ LỖI của nqh-skill-forge: SAI … → ĐÚNG …`.
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
| 2026-09-22 | review | Bước 7 chỉ bắt dán khối vào skill MỚI; skill ĐÃ CÓ không ai áp nên vĩnh viễn không có sổ | 7b nêu rõ ai áp và khi nào — agent bất kỳ vừa bị nhắc mà skill đó chưa có sổ thì dán khối rỗng vào SKILL.md trong repo ngay trong phiên |
| 2026-09-22 | review | Khối dán sang skill con ghi "trần 12 dòng" và trỏ "luật ở Bước 7", trong khi skill con không có Bước 7 và trần thật là 10 | Một bản gốc duy nhất `references/khoi-so-loi.md`, tự chứa 3 dòng luật, trần 10 dòng suy ra được từ luật `SKILL.md < 300 dòng` |
| 2026-09-22 | review | Bước 7 nói ghi sổ "nếu là loại THÀNH LUẬT", footer điều 2 nói ghi vô điều kiện — hai hợp đồng chọi nhau | Một hợp đồng duy nhất ở 7d kèm thứ tự ưu tiên: sửa output LUÔN LUÔN, ghi sổ CHỈ KHI THÀNH LUẬT; mọi chỗ khác chỉ nói lại 7d |
| 2026-09-22 | review | Trình bày kết luận của chính agent như thể Hiếu đã nói, trong khi quét hết tin nhắn của Hiếu không có dòng nào như vậy | Cột Nguồn bắt buộc, đúng ba giá trị `Hiếu · review · tự đo`; không chắc thì ghi nguồn yếu hơn, đừng nâng lên thành "Hiếu" |
| 2026-09-22 | tự đo | Coi `~/.claude/skills/<ten>/` là một bản riêng để sửa, hoặc sửa bản dưới `synced/` | `readlink`: 23 symlink, 21 trỏ về hai repo (17 public + 4 private), 2 về kho cũ — sửa file trong repo mới có hiệu lực |
| 2026-09-22 | review | Áp một cơ chế mới xuống cả bộ skill trong một lượt khi chưa có bản mẫu được duyệt | Sửa một skill mẫu trước, duyệt hợp đồng, rồi mới nhân bản xuống phần còn lại |
