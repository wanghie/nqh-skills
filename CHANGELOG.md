# Changelog

## 1.0.0

Gom 4 repo skill rời rạc về một repo duy nhất.

**Gộp vào:**

- `Skill_nqh_agent` → `nqh-research-creator-product`
- `research-apps` → `nqh-research-market`, `nqh-research-teardown`, `nqh-dev-secrets`
- `Skill_Video_editor` (nhánh master) → 6 skill `nqh-video-*` + `lib/` + `presets/`
- `Vibe-Code/_khac/nqh-skills` → `nqh-app-landing`

**Bỏ:**

- `SKILL-AI-AGENT` — trùng y hệt `research-apps`, không có nội dung riêng.

**Đổi:**

- Chuẩn hoá tên: tất cả skill dùng tiền tố `nqh-<nhóm>-`. Bảng đối chiếu tên cũ/mới ở `README.md`.
- Thêm `tools/build_index.py` sinh bảng index tự động từ frontmatter, đồng thời kiểm tra tên thư mục khớp `name:`.
- `setup` thêm cờ `--clean` để dọn symlink chết trỏ về repo cũ.
