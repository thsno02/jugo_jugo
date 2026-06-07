#!/usr/bin/env python3
"""Mechanical audit of all knowledge cards in the v4 loop KB."""

import os, re, json, glob, yaml
from collections import defaultdict, Counter
from pathlib import Path

BASE = Path("/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/loops/v4_llm_wiki_loop_20260602")
CARDS_DIR = BASE / "outputs/llm_wiki/kb/cards"
JUST_DIR = BASE / "outputs/llm_wiki/kb/justification"
AUDIT_DIR = BASE / "outputs/llm_wiki/kb/audits"
AUDIT_DIR.mkdir(parents=True, exist_ok=True)

MANDATORY_FIELDS = [
    "id", "title", "status", "card_type", "tags",
    "created_time", "edited_time", "edited_entity",
    "source_ids", "justification", "canonical_concept",
    "aliases", "summary", "related"
]

VALID_FOOTNOTE_PREFIXES = {"src", "card", "dist", "url"}

# ─── Helpers ───────────────────────────────────────────────────────────────

def parse_card(filepath):
    """Parse a card file into frontmatter dict and body string."""
    text = filepath.read_text(encoding="utf-8")
    # Match YAML front matter
    m = re.match(r'^---\n(.*?)\n---\n?(.*)', text, re.DOTALL)
    if not m:
        return None, text, "no_frontmatter"
    raw_yaml = m.group(1)
    body = m.group(2)
    try:
        fm = yaml.safe_load(raw_yaml)
    except yaml.YAMLError as e:
        return None, body, f"yaml_parse_error: {e}"
    return fm, body, None


def extract_footnote_markers(body):
    """Return set of footnote keys used in body text (e.g. 'src-1')."""
    # Match [^xxx] but NOT at start of line followed by ]: (which is a def)
    markers = set()
    for line in body.split('\n'):
        # Skip definition lines
        if re.match(r'^\[[\^]', line):
            continue
        markers.update(re.findall(r'\[\^([^\]]+)\]', line))
    # Remove any that are actually definitions (found in footnote section)
    return markers


def extract_footnote_defs(body):
    """Return dict of footnote key -> definition text."""
    defs = {}
    for m in re.finditer(r'^\[\^([^\]]+)\]:\s*(.*)', body, re.MULTILINE):
        defs[m.group(1)] = m.group(2)
    return defs


def extract_footnote_markers_only(body):
    """Return set of footnote keys referenced in body (excluding def lines)."""
    markers = set()
    defs_keys = set()
    for line in body.split('\n'):
        # If line starts with [^...]: it's a definition
        def_match = re.match(r'^\[\^([^\]]+)\]:', line)
        if def_match:
            defs_keys.add(def_match.group(1))
            continue
        # Find all [^xxx] references in non-def lines
        for m in re.finditer(r'\[\^([^\]]+)\]', line):
            markers.add(m.group(1))
    return markers


def get_footnote_prefix(key):
    """Extract prefix from footnote key like 'src-1' -> 'src'."""
    parts = key.split('-', 1)
    return parts[0] if len(parts) > 0 else key


def extract_card_targets_from_defs(defs):
    """From footnote defs with [^card-*] or [^dist-*], extract target card slugs."""
    targets = {}
    for key, deftext in defs.items():
        prefix = get_footnote_prefix(key)
        if prefix in ("card", "dist"):
            # Try to find (slug.md) pattern
            m = re.search(r'\(([^)]+)\.md\)', deftext)
            if m:
                targets[key] = m.group(1)
            else:
                # Try bare slug reference
                m2 = re.search(r'^\[.*?\]\(([^)]+)\)', deftext)
                if m2:
                    slug = m2.group(1).replace('.md', '')
                    targets[key] = slug
    return targets


