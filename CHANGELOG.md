# Changelog

## 1.3.1

Cơ chế SỔ LỖI ĐÃ BỊ NHẮC áp xuống **cả 17 skill** của kho này, không chỉ skill mới.

**Sửa `nqh-skill-forge` — 4 lỗi review bắt được:**

- Bước 7 cũ chỉ bắt dán khối vào skill MỚI, nên skill đã có vĩnh viễn không có sổ.
  Thêm 7b: bảng "ai áp, khi nào" cho ba tình huống.
- Khối dán sang skill con từng ghi "trần 12 dòng" và trỏ "luật ở Bước 7" — skill con
  không có Bước 7. Giờ khối có một bản gốc duy nhất
  `skills/nqh-skill-forge/references/khoi-so-loi.md`, tự chứa 3 dòng luật, trần
  thống nhất **10 dòng** suy ra từ luật `SKILL.md < 300 dòng` (27 dòng khung + 1
  dòng trắng + 10 dòng sổ = 38 → thân skill dừng dưới 262 dòng).
- Hai hợp đồng chọi nhau (Bước 7 "nếu THÀNH LUẬT" vs footer "ghi vô điều kiện") gộp
  về 7d, có blockquote thứ tự ưu tiên: **sửa output LUÔN LUÔN, ghi sổ CHỈ KHI THÀNH
  LUẬT**, 7d thắng mọi chỗ nói khác.
- 7c trả lời dứt khoát "ghi vào bản nào": FILE TRONG REPO, kèm đường dẫn cả hai kho.

**Thêm `tools/check_so_loi.py`:** bắt thiếu khối, bảng sai 4 cột, sổ quá 10 dòng,
nguồn lạ ngoài `Hiếu · review · tự đo`, khối lệch bản gốc, file vượt 300 dòng. Nó
còn tự đối chiếu con số trần ghi trong khối với số dòng thật của khối, nên "tham
chiếu chết" kiểu trần 12/10 không tái diễn âm thầm. Hiện: 17/17 skill sạch, 0 lỗi.

**Áp xuống 16 skill còn lại:** mỗi SKILL.md thêm `## SỔ LỖI ĐÃ BỊ NHẮC` ở cuối,
bảng 4 cột `Ngày | Nguồn | SAI | ĐÚNG` **rỗng** (chỉ header) + 3 dòng luật. Không
bịa dòng mẫu cho skill chưa từng bị feedback — bảng rỗng là trung thực.

**4 file vượt trần 300 dòng, KHÔNG cắt nội dung có sẵn** (cần Hiếu chốt tách
`references/`):

| Skill | Trước | Sau | Ghi chú |
|---|---|---|---|
| `nqh-research-creator-product` | 655 | 683 | đã vượt từ trước |
| `nqh-research-niche-product` | 460 | 488 | đã vượt từ trước |
| `nqh-app-ux-teardown` | 357 | 385 | đã vượt từ trước |
| `nqh-appstore-shots` | 294 | 322 | **mới cán mốc vì thêm sổ** |

**Đổi khác:** cột NGUỒN bắt buộc cho mọi dòng sổ. Sổ của `nqh-skill-forge` có 6
dòng, nguồn `review` hoặc `tự đo`, không dòng nào gán cho Hiếu. Checklist 13 dòng,
bảng tra nhanh 12 tình huống, cặp SAI/ĐÚNG và cách xử test kích hoạt tách sang
`skills/nqh-skill-forge/references/tra-cuu.md`.

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
