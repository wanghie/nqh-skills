---
name: nqh-dev-secrets
description: Giữ API key và mật khẩu an toàn khi giao việc cho AI agent, và đẩy code lên GitHub mà không làm lộ gì. Dùng khi chạm tới API key, secret, .env, 1Password, biến môi trường, khi nối một API hay MCP mới, trước khi commit hoặc push, khi dựng CI, khi cho người thứ hai hoặc một agent khác vào repo, và khi "merge rồi mà trang không đổi".
---

# /secrets

Giao việc cho agent mà không trao chìa khoá, và đẩy code mà không làm lộ gì.

---

## Khi nào dùng

Đọc file này trước khi làm bất cứ việc nào sau đây:

- Chạm tới API key, secret, `.env`, biến môi trường
- Nối một API hoặc MCP mới vào agent
- Commit hoặc push, nhất là lần đầu của một dự án
- Cho người thứ hai, hoặc một agent khác, vào repo của mình
- Dựng CI, hoặc quyết định luật nào cần tự động kiểm
- Gặp câu "merge rồi mà trang không đổi"

---

## 1. Hai loại chìa khoá, đừng nhầm

**Public key** giống số tài khoản ngân hàng. Ai biết cũng được.

**Private key** (secret key) giống mật khẩu Internet Banking. Lộ là mất.

Nhiều dịch vụ gọi cả hai đều là "API key". Luật một dòng:

> Key nào bắt đầu bằng `sk_`, `sb_secret_`, `secret`, `service_role`, hoặc dịch vụ
> gọi nó là **secret**, thì **không bao giờ rời khỏi máy bạn**.

---

## 2. Lưu ở đâu, ba tầng

| Tầng | Công cụ | Dùng khi |
|---|---|---|
| Quản lý mật khẩu | 1Password, Bitwarden, Doppler | Nguồn sự thật cho cả team. Agent phải hỏi quyền mỗi lần lấy |
| Secret của chính nền tảng | Vercel env, GitHub Actions secrets, Supabase Vault, Cloudflare Workers secrets | Key chỉ dùng cho một dịch vụ |
| Kho khoá chuyên dụng | AWS Secrets Manager, Google Secret Manager, HashiCorp Vault | Nhiều môi trường, cần nhật ký ai lấy key lúc nào |

Trên máy: macOS Keychain, `.env` nằm trong `.gitignore` không ngoại lệ, và
`.env.example` chỉ chứa **tên biến, không chứa giá trị**.

### Bốn chỗ người ta thật sự mất key

```
export API_KEY=...   trong .zshrc
nhắn key vào Slack hoặc Zalo cho chính mình
để trong Notion, Google Keep, Apple Notes
clipboard, tức vừa bấm sao chép xong rồi quên
```

### Xoá clipboard sau khi dùng key

Clipboard là bề mặt duy nhất hệ điều hành không gác. Mọi tiến trình đều đọc
được, im lặng, không để lại dấu. Universal Clipboard đẩy nó qua iCloud sang
iPhone và iPad. Nó nằm đó tới khi bị đè.

Chạy ngay sau khi vừa xong việc với key:

```bash
pbcopy < /dev/null
```

---

## 3. Bốn luật khi giao việc cho agent

Chép bốn dòng này vào `AGENTS.md` của dự án bạn.

### Luật 1. Đưa tên biến, đừng đưa giá trị

```
SAI     Gọi API Linear giúp tôi, key là lin_api_a1b2c3...
ĐÚNG    Key nằm ở biến LINEAR_API_KEY. Đọc từ process.env, đừng in ra.
```

Dán chuỗi key vào khung chat là nó nằm vĩnh viễn trong lịch sử hội thoại và
log của bên thứ ba. Bạn không xoá được. Tên biến thì ai đọc cũng vô hại.

### Luật 2. Đừng để nó in key ra màn hình

```
SAI     console.log('key:', process.env.API_KEY)
        echo $API_KEY
        curl -v ...                    cờ -v in cả header Authorization

ĐÚNG    echo ${API_KEY:0:8}...                     chỉ tám ký tự đầu
        [ -n "$API_KEY" ] && echo "co key"         chỉ kiểm có hay không
        curl -s ... -o /dev/null -w "%{http_code}" chỉ xem mã trả về
```

Terminal có thể đang share màn hình hoặc ghi hình. Log của nền tảng và CI cũng lưu.

### Luật 3. Quét trước khi push, kể cả repo private

```bash
git diff --cached | grep -inE "sk-[a-zA-Z0-9]{20}|sb_secret_[A-Za-z0-9_-]{10}|AKIA[0-9A-Z]{16}|ghp_[a-zA-Z0-9]{36}|xox[baprs]-|-----BEGIN"
```

Có kết quả là dừng. Hôm nay private, mai bạn đổi ý mở mã nguồn, là lộ hết.

### Luật 4. Lộ rồi thì xoay key, đừng đi xoá commit

**Git giữ mọi blob vĩnh viễn:**

- Xoá file ở commit sau **không** xoá nó khỏi lịch sử
- Force-push sau `git filter-repo` **không** xoá nó khỏi các bản đã clone
- Chuyển repo sang private **không** xoá nó, vì fork dùng chung kho object

Việc duy nhất còn tác dụng: vào dịch vụ đó, huỷ key cũ, tạo key mới.

---

## 4. Cách để agent chạm được mà không cầm chìa

Mô hình nên hướng tới, không phải `.env`:

```
ĐỂ TRONG .env                       ĐỂ TRONG 1PASSWORD
agent cần một khoá                  agent cần một khoá
   ↓                                   ↓
nó tự mở file .env                  nó chỉ có tên chỗ cất: op://...
   ↓                                   ↓
có khoá, gọi API                    1Password nhận yêu cầu
                                       ↓
Không ai được hỏi.                  MÁY HỎI VÂN TAY CỦA BẠN
Không bước nào ở giữa.                 ↓
Không để lại dấu vết.               trả khoá cho đúng lệnh đó
                                    giá trị không hiện ra màn hình
```

Cài một lần: 1Password → `Settings` → `Developer` → bật `Command-Line Interface`.
Rồi giao cho agent:

```
Hãy lấy toàn bộ mã khoá đang nằm trong .env của tôi, đẩy lên 1Password,
sắp xếp thành từng vault theo từng dự án.
Không in giá trị của key nào ra màn hình.
```

**Đánh đổi:** cách này chậm hơn, vì mỗi lần agent cần là bạn phải chạm vân tay.
Dự án không có dữ liệu nhạy cảm thì `.env` là đủ. Có dữ liệu khách hàng, có tiền,
có tài khoản ngân hàng thì đổi lấy sự bất tiện đó là xứng.

---

## 5. Khoá nằm đúng một chỗ là rủi ro

> Khoá quan trọng nhất phải nằm ở **ít nhất hai chỗ**, và **một trong hai chỗ đó
> phải hỏi con người** trước khi đưa ra.

Kiểm dự án của bạn ngay: mỗi khoá đang nằm ở mấy chỗ?

---

## 6. Ba thứ không bao giờ commit

**Khoá bảo mật.** Không API key, không token, không `.env`.

**Danh sách người dùng thật.** Không `.xlsx`, không `.csv` có tên và email thật.

**Tệp nặng.** Video, ảnh gốc, bản dựng. Chúng đi qua kho riêng, không qua git.

Trước mỗi commit nhìn `git status` một lượt, và `git add <file cụ thể>` chứ đừng
`git add -A`.

---

## 7. Làm chung với người thứ hai, và với agent khác

### Đặt luật đúng chỗ agent thật sự đọc

Agent chỉ tự nạp `AGENTS.md` hoặc `CLAUDE.md` ở **gốc đúng repo nó đang đứng**.
Viết hướng dẫn tuyệt vời mà để ở repo khác thì nó không bao giờ đọc tới.

### Viết ra danh sách "dừng lại và hỏi người"

Agent có quyền kỹ thuật không có nghĩa là nó được tự quyết. Ví dụ:

1. Chạy bất kỳ lệnh nào có `--apply`, vì cờ đó ghi thật
2. Push thẳng vào `main`
3. Đụng vào danh tính người dùng
4. Xoá hoặc sửa dữ liệu người khác đã nộp
5. Đổi khoá phiên đăng nhập, vì đổi là đá văng toàn bộ người đang đăng nhập

### Bắt agent kéo bản mới nhất trước khi làm

```bash
git checkout main && git pull
```

Làm trên bản cũ là làm theo luật đã bị sửa, và cái sai đó chỉ lộ sau khi đã push.

---

## 8. Tài liệu không phải là bảo đảm

Viết luật vào `CONTRIBUTING.md` không ngăn được ai làm sai. Chỉ CI mới ngăn.

Bộ kiểm tối thiểu cho một dự án nhỏ, chạy trên mọi pull request:

```yaml
- Không tệp cấm, không chuỗi giống khoá trong repo
- Test cũ không gãy
- File máy sinh ra phải khớp với nguồn của nó
- Mọi đường dẫn tới tệp ngoài phải trỏ vào thứ có thật
```

Mỗi bước khi đỏ phải **in ra phải làm gì**, không chỉ in ra là sai.

---

## 9. Merge xong chưa chắc đã lên trang

Nền tảng deploy có thể chặn theo **tác giả commit**. Vercel chỉ build khi người
tạo commit nằm trong team. Không nằm trong đó thì lượt deploy hiện
`Deployment was blocked`, code vẫn đúng chỗ trên `main`, mà trang không đổi.

Nó chặn cả `github-actions[bot]`, tức chặn luôn workflow tự động của bạn.

Gặp câu "merge rồi mà trang không đổi" thì **kiểm quyền deploy trước khi đi tìm
lỗi trong code**.

---

## 10. Luật xuyên suốt: lỗi im lặng là loại đắt nhất

> Mỗi đường đi phải có một chỗ báo khi việc đáng lẽ xảy ra thì không xảy ra.
> Không có chỗ đó thì im lặng bị đọc thành thành công.

Áp vào mọi thứ bạn build: sau khi ghi, đọc lại và so. Sau khi tải lên, đo lại
kích thước. Sau khi merge, kiểm xem nó có thật sự lên không.

---

## Bảng tra nhanh

| Tình huống | Làm gì |
|---|---|
| Vừa copy một key | `pbcopy < /dev/null` sau khi dùng xong |
| Agent xin key để gọi API | Đưa tên biến, không đưa giá trị |
| Sắp push lần đầu | Quét theo Luật 3, kiểm `.gitignore` có `.env` |
| Lỡ dán key vào chat | Xoay key ngay. Đừng xoá commit, vô ích |
| Cho người mới vào repo | Viết `AGENTS.md` ở gốc repo đó |
| Merge rồi mà trang không đổi | Kiểm quyền deploy trước, đừng sửa code |
| Nghi một tệp lên thiếu | Đọc lại kích thước trên kho, so với bản ở máy |