def detect_dual_format_related(raw_yaml_text):
    """Detect if related field has both inline [] and indented - items."""
    # Find the related: line
    lines = raw_yaml_text.split('\n')
    related_idx = None
    for i, line in enumerate(lines):
        if re.match(r'^related:', line):
            related_idx = i
            break
    if related_idx is None:
        return False
    related_line = lines[related_idx]
    has_inline = bool(re.search(r'\[.*\]', related_line))
    # Check if next lines have indented - items
    has_indented = False
    for j in range(related_idx + 1, len(lines)):
        if re.match(r'^  - ', lines[j]) or re.match(r'^  -', lines[j]):
            has_indented = True
        elif re.match(r'^\S', lines[j]):
            break
    return has_inline and has_indented


def extract_related_slugs_from_yaml(fm):
    """Extract related slugs from the parsed YAML (which merges both formats)."""
    related = fm.get("related", [])
    if related is None:
        return []
    if isinstance(related, list):
        return [str(r) for r in related]
    if isinstance(related, str):
        return [related]
    return []


# ─── Main audit ────────────────────────────────────────────────────────────

card_files = sorted(CARDS_DIR.glob("*.md"))
all_card_slugs = {f.stem for f in card_files}

findings = {
    "yaml_schema": [],
    "footnotes": [],
    "related_fidelity": [],
    "loop_independence": [],
}

suspects = {
    "atomicity": [],
    "alias": [],
    "drift": [],
    "dual_related_format": [],
}

counters = Counter()

# Per-card data for cross-card checks
card_related_map = {}  # slug -> set of related slugs
card_footnote_link_map = {}  # slug -> set of linked slugs (from card/dist footnotes)
created_times = {}  # slug -> created_time

