#!/usr/bin/env python3
"""Build kb/indexes/cards.md from all adopted v3 cards.

Walks `outputs/llm_wiki/kb/cards/<id>.md`, extracts frontmatter
(id, title, card_type, status, source_ids, provenance_card), and the
matching kb provenance file to check for `v2_anchor`. Writes a Chinese
markdown index sorted by id.
"""
from __future__ import annotations
import re
import pathlib

LOOP = pathlib.Path(__file__).resolve().parents[1]
CARDS = LOOP / "outputs/llm_wiki/kb/cards"
PROV = LOOP / "outputs/llm_wiki/kb/provenance"
INDEX = LOOP / "outputs/llm_wiki/kb/indexes/cards.md"


def parse_frontmatter(path: pathlib.Path) -> dict:
    out: dict[str, object] = {}
    in_fm = False
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("---"):
            if not in_fm:
                in_fm = True
                i += 1
                continue
            else:
                break
        if in_fm:
            m = re.match(r"^(\w[\w_]*):\s*(.*)$", line)
            if m:
                key, val = m.group(1), m.group(2).strip()
                if val.startswith("[") and val.endswith("]"):
                    inner = val[1:-1].strip()
                    items = [s.strip().strip('"').strip("'") for s in inner.split(",") if s.strip()] if inner else []
                    out[key] = items
                elif val == "":
                    # could be a block list/object — peek ahead
                    block_items = []
                    j = i + 1
                    while j < len(lines) and lines[j].startswith(" "):
                        bm = re.match(r"^\s*-\s*(.+?)\s*$", lines[j])
                        if bm:
                            block_items.append(bm.group(1).strip().strip('"').strip("'"))
                            j += 1
                            continue
                        break
                    if block_items:
                        out[key] = block_items
                        i = j - 1
                    else:
                        out[key] = ""
                else:
                    out[key] = val
        i += 1
    return out


def has_v2_anchor(prov_path: pathlib.Path) -> str | None:
    if not prov_path.exists():
        return None
    text = prov_path.read_text(encoding="utf-8")
    m = re.search(r"^v2_anchor:\s*\n\s*card_id:\s*(\S+)", text, re.M)
    if m:
        return m.group(1)
    return None


def main() -> None:
    rows = []
    for cp in sorted(CARDS.glob("*.md")):
        if cp.name == "README.md":
            continue
        fm = parse_frontmatter(cp)
        cid = fm.get("id") or cp.stem
        title = fm.get("title", "")
        ctype = fm.get("card_type", "")
        status = fm.get("status", "")
        sids = fm.get("source_ids", [])
        if isinstance(sids, list):
            sid_str = ", ".join(sids)
        else:
            sid_str = str(sids)
        v2 = has_v2_anchor(PROV / f"{cid}.md")
        rows.append((cid, title, ctype, status, sid_str, v2))

    accepted = [r for r in rows if r[3] == "accepted"]
    by_type: dict[str, int] = {}
    for r in accepted:
        by_type[r[2]] = by_type.get(r[2], 0) + 1
    v2_deltas = [r for r in accepted if r[5]]

    out_lines = [
        "# v3 KB 卡片索引",
        "",
        f"截至 2026-05-27，v3 KB 共有 **{len(accepted)}** 张 `accepted` 卡片（{len(v2_deltas)} 张携带 `v2_anchor` 反链 v2 accepted card）。所有卡片均通过 publication_gate 或 fusion_audit。",
        "",
        "## 按 card_type 统计",
        "",
        "| card_type | 数量 |",
        "| --- | ---: |",
    ]
    for k in sorted(by_type, key=lambda x: -by_type[x]):
        out_lines.append(f"| `{k}` | {by_type[k]} |")
    out_lines.extend([
        "",
        f"| **总计** | **{len(accepted)}** |",
        "",
        "## 卡片清单",
        "",
        "| id | title | card_type | source_id | v2_anchor |",
        "| --- | --- | --- | --- | --- |",
    ])
    for cid, title, ctype, status, sid_str, v2 in accepted:
        v2_cell = f"`{v2}`" if v2 else ""
        out_lines.append(f"| `{cid}` | {title} | `{ctype}` | `{sid_str}` | {v2_cell} |")

    if v2_deltas:
        out_lines.extend([
            "",
            "## v2 anchored 卡片（fusion_audit 通过的 provenance_delta）",
            "",
            "下列 v3 卡片在 v2 accepted KB 中有同主题锚卡，本卡作为 delta / 扩展 / 第三方实现而被采纳。",
            "",
        ])
        for cid, title, _, _, _, v2 in v2_deltas:
            out_lines.append(f"- `{cid}` — {title} ↔ v2 `{v2}`")

    INDEX.parent.mkdir(parents=True, exist_ok=True)
    INDEX.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    print(f"wrote {INDEX.relative_to(LOOP)} with {len(accepted)} accepted cards ({len(v2_deltas)} v2-anchored)")


if __name__ == "__main__":
    main()
