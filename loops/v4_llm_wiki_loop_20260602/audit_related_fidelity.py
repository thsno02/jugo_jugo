#!/usr/bin/env python3
"""
Audit: Related-Field Derivation Fidelity and Link Symmetry
Checks all 280 cards for:
1. related: field vs footnote-derived set concordance
2. Asymmetric links
3. Non-empty related: but zero cross-ref footnotes
4. Cross-ref footnotes but empty related:
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict

CARDS_DIR = Path("loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/cards")

def parse_card(filepath):
    """Parse a card's YAML frontmatter and body."""
    text = filepath.read_text(encoding="utf-8")

    # Extract YAML frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    if not fm_match:
        return None, None, text

    fm_raw = fm_match.group(1)
    try:
        fm = yaml.safe_load(fm_raw)
    except yaml.YAMLError:
        fm = {}

    body = text[fm_match.end():]
    return fm, fm_raw, body

def extract_related(fm):
    """Extract related slugs from frontmatter."""
    related = fm.get("related", [])
    if related is None:
        return set()
    if isinstance(related, str):
        # Handle case where related is a string like "[a, b]"
        related = [r.strip() for r in related.strip("[]").split(",") if r.strip()]
    return set(related)

def extract_footnote_slugs(body):
    """Extract slugs from [^card-*] and [^dist-*] footnote definitions."""
    slugs = set()

    # Pattern 1: [^card-N]: [Title](filename.md) or [^dist-N]: [Title](filename.md)
    # Pattern 2: [^card-slug-name]: [Title](filename.md) or [^dist-slug-name]: ...
    # We look for footnote DEFINITIONS (at start of line or after whitespace)
    # The key pattern: [^card-...]: ... (slug.md) ...

    # Match footnote definitions that contain a .md link
    pattern = r'\[\^(?:card|dist)-[^\]]+\]:\s*\[.*?\]\(([^)]*\.md)\)'
    for m in re.finditer(pattern, body):
        md_file = m.group(1)
        # Extract slug from filename (strip .md and any path prefix)
        slug = os.path.basename(md_file).replace(".md", "")
        slugs.add(slug)

    return slugs

def count_footnote_refs(body):
    """Count [^card-*] and [^dist-*] footnote references (both definitions and inline refs)."""
    # Footnote definitions: [^card-...]:
    defs = re.findall(r'\[\^(?:card|dist)-[^\]]+\]:', body)
    return len(defs)