for cf in card_files:
    slug = cf.stem
    raw_text = cf.read_text(encoding="utf-8")

    # Parse frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---\n?(.*)', raw_text, re.DOTALL)
    if not fm_match:
        findings["yaml_schema"].append({
            "card": slug,
            "check": "frontmatter_parse",
            "severity": "critical",
            "detail": "No valid YAML frontmatter found"
        })
        counters["yaml_schema"] += 1
        continue

    raw_yaml_text = fm_match.group(1)
    body = fm_match.group(2)

    try:
        fm = yaml.safe_load(raw_yaml_text)
    except yaml.YAMLError as e:
        findings["yaml_schema"].append({
            "card": slug,
            "check": "yaml_parse",
            "severity": "critical",
            "detail": f"YAML parse error: {e}"
        })
        counters["yaml_schema"] += 1
        continue

    if not isinstance(fm, dict):
        findings["yaml_schema"].append({
            "card": slug,
            "check": "yaml_type",
            "severity": "critical",
            "detail": f"Frontmatter is not a dict, got {type(fm).__name__}"
        })
        counters["yaml_schema"] += 1
        continue

    # ── 1. YAML SCHEMA checks ──────────────────────────────────────────

    # 1a. Missing mandatory fields
    for field in MANDATORY_FIELDS:
        if field not in fm:
            findings["yaml_schema"].append({
                "card": slug,
                "check": "missing_field",
                "severity": "critical",
                "detail": f"Missing mandatory field: {field}"
            })
            counters["yaml_schema"] += 1

    # 1b. id == filename
    if fm.get("id") != slug:
        findings["yaml_schema"].append({
            "card": slug,
            "check": "id_filename_mismatch",
            "severity": "critical",
            "detail": f"id='{fm.get('id')}' != filename='{slug}'"
        })
        counters["yaml_schema"] += 1

    # 1c. status == accepted
    if fm.get("status") != "accepted":
        findings["yaml_schema"].append({
            "card": slug,
            "check": "status_not_accepted",
            "severity": "major",
            "detail": f"status='{fm.get('status')}', expected 'accepted'"
        })
        counters["yaml_schema"] += 1

    # 1d. justification file exists
    just_ref = fm.get("justification", "")
    if just_ref:
        # Resolve relative path from card dir
        just_path = JUST_DIR / (slug + ".md")
        if not just_path.exists():
            findings["yaml_schema"].append({
                "card": slug,
                "check": "justification_missing",
                "severity": "major",
                "detail": f"Justification file not found: {just_path.name}"
            })
            counters["yaml_schema"] += 1

    # 1e. Detect dual-format related
    if detect_dual_format_related(raw_yaml_text):
        findings["yaml_schema"].append({
            "card": slug,
            "check": "dual_format_related",
            "severity": "major",
            "detail": "related: has both inline [] and indented - items (YAML merge may produce unexpected results)"
        })
        counters["yaml_schema"] += 1
        suspects["dual_related_format"].append(slug)

    # Store created_time
    created_times[slug] = str(fm.get("created_time", ""))

    # Store related slugs
    related_slugs = extract_related_slugs_from_yaml(fm)
    card_related_map[slug] = set(related_slugs)

    # ── 2. FOOTNOTES checks ────────────────────────────────────────────

    markers = extract_footnote_markers_only(body)
    defs = extract_footnote_defs(body)
    defs_keys = set(defs.keys())

    # 2a. Orphan markers (no def)
    orphan_markers = markers - defs_keys
    for om in sorted(orphan_markers):
        findings["footnotes"].append({
            "card": slug,
            "check": "orphan_marker",
            "severity": "major",
            "detail": f"Footnote marker [^{om}] has no definition"
        })
        counters["footnotes"] += 1

    # 2b. Orphan defs (no marker)
    orphan_defs = defs_keys - markers
    for od in sorted(orphan_defs):
        findings["footnotes"].append({
            "card": slug,
            "check": "orphan_def",
            "severity": "minor",
            "detail": f"Footnote definition [^{od}] has no marker in body"
        })
        counters["footnotes"] += 1

    # 2c. Check prefixes
    all_fn_keys = markers | defs_keys
    for key in sorted(all_fn_keys):
        prefix = get_footnote_prefix(key)
        if prefix not in VALID_FOOTNOTE_PREFIXES:
            findings["footnotes"].append({
                "card": slug,
                "check": "invalid_prefix",
                "severity": "major",
                "detail": f"Footnote [^{key}] has invalid prefix '{prefix}', expected one of {VALID_FOOTNOTE_PREFIXES}"
            })
            counters["footnotes"] += 1

    # 2d. Non-comparison cards must have >=1 [^src-*]
    is_comparison = slug.startswith("comparison-") or fm.get("card_type") in ("distinction", "comparison")
    src_keys = [k for k in defs_keys if get_footnote_prefix(k) == "src"]
    if not is_comparison and len(src_keys) == 0:
        findings["footnotes"].append({
            "card": slug,
            "check": "no_source_footnote",
            "severity": "major",
            "detail": "Non-comparison card has no [^src-*] footnotes"
        })
        counters["footnotes"] += 1

    # 2e. Check [^card-*]/[^dist-*] link targets exist
    link_targets = extract_card_targets_from_defs(defs)
    linked_slugs = set()
    for fn_key, target_slug in link_targets.items():
        linked_slugs.add(target_slug)
        if target_slug not in all_card_slugs:
            findings["footnotes"].append({
                "card": slug,
                "check": "broken_card_link",
                "severity": "major",
                "detail": f"[^{fn_key}] links to '{target_slug}' which does not exist as a card"
            })
            counters["footnotes"] += 1

    card_footnote_link_map[slug] = linked_slugs

    # ── 3. RELATED FIDELITY (per-card part) ────────────────────────────

    # Compare footnote link targets with related field
    footnote_linked = linked_slugs
    related_set = card_related_map.get(slug, set())

    # Slugs in footnotes but not in related
    fn_not_in_related = footnote_linked - related_set
    for s in sorted(fn_not_in_related):
        findings["related_fidelity"].append({
            "card": slug,
            "check": "footnote_not_in_related",
            "severity": "minor",
            "detail": f"Card/dist footnote links to '{s}' but not listed in related field"
        })
        counters["related_fidelity"] += 1

    # Slugs in related but not in footnotes (info only)
    related_not_in_fn = related_set - footnote_linked
    # This is normal - related can include conceptual links without footnotes

    # ── 4. LOOP INDEPENDENCE ───────────────────────────────────────────

    for pattern in ["v3_llm_wiki_loop", "v2_llm_wiki_loop", "v1_topic_hub"]:
        if pattern in raw_text:
            findings["loop_independence"].append({
                "card": slug,
                "check": "cross_loop_reference",
                "severity": "critical",
                "detail": f"Card text contains reference to '{pattern}'"
            })
            counters["loop_independence"] += 1

    # ── 5. SUSPECT SIGNALS ─────────────────────────────────────────────

    title = fm.get("title", "")
    source_ids = fm.get("source_ids", []) or []
    aliases = fm.get("aliases", []) or []
    summary_text = fm.get("summary", "") or ""

    # 5a. ATOMICITY suspects
    body_lines = [l for l in body.strip().split('\n') if l.strip()]
    atomicity_reasons = []
    # Title contains conjunction (but not vs)
    for conj in ["与", "和", " and ", " with "]:
        if conj.lower() in title.lower() and " vs " not in title.lower() and " vs." not in title.lower():
            atomicity_reasons.append(f"title contains '{conj.strip()}'")
    # Body > 45 lines
    if len(body_lines) > 45:
        atomicity_reasons.append(f"body has {len(body_lines)} lines (>45)")
    # 2+ source_ids
    if isinstance(source_ids, list) and len(source_ids) >= 2:
        atomicity_reasons.append(f"{len(source_ids)} source_ids")

    if atomicity_reasons:
        suspects["atomicity"].append({
            "card": slug,
            "reasons": atomicity_reasons
        })

    # 5b. ALIAS suspects
    summary_lower = summary_text.lower()
    missing_aliases = []
    for alias in aliases:
        if str(alias).lower() not in summary_lower:
            missing_aliases.append(str(alias))
    if missing_aliases:
        suspects["alias"].append({
            "card": slug,
            "missing_in_summary": missing_aliases
        })

    # 5c. DRIFT - collect created_time for clustering
    # (done after loop)


