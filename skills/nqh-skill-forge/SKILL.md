---
name: nqh-skill-forge
description: "Biến một quy trình hoặc kinh nghiệm thành file SKILL.md chuẩn — bạn kể thông tin, skill lo phần còn lại. Mọi skill sinh ra đều có SỔ LỖI ĐÃ BỊ NHẮC để không lặp lại lỗi đã bị feedback. Kích hoạt khi nói \"viết skill\", \"làm skill cho việc này\", \"sửa skill\", \"skill không tự bật\", \"chuẩn hoá bộ skill\"."
---

# /nqh-skill-forge

Skill không phải một bài viết hay. Skill là một tờ luật agent đọc GIỮA LÚC đang
làm việc, khi nó đang vội và đang muốn đi tắt. Viết cho lúc đó, không viết cho
lúc người ta ngồi đọc.

Ba thứ quyết định một skill sống hay chết: **description có làm agent tự bật
đúng lúc không**, **các bước có kiểm được không**, và **skill có ghi lại lỗi đã
bị nhắc không**. Thiếu thứ ba thì mỗi phiên lại sai đúng chỗ cũ.

## Dùng khi nào

- Có một quy trình đang lặp lại bằng tay, mỗi lần phải dán lại prompt
- Có một lần hỏng thật, muốn nó không hỏng lần thứ hai
- Có một skill đã viết nhưng agent không tự bật, hoặc bật sai lúc
- Muốn chuẩn hoá cả một bộ skill cho team

**Không dùng khi:** việc chỉ làm một lần, hoặc luật thay đổi mỗi tuần. Skill là
thứ đọng lại, không phải chỗ ghi việc đang chạy.

---

## Bước 0 — Gom đủ 6 mẩu thông tin trước khi viết một chữ nào

Người dùng chỉ cần kể. Việc của agent là **soi đủ 6 mẩu này**, thiếu mẩu nào
thì hỏi đúng mẩu đó.

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
SAU KHI đã bật. Description sai thì cả file vô nghĩa.

Công thức ba mệnh đề:

```
[Làm gì, kèm ràng buộc cứng đặc trưng].
[Dùng khi <tình huống>].
[Kích hoạt khi nói "cụm 1", "cụm 2", "cụm 3"].
```

- `name`: kebab-case, tiếng Anh, có tiền tố họ skill (`nqh-`, `bto-`), trùng
  đúng tên thư mục
- Viết ngôi thứ ba, tả skill, không xưng "tôi"
- Nhét **đúng cụm từ người dùng thật sự gõ**, kể cả tiếng Việt lẫn tiếng Anh
- Giữ dưới ~500 ký tự. Nhồi mọi thứ vào description làm loãng tín hiệu
- Nêu luôn cái làm nó KHÁC các skill họ hàng, nếu có

```
SAI     Skill giúp research thị trường một cách chuyên nghiệp.
ĐÚNG    Research sâu một thị trường bằng nhiều agent song song, bắt buộc có TAM
        SAM SOM. Dùng khi cần biết thị trường có những ai, giá bao nhiêu, còn
        khoảng trống nào. Kích hoạt khi nói "research market", "research thị
        trường", "làm research về".
```

Câu SAI hỏng vì không chứa cụm nào người dùng sẽ gõ, và không nói skill ép làm gì.

## Bước 2 — Một câu luận đề ngay dưới tiêu đề

`# /ten-skill`, xuống dòng, rồi 2-3 câu nói cái nhìn cốt lõi. Không phải tóm
tắt, mà là **câu làm agent hiểu tinh thần** để xử đúng cả những tình huống file
chưa liệt kê.

## Bước 3 — Bước 0 của skill luôn là "đặt mục tiêu" hoặc "có đáng làm không"

Mọi skill tốt đều chặn ở đầu, trước khi tốn công: loại nghiên cứu, sản xuất thì
bắt viết mục tiêu một câu; loại build, cam kết dài thì bắt trả lời "có đáng làm
không" và cho phép kết luận **dừng lại**. Ghi rõ dừng là kết quả tốt, không phải
thất bại. Không có bước 0 thì agent trả về một bản chung chung.

## Bước 4 — Chia bước, mỗi bước một hành động kiểm được

- Đánh số. Tiêu đề bắt đầu bằng **động từ mệnh lệnh**
- Mỗi bước phải có **điều kiện xong** nhìn là biết
- Mỗi bước nên kèm một khối **copy-dán được**: đoạn prompt giao cho agent con,
  lệnh bash, bảng, hoặc công thức tính