def main():
    card_files = sorted(CARDS_DIR.glob("*.md"))
    print(f"Total card files found: {len(card_files)}")
    print()

    # Data structures
    card_related = {}      # slug -> set of related slugs
    card_footnote = {}     # slug -> set of footnote-derived slugs
    card_fn_count = {}     # slug -> count of card/dist footnote definitions
    all_slugs = set()
    parse_errors = []

    for f in card_files:
        slug = f.stem
        all_slugs.add(slug)

        fm, fm_raw, body = parse_card(f)
        if fm is None:
            parse_errors.append(slug)
            card_related[slug] = set()
            card_footnote[slug] = set()
            card_fn_count[slug] = 0
            continue

        card_related[slug] = extract_related(fm)
        card_footnote[slug] = extract_footnote_slugs(body)
        card_fn_count[slug] = count_footnote_refs(body)

    if parse_errors:
        print(f"PARSE ERRORS ({len(parse_errors)}): {parse_errors}")
        print()

    # ===== CHECK 1: related: vs footnote-derived set concordance =====
    print("=" * 80)
    print("CHECK 1: related: field vs footnote-derived set concordance")
    print("=" * 80)

    exact_match = 0
    has_delta = 0
    extra_in_related = []   # slugs in related: but not in footnotes
    missing_from_related = []  # slugs in footnotes but not in related:

    for slug in sorted(all_slugs):
        rel = card_related[slug]
        fn = card_footnote[slug]

        extra = rel - fn
        missing = fn - rel

        if not extra and not missing:
            exact_match += 1
        else:
            has_delta += 1
            if extra:
                extra_in_related.append((slug, extra))
            if missing:
                missing_from_related.append((slug, missing))

    print(f"  Cards with EXACT match (related == footnotes): {exact_match}")
    print(f"  Cards with deltas: {has_delta}")
    print()

    if extra_in_related:
        print(f"  --- Extra in related: (in related: but NOT in footnotes) [{len(extra_in_related)} cards] ---")
        for slug, extras in extra_in_related:
            print(f"    {slug}: extra = {sorted(extras)}")
        print()

    if missing_from_related:
        print(f"  --- Missing from related: (in footnotes but NOT in related:) [{len(missing_from_related)} cards] ---")
        for slug, missings in missing_from_related:
            print(f"    {slug}: missing = {sorted(missings)}")
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
                asymmetric_pairs.append((slug, target, "A->B exists, B->A missing"))
            elif b_has_a and not a_has_b:
                asymmetric_pairs.append((target, slug, "A->B exists, B->A missing"))

    print(f"  Total asymmetric pairs: {len(asymmetric_pairs)}")
    if asymmetric_pairs:
        # Also check if target exists as a card
        for a, b, direction in asymmetric_pairs:
            exists = b in all_slugs
            print(f"    {a} -> {b}  ({direction}) [target exists: {exists}]")
    print()

    # ===== CHECK 3: Non-empty related: but ZERO cross-ref footnotes =====
    print("=" * 80)
    print("CHECK 3: Non-empty related: but ZERO [^card-*]/[^dist-*] footnote definitions")
    print("         (mechanically populated, not footnote-derived)")
    print("=" * 80)

    mechanical = []
    for slug in sorted(all_slugs):
        if card_related[slug] and card_fn_count[slug] == 0:
            mechanical.append((slug, sorted(card_related[slug])))

    print(f"  Cards with non-empty related: but zero cross-ref footnotes: {len(mechanical)}")
    for slug, rels in mechanical:
        print(f"    {slug}: related={rels}")
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

    print(f"  Cards with footnotes but empty related: {len(missed)}")
    for slug, count, fn_slugs in missed:
        print(f"    {slug}: {count} footnote defs, derived slugs={fn_slugs}")
    print()

    # ===== CHECK 5: Dangling references (related: points to non-existent card) =====
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

    # ===== SUMMARY STATISTICS =====
    print("=" * 80)
    print("SUMMARY STATISTICS")
    print("=" * 80)

    cards_with_related = sum(1 for s in all_slugs if card_related[s])
    cards_without_related = sum(1 for s in all_slugs if not card_related[s])
    cards_with_footnotes = sum(1 for s in all_slugs if card_fn_count[s] > 0)
    cards_without_footnotes = sum(1 for s in all_slugs if card_fn_count[s] == 0)

    total_related_links = sum(len(card_related[s]) for s in all_slugs)
    total_footnote_slugs = sum(len(card_footnote[s]) for s in all_slugs)

    # Symmetric pair count
    sym_count = 0
    for slug in all_slugs:
        for target in card_related[slug]:
            if slug in card_related.get(target, set()):
                sym_count += 1
    sym_count //= 2  # Each pair counted twice

    print(f"  Total cards: {len(all_slugs)}")
    print(f"  Cards with non-empty related: {cards_with_related}")
    print(f"  Cards with empty related: {cards_without_related}")
    print(f"  Cards with cross-ref footnotes: {cards_with_footnotes}")
    print(f"  Cards without cross-ref footnotes: {cards_without_footnotes}")
    print(f"  Total related: links: {total_related_links}")
    print(f"  Total footnote-derived slugs: {total_footnote_slugs}")
    print(f"  Symmetric pairs (both directions present): {sym_count}")
    print(f"  Asymmetric pairs: {len(asymmetric_pairs)}")
    print(f"  Exact concordance (related == footnotes): {exact_match}/{len(all_slugs)}")
    print(f"  Dangling references: {len(dangling)}")
    print(f"  Mechanical populate (related but no footnotes): {len(mechanical)}")
    print(f"  Derive misses (footnotes but no related): {len(missed)}")

if __name__ == "__main__":
    main()
