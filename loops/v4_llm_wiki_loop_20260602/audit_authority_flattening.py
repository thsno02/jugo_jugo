#!/usr/bin/env python3
"""
Source Authority Flattening Audit
=================================
For each KB card:
1. Extract source_ids → classify each source by type (arxiv, webpage-blog,
   webpage-docs, hacker-news, pypi, gist, github-repo, reddit).
2. Grep card body for qualifier/hedge words.
3. Compute per-source-type stats: avg qualifier count.
4. Flag authority flattening: if non-academic sources have FEWER qualifiers
   than academic sources, anecdotes are presented with more confidence.
5. Report distribution table + top 10 authority-gap cards.
"""

import os, re, sys, yaml, json
from pathlib import Path
from collections import defaultdict

CARDS_DIR = Path("loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/cards")
RAW_DIR = Path("data/raw")

# ── 1. Build source_id → type mapping from filesystem ──────────────────────
SOURCE_TYPE_MAP = {}  # source_id → type label

type_dirs = {
    "arxiv": "arxiv",
    "webpage": "webpage",
    "hacker-news": "hacker_news",
    "pypi": "pypi",
    "gist": "gist_raw",
    "github-repo": "github_repo",
    "reddit": "reddit",
}

for type_label, dirname in type_dirs.items():
    dirpath = RAW_DIR / dirname
    if dirpath.exists():
        for entry in dirpath.iterdir():
            if entry.is_dir():
                SOURCE_TYPE_MAP[entry.name] = type_label

# Sub-classify arxiv into experimental vs theoretical based on content hints
# (heuristic: papers with "experiment" / "evaluation" / "benchmark" sections
#  are experimental; others theoretical)
ARXIV_SUBTYPE = {}
for sid, stype in list(SOURCE_TYPE_MAP.items()):
    if stype == "arxiv":
        bundle = RAW_DIR / "arxiv" / sid / "agent_source_bundle.txt"
        if bundle.exists():
            text = bundle.read_text(errors="ignore").lower()
            exp_keywords = ["experiment", "evaluation", "benchmark", "empirical",
                            "ablation", "baseline", "dataset", "f1", "accuracy",
                            "precision", "recall", "bleu", "rouge"]
            exp_hits = sum(1 for kw in exp_keywords if kw in text)
            ARXIV_SUBTYPE[sid] = "arxiv-experimental" if exp_hits >= 3 else "arxiv-theoretical"
        else:
            ARXIV_SUBTYPE[sid] = "arxiv-theoretical"

# Sub-classify webpage into blog vs docs
WEBPAGE_SUBTYPE = {}
doc_keywords = ["docs", "documentation", "reference", "api", "guide", "toolkit",
                "nist", "owasp", "wikibase", "obsidian-help", "langchain",
                "microsoft-agent-governance"]
for sid, stype in list(SOURCE_TYPE_MAP.items()):
    if stype == "webpage":
        is_docs = any(kw in sid.lower() for kw in doc_keywords)
        WEBPAGE_SUBTYPE[sid] = "webpage-docs" if is_docs else "webpage-blog"

def classify_source(sid):
    """Return fine-grained type for a source_id."""
    base = SOURCE_TYPE_MAP.get(sid)
    if base == "arxiv":
        return ARXIV_SUBTYPE.get(sid, "arxiv-experimental")
    if base == "webpage":
        return WEBPAGE_SUBTYPE.get(sid, "webpage-blog")
    if base:
        return base
    # Fallback heuristics from name
    if sid.startswith("arxiv-"):
        return "arxiv-experimental"
    if sid.startswith("pypi-"):
        return "pypi"
    if "hacker-news" in sid or sid.startswith("hn-"):
        return "hacker-news"
    if sid.startswith("repo-"):
        return "github-repo"
    if sid.startswith("reddit-"):
        return "reddit"
    if "gist" in sid:
        return "gist"
    return "webpage-blog"  # default

# ── 2. Qualifier / hedge words ─────────────────────────────────────────────
QUALIFIERS_ZH = ["可能", "或许", "暗示", "实证", "控制实验", "经验性",
                  "据报道", "有待验证", "尚未", "初步", "假设", "推测",
                  "不确定", "一定程度"]