- Prompt giao cho agent con thì đóng khung `>` như một bản hợp đồng, viết sẵn
  cả yêu cầu định dạng trả về và cái nó KHÔNG được tự làm
- Nhiều việc độc lập thì nói thẳng "thả 2-3 agent chạy song song", chia việc rõ

```
SAI     ## Bước 2 — Phân tích dữ liệu
ĐÚNG    ## Bước 2 — Quy mọi đơn giá về cùng một đơn vị rồi in giả định quy đổi
```

## Bước 5 — Luật cứng: đặt tên nó, cặp SAI/ĐÚNG, gắn với chuyện thật

- Đặt tên cho luật để còn gọi lại: "Luật sạch phòng", "Luật 3 — quét trước khi
  push". Luật có tên thì được nhắc; luật không tên thì bị trôi
- Luật quan trọng viết dạng blockquote một dòng, đọc là nhớ
- Ưu tiên **cặp SAI/ĐÚNG hai cột** hơn một đoạn văn giải thích
- Mỗi luật nặng gắn một câu chuyện hỏng thật. Một dòng là đủ
- Có đánh đổi thì **nói thẳng**: "cách này chậm hơn vì...; dự án nhỏ thì không
  cần". Skill giấu đánh đổi là skill bị bỏ giữa chừng
- Phân biệt **rủi ro đo được** với **doạ chung chung**

## Bước 6 — Checklist tự kiểm, rồi một câu để nhớ

Checklist `- [ ]` đặt ngay trước lúc giao kết quả. Mỗi dòng kiểm được bằng mắt.
Nhét vào ít nhất một dòng **bắt con người phải đọc**, kiểu:

```
- [ ] Bạn đã đọc hết và sửa ít nhất một chỗ agent nói sai. Chưa tìm thấy chỗ
      sai nào thì gần như chắc chắn là chưa đọc kỹ
```

Skill dài (trên ~200 dòng) thì thêm mục `## Bảng tra nhanh`: hai cột tình
huống → làm gì. Đóng file bằng mục `## Nhớ một câu` nếu có một câu đáng nhớ.

---

## Bước 7 — Dán hai khối bắt buộc ở cuối file: footer và SỔ LỖI

Mọi skill sinh ra từ đây kết thúc bằng đúng hai khối, theo thứ tự này. Khối 1 là
lời hứa tự sửa. Khối 2 là **nơi ghi** để lần sau không sai lại. Chỉ có khối 1
thì feedback bay mất lúc hết phiên, phiên sau agent sai đúng chỗ cũ — đó là lỗi
nặng nhất của bộ skill bản v1.

### Khối 1 — footer "Skill này phải tự tốt lên"

Dán nguyên mục `## Skill này phải tự tốt lên` ở **cuối file này** (bản 5 điều)
vào cuối SKILL.md mới, giữ nguyên chữ, chỉ đổi tên người và kênh hỏi. Bản 3 điều
cũ đã bỏ: nó chỉ "đề xuất" chứ không có nơi ghi.

### Khối 2 — SỔ LỖI ĐÃ BỊ NHẮC

Dán nguyên mục `## SỔ LỖI ĐÃ BỊ NHẮC` ở **cuối file này** vào cuối SKILL.md mới:
giữ nguyên chữ và luật ghi, xoá 3 dòng ví dụ, để lại một dòng `| — | — | — |`.
Không viết lại bằng lời khác — sổ mỗi skill một khác, luật ghi thì chung.

Sổ nằm **trong chính SKILL.md**, không phải file riêng: agent chỉ đọc SKILL.md
lúc kích hoạt. Feedback để ở file bên cạnh là feedback không ai đọc.

### Dấu hiệu "đây là feedback", và ba việc làm NGAY

Dấu hiệu: "sai rồi", "không phải thế", "đừng…", "bỏ… đi", "lần sau…", "từ giờ…",
"tôi đã bảo rồi", "vẫn còn…", "đã nói bao nhiêu lần", hoặc người dùng tự tay sửa
lại output vừa nhận.

1. **Sửa output ngay** — sửa mọi chỗ mắc cùng lỗi, không chỉ chỗ bị chỉ tay.
2. **Ghi một dòng vào sổ** của đúng skill vừa chạy, nếu là loại THÀNH LUẬT.
3. **Nói ra**: "Đã ghi vào SỔ LỖI của `<ten-skill>`: SAI … → ĐÚNG …". Không nói
   thì người dùng phải tin suông là feedback không bay mất.

