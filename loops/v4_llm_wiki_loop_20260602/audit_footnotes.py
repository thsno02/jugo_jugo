#!/usr/bin/env python3
"""Audit footnote structural integrity across all v4 llm_wiki cards."""

import os
import re
import json
from pathlib import Path

CARDS_DIR = Path("loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/cards")

# Regex patterns
# Marker in body: [^xxx] but NOT [^xxx]: (which is a definition)
MARKER_RE = re.compile(r'\[\^([a-zA-Z0-9_-]+)\](?!:)')
# Definition in footnotes: [^xxx]: ...
DEF_RE = re.compile(r'^\[\^([a-zA-Z0-9_-]+)\]:', re.MULTILINE)
# Valid prefixes
VALID_PREFIXES = {'src', 'card', 'dist', 'url'}
# Absolute path pattern
ABS_PATH_RE = re.compile(r'/Users/[^\s]+')

results = {
    "check1_orphan_markers": [],       # markers with no definition
    "check2_orphan_definitions": [],   # definitions never referenced
    "check3_invalid_prefixes": [],     # invalid footnote prefixes
    "check4_missing_src": [],          # non-comparison cards without [^src-*]
    "check5_broken_card_links": [],    # [^card-*] or [^dist-*] linking to non-existent cards
    "check6_absolute_paths": [],       # absolute paths in footnote definitions
}

card_files = sorted(CARDS_DIR.glob("*.md"))
all_card_slugs = {f.stem for f in card_files}

print(f"Total cards found: {len(card_files)}")

for card_path in card_files:
    card_id = card_path.stem
    content = card_path.read_text(encoding='utf-8')

    # Split into body and footnotes section
    footnotes_split = content.split("## Footnotes")
    if len(footnotes_split) < 2:
        # No footnotes section at all
        body = content
        footnotes_section = ""
    else:
        body = footnotes_split[0]
        footnotes_section = footnotes_split[1]

    # Find all markers in body text (excluding YAML frontmatter)
    # Strip frontmatter
    fm_match = re.match(r'^---\n.*?\n---\n', body, re.DOTALL)
    if fm_match:
        body_text = body[fm_match.end():]
    else:
        body_text = body

    # All [^xxx] markers in body
    body_markers = set(MARKER_RE.findall(body_text))

    # All [^xxx]: definitions in footnotes
    footnote_defs = set(DEF_RE.findall(footnotes_section))

    # Also collect all footnote keys from the full content for prefix check
    all_footnote_keys = body_markers | footnote_defs

    # CHECK 1: Orphan markers (in body but no definition)
    orphan_markers = body_markers - footnote_defs
    if orphan_markers:
        results["check1_orphan_markers"].append({
            "card": card_id,
            "orphans": sorted(orphan_markers)
        })

    # CHECK 2: Orphan definitions (defined but never referenced in body)
    orphan_defs = footnote_defs - body_markers
    if orphan_defs:
        results["check2_orphan_definitions"].append({
            "card": card_id,
            "orphans": sorted(orphan_defs)
        })

    # CHECK 3: Invalid prefixes
    for key in all_footnote_keys:
        prefix = key.split('-')[0] if '-' in key else key
        if prefix not in VALID_PREFIXES:
            results["check3_invalid_prefixes"].append({
                "card": card_id,
                "key": key,
                "prefix": prefix
            })

    # CHECK 4: Non-comparison cards must have at least one [^src-*]
    is_comparison = card_id.startswith("comparison-")
    has_src = any(k.startswith("src-") for k in all_footnote_keys)
    if not is_comparison and not has_src:
        results["check4_missing_src"].append(card_id)

    # CHECK 5: [^card-*] and [^dist-*] footnotes should link to existing cards
    for key in all_footnote_keys:
        if key.startswith("card-") or key.startswith("dist-"):
            # Extract slug: the part after "card-" or "dist-"
            if key.startswith("card-"):
                slug = key[5:]  # remove "card-"
            else:
                slug = key[5:]  # remove "dist-"

            # Skip numeric-only slugs (like card-1, dist-2) — these are just numbered refs
            if slug.isdigit():
                # For numbered card/dist footnotes, check the definition text for a .md file
                # Find the definition line
                def_match = re.search(rf'^\[\^{re.escape(key)}\]:\s*(.+)$', footnotes_section, re.MULTILINE)
                if def_match:
                    def_text = def_match.group(1)
                    # Look for .md file references
                    md_refs = re.findall(r'([a-zA-Z0-9_-]+)\.md', def_text)
                    for md_ref in md_refs:
                        if md_ref not in all_card_slugs:
                            results["check5_broken_card_links"].append({
                                "card": card_id,
                                "footnote": key,
                                "linked_slug": md_ref,
                                "definition_text": def_text.strip()[:200]
                            })
            else:
                # Named slug — check if slug matches a card
                if slug not in all_card_slugs:
                    results["check5_broken_card_links"].append({
                        "card": card_id,
                        "footnote": key,
                        "linked_slug": slug,
                        "definition_text": ""
                    })

    # CHECK 6: Absolute paths in footnote definitions
    if footnotes_section:
        for line_num, line in enumerate(footnotes_section.splitlines(), 1):
            abs_matches = ABS_PATH_RE.findall(line)
            if abs_matches:
                results["check6_absolute_paths"].append({
                    "card": card_id,
                    "line": line.strip()[:200],
                    "paths": abs_matches
                })