QUALIFIERS_EN = ["suggests", "may", "might", "anecdotal", "could",
                 "potentially", "arguably", "preliminary", "hypothesi",
                 "speculative", "uncertain", "reportedly", "appears to",
                 "seems to", "likely", "possibly", "tentative"]

def count_qualifiers(text):
    """Count qualifier/hedge words in text (case-insensitive for EN)."""
    lower = text.lower()
    count = 0
    details = {}
    for q in QUALIFIERS_ZH:
        n = text.count(q)
        if n:
            details[q] = n
            count += n
    for q in QUALIFIERS_EN:
        n = lower.count(q)
        if n:
            details[q] = n
            count += n
    return count, details

# ── 3. Parse all cards ─────────────────────────────────────────────────────
def parse_card(filepath):
    """Return (frontmatter_dict, body_text) from a card markdown file."""
    raw = filepath.read_text(errors="ignore")
    # Split YAML front matter
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", raw, re.DOTALL)
    if not m:
        return None, raw
    try:
        fm = yaml.safe_load(m.group(1))
    except Exception:
        fm = {}
    body = m.group(2)
    return fm, body

cards_data = []
for f in sorted(CARDS_DIR.glob("*.md")):
    fm, body = parse_card(f)
    if fm is None:
        continue
    card_id = fm.get("id", f.stem)
    source_ids = fm.get("source_ids", [])
    if not isinstance(source_ids, list):
        source_ids = [source_ids] if source_ids else []

    # Classify sources
    source_types = [classify_source(sid) for sid in source_ids]
    source_type_set = set(source_types)

    # Count qualifiers in body (exclude footnotes section for cleaner signal)
    body_main = body.split("## Footnotes")[0] if "## Footnotes" in body else body
    qual_count, qual_details = count_qualifiers(body_main)

    # Word count for normalization
    word_count = len(body_main.split())

    cards_data.append({
        "id": card_id,
        "file": f.name,
        "source_ids": source_ids,
        "source_types": source_types,
        "source_type_set": source_type_set,
        "qual_count": qual_count,
        "qual_details": qual_details,
        "word_count": word_count,
        "qual_density": qual_count / max(word_count, 1) * 100,  # per 100 words
    })

# ── 4. Per-source-type aggregation ─────────────────────────────────────────
# A card may have multiple source types; assign it to each type it references.
type_stats = defaultdict(lambda: {"cards": [], "total_qual": 0, "total_words": 0, "count": 0})

# Also track "primary type" = the dominant source type for each card
# For simplicity, assign card to ALL its source types
for c in cards_data:
    for st in c["source_type_set"]:
        bucket = type_stats[st]
        bucket["cards"].append(c)
        bucket["total_qual"] += c["qual_count"]
        bucket["total_words"] += c["word_count"]
        bucket["count"] += 1

# Academic vs non-academic grouping
ACADEMIC_TYPES = {"arxiv-experimental", "arxiv-theoretical"}
NON_ACADEMIC_TYPES = {"webpage-blog", "hacker-news", "gist", "reddit", "pypi"}
DOCS_TYPES = {"webpage-docs", "github-repo"}

# ── 5. Report ──────────────────────────────────────────────────────────────
print("=" * 80)
print("SOURCE AUTHORITY FLATTENING AUDIT")
print("=" * 80)
print(f"\nTotal cards analyzed: {len(cards_data)}")
print()

# Distribution table
print("┌─────────────────────┬───────┬──────────┬──────────┬──────────────┬──────────────┐")
print("│ Source Type          │ Cards │ Avg Qual │ Med Qual │ Qual/100w    │ Total Quals  │")
print("├─────────────────────┼───────┼──────────┼──────────┼──────────────┼──────────────┤")

type_order = ["arxiv-experimental", "arxiv-theoretical", "webpage-docs",
              "webpage-blog", "hacker-news", "gist", "pypi", "github-repo", "reddit"]