### MỘT LẦN hay THÀNH LUẬT — đừng để agent tự đoán

| Ghi vào sổ khi (đúng một dòng là ghi) | Chỉ sửa output, KHÔNG ghi sổ |
|---|---|
| Nói về CÁCH LÀM, không về dữ liệu của lần này | Gắn với dữ liệu riêng lần này: tên, số, link sai |
| Có chữ chỉ tương lai: "lần sau", "từ giờ", "luôn", "đừng bao giờ" | Là đổi ý muốn, không phải sửa lỗi: "thôi làm bản ngắn hơn" |
| Người dùng đang nhắc lại lần hai | Chọn một trong hai phương án ngang nhau |
| Lỗi này chắc chắn lặp lại ở lần chạy sau với input khác | Chỉ đúng cho một khách, một kênh, một file |

Không xếp được vào cột nào thì hỏi đúng một câu: "cái này áp cho mọi lần sau,
hay chỉ lần này?" Hỏi một câu rẻ hơn ghi sai một luật cứng vào sổ.

### Luật chống phình sổ

> Sổ tối đa **12 dòng**. Sổ là hàng chờ, không phải kho.

- Một dòng bị nhắc **lần thứ hai** → nâng thành luật cứng có tên trong thân
  skill (Bước 5), rồi **xoá khỏi sổ**: thân skill đã chặn thì sổ khỏi giữ
- Đủ 12 dòng mà có dòng mới → gộp các dòng cùng chủ đề thành một, hoặc nâng hai
  dòng cũ nhất lên luật cứng. **Không xoá một dòng chỉ vì nó cũ**
- Thêm dòng xong thì `wc -l SKILL.md`: phải dưới 300 theo Bước 8. Quá thì tách
  phần tra cứu ra file cạnh bên, **không cắt sổ**

---

## Bước 8 — Xuất file, đặt đúng chỗ

```
~/.claude/skills/<ten-skill>/SKILL.md      Claude Code, tự nạp
```

- Một skill một thư mục, tên thư mục **trùng** `name` trong frontmatter
- File phụ (template, ví dụ, script) để cạnh SKILL.md và **dẫn link từ trong
  SKILL.md**, agent không tự đoán ra
- SKILL.md giữ gọn, nhắm dưới 300 dòng. Dài hơn thì tách phần tra cứu ra file
  riêng, SKILL.md chỉ giữ luật, bước và sổ lỗi
- Bản gốc để sửa là bản trong kho public `nqh-skills/skills/`. Thư mục
  `~/.claude/skills/synced/` do Cloud đồng bộ — sửa tay ở đó sẽ bị ghi đè
- Trong phiên Cowork không ghi thẳng được vào tài khoản: dựng file rồi dùng
  `propose_skills` để người dùng bấm lưu, đồng thời gửi kèm file cho họ

## Bước 9 — Test kích hoạt trước khi coi là xong

Mở **phiên agent mới** và thử ba câu:

1. Một câu dùng đúng từ khoá trong description → phải bật
2. Một câu tả việc bằng lời khác, không dùng từ khoá → nên bật
3. Một câu thuộc skill họ hàng gần nhất → **không** được bật

Câu 2 trượt thì thêm cụm từ vào description. Câu 3 bật nhầm thì thêm mệnh đề
phân biệt vào description, không sửa body.

---

## Luật viết, áp cho mọi skill sinh ra từ đây

- Tiếng Việt, câu ngắn, không emoji, không lời quảng cáo
- Không có câu nào chỉ để nối ý. Cắt được là cắt
- Không viết "hãy chuyên nghiệp", "hãy cẩn thận". Đó không phải chỉ dẫn
- Ưu tiên bảng và khối lệnh hơn đoạn văn
- Xuống dòng quanh cột 80 cho dễ đọc trong terminal
- Skill nói với agent, không nói với độc giả. Câu lệnh, không phải bài giảng

---

## Checklist trước khi giao skill

