# nqh-skills

Kho skill cá nhân của Nguyễn Quang Hiếu (WANGHIE) cho Claude Code / Cowork.
Một skill = một thư mục = một file `SKILL.md` agent tự đọc khi gặp đúng loại việc.

Repo private. Đây là **nơi duy nhất** chứa skill — không tạo repo skill mới.

---

## Quy ước đặt tên

```
nqh-<nhóm>-<việc>
```

Nhóm cố định, gõ tiền tố là ra cả cụm:

| Tiền tố | Nhóm | Ví dụ |
|---|---|---|
| `nqh-research-` | Nghiên cứu thị trường, đối thủ, sản phẩm | `nqh-research-market` |
| `nqh-video-` | Dựng video, short, caption | `nqh-video-captions` |
| `nqh-content-` | Viết nội dung, giọng văn | `nqh-content-engine` |
| `nqh-app-` | App, UI, landing page | `nqh-app-landing` |
| `nqh-dev-` | Code, ops, bảo mật | `nqh-dev-secrets` |

Luật cứng:

1. Tên thư mục **phải trùng** `name:` trong frontmatter. `tools/build_index.py` sẽ báo lỗi nếu lệch.
2. Chỉ chữ thường và gạch ngang. Không gạch dưới, không viết hoa.
3. `description` trong frontmatter phải chứa **từ khoá kích hoạt trong dấu ngoặc kép** — đó là thứ agent dùng để tự chọn skill, và là thứ bảng index bên dưới trích ra.
4. Thêm skill mới → chạy `python3 tools/build_index.py` để cập nhật bảng.

---

## Danh sách skill

<!-- INDEX:START -->

### App / Design

| Skill | Dùng khi | Gọi bằng |
|---|---|---|
| [`nqh-app-landing`](./skills/nqh-app-landing) | Dùng khi Hiếu muốn dựng LANDING PAGE cho một app điện thoại và/hoặc bộ ẢNH APP STORE, bắt đầu bằng việc nghiên cứu đối thủ cùng ngách rồi bóc DNA trang của họ | `làm landing cho app`, `trang giới thiệu app`, `landing page app`, `ảnh app store`, `screenshot app store`, `dựng trang bán app` |
| [`nqh-app-ux-teardown`](./skills/nqh-app-ux-teardown) | Bóc UX app đối thủ thành quyết định sản phẩm — bóc 3 app một lượt để tách quy ước ngành khỏi lựa chọn riêng, kiểm điều kiện chuyển giao trước khi mượn cơ chế, đếm friction và… | `bóc UX app`, `teardown UX`, `bóc hiệu ứng của`, `app này UX thế nào`, `nghiên cứu app đối thủ` |

### Dev / Ops

| Skill | Dùng khi | Gọi bằng |
|---|---|---|
| [`nqh-dev-secrets`](./skills/nqh-dev-secrets) | Giữ API key và mật khẩu an toàn khi giao việc cho AI agent, và đẩy code lên GitHub mà không làm lộ gì. Dùng khi chạm tới API key, secret, .env, 1Password, biến môi trường, khi… | `merge rồi mà trang không đổi` |

### Nghiên cứu

| Skill | Dùng khi | Gọi bằng |
|---|---|---|
| [`nqh-research-creator-product`](./skills/nqh-research-creator-product) | Bóc tách 1 sản phẩm cụ thể của creator qua công tắc loại (SaaS / Dịch vụ / Vật lý / Digital / Cộng đồng) + bộ lớp riêng theo loại. Có nhánh dịch vụ với kinh tế đơn vị + kinh tế… | `research sản phẩm creator`, `bóc tách sản phẩm X`, `clone sản phẩm này được không` |
| [`nqh-research-market`](./skills/nqh-research-market) | Research sâu một thị trường bằng nhiều agent chạy song song, ra một bản research đã kiểm chứng, mọi nhận định gắn nhãn độ tin, số phải tự tính chứ không trích lại, bắt buộc có… | `research market`, `research thị trường`, `làm research về`, `so sánh thị trường` |
| [`nqh-research-niche-product`](./skills/nqh-research-niche-product) | Quét CẢ MỘT NGÁCH trên TikTok/Instagram/YouTube cho tới khi bão hoà, lọc creator bán sản phẩm của chính họ, ra bảng vật lý/digital/dịch vụ × giá × tính năng × chân dung khách,… | `tìm sản phẩm ngách`, `find niche product`, `cả ngách này ai đang bán gì`, `quét cả ngách` |
| [`nqh-research-teardown`](./skills/nqh-research-teardown) | Phân rã một sản phẩm có sẵn để hiểu ruột của nó, viết thành bản đặc tả sạch, rồi build bản của riêng mình trong một phiên làm việc mới chỉ đọc đặc tả. Đúng phương pháp… | `teardown`, `phân rã sản phẩm`, `reverse engineer`, `build cái tương tự X`, `sản phẩm X hoạt động thế nào` |

### Video

