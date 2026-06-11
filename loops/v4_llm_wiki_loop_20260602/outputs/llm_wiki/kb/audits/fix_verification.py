#!/usr/bin/env python3
"""Comprehensive validation of all KB cards."""

import json
import os
import re
import sys
from pathlib import Path

import yaml

CARDS_DIR = Path("loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/cards")
JJ_DIR = Path("loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/justification")
AUDITS_DIR = Path("loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits")

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)", re.DOTALL)
FOOTNOTE_MARKER_RE = re.compile(r"\[\^([^\]]+)\](?!:)")   # [^xxx] not followed by :
FOOTNOTE_DEF_RE = re.compile(r"^\[\^([^\]]+)\]:", re.MULTILINE)
SRC_FOOTNOTE_RE = re.compile(r"\[\^src-[^\]]*\]")


def parse_card(filepath: Path):
    """Return (frontmatter_dict, body_str) or raise on failure."""
    text = filepath.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError("no YAML frontmatter delimiters found")
    fm = yaml.safe_load(m.group(1))
    body = m.group(2)
    return fm, body


def main():
    card_files = sorted(CARDS_DIR.glob("*.md"))
    all_slugs = {f.stem for f in card_files}

    # Accumulators
    yaml_errors = []
    broken_refs = {}          # card -> [missing slugs]
    orphan_cards = []
    footnote_errors = {}      # card -> [missing defs]
    comparison_missing_src = []
    jj_missing_creation = []

    # For related link analysis
    outgoing = {}   # slug -> set of related slugs
    incoming = {s: set() for s in all_slugs}

    # --- Check 1-4: iterate over cards ---
    parsed_cards = {}
    for cf in card_files:
        slug = cf.stem

        # Check 1: YAML parse
        try:
            fm, body = parse_card(cf)
        except Exception as e:
            yaml_errors.append({"file": slug, "error": str(e)})
            outgoing[slug] = set()
            continue

        parsed_cards[slug] = (fm, body)

        # Check 2: broken related refs
        related = fm.get("related", []) or []
        if isinstance(related, str):
            related = [related]
        out_set = set()
        broken = []
        for r in related:
            r_slug = r.strip()
            if not r_slug:
                continue
            out_set.add(r_slug)
            if r_slug not in all_slugs:
                broken.append(r_slug)
        outgoing[slug] = out_set
        for r_slug in out_set:
            if r_slug in incoming:
                incoming[r_slug].add(slug)
        if broken:
            broken_refs[slug] = broken

        # Check 4: footnote integrity
        markers = set(FOOTNOTE_MARKER_RE.findall(body))
        defs = set(FOOTNOTE_DEF_RE.findall(body))
        missing_defs = markers - defs
        if missing_defs:
            footnote_errors[slug] = sorted(missing_defs)

        # Check 5: comparison cards src footnotes
        if slug.startswith("comparison-"):
            if not SRC_FOOTNOTE_RE.search(body):
                comparison_missing_src.append(slug)

    # Check 3: orphan cards (0 outgoing + 0 incoming)
    for slug in all_slugs:
        out_count = len(outgoing.get(slug, set()))
        in_count = len(incoming.get(slug, set()))
        if out_count == 0 and in_count == 0:
            orphan_cards.append(slug)

    # Check 6: JJ completeness
    jj_files = sorted(JJ_DIR.glob("*.md"))
    for jf in jj_files:
        text = jf.read_text(encoding="utf-8")
        if "## creation" not in text.lower():
            jj_missing_creation.append(jf.stem)

    # --- Compute stats ---
    total_cards = len(card_files)
    cards_with_related = sum(1 for s, rels in outgoing.items() if len(rels) > 0)
    total_related_links = sum(len(rels) for rels in outgoing.values())
    avg_links = round(total_related_links / total_cards, 2) if total_cards else 0
    comparison_cards_total = sum(1 for s in all_slugs if s.startswith("comparison-"))
    comparison_with_src = comparison_cards_total - len(comparison_missing_src)

    # --- Build results ---
    checks = {
        "1_yaml_parse": {
            "pass": len(yaml_errors) == 0,
            "total": total_cards,
            "failures": len(yaml_errors),
            "details": yaml_errors
        },
        "2_no_broken_related_refs": {
            "pass": len(broken_refs) == 0,
            "total_links_checked": total_related_links,
            "failures": sum(len(v) for v in broken_refs.values()),
            "details": broken_refs
        },
        "3_no_orphan_cards": {
            "pass": len(orphan_cards) == 0,
            "total": total_cards,
            "orphans": len(orphan_cards),
            "details": sorted(orphan_cards)
        },
        "4_footnote_integrity": {
            "pass": len(footnote_errors) == 0,
            "cards_checked": total_cards - len(yaml_errors),
            "failures": len(footnote_errors),
            "details": footnote_errors
        },
        "5_comparison_src_footnotes": {
            "pass": len(comparison_missing_src) == 0,
            "comparison_cards_total": comparison_cards_total,
            "with_src_footnote": comparison_with_src,
            "failures": len(comparison_missing_src),
            "details": sorted(comparison_missing_src)
        },
        "6_jj_creation_header": {
            "pass": len(jj_missing_creation) == 0,
            "jj_files_total": len(jj_files),
            "failures": len(jj_missing_creation),
            "details": sorted(jj_missing_creation)
        }
    }

    stats = {
        "total_cards": total_cards,
        "cards_with_nonempty_related": cards_with_related,
        "total_related_links": total_related_links,
        "avg_links_per_card": avg_links,
        "comparison_cards_with_src": f"{comparison_with_src}/{comparison_cards_total}"
    }

    result = {"checks": checks, "stats": stats}

    # Write JSON
    AUDITS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = AUDITS_DIR / "fix_verification.json"
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    # Print summary
    print("=" * 60)
    print("FIX VERIFICATION REPORT")
    print("=" * 60)
    for name, check in checks.items():
        status = "PASS" if check["pass"] else "FAIL"
        fail_count = check.get("failures", check.get("orphans", 0))
        print(f"  [{status}] {name}: {fail_count} issue(s)")
        if not check["pass"] and check.get("details"):
            details = check["details"]
            if isinstance(details, list):
                for d in details[:10]:
                    print(f"         - {d}")
                if len(details) > 10:
                    print(f"         ... and {len(details)-10} more")
            elif isinstance(details, dict):
                for k, v in list(details.items())[:10]:
                    print(f"         - {k}: {v}")
                if len(details) > 10:
                    print(f"         ... and {len(details)-10} more")
    print()
    print("STATS:")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    print()
    print(f"Results written to: {out_path}")

    # Exit code: 0 if all pass, 1 otherwise
    all_pass = all(c["pass"] for c in checks.values())
    sys.exit(0 if all_pass else 1)


if __name__ == "__main__":
    main()