# ── Cross-card checks ──────────────────────────────────────────────────

# 3. Asymmetric related links
asymmetric_count = 0
asymmetric_details = []
for slug_a, related_a in card_related_map.items():
    for slug_b in related_a:
        if slug_b in card_related_map:
            if slug_a not in card_related_map[slug_b]:
                asymmetric_details.append({
                    "card": slug_a,
                    "check": "asymmetric_link",
                    "severity": "minor",
                    "detail": f"'{slug_a}' lists '{slug_b}' in related, but '{slug_b}' does not list '{slug_a}'"
                })
                asymmetric_count += 1
        else:
            # related points to non-existent card
            findings["related_fidelity"].append({
                "card": slug_a,
                "check": "related_target_missing",
                "severity": "major",
                "detail": f"related lists '{slug_b}' which does not exist as a card"
            })
            counters["related_fidelity"] += 1

findings["related_fidelity"].extend(asymmetric_details)
counters["related_fidelity"] += asymmetric_count

# 4. Loop independence - check loop_state.json and status.json
loop_state_path = BASE / "loop_state.json"
status_path = BASE / "status.json"
for fpath, label in [(loop_state_path, "loop_state.json"), (status_path, "status.json")]:
    if fpath.exists():
        content = fpath.read_text()
        for pattern in ["v3_llm_wiki_loop", "v2_llm_wiki_loop", "v1_topic_hub"]:
            if pattern in content:
                findings["loop_independence"].append({
                    "card": label,
                    "check": "cross_loop_reference_in_state",
                    "severity": "critical",
                    "detail": f"{label} contains reference to '{pattern}'"
                })
                counters["loop_independence"] += 1

# 5c. DRIFT suspects - cluster by created_time
time_clusters = defaultdict(list)
for slug, ct in created_times.items():
    time_clusters[ct].append(slug)

