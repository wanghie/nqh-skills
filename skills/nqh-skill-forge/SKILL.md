---
name: nqh-skill-forge
description: "Biến một quy trình hoặc kinh nghiệm thành file SKILL.md chuẩn — bạn kể thông tin, skill lo phần còn lại. Mọi skill sinh ra đều mang một SỔ LỖI ĐÃ BỊ NHẮC để lỗi đã feedback không lặp lại. Kích hoạt khi nói \"viết skill\", \"làm skill cho việc này\", \"sửa skill\", \"skill không tự bật\", \"chuẩn hoá bộ skill\"."
---

# /nqh-skill-forge

Skill không phải một bài viết hay. Skill là một tờ luật agent đọc GIỮA LÚC đang
làm việc, khi nó đang vội và đang muốn đi tắt. Viết cho lúc đó, không viết cho
lúc người ta ngồi đọc.

Ba thứ quyết định một skill sống hay chết: **description có làm agent tự bật đúng
lúc không**, **các bước có kiểm được không**, và **lỗi đã bị nhắc có được ghi lại
trong file không**. Thiếu thứ ba thì mỗi phiên agent lại sai đúng chỗ cũ, và
người dùng phải nhắc đến lần thứ năm.

## Dùng khi nào

- Có một quy trình đang lặp lại bằng tay, mỗi lần phải dán lại prompt
- Có một lần hỏng thật, muốn nó không hỏng lần thứ hai
- Có một skill đã viết nhưng agent không tự bật, hoặc bật sai lúc
- Muốn chuẩn hoá cả một bộ skill cho team

**Không dùng khi:** việc chỉ làm một lần, hoặc luật thay đổi mỗi tuần. Skill là
thứ đọng lại, không phải chỗ ghi việc đang chạy.

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

Luật hỏi:

- Hỏi tối đa **3 câu một lượt**, gộp lại, không hỏi từng câu một
- **Không hỏi lại thứ người dùng đã nói.** Đọc kỹ trước khi hỏi
- Người dùng nói "cứ làm đi" thì tự điền giả định, viết luôn, và **in một mục
  `## Giả định tôi đã tự điền` ở cuối** để họ sửa. Không đứng chờ

Mẩu 4 quan trọng nhất. Luật rút từ chuyện thật thì agent làm theo; luật lấy từ
sách thì agent bỏ qua. Không moi được chuyện thật thì hỏi thẳng: "lần gần nhất
việc này hỏng là hỏng thế nào".

## Bước 1 — Viết frontmatter trước, và viết cho MÁY đọc

Đây là phần duy nhất luôn nằm sẵn trong context của agent. Body chỉ được đọc
SAU KHI đã bật. Description sai thì cả file vô nghĩa. Công thức ba mệnh đề:

```
[Làm gì, kèm ràng buộc cứng đặc trưng]. [Dùng khi <tình huống>]. [Kích hoạt khi nói "cụm 1", "cụm 2", "cụm 3"].
```

- `name`: kebab-case, tiếng Anh, có tiền tố họ skill (`nqh-`, `bto-`), trùng
  đúng tên thư mục
- Viết ngôi thứ ba, tả skill, không xưng "tôi". Nhét **đúng cụm từ người dùng
  thật sự gõ**, kể cả tiếng Việt lẫn tiếng Anh
- Giữ dưới ~500 ký tự. Nhồi mọi thứ vào description làm loãng tín hiệu
- Nêu luôn cái làm nó KHÁC các skill họ hàng, nếu có

## Bước 2 — Một câu luận đề ngay dưới tiêu đề

`# /ten-skill`, xuống dòng, rồi 2-3 câu nói cái nhìn cốt lõi. Không phải tóm tắt,
mà là **câu làm agent hiểu tinh thần** để xử đúng cả tình huống file chưa liệt kê.

## Bước 3 — Bước 0 của skill luôn là "đặt mục tiêu" hoặc "có đáng làm không"

Mọi skill tốt đều chặn ở đầu, trước khi tốn công. Loại nghiên cứu, sản xuất thì
bắt viết mục tiêu một câu. Loại build, cam kết dài thì bắt trả lời "có đáng làm
không", và cho phép kết luận **dừng lại** — ghi rõ dừng là kết quả tốt, không phải
thất bại. Không có bước 0 thì agent trả về một bản chung chung không dùng vào việc gì.

