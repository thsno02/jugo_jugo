#!/usr/bin/env python3
"""
fusion_candidates.py — 倒排索引发现跨源共享 term 的候选对

读取 drafts/cards/*.md 的 frontmatter，构建 normalized term → card_id 倒排索引，
输出每对来自不同 source_id 的卡，格式:
  card_a_id | card_b_id | shared_terms
"""

import os
import re
import string
import yaml
from collections import defaultdict
from itertools import combinations
from pathlib import Path

CARDS_DIR = Path(__file__).resolve().parent.parent / "outputs" / "llm_wiki" / "drafts" / "cards"


def normalize_term(term: str) -> str:
    """Lowercase, strip, remove punctuation (keep CJK and alphanumeric)."""
    t = term.lower().strip()
    # Remove ASCII punctuation but keep CJK characters and digits
    t = re.sub(r'[^\w\s一-鿿㐀-䶿]', '', t)
    # Collapse whitespace
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def parse_frontmatter(filepath: Path) -> dict | None:
    """Parse YAML frontmatter from a markdown file."""
    text = filepath.read_text(encoding='utf-8')
    if not text.startswith('---'):
        return None
    end = text.find('---', 3)
    if end == -1:
        return None
    try:
        fm = yaml.safe_load(text[3:end])
    except yaml.YAMLError:
        return None
    return fm


def main():
    # 1. Parse all cards
    cards = {}  # id -> {canonical_concept, aliases, source_ids}
    for f in sorted(CARDS_DIR.glob("*.md")):
        fm = parse_frontmatter(f)
        if fm is None:
            continue
        card_id = fm.get('id', f.stem)
        canonical = fm.get('canonical_concept', '')
        aliases = fm.get('aliases', []) or []
        source_ids = fm.get('source_ids', []) or []
        if isinstance(source_ids, str):
            source_ids = [source_ids]
        cards[card_id] = {
            'canonical_concept': canonical,
            'aliases': aliases,
            'source_ids': set(source_ids),
        }

    # 2. Build inverted index: normalized_term -> set of card_ids
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

    # 3. Find candidate pairs: entries with 2+ cards from different source_ids
    pair_terms = defaultdict(list)  # (card_a, card_b) -> [shared_terms]

    for norm_term, card_ids in inverted.items():
        if len(card_ids) < 2:
            continue
        # Filter to pairs from different sources
        card_list = sorted(card_ids)
        for a, b in combinations(card_list, 2):
            sources_a = cards[a]['source_ids']
            sources_b = cards[b]['source_ids']
            # Different source requirement: no overlap in source_ids
            if sources_a.isdisjoint(sources_b):
                pair_key = (a, b)
                pair_terms[pair_key].append(norm_term)

    # 4. Output
    for (a, b), terms in sorted(pair_terms.items()):
        terms_str = ", ".join(sorted(terms))
        print(f"{a} | {b} | {terms_str}")


if __name__ == '__main__':
    main()