suspects["drift"] = [
    {"created_time": ct, "count": len(slugs), "cards": slugs[:10], "total_in_cluster": len(slugs)}
    for ct, slugs in sorted(time_clusters.items())
]

# ── Summary stats ──────────────────────────────────────────────────────

total_defects = sum(counters.values())

summary = {
    "total_cards": len(card_files),
    "total_defects": total_defects,
    "defects_by_category": dict(counters),
    "comparison_cards": sum(1 for s in all_card_slugs if s.startswith("comparison-")),
    "suspect_counts": {
        "atomicity": len(suspects["atomicity"]),
        "alias": len(suspects["alias"]),
        "drift_clusters": len(suspects["drift"]),
        "dual_related_format": len(suspects["dual_related_format"]),
    },
    "cross_card_stats": {
        "total_related_links": sum(len(v) for v in card_related_map.values()),
        "asymmetric_links": asymmetric_count,
        "cards_with_no_related": sum(1 for v in card_related_map.values() if len(v) == 0),
    }
}

report = {
    "summary": summary,
    "findings": findings,
}

suspect_report = {
    "suspect_counts": summary["suspect_counts"],
    "suspects": suspects,
}

# Write outputs
with open(AUDIT_DIR / "mechanical_report.json", "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)

with open(AUDIT_DIR / "suspect_lists.json", "w", encoding="utf-8") as f:
    json.dump(suspect_report, f, ensure_ascii=False, indent=2)

# Print summary
print("=" * 60)
print("MECHANICAL AUDIT SUMMARY")
print("=" * 60)
print(f"Total cards scanned: {len(card_files)}")
print(f"Total defects found: {total_defects}")
print()
print("Defects by category:")
for cat, count in sorted(counters.items()):
    print(f"  {cat}: {count}")
print()
print("Suspect counts:")
for cat, count in sorted(summary["suspect_counts"].items()):
    print(f"  {cat}: {count}")
print()
print(f"Cross-card stats:")
print(f"  Total related links: {summary['cross_card_stats']['total_related_links']}")
print(f"  Asymmetric links: {summary['cross_card_stats']['asymmetric_links']}")
print(f"  Cards with no related: {summary['cross_card_stats']['cards_with_no_related']}")
print()
print(f"Reports written to:")
print(f"  {AUDIT_DIR / 'mechanical_report.json'}")
print(f"  {AUDIT_DIR / 'suspect_lists.json'}")

# Print top findings
print()
print("=" * 60)
print("TOP FINDINGS (first 5 per category)")
print("=" * 60)
for cat, items in findings.items():
    if items:
        print(f"\n--- {cat} ({len(items)} findings) ---")
        for item in items[:5]:
            print(f"  [{item['severity']}] {item['card']}: {item['detail']}")
        if len(items) > 5:
            print(f"  ... and {len(items) - 5} more")

print()
print("=" * 60)
print("SUSPECT HIGHLIGHTS")
print("=" * 60)
print(f"\nAtomicity suspects ({len(suspects['atomicity'])}):")
for s in suspects["atomicity"][:5]:
    print(f"  {s['card']}: {', '.join(s['reasons'])}")
if len(suspects["atomicity"]) > 5:
    print(f"  ... and {len(suspects['atomicity']) - 5} more")

print(f"\nAlias suspects ({len(suspects['alias'])}):")
for s in suspects["alias"][:5]:
    print(f"  {s['card']}: missing [{', '.join(s['missing_in_summary'][:3])}]")
if len(suspects["alias"]) > 5:
    print(f"  ... and {len(suspects['alias']) - 5} more")

print(f"\nDrift clusters ({len(suspects['drift'])}):")
for s in suspects["drift"]:
    print(f"  {s['created_time']}: {s['total_in_cluster']} cards")

print(f"\nDual-format related ({len(suspects['dual_related_format'])}):")
for s in suspects["dual_related_format"][:10]:
    print(f"  {s}")