## Bước 4 — Chia bước, mỗi bước một hành động kiểm được

- Đánh số. Tiêu đề bắt đầu bằng **động từ mệnh lệnh**
- Mỗi bước phải có **điều kiện xong** nhìn là biết
- Mỗi bước nên kèm một khối **copy-dán được**: đoạn prompt giao cho agent con,
  lệnh bash, bảng, hoặc công thức tính
- Prompt giao cho agent con thì đóng khung `>` như một bản hợp đồng, viết sẵn
  cả yêu cầu định dạng trả về và cái nó KHÔNG được tự làm
- Nhiều việc độc lập thì nói thẳng "thả 2-3 agent chạy song song", chia việc rõ

## Bước 5 — Luật cứng: đặt tên nó, cặp SAI/ĐÚNG, gắn với chuyện thật

- Đặt tên cho luật để còn gọi lại: "Luật sạch phòng", "Luật 3 — quét trước khi
  push". Luật có tên thì được nhắc; luật không tên thì bị trôi
- Luật quan trọng viết dạng blockquote một dòng, đọc là nhớ
- Ưu tiên **cặp SAI/ĐÚNG hai cột** hơn một đoạn văn giải thích
- Mỗi luật nặng gắn một câu chuyện hỏng thật. Một dòng là đủ
- Có đánh đổi thì **nói thẳng**: "cách này chậm hơn vì...; dự án nhỏ thì không
  cần". Skill giấu đánh đổi là skill bị bỏ giữa chừng
- Phân biệt **rủi ro đo được** với **doạ chung chung**; không chứng minh được thì viết đúng mức đó

## Bước 6 — Checklist tự kiểm, rồi một câu để nhớ

Checklist `- [ ]` đặt ngay trước lúc giao kết quả. Mỗi dòng kiểm được bằng mắt.
Nhét vào ít nhất một dòng **bắt con người phải đọc**, kiểu:

> - [ ] Bạn đã đọc hết và sửa ít nhất một chỗ agent nói sai. Chưa tìm thấy chỗ
>   sai nào thì gần như chắc chắn là chưa đọc kỹ

Skill dài (trên ~200 dòng) thì thêm một bảng tra nhanh hai cột tình huống → làm gì;
SKILL.md đã chật thì để bảng đó ở file cạnh bên và dẫn link. Đóng file bằng mục
`## Nhớ một câu` nếu có một câu đáng nhớ.

## Bước 7 — Dán hai khối bắt buộc vào cuối file, cả skill MỚI và skill ĐÃ CÓ

Mọi skill kết thúc bằng đúng hai khối, theo thứ tự: khối `Skill này phải tự tốt lên`
(bản 5 điều), rồi khối SỔ LỖI. Khối 1 chỉ "đề xuất cập nhật" — đề xuất xong là hết
phiên, feedback bay mất; khối 2 là NƠI GHI, thiếu nó là skill chưa xong. Sổ nằm TRONG
chính SKILL.md: agent chỉ nạp SKILL.md lúc kích hoạt.

### 7a — Skill MỚI: dán lúc xuất file

Copy nguyên hai mục ở **cuối file này** sang cuối SKILL.md mới, không diễn đạt lại.
Bảng sổ để **rỗng, chỉ hai dòng header** — bịa dòng mẫu là bịa lịch sử.

### 7b — Skill ĐÃ CÓ: cơ chế không tự đi theo, phải có người áp

| Ai | Khi nào | Làm gì |
|---|---|---|
| Agent đang chạy skill bất kỳ | Nhận feedback mà skill đó chưa có sổ | Dán khối RỖNG vào cuối SKILL.md trong repo, ghi dòng đầu tiên, ngay trong phiên đó |
| Agent đang chạy skill này | Được gọi "sửa skill", "chuẩn hoá bộ skill" | Quét cả hai kho, skill nào thiếu khối thì dán khối RỖNG. **Không** bịa dòng cho skill chưa từng bị nhắc |
| Agent đang chạy skill này | Sinh skill mới | Theo 7a |

