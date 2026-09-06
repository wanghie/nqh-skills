# Luật khi agent làm việc trên repo này

## Trước khi thêm skill

1. Đọc `README.md` phần Quy ước đặt tên. Tên sai = không merge.
2. Tìm xem đã có skill làm việc đó chưa: `grep -ril "<việc>" skills/`. Trùng chức năng thì sửa skill cũ, không tạo skill mới.
3. Thư mục mới đặt trong `skills/`, tên `nqh-<nhóm>-<việc>`, bên trong bắt buộc có `SKILL.md`.

## Frontmatter bắt buộc

```yaml
---
name: <trùng y hệt tên thư mục>
description: <việc skill làm>. Kích hoạt khi nói "từ khoá 1", "từ khoá 2", "từ khoá 3".
---
```

`description` là thứ duy nhất agent đọc để quyết định có dùng skill hay không. Viết cho máy chọn đúng, không viết cho người đọc hay.

## Sau khi sửa

```bash
python3 tools/build_index.py     # cập nhật bảng index trong README
```

Script sẽ thoát với mã lỗi nếu tên thư mục lệch `name:`. Sửa xong mới commit.

## Cấm

- Không đưa API key, token, mật khẩu, đường dẫn máy cá nhân, dữ liệu khách vào bất kỳ file nào.
- Không commit file media (`.mp4`, `.mov`, `.wav`) — đã chặn trong `.gitignore`.
- Không tạo repo skill mới ở nơi khác. Skill mới về đây.

## Version

`VERSION` tăng theo semver. Đổi nội dung skill → patch. Thêm skill → minor. Đổi quy ước đặt tên → major.
Ghi lại trong `CHANGELOG.md`.