- [ ] `name` kebab-case, trùng tên thư mục
- [ ] `description` đủ ba mệnh đề, có ít nhất 3 cụm từ khoá người dùng thật sự gõ
- [ ] Có một câu luận đề dưới tiêu đề
- [ ] Có mục "Dùng khi nào" và có nói lúc nào KHÔNG dùng
- [ ] Có bước 0 chặn đầu (mục tiêu hoặc có đáng làm không)
- [ ] Mỗi bước có động từ mệnh lệnh và điều kiện xong
- [ ] Có ít nhất một khối copy-dán được
- [ ] Có ít nhất một luật cứng được đặt tên, kèm cặp SAI/ĐÚNG
- [ ] Có checklist tự kiểm, trong đó có một dòng bắt con người đọc
- [ ] Có footer "Skill này phải tự tốt lên" bản 5 điều
- [ ] Có mục `## SỔ LỖI ĐÃ BỊ NHẮC` ở cuối file, kèm luật ghi và trần 12 dòng
- [ ] Đã chạy test 3 câu ở Bước 9
- [ ] Đã in mục "Giả định tôi đã tự điền" nếu có chỗ tự điền

---

## Bảng tra nhanh

| Tình huống | Làm gì |
|---|---|
| Người dùng kể một quy trình dài | Soi 6 mẩu ở Bước 0, hỏi gộp phần thiếu |
| Người dùng nói "cứ làm đi" | Viết luôn, in mục giả định ở cuối |
| Người dùng nói "sai rồi", "lần sau đừng…" | Sửa output, ghi một dòng vào sổ, nói là đã ghi |
| Không rõ feedback một lần hay thành luật | Hỏi một câu: áp mọi lần sau hay chỉ lần này |
| Sổ lỗi đã đủ 12 dòng | Gộp dòng cùng chủ đề, hoặc nâng lên luật cứng rồi xoá khỏi sổ |
| Skill không tự bật | Sửa description, thêm cụm từ thật, đừng đụng body |
| Skill bật nhầm việc | Thêm mệnh đề phân biệt vào description |
| Skill phình quá dài | Tách phần tra cứu ra file cạnh bên, dẫn link |
| Luật nghe hay mà không có chuyện thật | Hỏi "lần gần nhất việc này hỏng thế nào" |
| Sửa skill đã có | Giữ nguyên `name`, chỉ vá phần trượt checklist |

## Nhớ một câu

Skill làm agent nhớ luật và đi đúng quy trình. Nó không làm kết quả thành đúng.
Ba việc vẫn của con người: đặt mục tiêu trước khi giao, đọc kết quả rồi sửa chỗ
sai trước khi tin, và duyệt trước khi thứ gì đó rời khỏi máy.

## Skill này phải tự tốt lên

1. **Đọc SỔ LỖI trước khi làm.** Mục `## SỔ LỖI ĐÃ BỊ NHẮC` ở cuối file này là
   luật cứng, không phải ghi chú. Đọc hết nó trước khi xuất chữ đầu tiên.
2. **Bị nhắc thì ghi ngay trong phiên đó.** Sửa output, thêm một dòng vào sổ,
   rồi nói ra là đã ghi. Không để đến cuối phiên, không chỉ "đề xuất".
3. **Eval sau mỗi lần chạy.** Tự chấm ngắn theo checklist: thiếu bước nào, chỗ
   nào người dùng phải sửa tay. Chỗ đáng sửa mà không phải lỗi bị nhắc thì đề
   xuất sửa thẳng vào SKILL.md này.
4. **Thi thoảng lookup để update.** Nơi đặt skill, giới hạn độ dài và cách agent
   nạp skill đổi theo phiên bản công cụ. Chi tiết nào đã vài tháng tuổi thì kiểm
   lại từ tài liệu gốc trước khi tin.
5. **Không biết thì hỏi người.** Cái gì ngoài tầm thì nói thẳng và chỉ người
   dùng đi hỏi ai.

## SỔ LỖI ĐÃ BỊ NHẮC

Đọc hết mục này TRƯỚC khi xuất chữ đầu tiên. Mỗi dòng là một lỗi người dùng đã
nhắc; lặp lại nó lần nữa là lỗi nặng hơn lần đầu. Ghi một dòng một lỗi kèm ngày,
dòng mới xuống dưới cùng, trần 12 dòng — luật chống phình ở Bước 7.

| Ngày | SAI | ĐÚNG |
|---|---|---|
| 2026-09-22 | Dùng đại từ "Tôi / Các bạn" trong content ngắn | Short, caption, post ngắn dùng "mình / bạn"; "Tôi / Các bạn" chỉ dành cho kịch bản dài |
| 2026-09-22 | Sửa thẳng file skill trong `~/.claude/skills/synced/` | Sửa bản trong kho public `nqh-skills/skills/`; thư mục synced do Cloud ghi đè |
| 2026-09-22 | Áp một cơ chế mới xuống cả bộ 21 skill trong một lượt | Sửa một skill mẫu, chờ Hiếu duyệt hợp đồng, rồi mới nhân bản |