Dán xong kiểm ba thứ: `wc -l` dưới 300, bảng đúng 4 cột `Ngày | Nguồn | SAI | ĐÚNG`,
bảng rỗng nếu chưa có feedback thật. File đã vượt 300 trước khi dán thì **báo ra cho
người dùng**, đừng cắt nội dung có sẵn để lấy chỗ.

### 7c — Ghi vào bản nào: FILE TRONG REPO

`~/.claude/skills/<ten-skill>` là **symlink** trỏ về repo: sửa file trong repo là có
hiệu lực ngay, không cần copy đi đâu.

```
~/Projects/nqh-skills/skills/<ten-skill>/SKILL.md          # kho public
~/Projects/nqh-skills-private/skills/<ten-skill>/SKILL.md  # kho private
```

- Không ghi vào `~/.claude/skills/synced/` — Cloud đồng bộ sẽ ghi đè
- Không coi `~/.claude/skills/<ten-skill>/` là bản riêng; `readlink` nó ra đường thật
- Ghi xong, `git -C <repo> diff` phải thấy dòng mới. Không thấy là chưa ghi

### 7d — Hợp đồng ghi sổ: một bản duy nhất, nằm ở đây

Dấu hiệu nhận ra feedback: khối sổ ở cuối file này, gạch đầu dòng thứ nhất. Nhận ra
rồi thì làm ba việc NGAY trong phiên đó:

1. **Sửa output, sửa hết cùng loại** — không chỉ chỗ bị chỉ tay: quét lại cả bài,
   cả file, cả phần đã gửi trong phiên này cho đúng lỗi đó
2. **Ghi một dòng vào sổ nếu lỗi thuộc loại THÀNH LUẬT** (bảng dưới) — ghi vào sổ
   của skill đã sinh ra đoạn bị nhắc; chạy chuỗi nhiều skill thì ghi vào skill sinh
   ra đoạn đó, không phải skill gọi đầu tiên
3. **Nói ra**: `Đã ghi vào SỔ LỖI của <ten-skill>: SAI … → ĐÚNG …`

> **Thứ tự ưu tiên.** Mục 7d là bản thật. Footer điều 2, bảng tra nhanh và khối sổ
> dán sang skill con đều chỉ về đây; chỗ nào nói khác thì 7d THẮNG và chỗ đó phải
> sửa. Hợp đồng: **sửa output thì luôn luôn; ghi sổ chỉ khi THÀNH LUẬT; MỘT LẦN thì
> sửa output rồi dừng, không ghi sổ.**

Quyết THÀNH LUẬT hay MỘT LẦN bằng đúng một câu hỏi, không đoán:

> Lỗi này có lặp lại với một input khác không? Có → ghi sổ. Không → chỉ sửa output.

| Ghi sổ (THÀNH LUẬT) | Chỉ sửa output (MỘT LẦN) |
|---|---|
| Nói về CÁCH LÀM: giọng, đại từ, định dạng, thứ tự, thứ phải bỏ | Gắn với dữ liệu lần này: sai tên, sai số, sai link |
| Có chữ chỉ tương lai: "lần sau", "từ giờ", "luôn", "đừng bao giờ" | Đổi ý muốn chứ không phải sửa lỗi: "thôi làm bản ngắn hơn" |
| Đang bị nhắc lần thứ hai | Chọn giữa hai phương án ngang nhau |

Không xếp được cột nào thì hỏi: "áp mọi lần sau, hay chỉ lần này?" Một câu hỏi rẻ hơn
một luật cứng ghi sai vào sổ.

### 7e — Viết một dòng sổ, và giữ sổ không phình

Bảng 4 cột, format cố định, dòng mới xuống dưới cùng:

```
| YYYY-MM-DD | Hiếu · review · tự đo | SAI: hành vi cụ thể của agent | ĐÚNG: hành vi thay vào, làm ngay được |
```

**Cột NGUỒN bắt buộc**, chỉ ba giá trị: `Hiếu` (Hiếu nói thật) · `review` (bộ máy
review bắt được) · `tự đo` (gọi tool ra kết quả). Cấm trình bày kết luận của agent như
thể Hiếu đã nói — bịa nguồn còn tệ hơn không ghi; không chắc thì ghi nguồn yếu hơn.
Cột SAI tả **hành vi quan sát được**: "viết nhạt" không ai kiểm được, "mở short bằng
câu hỏi tu từ" thì soi một giây là biết.

