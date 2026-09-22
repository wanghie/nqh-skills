#!/usr/bin/env python3
"""Kiểm cơ chế SỔ LỖI ĐÃ BỊ NHẮC trên mọi SKILL.md của kho này.

Chạy:  python3 tools/check_so_loi.py
Thoát mã 1 nếu có LỖI. CẢNH BÁO không làm hỏng build, nhưng phải báo cho người dùng.

Bản gốc của khối sổ nằm ở kho public:
    skills/nqh-skill-forge/references/khoi-so-loi.md
Kho private không chứa bản gốc — đặt biến KHOI_GOC trỏ sang kho public để so khối:
    KHOI_GOC=~/Projects/nqh-skills/skills/nqh-skill-forge/references/khoi-so-loi.md
"""
import os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEADING = "## SỔ LỖI ĐÃ BỊ NHẮC"
TRAN_SO = 10
TRAN_DONG = 300
HEADER = "| Ngày | Nguồn | SAI | ĐÚNG |"
SEP = "|---|---|---|---|"
NGUON_HOP_LE = {"Hiếu", "review", "tự đo"}
ROW = re.compile(r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|([^|]*)\|")

def ban_goc() -> list[str] | None:
    p = os.environ.get("KHOI_GOC")
    cands = [Path(p).expanduser()] if p else []
    cands += [ROOT / "skills/nqh-skill-forge/references/khoi-so-loi.md",
              ROOT.parent / "nqh-skills/skills/nqh-skill-forge/references/khoi-so-loi.md"]
    for c in cands:
        if c.is_file():
            return c.read_text(encoding="utf-8").rstrip("\n").split("\n")
    return None

def main() -> int:
    goc = ban_goc()
    loi, canh_bao, ok = [], [], 0

    if goc:
        # Bản gốc phải tự nhất quán: con số trong khối phải khớp số dòng thật của khối.
        khung = len(goc)
        than = TRAN_DONG - khung - 1 - TRAN_SO
        txt = "\n".join(goc)
        if f"chiếm {khung} dòng khung" not in txt or f"dưới {than} dòng" not in txt:
            loi.append(f"khoi-so-loi.md: khối dài {khung} dòng nhưng chữ trong khối ghi "
                       f"số khác (phải là 'chiếm {khung} dòng khung' và 'dưới {than} dòng')")
    else:
        canh_bao.append("không tìm thấy khoi-so-loi.md — bỏ qua bước so khối với bản gốc")

    for f in sorted(ROOT.glob("skills/*/SKILL.md")):
        ten = f.parent.name
        lines = f.read_text(encoding="utf-8").rstrip("\n").split("\n")
        n = len(lines)
        if n >= TRAN_DONG:
            canh_bao.append(f"{ten}: {n} dòng, vượt trần {TRAN_DONG} — BÁO cho người dùng, "
                            f"tách phần tra cứu ra references/, không cắt sổ")
        if HEADING not in lines:
            loi.append(f"{ten}: thiếu mục '{HEADING}'")
            continue
        i = lines.index(HEADING)
        khoi = lines[i:]
        if HEADER not in khoi or SEP not in khoi:
            loi.append(f"{ten}: bảng sổ không đúng 4 cột '{HEADER}'")
            continue
        j = khoi.index(SEP)
        if goc:
            khung_thuc = [l.replace(ten, "<ten-skill>") for l in khoi[: j + 1]]
            if khung_thuc != goc:
                loi.append(f"{ten}: khối sổ lệch bản gốc khoi-so-loi.md "
                           f"(dán lại, đừng chép tay)")
        rows = [l for l in khoi[j + 1:] if l.strip().startswith("|")]
        if len(rows) > TRAN_SO:
            loi.append(f"{ten}: sổ có {len(rows)} dòng, quá trần {TRAN_SO}")
        for r in rows:
            m = ROW.match(r)
            if not m:
                loi.append(f"{ten}: dòng sổ sai định dạng '| YYYY-MM-DD | Nguồn | SAI | ĐÚNG |'"
                           f" → {r[:60]}")
                continue
            nguon = m.group(2).strip()
            if nguon not in NGUON_HOP_LE:
                loi.append(f"{ten}: nguồn '{nguon}' không hợp lệ "
                           f"(chỉ: {' · '.join(sorted(NGUON_HOP_LE))})")
        ok += 1

    for c in canh_bao:
        print(f"CẢNH BÁO  {c}")
    for e in loi:
        print(f"LỖI       {e}")
    print(f"\n{ok} skill có SỔ LỖI đúng chuẩn · {len(loi)} lỗi · {len(canh_bao)} cảnh báo")
    return 1 if loi else 0

if __name__ == "__main__":
    sys.exit(main())
