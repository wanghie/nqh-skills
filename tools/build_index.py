#!/usr/bin/env python3
"""Sinh lại bảng index trong README.md từ frontmatter của từng SKILL.md.

Chạy:  python3 tools/build_index.py
Không sửa tay bảng index — sửa description trong SKILL.md rồi chạy lại lệnh này.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
README = ROOT / "README.md"
START, END = "<!-- INDEX:START -->", "<!-- INDEX:END -->"

GROUPS = {
    "nqh-research-": "Nghiên cứu",
    "nqh-video-":    "Video",
    "nqh-app-":      "App / Design",
    "nqh-content-":  "Nội dung",
    "nqh-dev-":      "Dev / Ops",
}

def frontmatter(p: Path) -> dict:
    txt = p.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", txt, re.S)
    if not m:
        return {}
    out, key = {}, None
    for line in m.group(1).split("\n"):
        km = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line)
        if km:
            key = km.group(1)
            out[key] = km.group(2).strip().strip('"').strip("'")
        elif key:
            out[key] += " " + line.strip()
    return out

def group_of(name: str) -> str:
    for prefix, label in GROUPS.items():
        if name.startswith(prefix):
            return label
    return "Khác"

def split_desc(desc: str):
    """Tách description thành (dùng khi, từ khoá kích hoạt)."""
    raw = re.findall(r'["“\u2018\']([^"”\u2019\']+)["”\u2019\']', desc)
    triggers, seen = [], set()
    for t in raw:
        # description viết trong YAML nháy kép để lại dấu \ ở cuối mỗi cụm
        t = t.strip().rstrip("\\").strip()
        if t and t not in seen:
            seen.add(t)
            triggers.append(t)
    body = re.split(r'(?:Kích hoạt|Dùng khi user nói|Dùng khi nói)', desc)[0].strip()
    body = body.rstrip(" .")
    if len(body) > 180:
        body = body[:177].rsplit(" ", 1)[0] + "…"
    return body, ", ".join(f"`{t}`" for t in triggers[:6])

def main() -> int:
    rows = []
    for d in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        sk = d / "SKILL.md"
        if not sk.exists():
            print(f"BỎ QUA (không có SKILL.md): {d.name}", file=sys.stderr)
            continue
        fm = frontmatter(sk)
        name = fm.get("name", d.name)
        if name != d.name:
            print(f"LỆCH TÊN: thư mục {d.name} != name: {name}", file=sys.stderr)
            return 1
        body, triggers = split_desc(fm.get("description", ""))
        rows.append((group_of(name), name, body, triggers))

    rows.sort(key=lambda r: (r[0], r[1]))
    lines, current = [], None
    for grp, name, body, triggers in rows:
        if grp != current:
            current = grp
            lines += ["", f"### {grp}", "",
                      "| Skill | Dùng khi | Gọi bằng |", "|---|---|---|"]
        lines.append(f"| [`{name}`](./skills/{name}) | {body} | {triggers} |")
    lines.append("")
    block = "\n".join(lines)

    txt = README.read_text(encoding="utf-8")
    new = re.sub(f"{re.escape(START)}.*?{re.escape(END)}",
                 f"{START}\n{block}\n{END}", txt, flags=re.S)
    README.write_text(new, encoding="utf-8")
    print(f"Đã cập nhật index: {len(rows)} skill.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