| Skill | Dùng khi | Gọi bằng |
|---|---|---|
| [`nqh-video-captions`](./skills/nqh-video-captions) | Burn phụ đề word-by-word (highlight từng từ đang nói) lên video, style riêng cho khán giả Việt và khán giả Anh — xử lý đúng dấu tiếng Việt, số từ mỗi dòng, font hỗ trợ Unicode | `gắn phụ đề`, `làm caption`, `sub kiểu Opus/Hormozi`, `burn sub`, `caption tiếng Việt bị lỗi dấu` |
| [`nqh-video-cut-silence`](./skills/nqh-video-cut-silence) | Cắt im lặng, khoảng chết và từ đệm (ừ, à, kiểu như / um, uh, you know) khỏi video talking head, dùng bộ từ đệm riêng cho khán giả Việt và khán giả Anh | `cắt im lặng`, `bỏ ừ à`, `làm gọn video`, `cut dead air`, `video nói lê thê quá` |
| [`nqh-video-punch-zoom`](./skills/nqh-video-punch-zoom) | Thêm nhịp cho video talking head bằng punch-zoom vào từ nhấn mạnh và Ken Burns push chậm ở đoạn dài, tự dò điểm nhấn từ transcript theo bộ từ khoá riêng cho tiếng Việt và tiếng Anh | `video nhìn tĩnh quá`, `thêm zoom`, `punch zoom`, `làm cho đỡ chán`, `thêm nhịp cho video` |
| [`nqh-video-reframe`](./skills/nqh-video-reframe) | Chuyển video ngang 16:9 sang dọc 9:16 (hoặc 4:5, 1:1) bám theo mặt người nói bằng MediaPipe, dùng kiểu cắt cảnh cứng thay vì pan trôi | `chuyển sang dọc`, `làm 9:16`, `crop cho TikTok/Reels/Shorts`, `video ngang muốn đăng short`, `reframe` |
| [`nqh-video-shorts`](./skills/nqh-video-shorts) | Chạy full pipeline biến 1 video talking head thô thành short 9:16 hoàn chỉnh — bóc transcript, cắt im lặng và từ đệm, reframe bám mặt, punch zoom, burn caption — theo đúng tệp… | `dựng thành short`, `làm reels từ video này`, `biến video này thành TikTok`, `chạy full pipeline`, `edit video này giúp tôi` |
| [`nqh-video-transcribe`](./skills/nqh-video-transcribe) | Tạo transcript word-level (JSON) cho video/audio bằng Whisper, tự nhận diện tệp khán giả Việt hay Anh. Dùng khi user muốn bóc lời video, lấy timestamp từng từ, hoặc trước khi… | `bóc transcript`, `lấy phụ đề`, `transcribe video này`, `chuẩn bị dựng short` |

<!-- INDEX:END -->

---

## Cài

```bash
git clone git@github.com:wanghie/nqh-skills.git ~/Projects/nqh-skills
cd ~/Projects/nqh-skills
./setup --clean      # nối symlink vào ~/.claude/skills, gỡ symlink chết của repo cũ
```

Sửa file trong repo → skill tự cập nhật (nhờ symlink). Mở phiên Claude Code mới để agent nhận.

Với Claude.ai / Cowork: Settings → Capabilities → Skills → upload thư mục skill dạng `.zip`.

---

## Tìm nhanh

| Cần | Làm |
|---|---|
| Xem có skill nào | Bảng index bên trên |
| Tìm theo từ khoá | `grep -ril "từ khoá" skills/` |
| Xem skill nào nhắc tới X | `grep -rn "X" skills/*/SKILL.md` |
| Trên GitHub | Gõ `nqh` vào ô search repo, hoặc lọc topic `claude-skills` |

---

## Skill còn nằm ngoài repo

Các skill đang chạy trong tài khoản Claude (không nằm trên đĩa dưới dạng file sửa được).
Khi nào cần version hoá thì export về đây:

- [ ] `nqh-content-engine` — viết lại kịch bản dài theo giọng NQH
- [ ] `nqh-shortform-engine` — content ngắn EN→VI
- [ ] `nqh-transcript-engine` — dịch transcript EN→VI
- [ ] `nqh-triky-engine` — giọng bác Tri Kỷ Cảm Xúc
- [ ] `nqh-thumbnail-engine` — bóc DNA thumbnail
- [ ] `nqh-broll-director` — prompt B-roll
- [ ] `nqh-app-designer` — dựng UI app từ một ý tưởng
- [ ] `nqh-skill-forge` — skill tạo ra skill
- [ ] `govrl-email-builder` — dựng thư onboarding GOVRL

---

## Đổi tên từ repo cũ

| Tên cũ | Tên mới | Repo cũ |
|---|---|---|
| `researchmarket` | `nqh-research-market` | research-apps |
| `teardown` | `nqh-research-teardown` | research-apps |
| `secrets` | `nqh-dev-secrets` | research-apps |
| `govrl-research-creator-product` | `nqh-research-creator-product` | Skill_nqh_agent |
| `sf-transcribe` | `nqh-video-transcribe` | Skill_Video_editor |
| `sf-cut-silence` | `nqh-video-cut-silence` | Skill_Video_editor |
| `sf-reframe` | `nqh-video-reframe` | Skill_Video_editor |
| `sf-punch-zoom` | `nqh-video-punch-zoom` | Skill_Video_editor |
| `sf-captions` | `nqh-video-captions` | Skill_Video_editor |
| `sf-shorts` | `nqh-video-shorts` | Skill_Video_editor |

Symlink cũ trong `~/.claude/skills` trỏ về tên cũ sẽ chết — `./setup --clean` dọn giúp.

## License

MIT
