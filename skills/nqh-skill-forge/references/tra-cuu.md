# nqh-skill-forge — tra cứu

Hai bảng tách khỏi `SKILL.md` để giữ file dưới 300 dòng (luật Bước 8). Mở file
này trước khi giao skill, và mỗi khi bí ở một tình huống.

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
- [ ] Có `## SỔ LỖI ĐÃ BỊ NHẮC` ở cuối, bảng đúng 4 cột `Ngày | Nguồn | SAI | ĐÚNG`
- [ ] Sổ của skill MỚI để rỗng (chỉ header), không có dòng mẫu bịa
- [ ] `wc -l` dưới 300 và thân skill dưới 268 để sổ lên đủ 10 dòng vẫn vừa
- [ ] Đã chạy test 3 câu ở Bước 9
- [ ] Đã in mục "Giả định tôi đã tự điền" nếu có chỗ tự điền

## Bảng tra nhanh

| Tình huống | Làm gì |
|---|---|
| Người dùng kể một quy trình dài | Soi 6 mẩu ở Bước 0, hỏi gộp phần thiếu |
| Người dùng nói "cứ làm đi" | Viết luôn, in mục giả định ở cuối |
| Skill không tự bật | Sửa description, thêm cụm từ thật, đừng đụng body |
| Skill bật nhầm việc | Thêm mệnh đề phân biệt vào description |
| Skill phình quá dài | Tách phần tra cứu ra file cạnh bên, dẫn link |
| Luật nghe hay mà không có chuyện thật | Hỏi "lần gần nhất việc này hỏng thế nào" |
| Sửa skill đã có | Giữ nguyên `name`, chỉ vá phần trượt checklist |
| Bị nhắc "sai rồi", "lần sau đừng…" | Sửa hết cùng loại, ghi một dòng vào sổ theo Bước 7d, nói là đã ghi |
| Skill đã có nhưng chưa có mục SỔ LỖI | Dán khối RỖNG vào cuối SKILL.md trong repo (Bước 7b), không bịa dòng |
| Không biết ghi vào bản nào | File trong repo; `~/.claude/skills` là symlink (Bước 7c) |
| Không rõ một lần hay thành luật | Hỏi một câu: áp mọi lần sau, hay chỉ lần này |
| Lỗi bị nhắc lần hai, hoặc sổ đã đầy | Nâng lên luật cứng có tên ở Bước 5 rồi xoá dòng khỏi sổ |

## Cặp SAI/ĐÚNG cho description (Bước 1)

```
SAI     Skill giúp research thị trường một cách chuyên nghiệp.
ĐÚNG    Research sâu một thị trường bằng nhiều agent song song, mọi nhận định
        gắn nhãn độ tin, bắt buộc có TAM SAM SOM. Dùng khi cần biết thị trường
        có những ai, giá bao nhiêu. Kích hoạt khi nói "research thị trường".
```

Câu SAI hỏng vì nó không chứa một cụm nào người dùng sẽ gõ, và không nói skill
ép làm gì.

## Cặp SAI/ĐÚNG cho tiêu đề bước (Bước 4)

```
SAI     ## Bước 2 — Phân tích dữ liệu
ĐÚNG    ## Bước 2 — Quy mọi đơn giá về cùng một đơn vị rồi in giả định quy đổi
```

## Test kích hoạt (Bước 9)

Mở **phiên agent mới** và thử ba câu:

1. Một câu dùng đúng từ khoá trong description → phải bật
2. Một câu tả việc bằng lời khác, không dùng từ khoá → nên bật
3. Một câu thuộc skill họ hàng gần nhất → **không** được bật

Câu 2 trượt thì thêm cụm từ vào description. Câu 3 bật nhầm thì thêm mệnh đề
phân biệt vào description, không sửa body.