type_avg = {}
for st in type_order:
    b = type_stats.get(st)
    if not b or b["count"] == 0:
        continue
    quals = [c["qual_count"] for c in b["cards"]]
    densities = [c["qual_density"] for c in b["cards"]]
    avg_q = sum(quals) / len(quals)
    med_q = sorted(quals)[len(quals) // 2]
    avg_d = sum(densities) / len(densities)
    type_avg[st] = avg_q
    print(f"│ {st:<19} │ {b['count']:>5} │ {avg_q:>8.2f} │ {med_q:>8.1f} │ {avg_d:>12.3f} │ {b['total_qual']:>12} │")

print("└─────────────────────┴───────┴──────────┴──────────┴──────────────┴──────────────┘")

# Academic vs non-academic summary
print("\n── Academic vs Non-Academic Summary ──")
acad_quals = [c["qual_count"] for c in cards_data if c["source_type_set"] & ACADEMIC_TYPES]
noac_quals = [c["qual_count"] for c in cards_data
              if (c["source_type_set"] & NON_ACADEMIC_TYPES) and not (c["source_type_set"] & ACADEMIC_TYPES)]
docs_quals = [c["qual_count"] for c in cards_data
              if (c["source_type_set"] & DOCS_TYPES) and not (c["source_type_set"] & ACADEMIC_TYPES)]

acad_avg = sum(acad_quals) / max(len(acad_quals), 1)
noac_avg = sum(noac_quals) / max(len(noac_quals), 1)

acad_densities = [c["qual_density"] for c in cards_data if c["source_type_set"] & ACADEMIC_TYPES]
noac_densities = [c["qual_density"] for c in cards_data
                  if (c["source_type_set"] & NON_ACADEMIC_TYPES) and not (c["source_type_set"] & ACADEMIC_TYPES)]

acad_avg_d = sum(acad_densities) / max(len(acad_densities), 1)
noac_avg_d = sum(noac_densities) / max(len(noac_densities), 1)

print(f"  Academic (arxiv) cards:      {len(acad_quals):>3} cards, avg qualifiers: {acad_avg:.2f}, avg density: {acad_avg_d:.3f}/100w")
print(f"  Non-academic (blog/HN/gist): {len(noac_quals):>3} cards, avg qualifiers: {noac_avg:.2f}, avg density: {noac_avg_d:.3f}/100w")
print(f"  Docs/repo cards:             {len(docs_quals):>3} cards")

if noac_avg < acad_avg:
    gap = acad_avg - noac_avg
    print(f"\n  *** AUTHORITY FLATTENING DETECTED ***")
    print(f"  Non-academic sources use {gap:.2f} FEWER qualifiers on average than academic sources.")
    print(f"  This means anecdotal/blog content is presented with MORE confidence than experimental papers.")
    flattening = True
elif noac_avg > acad_avg:
    print(f"\n  No flattening: non-academic sources use MORE qualifiers ({noac_avg:.2f}) than academic ({acad_avg:.2f}).")
    flattening = False
else:
    print(f"\n  Qualifiers are equal across types.")
    flattening = False

# Density comparison
print(f"\n── Density Comparison (qualifiers per 100 words) ──")
if noac_avg_d < acad_avg_d:
    print(f"  Academic density:     {acad_avg_d:.3f}/100w")
    print(f"  Non-academic density: {noac_avg_d:.3f}/100w")
    print(f"  Gap: {acad_avg_d - noac_avg_d:.3f}/100w → non-academic text is more assertive per word")

# ── 6. Top 10 authority-gap cards ──────────────────────────────────────────
# Cards with: (a) non-academic source only, (b) fewest qualifiers, (c) longest body
# "Authority gap" = card presents non-academic content with high confidence
# Score: low qualifiers + non-academic source + substantial body

print("\n── Top 10 Cards with Highest Authority Gap ──")
print("   (non-academic source, low qualifier density, substantial body)\n")

# Filter: only non-academic, no academic co-source
noac_cards = [c for c in cards_data
              if (c["source_type_set"] & NON_ACADEMIC_TYPES)
              and not (c["source_type_set"] & ACADEMIC_TYPES)
              and c["word_count"] >= 30]  # skip stub cards

# Sort by qualifier density ascending (least hedged first), break ties by word_count desc
noac_cards.sort(key=lambda c: (c["qual_density"], -c["word_count"]))

print(f"{'#':>2} {'Card ID':<50} {'Type':<16} {'Quals':>5} {'Words':>5} {'Q/100w':>7}")
print(f"{'─'*2} {'─'*50} {'─'*16} {'─'*5} {'─'*5} {'─'*7}")

for i, c in enumerate(noac_cards[:10], 1):
    types_str = ",".join(sorted(c["source_type_set"]))
    print(f"{i:>2} {c['id']:<50} {types_str:<16} {c['qual_count']:>5} {c['word_count']:>5} {c['qual_density']:>7.3f}")

# ── 7. Reverse check: most-hedged academic cards ──────────────────────────
print("\n── Top 5 Most-Hedged Academic Cards (for contrast) ──\n")
acad_cards = [c for c in cards_data
              if (c["source_type_set"] & ACADEMIC_TYPES) and c["word_count"] >= 30]
acad_cards.sort(key=lambda c: -c["qual_density"])

print(f"{'#':>2} {'Card ID':<50} {'Type':<20} {'Quals':>5} {'Words':>5} {'Q/100w':>7}")
print(f"{'─'*2} {'─'*50} {'─'*20} {'─'*5} {'─'*5} {'─'*7}")
for i, c in enumerate(acad_cards[:5], 1):
    types_str = ",".join(sorted(c["source_type_set"]))
    print(f"{i:>2} {c['id']:<50} {types_str:<20} {c['qual_count']:>5} {c['word_count']:>5} {c['qual_density']:>7.3f}")

# ── 8. Zero-qualifier cards breakdown ─────────────────────────────────────
print("\n── Zero-Qualifier Cards by Source Type ──\n")
zero_by_type = defaultdict(list)
for c in cards_data:
    if c["qual_count"] == 0:
        for st in c["source_type_set"]:
            zero_by_type[st].append(c["id"])

for st in type_order:
    if st in zero_by_type:
        total_in_type = type_stats[st]["count"] if st in type_stats else 0
        pct = len(zero_by_type[st]) / max(total_in_type, 1) * 100
        print(f"  {st:<20}: {len(zero_by_type[st]):>3} / {total_in_type:>3} cards ({pct:.0f}%) have zero qualifiers")

# ── 9. Per-source-id stats for HN specifically ────────────────────────────
print("\n── Hacker News cards detail ──\n")
hn_cards = [c for c in cards_data if "hacker-news" in c["source_type_set"]]
for c in sorted(hn_cards, key=lambda x: x["qual_density"]):
    print(f"  {c['id']:<50} quals={c['qual_count']:>2}  words={c['word_count']:>3}  density={c['qual_density']:.3f}")

# ── 10. Final verdict ─────────────────────────────────────────────────────
print("\n" + "=" * 80)
print("VERDICT")
print("=" * 80)

# Count how many non-academic zero-qualifier cards exist
noac_zero = len([c for c in noac_cards if c["qual_count"] == 0])
total_noac = len(noac_cards)

if flattening:
    severity = "HIGH" if (acad_avg - noac_avg) > 0.5 else "MODERATE"
    print(f"\n  Authority flattening: {severity}")
    print(f"  Academic avg qualifiers: {acad_avg:.2f}")
    print(f"  Non-academic avg qualifiers: {noac_avg:.2f}")
    print(f"  Gap: {acad_avg - noac_avg:.2f} fewer qualifiers in non-academic cards")
    print(f"  Zero-qualifier non-academic cards: {noac_zero}/{total_noac} ({noac_zero/max(total_noac,1)*100:.0f}%)")
    print(f"\n  Recommendation: Add hedging language to non-academic-sourced cards,")
    print(f"  especially those with 0 qualifiers. Blog/HN/gist content should")
    print(f"  carry explicit epistemic markers (e.g., '据社区反馈', '经验性观察').")
else:
    print(f"\n  No significant authority flattening detected.")
    print(f"  Academic avg: {acad_avg:.2f}, Non-academic avg: {noac_avg:.2f}")
    print(f"  Zero-qualifier non-academic cards: {noac_zero}/{total_noac} ({noac_zero/max(total_noac,1)*100:.0f}%)")

print()
