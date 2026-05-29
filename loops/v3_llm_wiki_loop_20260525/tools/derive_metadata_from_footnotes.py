#!/usr/bin/env python3
"""Regenerate frontmatter `related:` (and optionally `source_ids:`) from each card's ## Footnotes section.

Per CARD_CONTRACT_V3.md, `related:` is auto-derived; do not maintain by hand.

Footnote target classification:
- target ends in `.md` and is a bare basename (no `/`)         -> v3 KB card (same loop)
- target contains `/loops/v2_llm_wiki_loop_*/...*.md`          -> v2 KB card (cross-loop)
- target contains `data/raw/...`                                -> raw source
- target starts with `http://` / `https://`                     -> external URL

Default: rewrite `related:` only (union of v3 + v2 card ids referenced in footnotes).
With --include-source-ids: also rewrite `source_ids:` from raw footnotes.

Usage:

    python3 tools/derive_metadata_from_footnotes.py              # all kb/cards/*.md
    python3 tools/derive_metadata_from_footnotes.py --dry-run    # print what would change
    python3 tools/derive_metadata_from_footnotes.py --include-source-ids
    python3 tools/derive_metadata_from_footnotes.py path/to/one_card.md
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

LOOP = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_CARDS_DIR = LOOP / "outputs/llm_wiki/kb/cards"

FOOTNOTE_LINE_RE = re.compile(r"^\[\^([^\]]+)\]:\s*(.+?)\s*$")
MD_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
URL_RE = re.compile(r"https?://\S+")
RAW_RE = re.compile(r"data/raw/[^\s`]+")
V2_PATH_RE = re.compile(r"v2_llm_wiki_loop_[^/]+/outputs/llm_wiki/kb/cards/([\w\-.]+)\.md")

RELATED_FIELD_RE = re.compile(r"^(related:\s*).*$", re.M)
SOURCE_IDS_FIELD_RE = re.compile(r"^(source_ids:\s*).*$", re.M)


def split_frontmatter(text: str) -> tuple[str, str, str] | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fm = text[4:end].rstrip("\n")
    body_start = end + 4
    if body_start < len(text) and text[body_start] == "\n":
        body_start += 1
    return text[:4], fm, text[body_start:]


def extract_footnotes(body: str) -> list[tuple[str, str]]:
    """Return list of (footnote_id, expansion_text)."""
    out: list[tuple[str, str]] = []
    in_footnotes_section = False
    for line in body.splitlines():
        if line.strip() == "## Footnotes":
            in_footnotes_section = True
            continue
        if line.startswith("## ") and in_footnotes_section:
            break
        if not in_footnotes_section:
            continue
        m = FOOTNOTE_LINE_RE.match(line)
        if m:
            out.append((m.group(1), m.group(2)))
    return out


def classify_target(expansion: str) -> dict:
    """Classify a footnote expansion into target categories."""
    found = {"v3_cards": [], "v2_cards": [], "raw_paths": [], "urls": []}

    # 1) markdown link targets
    for _label, target in MD_LINK_RE.findall(expansion):
        target = target.strip()
        if target.startswith("http://") or target.startswith("https://"):
            found["urls"].append(target)
            continue
        m2 = V2_PATH_RE.search(target)
        if m2:
            found["v2_cards"].append(m2.group(1))
            continue
        # bare basename or relative path ending in .md (treat last segment as id if simple)
        if target.endswith(".md"):
            base = target.rsplit("/", 1)[-1][:-3]
            # exclude v2 path we already matched, and exclude README
            if base and base != "README":
                found["v3_cards"].append(base)
            continue

    # 2) angle-bracket URLs
    for url in URL_RE.findall(expansion):
        url = url.rstrip(">,.)")
        if url not in found["urls"]:
            found["urls"].append(url)

    # 3) raw paths (backtick-quoted or bare)
    for raw in RAW_RE.findall(expansion):
        raw = raw.rstrip("`,.)")
        if raw not in found["raw_paths"]:
            found["raw_paths"].append(raw)

    return found


def derive_related(footnotes: list[tuple[str, str]]) -> list[str]:
    related: list[str] = []
    seen: set[str] = set()
    for _fid, expansion in footnotes:
        cls = classify_target(expansion)
        for cid in cls["v3_cards"] + cls["v2_cards"]:
            if cid not in seen:
                seen.add(cid)
                related.append(cid)
    return related


def derive_source_ids(footnotes: list[tuple[str, str]]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for _fid, expansion in footnotes:
        cls = classify_target(expansion)
        for raw in cls["raw_paths"]:
            # source_id convention: the path segment under data/raw/<type>/<source_id>/...
            parts = raw.split("/")
            if len(parts) >= 4 and parts[0] == "data" and parts[1] == "raw":
                sid = parts[3]
                if sid not in seen:
                    seen.add(sid)
                    out.append(sid)
    return out


def replace_field(fm: str, field_re: re.Pattern, new_value_str: str) -> tuple[str, bool]:
    """Replace `field: ...` with `field: [v1, v2]` style. Returns (new_fm, changed)."""
    new_fm, n = field_re.subn(lambda m: m.group(1) + new_value_str, fm, count=1)
    if n == 0:
        return fm, False
    return new_fm, new_fm != fm


def format_list_value(values: list[str]) -> str:
    if not values:
        return "[]"
    return "[" + ", ".join(values) + "]"


def process_card(path: pathlib.Path, dry_run: bool, include_source_ids: bool) -> dict:
    text = path.read_text(encoding="utf-8")
    parts = split_frontmatter(text)
    if not parts:
        return {"path": path, "skipped": "no_frontmatter"}
    head, fm, body = parts

    footnotes = extract_footnotes(body)
    if not footnotes:
        return {"path": path, "skipped": "no_footnotes", "footnotes": 0}

    new_related = derive_related(footnotes)
    new_related_str = format_list_value(new_related)

    fm_new, related_changed = replace_field(fm, RELATED_FIELD_RE, new_related_str)
    fields_changed = []
    if related_changed:
        fields_changed.append("related")

    source_ids_changed = False
    if include_source_ids:
        new_sids = derive_source_ids(footnotes)
        if new_sids:  # only rewrite if we found any
            fm_new, source_ids_changed = replace_field(
                fm_new, SOURCE_IDS_FIELD_RE, format_list_value(new_sids)
            )
            if source_ids_changed:
                fields_changed.append("source_ids")

    if not fields_changed:
        return {"path": path, "skipped": "no_change", "footnotes": len(footnotes)}

    new_text = head + fm_new + "\n---\n" + body
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")

    return {
        "path": path,
        "footnotes": len(footnotes),
        "changed": fields_changed,
        "new_related": new_related,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", help="Specific card files; default = all kb/cards/*.md")
    ap.add_argument("--dry-run", action="store_true", help="Print what would change without writing")
    ap.add_argument("--include-source-ids", action="store_true", help="Also rewrite source_ids from raw footnotes")
    ap.add_argument("--cards-dir", default=str(DEFAULT_CARDS_DIR), help="kb cards dir (default: outputs/llm_wiki/kb/cards)")
    args = ap.parse_args()

    if args.paths:
        targets = [pathlib.Path(p) for p in args.paths]
    else:
        targets = sorted(p for p in pathlib.Path(args.cards_dir).glob("*.md") if p.name != "README.md")

    n_changed = 0
    n_skipped = 0
    n_no_change = 0
    total = len(targets)

    for p in targets:
        res = process_card(p, args.dry_run, args.include_source_ids)
        if "skipped" in res:
            if res["skipped"] == "no_change":
                n_no_change += 1
            else:
                n_skipped += 1
            continue
        n_changed += 1
        marker = "[dry-run] " if args.dry_run else ""
        rel = res["path"].relative_to(LOOP)
        changed_fields = ",".join(res["changed"])
        print(f"{marker}{rel}: changed={changed_fields}, footnotes={res['footnotes']}, related={len(res['new_related'])}")

    print()
    print(f"summary: total={total} changed={n_changed} no_change={n_no_change} skipped={n_skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