> **Trần sổ: 10 dòng** — một con số duy nhất cho cả bộ, suy ra từ luật `SKILL.md
> dưới 300 dòng`: khối sổ chiếm 22 dòng khung, cộng 10 dòng dữ liệu là 32, nên thân
> skill phải dừng dưới 268 dòng. Luật 300 dòng THẮNG nếu hai luật chọi nhau.

- Đọc sổ trước khi thêm. Đã có dòng gần giống = đang bị nhắc **lần thứ hai** → KHÔNG
  thêm dòng mới; nâng thành luật cứng có tên ở thân skill (Bước 5), xoá dòng khỏi sổ
- Sổ đầy mà có dòng mới → gộp các dòng cùng chủ đề, hoặc nâng dòng bị lặp nhiều nhất
  lên luật cứng. **Không xoá một dòng chỉ vì nó cũ**
- Dòng sổ chọi luật trong thân skill → thân skill sai, sửa thân skill
- Sắp cán 300 thì tách phần tra cứu ra file cạnh bên, **không cắt sổ**:

```bash
wc -l SKILL.md              # < 300, luật này thắng
grep -c '^| 20' SKILL.md    # số dòng sổ, <= 10
```

## Bước 8 — Xuất file, đặt đúng chỗ

Bản thật là bản trong repo, đường dẫn ở Bước 7c; `~/.claude/skills/<ten-skill>/SKILL.md`
chỉ là symlink trỏ về đó, và là chỗ Claude Code tự nạp.

- Một skill một thư mục, tên thư mục **trùng** `name` trong frontmatter
- File phụ (template, ví dụ, script) để cạnh SKILL.md và **dẫn link từ trong
  SKILL.md**, agent không tự đoán ra
- SKILL.md dưới 300 dòng VÀ còn chỗ cho sổ lên đủ trần. Dài hơn thì tách phần tra cứu
  ra file riêng; SKILL.md chỉ giữ luật, bước và sổ
- Skill giọng văn và chuyện đời tư về kho private; skill quy trình/kỹ thuật ở kho
  public. Thư mục `~/.claude/skills/synced/` do Cloud đồng bộ — sửa tay ở đó bị ghi đè
- Trong phiên Cowork không ghi thẳng được vào tài khoản: dựng file rồi dùng
  `propose_skills` để người dùng bấm lưu, đồng thời gửi kèm file cho họ

## Bước 9 — Test kích hoạt trước khi coi là xong

Mở **phiên agent mới**, thử ba câu (đúng từ khoá → phải bật; tả bằng lời khác → nên
bật; việc của skill họ hàng → **không** được bật). Cách xử khi trượt: mục "Test kích
hoạt" ở [`references/tra-cuu.md`](./references/tra-cuu.md).

## Luật viết, áp cho mọi skill sinh ra từ đây

- Tiếng Việt, câu ngắn, không emoji, không lời quảng cáo
- Không có câu nào chỉ để nối ý. Cắt được là cắt
- Không viết "hãy chuyên nghiệp", "hãy cẩn thận". Đó không phải chỉ dẫn. Ưu tiên
  bảng và khối lệnh hơn đoạn văn
- Xuống dòng quanh cột 80 cho dễ đọc trong terminal
- Skill nói với agent, không nói với độc giả. Câu lệnh, không phải bài giảng

## Trước khi giao: chạy checklist

Checklist 15 dòng và bảng tra nhanh 12 tình huống nằm ở
[`references/tra-cuu.md`](./references/tra-cuu.md). **Mở file đó và chạy hết
checklist trước khi giao skill** — bỏ bước này là bỏ luôn phần kiểm được của skill.

## Nhớ một câu

Skill làm agent nhớ luật và đi đúng quy trình. Nó không làm kết quả thành đúng.
Ba việc vẫn của con người: đặt mục tiêu trước khi giao, đọc kết quả rồi sửa chỗ
sai trước khi tin, và duyệt trước khi thứ gì đó rời khỏi máy.

## Skill này phải tự tốt lên

1. **Đọc SỔ LỖI trước khi làm.** Mục sổ ở cuối file này là luật cứng, không phải ghi
   chú. Đọc hết trước khi xuất chữ đầu tiên.
