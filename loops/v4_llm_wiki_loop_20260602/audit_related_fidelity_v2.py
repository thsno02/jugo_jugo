#!/usr/bin/env python3
"""
Audit: Related-Field Derivation Fidelity and Link Symmetry (v2 - regex-based)
Uses regex for related: extraction to avoid YAML parsing edge cases.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

CARDS_DIR = Path("loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/cards")

def parse_card(filepath):
    """Parse a card's frontmatter and body using regex."""
    text = filepath.read_text(encoding="utf-8")
    fm_match = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    if not fm_match:
        return None, text
    return fm_match.group(1), text[fm_match.end():]

def extract_related(fm_raw):
    """Extract related slugs from frontmatter using regex."""
    # Match related: [slug1, slug2, ...]
    rel_match = re.search(r'^related:\s*\[(.*?)\]', fm_raw, re.MULTILINE | re.DOTALL)
    if not rel_match:
        return set()
    items = rel_match.group(1)
    slugs = set(x.strip() for x in items.split(',') if x.strip())
    return slugs

def extract_footnote_slugs(body):
    """Extract slugs from [^card-*] and [^dist-*] footnote definitions."""
    slugs = set()
    pattern = r'\[\^(?:card|dist)-[^\]]+\]:\s*\[.*?\]\(([^)]*\.md)\)'
    for m in re.finditer(pattern, body):
        md_file = m.group(1)
        slug = os.path.basename(md_file).replace(".md", "")
        slugs.add(slug)
    return slugs

def count_footnote_defs(body):
    """Count [^card-*] and [^dist-*] footnote definitions."""
    defs = re.findall(r'\[\^(?:card|dist)-[^\]]+\]:', body)
    return len(defs)

