#!/usr/bin/env python3
"""
batch_link.py — 批量添加双向 related link

1. 复用 fusion_candidates 逻辑获取候选对（从 kb/cards/ 读取）
2. 过滤: 排除涉及 superseded/archived 卡的对（kb/cards/ 中只有 accepted 卡，天然过滤）
3. 对每对: 互相 append 到 related 列表（去重）
4. 写回（仅改 frontmatter，body 不变）
"""

import re
import yaml
from collections import defaultdict
from itertools import combinations
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "outputs" / "llm_wiki"
KB_CARDS = BASE / "kb" / "cards"


def normalize_term(term: str) -> str:
    """Lowercase, strip, remove punctuation (keep CJK and alphanumeric)."""
    t = term.lower().strip()
    t = re.sub(r'[^\w\s一-鿿㐀-䶿]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def split_frontmatter(text: str) -> tuple[str, str]:
    """Split markdown into raw YAML frontmatter and body (after second ---)."""
    if not text.startswith("---"):
        return "", text
    end = text.find("---", 3)
    if end == -1:
        return "", text
    raw_yaml = text[3:end]
    body = text[end + 3:]
    return raw_yaml, body


def reassemble(fm_dict: dict, body: str) -> str:
    """Reassemble frontmatter dict + body into markdown file content."""
    yaml_str = yaml.dump(
        fm_dict,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=200,
    )
    return f"---\n{yaml_str}---{body}"


def find_fusion_candidates(cards: dict) -> list[tuple[str, str]]:
    """
    Reuse fusion_candidates logic: inverted index on canonical_concept + aliases,
    return pairs from different source_ids.
    """
    inverted = defaultdict(set)
    for card_id, info in cards.items():
        terms = [info['canonical_concept']] + info['aliases']
        seen_norms = set()
        for term in terms:
            if not term:
                continue
            norm = normalize_term(term)
            if norm and norm not in seen_norms:
                seen_norms.add(norm)
                inverted[norm].add(card_id)

    pairs = set()
    for norm_term, card_ids in inverted.items():
        if len(card_ids) < 2:
            continue
        card_list = sorted(card_ids)
        for a, b in combinations(card_list, 2):
            sources_a = cards[a]['source_ids']
            sources_b = cards[b]['source_ids']
            if sources_a.isdisjoint(sources_b):
                pairs.add((a, b) if a < b else (b, a))

    return sorted(pairs)


def main():
    # 1. Parse all accepted cards in kb/cards/
    cards_meta = {}  # id -> {canonical_concept, aliases, source_ids}
    cards_files = {}  # id -> filepath

    for f in sorted(KB_CARDS.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        raw_yaml, body = split_frontmatter(text)
        if not raw_yaml:
            continue
        try:
            fm = yaml.safe_load(raw_yaml)
        except yaml.YAMLError:
            continue
        if not isinstance(fm, dict):
            continue

        card_id = fm.get('id', f.stem)
        canonical = fm.get('canonical_concept', '')
        aliases = fm.get('aliases', []) or []
        source_ids = fm.get('source_ids', []) or []
        if isinstance(source_ids, str):
            source_ids = [source_ids]

        cards_meta[card_id] = {
            'canonical_concept': canonical,
            'aliases': aliases,
            'source_ids': set(source_ids),
        }
        cards_files[card_id] = f

    # 2. Find fusion candidate pairs
    pairs = find_fusion_candidates(cards_meta)
    print(f"Found {len(pairs)} candidate pairs from fusion logic")

    # 3. Build link map: card_id -> set of card_ids to add to related
    link_map = defaultdict(set)
    for a, b in pairs:
        link_map[a].add(b)
        link_map[b].add(a)

    # 4. Update cards
    updated_cards = 0
    total_links_added = 0

    for card_id, new_related in sorted(link_map.items()):
        filepath = cards_files.get(card_id)
        if filepath is None:
            continue

        text = filepath.read_text(encoding="utf-8")
        raw_yaml, body = split_frontmatter(text)
        if not raw_yaml:
            continue

        fm = yaml.safe_load(raw_yaml)
        if not isinstance(fm, dict):
            continue

        # Get existing related list
        existing_related = fm.get('related', []) or []
        if isinstance(existing_related, str):
            existing_related = [existing_related]

        existing_set = set(existing_related)
        additions = new_related - existing_set

        if not additions:
            continue

        # Append new links (deduplicated)
        updated_related = existing_related + sorted(additions)
        fm['related'] = updated_related

        # Write back
        new_text = reassemble(fm, body)
        filepath.write_text(new_text, encoding="utf-8")

        updated_cards += 1
        total_links_added += len(additions)

    print(f"Batch link complete:")
    print(f"  Pairs linked: {len(pairs)}")
    print(f"  Cards updated: {updated_cards}")
    print(f"  Total link entries added: {total_links_added}")


if __name__ == "__main__":
    main()
