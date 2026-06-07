#!/usr/bin/env python3
"""Refined check 5: distinguish named-slug mismatches from false positives."""

import os
import re
from pathlib import Path

CARDS_DIR = Path("/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/cards")

MARKER_RE = re.compile(r'\[\^([a-zA-Z0-9_-]+)\](?!:)')
DEF_RE = re.compile(r'^\[\^([a-zA-Z0-9_-]+)\]:\s*(.+)$', re.MULTILINE)
# Markdown link pattern: (xxx.md)
MD_LINK_RE = re.compile(r'\(([a-zA-Z0-9_-]+)\.md\)')

card_files = sorted(CARDS_DIR.glob("*.md"))
all_card_slugs = {f.stem for f in card_files}

print("=== CHECK 5 REFINED: card/dist footnote link integrity ===\n")

broken_named = []
broken_md_links = []

for card_path in card_files:
    card_id = card_path.stem
    content = card_path.read_text(encoding='utf-8')

    footnotes_split = content.split("## Footnotes")
    if len(footnotes_split) < 2:
        continue
    footnotes_section = footnotes_split[1]

    # Get body markers
    fm_match = re.match(r'^---\n.*?\n---\n', footnotes_split[0], re.DOTALL)
    body_text = footnotes_split[0][fm_match.end():] if fm_match else footnotes_split[0]
    body_markers = set(MARKER_RE.findall(body_text))

    for match in DEF_RE.finditer(footnotes_section):
        key = match.group(1)
        def_text = match.group(2)

        if key.startswith("card-") or key.startswith("dist-"):
            prefix = "card-" if key.startswith("card-") else "dist-"
            slug_from_key = key[len(prefix):]

            # Check A: Named slugs (non-numeric) should match a card
            if not slug_from_key.isdigit():
                if slug_from_key not in all_card_slugs:
                    # Check the actual markdown link in definition
                    md_links = MD_LINK_RE.findall(def_text)
                    actual_target = md_links[0] if md_links else "NO_LINK_FOUND"
                    target_exists = actual_target in all_card_slugs
                    broken_named.append({
                        "card": card_id,
                        "footnote": key,
                        "slug_from_key": slug_from_key,
                        "actual_md_link": actual_target,
                        "target_exists": target_exists,
                    })

            # Check B: Markdown links in definition should resolve
            md_links = MD_LINK_RE.findall(def_text)
            for ml in md_links:
                if ml not in all_card_slugs:
                    broken_md_links.append({
                        "card": card_id,
                        "footnote": key,
                        "md_link": ml,
                        "def_text": def_text.strip()[:200]
                    })

print("--- A. Named slug mismatches (footnote key slug != any card) ---")
if broken_named:
    for item in broken_named:
        status = "ACTUAL LINK OK" if item["target_exists"] else "ACTUAL LINK BROKEN"
        print(f"  {item['card']}: [^{item['footnote']}]")
        print(f"    key-slug='{item['slug_from_key']}' not a card, actual link='{item['actual_md_link']}' ({status})")
else:
    print("  PASS: All named card/dist slugs resolve.")

print("\n--- B. Markdown links in card/dist definitions that don't resolve ---")
if broken_md_links:
    for item in broken_md_links:
        print(f"  {item['card']}: [^{item['footnote']}] -> ({item['md_link']}.md) NOT FOUND")
        print(f"    def: {item['def_text']}")
else:
    print("  PASS: All markdown links in card/dist footnote definitions resolve to existing cards.")
