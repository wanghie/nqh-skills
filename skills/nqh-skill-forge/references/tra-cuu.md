# nqh-skill-forge — tra cứu

Phần tra cứu tách khỏi `SKILL.md` để file chính còn chỗ cho SỔ LỖI lên đủ trần 10
dòng. Mở file này ở Bước 9 và trước lúc giao skill.

## Checklist trước khi giao skill

- [ ] `name` kebab-case, trùng tên thư mục
- [ ] `description` đủ ba mệnh đề, có ít nhất 3 cụm từ khoá người dùng thật sự gõ
- [ ] Có câu luận đề dưới tiêu đề, có mục "Dùng khi nào" kèm lúc KHÔNG dùng
- [ ] Có bước 0 chặn đầu (đặt mục tiêu hoặc "có đáng làm không")
- [ ] Mỗi bước có động từ mệnh lệnh và điều kiện xong nhìn là biết
- [ ] Có ít nhất một khối copy-dán được
- [ ] Có ít nhất một luật cứng được đặt tên, kèm cặp SAI/ĐÚNG
- [ ] Có checklist tự kiểm, trong đó có một dòng bắt con người đọc
- [ ] Có footer `## Skill này phải tự tốt lên` bản 5 điều
- [ ] Có `## SỔ LỖI ĐÃ BỊ NHẮC` copy nguyên văn từ `references/khoi-so-loi.md`,
      bảng 4 cột `Ngày | Nguồn | SAI | ĐÚNG`, rỗng nếu chưa có feedback thật
- [ ] `python3 tools/check_so_loi.py` sạch ở kho chứa skill
- [ ] Đã chạy test 3 câu ở Bước 9 trong một phiên agent mới
- [ ] Đã in mục "Giả định tôi đã tự điền" nếu có chỗ tự điền

## Cặp SAI/ĐÚNG

Description:

```
SAI     Skill giúp research thị trường một cách chuyên nghiệp.
ĐÚNG    Research sâu một thị trường bằng nhiều agent song song, bắt buộc có TAM
        SAM SOM. Dùng khi cần biết thị trường có những ai, giá bao nhiêu, còn
        khoảng trống nào. Kích hoạt khi nói "research market", "research thị
        trường", "làm research về".
```

Câu SAI hỏng vì không chứa cụm nào người dùng sẽ gõ, và không nói skill ép làm gì.

Tiêu đề bước:

```
SAI     ## Bước 2 — Phân tích dữ liệu
ĐÚNG    ## Bước 2 — Quy mọi đơn giá về cùng một đơn vị rồi in giả định quy đổi
```

## Test kích hoạt — xử khi trượt

| Câu thử | Kỳ vọng | Trượt thì làm gì |
|---|---|---|
| Đúng từ khoá trong description | Phải bật | Kiểm `name` có trùng tên thư mục, symlink còn sống (`readlink`) |
| Tả việc bằng lời khác, không dùng từ khoá | Nên bật | Thêm đúng cụm từ người dùng gõ vào description, không đụng body |
| Việc của skill họ hàng gần nhất | **Không** được bật | Thêm mệnh đề phân biệt ("KHÁC <skill kia> ở chỗ…") vào description |

## Bảng tra nhanh

| Tình huống | Làm gì |
|---|---|
| Người dùng kể một quy trình dài | Soi 6 mẩu ở Bước 0, hỏi gộp phần thiếu |
| Người dùng nói "cứ làm đi" | Viết luôn, in mục giả định ở cuối |
| Người dùng nói "sai rồi", "lần sau đừng…" | Sửa output; ghi sổ nếu THÀNH LUẬT; nói ra là đã ghi |
| Không rõ feedback một lần hay thành luật | Hỏi một câu: áp mọi lần sau hay chỉ lần này |
| Skill vừa bị nhắc mà chưa có sổ | Dán khối rỗng từ `khoi-so-loi.md` vào SKILL.md trong repo, rồi ghi dòng đầu |
| Sổ đã đủ 10 dòng | Gộp dòng cùng chủ đề, hoặc nâng dòng lặp nhiều nhất lên luật cứng rồi xoá khỏi sổ |
| Dán sổ xong không biết đúng chưa | `python3 tools/check_so_loi.py` |
| SKILL.md vượt 300 dòng sau khi dán sổ | Báo ra cho người dùng, tách phần tra cứu sang `references/`, **không cắt sổ** |
| Skill không tự bật | Sửa description, thêm cụm từ thật, đừng đụng body |
| Skill bật nhầm việc | Thêm mệnh đề phân biệt vào description |
| Luật nghe hay mà không có chuyện thật | Hỏi "lần gần nhất việc này hỏng thế nào" |
| Sửa skill đã có | Giữ nguyên `name`, chỉ vá phần trượt checklist |
