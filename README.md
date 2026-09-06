# nqh-skills

Bộ Claude Agent Skills cá nhân của Nguyễn Quang Hiếu (WANGHIE).

## Skills

| Skill | Việc |
|---|---|
| [`nqh-app-landing`](./nqh-app-landing) | Dựng landing page cho app điện thoại + bộ ảnh App Store, bắt đầu từ nghiên cứu đối thủ cùng ngách |

## Cài đặt

### Claude Code

```bash
git clone https://github.com/wanghie/nqh-skills.git
mkdir -p ~/.claude/skills
ln -sfn "$(pwd)/nqh-skills/nqh-app-landing" ~/.claude/skills/nqh-app-landing
```

### Claude.ai / Cowork

Settings → Capabilities → Skills → upload thư mục skill dưới dạng `.zip`.

## Skill phụ thuộc

`nqh-app-landing` gọi tới 6 skill cộng đồng. Cài kèm:

```bash
mkdir -p ~/Vibe-Code/_khac && cd ~/Vibe-Code/_khac
git clone https://github.com/boraoztunc/skills.git bora-skills
mkdir -p ~/.claude/skills
for s in competitor-alternatives landing-page page-cro app-store-screenshots frontend-design; do
  ln -sfn ~/Vibe-Code/_khac/bora-skills/$s ~/.claude/skills/$s
done
npx skills add https://github.com/inference-sh/skills --skill landing-page-design
```

Không cài cũng chạy được — mỗi bước đã có checklist rút gọn nhúng sẵn trong `SKILL.md`.

## Nguồn tham khảo

- [boraoztunc/skills](https://github.com/boraoztunc/skills)
- [inference-sh/skills](https://github.com/inference-sh/skills)

## License

MIT