def main():
    card_files = sorted(CARDS_DIR.glob("*.md"))
    print(f"Total card files found: {len(card_files)}")
    print()

    card_related = {}
    card_footnote = {}
    card_fn_count = {}
    all_slugs = set()

    for f in card_files:
        slug = f.stem
        all_slugs.add(slug)
        fm_raw, body = parse_card(f)
        if fm_raw is None:
            card_related[slug] = set()
            card_footnote[slug] = set()
            card_fn_count[slug] = 0
            continue
        card_related[slug] = extract_related(fm_raw)
        card_footnote[slug] = extract_footnote_slugs(body)
        card_fn_count[slug] = count_footnote_defs(body)

    # ===== CHECK 1: related: vs footnote-derived set concordance =====
    print("=" * 80)
    print("CHECK 1: related: field vs footnote-derived set concordance")
    print("=" * 80)

    both_empty = 0
    both_match_nonempty = 0
    has_delta = 0
    extra_in_related = []
    missing_from_related = []

    for slug in sorted(all_slugs):
        rel = card_related[slug]
        fn = card_footnote[slug]
        extra = rel - fn
        missing = fn - rel

        if not rel and not fn:
            both_empty += 1
        elif not extra and not missing:
            both_match_nonempty += 1
        else:
            has_delta += 1
            if extra:
                extra_in_related.append((slug, extra))
            if missing:
                missing_from_related.append((slug, missing))

    total_exact = both_empty + both_match_nonempty
    print(f"  Total exact match: {total_exact}/280")
    print(f"    Both empty (trivial): {both_empty}")
    print(f"    Both non-empty and matching: {both_match_nonempty}")
    print(f"  Cards with deltas: {has_delta}")
    print()

    if extra_in_related:
        print(f"  --- Extra in related: (in related: but NOT in footnotes) [{len(extra_in_related)} cards] ---")
        total_extra = sum(len(e) for _, e in extra_in_related)
        print(f"  Total extra slug instances: {total_extra}")
        for slug, extras in extra_in_related[:10]:
            print(f"    {slug}: extra = {sorted(extras)}")
        if len(extra_in_related) > 10:
            print(f"    ... and {len(extra_in_related) - 10} more cards")
        print()

    if missing_from_related:
        print(f"  --- Missing from related: (in footnotes but NOT in related:) [{len(missing_from_related)} cards] ---")
        total_missing = sum(len(m) for _, m in missing_from_related)
        print(f"  Total missing slug instances: {total_missing}")
        for slug, missings in missing_from_related[:10]:
            print(f"    {slug}: missing = {sorted(missings)}")
        if len(missing_from_related) > 10:
            print(f"    ... and {len(missing_from_related) - 10} more cards")
        print()

    # ===== CHECK 2: Asymmetric links =====
    print("=" * 80)
    print("CHECK 2: Asymmetric links (A->B in related: but B->A not in related:)")
    print("=" * 80)

    asymmetric_pairs = []
    checked_pairs = set()

    for slug in sorted(all_slugs):
        for target in card_related[slug]:
            pair = tuple(sorted([slug, target]))
            if pair in checked_pairs:
                continue
            checked_pairs.add(pair)
            a_has_b = target in card_related[slug]
            b_has_a = slug in card_related.get(target, set())
            if a_has_b and not b_has_a:
                asymmetric_pairs.append((slug, target))
            elif b_has_a and not a_has_b:
                asymmetric_pairs.append((target, slug))

    # Check dangling
    dangling_asym = [(a, b) for a, b in asymmetric_pairs if b not in all_slugs]
    valid_asym = [(a, b) for a, b in asymmetric_pairs if b in all_slugs]

    # Symmetric pair count
    sym_count = 0
    for slug in all_slugs:
        for target in card_related[slug]:
            if slug in card_related.get(target, set()):
                sym_count += 1
    sym_count //= 2

    print(f"  Total unique directed links: {sum(len(card_related[s]) for s in all_slugs)}")
    print(f"  Symmetric pairs (both A->B and B->A): {sym_count}")
    print(f"  Asymmetric pairs: {len(asymmetric_pairs)}")
    print(f"    of which target exists: {len(valid_asym)}")
    print(f"    of which target is dangling: {len(dangling_asym)}")
    if len(asymmetric_pairs) > 0:
        sym_ratio = sym_count / (sym_count + len(asymmetric_pairs)) * 100
        print(f"  Symmetry rate: {sym_ratio:.1f}%")
    print()

    # Sample asymmetric pairs
    print(f"  Sample asymmetric pairs (first 15):")
    for a, b in asymmetric_pairs[:15]:
        exists = b in all_slugs
        print(f"    {a} -> {b} [target exists: {exists}]")
    if len(asymmetric_pairs) > 15:
        print(f"    ... and {len(asymmetric_pairs) - 15} more")
    print()

    # ===== CHECK 3: Non-empty related: but ZERO cross-ref footnotes =====
    print("=" * 80)
    print("CHECK 3: Non-empty related: but ZERO cross-ref footnotes")
    print("         (mechanically populated, not footnote-derived)")
    print("=" * 80)

    mechanical = []
    for slug in sorted(all_slugs):
        if card_related[slug] and card_fn_count[slug] == 0:
            mechanical.append((slug, sorted(card_related[slug])))

    print(f"  Count: {len(mechanical)}")
    total_mech_links = sum(len(r) for _, r in mechanical)
    print(f"  Total links in these cards: {total_mech_links}")
    for slug, rels in mechanical[:10]:
        print(f"    {slug}: related={rels}")
    if len(mechanical) > 10:
        print(f"    ... and {len(mechanical) - 10} more")
    print()

    # ===== CHECK 4: Cross-ref footnotes but empty related: =====
    print("=" * 80)
    print("CHECK 4: [^card-*]/[^dist-*] footnotes present but related: is empty")
    print("         (derive script missed them)")
    print("=" * 80)

    missed = []
    for slug in sorted(all_slugs):
        if card_fn_count[slug] > 0 and not card_related[slug]:
            missed.append((slug, card_fn_count[slug], sorted(card_footnote[slug])))

    print(f"  Count: {len(missed)}")
    total_missed_fn = sum(c for _, c, _ in missed)
    print(f"  Total footnote defs in these cards: {total_missed_fn}")
    for slug, count, fn_slugs in missed[:10]:
        print(f"    {slug}: {count} footnote defs -> {fn_slugs}")
    if len(missed) > 10:
        print(f"    ... and {len(missed) - 10} more")
    print()

    # ===== CHECK 5: Dangling references =====
    print("=" * 80)
    print("CHECK 5: Dangling references in related: (slug not in card set)")
    print("=" * 80)

    dangling = []
    for slug in sorted(all_slugs):
        for target in card_related[slug]:
            if target not in all_slugs:
                dangling.append((slug, target))

    print(f"  Dangling references: {len(dangling)}")
    for slug, target in dangling:
        print(f"    {slug} -> {target} (DOES NOT EXIST)")
    print()

    # ===== CHECK 6: Footnotes pointing to non-existent cards =====
    print("=" * 80)
    print("CHECK 6: Footnote links to non-existent cards")
    print("=" * 80)

    fn_dangling = []
    for slug in sorted(all_slugs):
        for target in card_footnote[slug]:
            if target not in all_slugs:
                fn_dangling.append((slug, target))

    print(f"  Dangling footnote links: {len(fn_dangling)}")
    for slug, target in fn_dangling:
        print(f"    {slug} -> {target} (DOES NOT EXIST)")
    print()

    # ===== SUMMARY =====
    print("=" * 80)
    print("SUMMARY STATISTICS")
    print("=" * 80)

    cards_with_related = sum(1 for s in all_slugs if card_related[s])
    cards_without_related = sum(1 for s in all_slugs if not card_related[s])
    cards_with_footnotes = sum(1 for s in all_slugs if card_fn_count[s] > 0)
    cards_without_footnotes = sum(1 for s in all_slugs if card_fn_count[s] == 0)

    total_related_links = sum(len(card_related[s]) for s in all_slugs)
    total_footnote_slugs = sum(len(card_footnote[s]) for s in all_slugs)

    print(f"  Total cards: {len(all_slugs)}")
    print(f"  Cards with non-empty related: {cards_with_related} ({cards_with_related/len(all_slugs)*100:.1f}%)")
    print(f"  Cards with empty related: {cards_without_related}")
    print(f"  Cards with cross-ref footnotes: {cards_with_footnotes} ({cards_with_footnotes/len(all_slugs)*100:.1f}%)")
    print(f"  Cards without cross-ref footnotes: {cards_without_footnotes}")
    print(f"  Total related: links: {total_related_links}")
    print(f"  Total footnote-derived slugs: {total_footnote_slugs}")
    print(f"  Concordance (both match exactly): {total_exact}/280 ({total_exact/280*100:.1f}%)")
    print(f"    Trivially empty: {both_empty}")
    print(f"    Non-trivially matching: {both_match_nonempty}")
    print(f"  Discordance: {has_delta}/280 ({has_delta/280*100:.1f}%)")

if __name__ == "__main__":
    main()
