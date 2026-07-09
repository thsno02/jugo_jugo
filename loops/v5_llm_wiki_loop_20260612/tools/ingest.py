#!/usr/bin/env python3
"""
ingest.py — 将 drafts/cards/ 的卡片 ingest 进 kb/

- superseded 卡 → kb/archive/ (justification → kb/justification/)
- 其余卡: status draft→accepted → kb/cards/ (justification → kb/justification/)
- 重建 kb/indexes/cards.md
"""

import shutil
import yaml
from pathlib import Path
from collections import defaultdict

BASE = Path(__file__).resolve().parent.parent / "outputs" / "llm_wiki"
DRAFTS_CARDS = BASE / "drafts" / "cards"
DRAFTS_JJ = BASE / "drafts" / "justification"
KB_CARDS = BASE / "kb" / "cards"
KB_ARCHIVE = BASE / "kb" / "archive"
KB_JJ = BASE / "kb" / "justification"
KB_INDEX = BASE / "kb" / "indexes" / "cards.md"


def split_frontmatter(text: str) -> tuple[str, str]:
    """Split markdown into raw YAML frontmatter and body (after second ---)."""
    if not text.startswith("---"):
        return "", text
    end = text.find("---", 3)
    if end == -1:
        return "", text
    # frontmatter is between first --- and second ---
    raw_yaml = text[3:end]
    body = text[end + 3:]  # everything after closing ---
    return raw_yaml, body


def reassemble(fm_dict: dict, body: str) -> str:
    """Reassemble frontmatter dict + body into markdown file content."""
    # Dump YAML with block style for lists
    yaml_str = yaml.dump(
        fm_dict,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=200,
    )
    return f"---\n{yaml_str}---{body}"


def main():
    # Ensure output dirs exist
    KB_CARDS.mkdir(parents=True, exist_ok=True)
    KB_ARCHIVE.mkdir(parents=True, exist_ok=True)
    KB_JJ.mkdir(parents=True, exist_ok=True)
    KB_INDEX.parent.mkdir(parents=True, exist_ok=True)

    accepted_count = 0
    archived_count = 0
    # For index: source_id -> [slug]
    index_data = defaultdict(list)

    for card_file in sorted(DRAFTS_CARDS.glob("*.md")):
        text = card_file.read_text(encoding="utf-8")
        raw_yaml, body = split_frontmatter(text)
        if not raw_yaml:
            print(f"  SKIP (no frontmatter): {card_file.name}")
            continue

        fm = yaml.safe_load(raw_yaml)
        if not isinstance(fm, dict):
            print(f"  SKIP (bad frontmatter): {card_file.name}")
            continue

        slug = card_file.stem
        status = fm.get("status", "draft")

        # Justification source file
        jj_file = DRAFTS_JJ / card_file.name

        if status == "superseded":
            # Move card to archive
            shutil.copy2(card_file, KB_ARCHIVE / card_file.name)
            # Move justification
            if jj_file.exists():
                shutil.copy2(jj_file, KB_JJ / jj_file.name)
            archived_count += 1
        else:
            # Change status to accepted
            fm["status"] = "accepted"
            new_text = reassemble(fm, body)
            (KB_CARDS / card_file.name).write_text(new_text, encoding="utf-8")
            # Move justification
            if jj_file.exists():
                shutil.copy2(jj_file, KB_JJ / jj_file.name)
            accepted_count += 1

            # Collect index data
            source_ids = fm.get("source_ids", []) or []
            if isinstance(source_ids, str):
                source_ids = [source_ids]
            first_source = source_ids[0] if source_ids else "_no_source"
            index_data[first_source].append(slug)

    # Build index file
    lines = []
    for source_id in sorted(index_data.keys()):
        lines.append(f"## {source_id}")
        for slug in sorted(index_data[source_id]):
            lines.append(f"- {slug}")
        lines.append("")  # blank line between groups

    KB_INDEX.write_text("\n".join(lines), encoding="utf-8")

    print(f"Ingest complete: {accepted_count} accepted, {archived_count} archived")
    print(f"Index written to {KB_INDEX} ({len(index_data)} source groups)")


if __name__ == "__main__":
    main()