# ==================== REPORT ====================
print("\n" + "="*80)
print("FOOTNOTE STRUCTURAL INTEGRITY AUDIT REPORT")
print("="*80)

print(f"\n--- CHECK 1: Orphan markers (body [^xxx] with no [^xxx]: definition) ---")
if results["check1_orphan_markers"]:
    for item in results["check1_orphan_markers"]:
        print(f"  FAIL: {item['card']}: {item['orphans']}")
    print(f"  Total cards with orphan markers: {len(results['check1_orphan_markers'])}")
else:
    print("  PASS: All body markers have matching definitions.")

print(f"\n--- CHECK 2: Orphan definitions (defined [^xxx]: but never referenced in body) ---")
if results["check2_orphan_definitions"]:
    for item in results["check2_orphan_definitions"]:
        print(f"  FAIL: {item['card']}: {item['orphans']}")
    print(f"  Total cards with orphan definitions: {len(results['check2_orphan_definitions'])}")
else:
    print("  PASS: All footnote definitions are referenced in body.")

print(f"\n--- CHECK 3: Invalid footnote prefixes (must be src/card/dist/url) ---")
if results["check3_invalid_prefixes"]:
    for item in results["check3_invalid_prefixes"]:
        print(f"  FAIL: {item['card']}: [^{item['key']}] has prefix '{item['prefix']}'")
    print(f"  Total invalid prefixes: {len(results['check3_invalid_prefixes'])}")
else:
    print("  PASS: All footnote prefixes are valid (src/card/dist/url).")

print(f"\n--- CHECK 4: Non-comparison cards missing [^src-*] footnote ---")
if results["check4_missing_src"]:
    for card_id in results["check4_missing_src"]:
        print(f"  FAIL: {card_id}")
    print(f"  Total cards missing src footnote: {len(results['check4_missing_src'])}")
else:
    print("  PASS: All non-comparison cards have at least one [^src-*] footnote.")

print(f"\n--- CHECK 5: Broken card/dist links (linked slug not found as card) ---")
if results["check5_broken_card_links"]:
    for item in results["check5_broken_card_links"]:
        print(f"  FAIL: {item['card']}: [^{item['footnote']}] -> slug '{item['linked_slug']}' not found")
        if item['definition_text']:
            print(f"         def: {item['definition_text']}")
    print(f"  Total broken links: {len(results['check5_broken_card_links'])}")
else:
    print("  PASS: All card/dist footnote links resolve to existing cards.")

print(f"\n--- CHECK 6: Absolute paths in footnote definitions ---")
if results["check6_absolute_paths"]:
    for item in results["check6_absolute_paths"]:
        print(f"  FAIL: {item['card']}: {item['paths']}")
        print(f"         line: {item['line']}")
    print(f"  Total cards with absolute paths: {len(results['check6_absolute_paths'])}")
else:
    print("  PASS: No absolute paths found in footnote definitions.")

# Summary
print("\n" + "="*80)
print("SUMMARY")
print("="*80)
total_issues = sum([
    len(results["check1_orphan_markers"]),
    len(results["check2_orphan_definitions"]),
    len(results["check3_invalid_prefixes"]),
    len(results["check4_missing_src"]),
    len(results["check5_broken_card_links"]),
    len(results["check6_absolute_paths"]),
])
for check_name, items in results.items():
    status = "PASS" if len(items) == 0 else f"FAIL ({len(items)} issues)"
    print(f"  {check_name}: {status}")
print(f"\nTotal issues found: {total_issues}")

# Dump raw results as JSON for further analysis
print("\n\n--- RAW JSON ---")
print(json.dumps(results, indent=2, ensure_ascii=False))