2. **Bị nhắc thì xử ngay trong phiên đó**, theo đúng hợp đồng ở Bước 7d và không
   diễn đạt lại: sửa output luôn luôn, ghi một dòng vào sổ **nếu lỗi thuộc loại
   THÀNH LUẬT**, rồi nói ra là đã ghi. Không để đến cuối phiên, không dừng ở mức
   "đề xuất". Hai chỗ nói khác nhau thì Bước 7d thắng.
3. **Eval sau mỗi lần chạy.** Tự chấm ngắn theo checklist: thiếu bước nào, chỗ nào
   người dùng phải sửa tay. Chỗ đáng sửa mà không phải lỗi bị nhắc thì đề xuất
   người dùng cập nhật thẳng vào SKILL.md này.
4. **Thi thoảng lookup để update.** Nơi đặt skill, giới hạn độ dài và cách agent nạp
   skill đổi theo phiên bản công cụ. Chi tiết đã vài tháng tuổi thì kiểm lại từ gốc.
5. **Không biết thì hỏi người.** Cái gì ngoài tầm thì nói thẳng và chỉ người dùng
   đi hỏi ai. Người thật là một nguồn trợ giúp, không phải chỉ có tài liệu.

## SỔ LỖI ĐÃ BỊ NHẮC

Đọc hết mục này TRƯỚC khi xuất chữ đầu tiên. Mỗi dòng là một lỗi đã bị nhắc; lặp
lại nó lần nữa là lỗi nặng hơn lần đầu. Bảng rỗng = skill này chưa từng bị nhắc.
**Bảng rỗng là trung thực — cấm bịa dòng mẫu cho có.**

- **Nhận ra feedback:** "sai rồi", "không phải thế", "đừng…", "bỏ… đi", "lần sau…",
  "từ giờ…", "tôi đã bảo rồi", "vẫn còn…", "nói bao nhiêu lần rồi", hoặc người dùng
  tự tay sửa output vừa nhận rồi gửi ngược lại.
- **Ghi gì:** sửa output và quét sửa hết chỗ cùng loại, thêm MỘT dòng vào bảng dưới
  (trong chính file này), rồi nói ra `Đã ghi vào SỔ LỖI của <ten-skill>: SAI … →
  ĐÚNG …`. Cột **Nguồn** bắt buộc, chỉ ba giá trị: `Hiếu` (Hiếu nói thật) · `review`
  (bộ máy review bắt được) · `tự đo` (gọi tool ra kết quả). Cấm trình bày kết luận
  của agent như thể Hiếu đã nói — bịa nguồn tệ hơn không ghi. Cột SAI tả hành vi
  quan sát được, không tả cảm giác.
- **Trần sổ: 10 dòng.** Suy ra từ luật `SKILL.md < 300 dòng`: khối này chiếm 22 dòng
  khung, cộng 10 dòng sổ là 32, nên thân skill phải dừng dưới 268 dòng. Sổ đầy mà có
  dòng mới → nâng dòng bị lặp nhiều nhất thành luật cứng có tên ở thân skill rồi xoá
  khỏi sổ; không xoá một dòng chỉ vì nó cũ. Luật `< 300 dòng` THẮNG khi hai luật chọi.

| Ngày | Nguồn | SAI | ĐÚNG |
|---|---|---|---|
| 2026-09-22 | review | Khối sổ dán sang skill con trỏ "luật ghi và trần sổ ở Bước 7" và ghi trần 12 dòng — skill con không có Bước 7, và trần thật là 10 | Khối dán sang skill con phải tự chứa 3 dòng luật và ghi thẳng trần 10 dòng, không trỏ ra mục ngoài file |
| 2026-09-22 | tự đo | Coi `~/.claude/skills/<ten-skill>/` là một bản riêng để sửa, hoặc sửa bản dưới `synced/` | `ls -la ~/.claude/skills` cho thấy 21 mục là symlink trỏ về hai repo — sửa file trong repo mới có hiệu lực |
| 2026-09-22 | review | Áp một cơ chế mới xuống cả bộ skill trong một lượt, chưa có bản mẫu được duyệt | Sửa một skill mẫu trước, duyệt hợp đồng, rồi mới nhân bản xuống phần còn lại |
