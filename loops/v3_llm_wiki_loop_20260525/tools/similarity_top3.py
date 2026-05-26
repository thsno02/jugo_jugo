#!/usr/bin/env python3
"""V3 title similarity top-3.

Tokenizes draft and accepted card titles with Jieba and computes Jaccard set
similarity per `SIMILARITY_MECHANISM_V3.md`. Reads the v2 cards index for
candidate titles. Writes one JSON artifact per draft card under
`outputs/llm_wiki/drafts/similarity/`.

Usage:

    python3 loops/v3_llm_wiki_loop_20260525/tools/similarity_top3.py

The script is intentionally self-contained: no flags, default paths only. It
prints a short status line per draft so the operator can verify each artifact.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

import jieba

REPO_ROOT = Path(__file__).resolve().parents[3]
LOOP_DIR = REPO_ROOT / "loops" / "v3_llm_wiki_loop_20260525"
DRAFT_CARDS_DIR = LOOP_DIR / "outputs" / "llm_wiki" / "drafts" / "cards"
SIMILARITY_DIR = LOOP_DIR / "outputs" / "llm_wiki" / "drafts" / "similarity"
V2_INDEX = REPO_ROOT / "loops" / "v2_llm_wiki_loop_20260525" / "outputs" / "llm_wiki" / "kb" / "indexes" / "cards.md"

TITLE_RE = re.compile(r"^title:\s*(.+?)\s*$")
ID_RE = re.compile(r"^id:\s*(.+?)\s*$")
INDEX_ROW_RE = re.compile(r"^\|\s*(?P<title>[^|]+?)\s*\|\s*`(?P<path>[^`]+)`\s*\|\s*(?P<status>[^|]+?)\s*\|")

PUNCT_RE = re.compile(r"[\s　\.,;:!\?\-—–\(\)\[\]\{\}\"'`~/\\\|\*\+#@\$%\^&、。，．；：！？（）《》“”‘’]+")


def normalize(text: str) -> str:
    text = text.strip().lower()
    text = PUNCT_RE.sub(" ", text)
    return text.strip()


def tokens(title: str) -> set[str]:
    normalized = normalize(title)
    if not normalized:
        return set()
    raw = jieba.lcut(normalized, cut_all=False)
    return {t.strip() for t in raw if t.strip()}


def jaccard(a: set[str], b: set[str]) -> float:
    if not a or not b:
        return 0.0
    inter = a & b
    union = a | b
    if not union:
        return 0.0
    return len(inter) / len(union)


def parse_draft_card(path: Path) -> tuple[str, str]:
    title = None
    card_id = None
    with path.open("r", encoding="utf-8") as f:
        in_fm = False
        for line in f:
            line = line.rstrip("\n")
            if line.startswith("---"):
                if not in_fm:
                    in_fm = True
                    continue
                else:
                    break
            if in_fm:
                m = TITLE_RE.match(line)
                if m:
                    title = m.group(1)
                m2 = ID_RE.match(line)
                if m2:
                    card_id = m2.group(1)
    if not title:
        raise RuntimeError(f"no title found in {path}")
    if not card_id:
        raise RuntimeError(f"no id found in {path}")
    return card_id, title


def parse_v2_index(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            m = INDEX_ROW_RE.match(line)
            if not m:
                continue
            title = m.group("title").strip()
            card_path = m.group("path").strip()
            status = m.group("status").strip()
            if title == "标题":
                continue
            rows.append({
                "title": title,
                "card_path": card_path,
                "status": status,
                "card_id": Path(card_path).stem,
            })
    return rows


def now_iso() -> str:
    tz = timezone(timedelta(hours=8))
    return datetime.now(tz).replace(microsecond=0).isoformat()


def main() -> int:
    if not V2_INDEX.exists():
        print(f"ERROR: v2 index missing: {V2_INDEX}", file=sys.stderr)
        return 2
    if not DRAFT_CARDS_DIR.exists():
        print(f"ERROR: draft cards dir missing: {DRAFT_CARDS_DIR}", file=sys.stderr)
        return 2

    SIMILARITY_DIR.mkdir(parents=True, exist_ok=True)

    existing = parse_v2_index(V2_INDEX)
    existing_tokens = [(row, tokens(row["title"])) for row in existing]

    drafts = sorted(p for p in DRAFT_CARDS_DIR.glob("*.md") if p.name != "README.md")
    if not drafts:
        print("WARN: no draft cards found", file=sys.stderr)
        return 0

    created = now_iso()
    artifacts: list[Path] = []

    for draft_path in drafts:
        card_id, title = parse_draft_card(draft_path)
        draft_tokens = tokens(title)
        scored: list[dict] = []
        for row, ex_tokens in existing_tokens:
            score = jaccard(draft_tokens, ex_tokens)
            shared = sorted(draft_tokens & ex_tokens)
            scored.append({
                "card_id": row["card_id"],
                "card_path": row["card_path"],
                "title": row["title"],
                "score": round(score, 4),
                "shared_tokens": shared,
            })
        scored.sort(key=lambda r: (-r["score"], r["card_id"]))
        top3 = scored[:3]
        for rank, entry in enumerate(top3, start=1):
            entry["rank"] = rank

        rel_draft = draft_path.relative_to(LOOP_DIR).as_posix()
        out = {
            "schema": "title_similarity_top3.v3",
            "draft_card": rel_draft,
            "draft_card_id": card_id,
            "draft_title": title,
            "tokenizer": "jieba",
            "tokenizer_version": getattr(jieba, "__version__", "unknown"),
            "metric": "jaccard_set_similarity",
            "comparison_base": "loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/indexes/cards.md",
            "comparison_base_card_count": len(existing),
            "draft_title_tokens": sorted(draft_tokens),
            "candidates": [
                {
                    "rank": e["rank"],
                    "card_id": e["card_id"],
                    "card_path": e["card_path"],
                    "title": e["title"],
                    "score": e["score"],
                    "shared_tokens": e["shared_tokens"],
                }
                for e in top3
            ],
            "created_time": created,
        }
        out_path = SIMILARITY_DIR / f"{card_id}.json"
        with out_path.open("w", encoding="utf-8") as f:
            json.dump(out, f, ensure_ascii=False, indent=2)
            f.write("\n")
        artifacts.append(out_path)
        print(f"OK {card_id} -> {out_path.relative_to(REPO_ROOT)} (top1 score={top3[0]['score'] if top3 else 'na'})")

    print(f"wrote {len(artifacts)} similarity artifact(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
