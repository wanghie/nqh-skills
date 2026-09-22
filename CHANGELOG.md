# Changelog

## 1.2.0

**Thêm:**

- `nqh-research-niche-product` — quét CẢ MỘT NGÁCH trên TikTok/Instagram/YouTube cho
  tới khi bão hoà, lọc creator bán sản phẩm của chính họ, ra bảng vật lý/digital/dịch
  vụ × giá × tính năng × chân dung khách, matrix định vị, TAM/SAM/SOM và khoảng trống
  đã kiểm bằng xu hướng xã hội. Khác `research-product-via-channel` (bóc MỘT kênh).

**Sửa:**

- `tools/build_index.py` — cụm từ khoá trong `description` viết bằng nháy kép escape
  (`\"...\"`) bị lọt dấu `\` vào bảng index. Nay strip dấu `\` cuối cụm và bỏ cụm
  trùng lặp.

## 1.1.0

**Thêm:**

- `nqh-app-ux-teardown` — bóc UX + motion của app đối thủ thành quyết định sản phẩm.
  Bóc 3 app một lượt để tách quy ước ngành khỏi lựa chọn riêng; Lớp 0 "điều kiện
  chuyển giao" chạy trước mọi lớp khác để chặn cargo-cult copy; đếm friction và vị
  trí paywall từ ảnh Mobbin; cột ĐỘC gắn cờ dark pattern; accessibility 5 dòng;
  motion đo bằng ffmpeg, chấm theo mục đích trước rồi mới chấm nhanh chậm.
  Đầu ra: TEARDOWN.md + MOTION-TOKENS.json + frame PNG làm chứng cứ.

**Đổi:**

- `README.md` — dọn mục "Skill còn nằm ngoài repo": bỏ 3 dòng đã gộp xong, ghi rõ
  các skill còn lại chỉ sống trong tài khoản Claude chứ không có file trên đĩa.

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
