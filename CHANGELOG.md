# Changelog

## 1.3.0

Tách kho: skill quy trình/kỹ thuật ở lại kho public này, skill giọng văn và chuyện
đời tư sang kho riêng `nqh-skills-private`.

**Thêm (từ skill Cloud sync về máy):**

- `nqh-broll-director` — biến một ý/đoạn kịch bản thành cặp prompt: ảnh frame đầu
  (Gemini) + video image-to-video (Kling/Higgsfield), khoá Style DNA cho cả bộ.
  Kèm 3 file tra cứu trong `references/`.
- `nqh-app-designer` — từ một câu ý tưởng app ra bộ màn hình UI dựng được trên canvas.
- `nqh-appstore-shots` — bộ ảnh App Store iOS đúng pixel Apple, QC theo luật review.
- `nqh-skill-forge` — biến một quy trình thành file SKILL.md chuẩn.

**Đổi:**

- `description` của `nqh-skill-forge` trước đây không có một cụm từ khoá nào nên agent
  không tự bật. Nay đủ ba mệnh đề theo đúng luật của chính nó. `nqh-app-designer` và
  `nqh-appstore-shots` chuẩn hoá về mệnh đề "Kích hoạt khi nói ...".
- `README.md` + `CLAUDE.md` — ghi rõ kho này PUBLIC, và skill nào phải về kho private.
  Mục "Skill còn nằm ngoài repo" trỏ sang `nqh-skills-private` cho 4 skill giọng văn.
  Bỏ dòng "Repo private" sai sự thật (kho trên GitHub đang public).

**Còn nợ:**

- 3 tên lệch quy ước `nqh-<nhóm>-<việc>` nên rơi vào nhóm "Khác" của bảng index:
  `nqh-broll-director`, `nqh-appstore-shots`, `nqh-skill-forge`. Giữ nguyên tên để
  không gãy thói quen gọi skill; đổi tên là việc cần Hiếu chốt.

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
