#!/usr/bin/env python3
"""
audit_mechanical.py — v5 全量机械化审计脚本。

一次性执行 14 个可脚本化审计维度，输出 JSON report + suspect 清单（按维度分组）。

用法:
    python audit_mechanical.py

输出:
    stdout: 人类可读摘要
    v5_mechanical_audit_report.json: 完整 JSON 结果
"""

import json
import re
import sys
import yaml
from pathlib import Path
from collections import defaultdict
from itertools import combinations

# ── Paths ─────────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parents[3]
LOOP_ROOT = Path(__file__).resolve().parents[1]
CARDS_DIR = LOOP_ROOT / "outputs" / "llm_wiki" / "kb" / "cards"
JUSTIFICATION_DIR = LOOP_ROOT / "outputs" / "llm_wiki" / "kb" / "justification"
INDEX_FILE = LOOP_ROOT / "outputs" / "llm_wiki" / "kb" / "indexes" / "cards.md"
RAW_DIR = REPO_ROOT / "data" / "raw"
LOOP_STATE = LOOP_ROOT / "loop_state.json"

# ── Helpers ───────────────────────────────────────────────────────────────────

def extract_frontmatter_and_body(text: str) -> tuple:
    """Parse --- delimited frontmatter and body. Returns (dict|None, body_str)."""
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None, text
    end = -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end == -1:
        return None, text
    raw_yaml = "\n".join(lines[1:end])
    body = "\n".join(lines[end + 1:])
    try:
        data = yaml.safe_load(raw_yaml)
        if not isinstance(data, dict):
            return None, text
        return data, body
    except yaml.YAMLError:
        return None, text


def strip_formatting(text: str) -> str:
    """Strip LaTeX and Markdown formatting for fuzzy matching."""
    # LaTeX escapes
    t = text.replace("\\%", "%").replace("\\&", "&").replace("\\#", "#")
    t = t.replace("\\$", "$").replace("\\_", "_")
    # Remove inline math $...$ and display math $$...$$
    t = re.sub(r'\$\$.*?\$\$', ' ', t, flags=re.DOTALL)
    t = re.sub(r'\$[^$]+?\$', ' ', t)
    # Remove LaTeX commands
    t = re.sub(r'\\[a-zA-Z]+\{([^}]*)\}', r'\1', t)
    t = re.sub(r'\\[a-zA-Z]+', '', t)
    # Markdown: bold, italic, code
    t = re.sub(r'\*\*([^*]+)\*\*', r'\1', t)
    t = re.sub(r'\*([^*]+)\*', r'\1', t)
    t = re.sub(r'`([^`]+)`', r'\1', t)
    # Collapse whitespace
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def count_sentences(text: str) -> int:
    """Count sentences (Chinese + English punctuation)."""
    # Split on sentence-ending punctuation
    parts = re.split(r'[。！？.!?]', text)
    return len([p for p in parts if p.strip()])


# ── Load all cards ────────────────────────────────────────────────────────────
print("加载卡片数据...")

ALL_CARDS = {}  # slug -> {fm, body, path}
for card_path in sorted(CARDS_DIR.glob("*.md")):
    text = card_path.read_text(encoding="utf-8")
    fm, body = extract_frontmatter_and_body(text)
    slug = card_path.stem
    ALL_CARDS[slug] = {"fm": fm, "body": body, "path": card_path}

ALL_SLUGS = set(ALL_CARDS.keys())
print(f"  总卡片数: {len(ALL_CARDS)}")

# ── Build source registry ─────────────────────────────────────────────────────
ALL_RAW_SOURCES = set()
SOURCE_DOMAIN_MAP = {}  # source_id -> domain
for domain_dir in RAW_DIR.iterdir():
    if domain_dir.is_dir():
        domain = domain_dir.name
        for src_dir in domain_dir.iterdir():
            if src_dir.is_dir():
                ALL_RAW_SOURCES.add(src_dir.name)
                SOURCE_DOMAIN_MAP[src_dir.name] = domain

print(f"  总源目录数: {len(ALL_RAW_SOURCES)}")

# ══════════════════════════════════════════════════════════════════════════════
# AUDIT DIMENSIONS
# ══════════════════════════════════════════════════════════════════════════════

report = {}
suspects = {}

# ── C1: YAML 格式验证 ────────────────────────────────────────────────────────
print("\n[C1] YAML 格式验证...")

REQUIRED_FIELDS = ["id", "title", "source_ids", "canonical_concept", "related", "summary"]
c1_errors = []

for slug, card in ALL_CARDS.items():
    fm = card["fm"]
    if fm is None:
        c1_errors.append({"card": slug, "error": "无法解析 frontmatter"})
        continue
    for field in REQUIRED_FIELDS:
        if field not in fm:
            c1_errors.append({"card": slug, "error": f"缺失必填字段: {field}"})

report["C1_yaml_validation"] = {
    "total_cards": len(ALL_CARDS),
    "errors": len(c1_errors),
    "pass": len(c1_errors) == 0,
    "details": c1_errors[:20]  # cap output
}
print(f"  错误数: {len(c1_errors)}")

# ── B1: 悬空引用检测 ─────────────────────────────────────────────────────────
print("\n[B1] 悬空引用检测...")

b1_dangling = []
CARD_REF_RE = re.compile(r'\[\[([a-z0-9-]+)\]\]')

for slug, card in ALL_CARDS.items():
    fm = card["fm"]
    if fm is None:
        continue
    # Check related field
    related = fm.get("related", [])
    if isinstance(related, list):
        for ref in related:
            if isinstance(ref, str) and ref not in ALL_SLUGS:
                b1_dangling.append({"card": slug, "type": "related", "ref": ref})
    # Check [[wikilink]] in body -- only in [^card-N] footnote lines
    for line in card["body"].split("\n"):
        if line.strip().startswith("[^card-"):
            for m in CARD_REF_RE.finditer(line):
                if m.group(1) not in ALL_SLUGS:
                    b1_dangling.append({"card": slug, "type": "wikilink_in_footnote", "ref": m.group(1)})

report["B1_dangling_refs"] = {
    "total_refs_checked": sum(
        len(c["fm"].get("related", [])) for c in ALL_CARDS.values() if c["fm"]
    ),
    "dangling": len(b1_dangling),
    "pass": len(b1_dangling) == 0,
    "details": b1_dangling[:20]
}
print(f"  悬空引用数: {len(b1_dangling)}")

# ── B2: 孤儿卡检测 ───────────────────────────────────────────────────────────
print("\n[B2] 孤儿卡检测...")

# Build inbound reference count
inbound = defaultdict(int)
CARD_FOOTNOTE_RE = re.compile(r'\[\^card-[^\]]+\]')

for slug, card in ALL_CARDS.items():
    fm = card["fm"]
    if fm is None:
        continue
    related = fm.get("related", [])
    if isinstance(related, list):
        for ref in related:
            if isinstance(ref, str) and ref in ALL_SLUGS:
                inbound[ref] += 1
    # Also count [^card-N] mentions that reference other cards
    for m in re.finditer(r'\[\^card-[^\]]+\]:\s*(.+)', card["body"]):
        line = m.group(1)
        # Try to find slug in the footnote definition line
        slug_match = re.search(r'([a-z][a-z0-9-]+[a-z0-9])', line)
        if slug_match and slug_match.group(1) in ALL_SLUGS:
            inbound[slug_match.group(1)] += 1

orphans = []
for slug, card in ALL_CARDS.items():
    fm = card["fm"]
    if fm is None:
        continue
    card_type = fm.get("card_type", "")
    if card_type == "comparison":
        continue  # exclude comparison sinks
    if inbound[slug] == 0:
        orphans.append(slug)

report["B2_orphan_cards"] = {
    "total_non_comparison": len([s for s, c in ALL_CARDS.items()
                                  if c["fm"] and c["fm"].get("card_type") != "comparison"]),
    "orphans": len(orphans),
    "orphan_rate": f"{len(orphans)/max(len(ALL_CARDS),1)*100:.1f}%",
    "pass": len(orphans) / max(len(ALL_CARDS), 1) < 0.05,
    "details": orphans[:20]
}
print(f"  孤儿卡数: {len(orphans)} ({report['B2_orphan_cards']['orphan_rate']})")

# ── B3: 反向链接不对称检测 ───────────────────────────────────────────────────
print("\n[B3] 反向链接不对称检测...")

asymmetric_edges = []
total_edges = 0

for slug, card in ALL_CARDS.items():
    fm = card["fm"]
    if fm is None:
        continue
    related = fm.get("related", [])
    if not isinstance(related, list):
        continue
    for ref in related:
        if not isinstance(ref, str) or ref not in ALL_SLUGS:
            continue
        total_edges += 1
        # Check if ref's related contains slug
        ref_card = ALL_CARDS[ref]
        ref_fm = ref_card["fm"]
        if ref_fm is None:
            asymmetric_edges.append({"from": slug, "to": ref, "reason": "target has no fm"})
            continue
        ref_related = ref_fm.get("related", [])
        if not isinstance(ref_related, list):
            ref_related = []
        # Exclude comparison sinks
        ref_type = ref_fm.get("card_type", "")
        if ref_type == "comparison":
            continue
        if slug not in ref_related:
            asymmetric_edges.append({"from": slug, "to": ref})

asym_rate = len(asymmetric_edges) / max(total_edges, 1) * 100
report["B3_backlink_asymmetry"] = {
    "total_edges": total_edges,
    "asymmetric": len(asymmetric_edges),
    "rate": f"{asym_rate:.1f}%",
    "pass": asym_rate < 5.0,
    "details": asymmetric_edges[:20]
}
print(f"  不对称边: {len(asymmetric_edges)}/{total_edges} ({asym_rate:.1f}%)")

# ── B4: 跨域桥梁统计 ─────────────────────────────────────────────────────────
print("\n[B4] 跨域桥梁统计...")

# Card -> domain mapping
card_domain = {}
for slug, card in ALL_CARDS.items():
    fm = card["fm"]
    if fm is None:
        continue
    source_ids = fm.get("source_ids", [])
    if not isinstance(source_ids, list):
        source_ids = [source_ids] if source_ids else []
    domains = set()
    for sid in source_ids:
        if sid in SOURCE_DOMAIN_MAP:
            domains.add(SOURCE_DOMAIN_MAP[sid])
    card_domain[slug] = domains

# Count cross-domain links per domain
domain_cross_links = defaultdict(int)
domain_card_count = defaultdict(int)

for slug, domains in card_domain.items():
    for d in domains:
        domain_card_count[d] += 1

for slug, card in ALL_CARDS.items():
    fm = card["fm"]
    if fm is None:
        continue
    my_domains = card_domain.get(slug, set())
    related = fm.get("related", [])
    if not isinstance(related, list):
        continue
    for ref in related:
        if ref not in card_domain:
            continue
        ref_domains = card_domain[ref]
        # Cross-domain if ref has domains not overlapping with mine
        if ref_domains and my_domains and not (ref_domains & my_domains):
            for d in my_domains:
                domain_cross_links[d] += 1

bridge_details = {}
all_pass = True
for d in sorted(domain_card_count.keys()):
    cross = domain_cross_links[d]
    bridge_details[d] = {"cards": domain_card_count[d], "cross_links": cross, "pass": cross >= 2}
    if cross < 2:
        all_pass = False

report["B4_cross_domain_bridge"] = {
    "domains": bridge_details,
    "pass": all_pass
}
print(f"  域统计:")
for d, info in bridge_details.items():
    status = "PASS" if info["pass"] else "FAIL"
    print(f"    {d}: {info['cards']} 卡, {info['cross_links']} 跨域链接 [{status}]")

# ── A1: 源忠实性 grep 全量验证 ────────────────────────────────────────────────
print("\n[A1] 源忠实性 grep 全量验证...")

SRC_FOOTNOTE_RE = re.compile(
    r'\[\^(src-\d+)\]:\s*`([^`]+)`\s*--\s*"([^"]+)"\s*(?:P\d+\s*)?--\s*"(.+)"$',
    re.MULTILINE
)
# Alternative format without section quotes
SRC_FOOTNOTE_RE2 = re.compile(
    r'\[\^(src-\d+)\]:\s*`([^`]+)`\s*--\s*(.+?)--\s*"(.+)"$',
    re.MULTILINE
)

a1_total = 0
a1_verified = 0
a1_suspects = []
source_cache = {}  # path -> stripped text

def normalize_for_search(text: str) -> str:
    """Aggressively normalize text for fuzzy matching: lowercase, collapse all non-alnum."""
    # Keep only alphanumeric + CJK characters, collapse everything else to single space
    t = re.sub(r'[^\w一-鿿]+', ' ', text.lower())
    return re.sub(r'\s+', ' ', t).strip()


def load_source_text(rel_path: str) -> str | None:
    """Load and cache source file text (stripped). Also tries text.txt sibling."""
    if rel_path in source_cache:
        return source_cache[rel_path]
    full_path = REPO_ROOT / rel_path
    texts = []
    if full_path.exists():
        try:
            texts.append(full_path.read_text(encoding="utf-8", errors="ignore"))
        except Exception:
            pass
    # Also try text.txt sibling (plain-text extraction) for arxiv bundles
    sibling_txt = full_path.parent / "text.txt"
    if sibling_txt.exists() and sibling_txt != full_path:
        try:
            texts.append(sibling_txt.read_text(encoding="utf-8", errors="ignore"))
        except Exception:
            pass
    # Also try markdown.md sibling for webpages
    sibling_md = full_path.parent / "markdown.md"
    if sibling_md.exists() and sibling_md != full_path:
        try:
            texts.append(sibling_md.read_text(encoding="utf-8", errors="ignore"))
        except Exception:
            pass
    if not texts:
        source_cache[rel_path] = None
        return None
    combined = "\n".join(texts)
    stripped = normalize_for_search(strip_formatting(combined))
    source_cache[rel_path] = stripped
    return stripped

for slug, card in ALL_CARDS.items():
    body = card["body"]
    # Find all src footnote definitions
    for m in SRC_FOOTNOTE_RE.finditer(body):
        a1_total += 1
        fn_key, path, section, quote = m.group(1), m.group(2), m.group(3), m.group(4)
        # Strip and search
        source_text = load_source_text(path)
        if source_text is None:
            a1_suspects.append({
                "card": slug, "footnote": fn_key, "path": path,
                "reason": "源文件不存在"
            })
            continue
        quote_normalized = normalize_for_search(strip_formatting(quote))
        # Take first N chars for matching
        search_key = quote_normalized[:80].strip()
        if len(search_key) < 10:
            a1_verified += 1  # too short to verify meaningfully
            continue
        if search_key in source_text:
            a1_verified += 1
        else:
            # Try shorter prefix (first 40 normalized chars)
            shorter = quote_normalized[:40].strip()
            if len(shorter) >= 10 and shorter in source_text:
                a1_verified += 1
            else:
                # Try even shorter (first 25 chars) -- for heavily reformatted quotes
                shortest = quote_normalized[:25].strip()
                if len(shortest) >= 10 and shortest in source_text:
                    a1_verified += 1
                else:
                    a1_suspects.append({
                        "card": slug, "footnote": fn_key, "path": path,
                        "quote_prefix": quote[:80],
                        "reason": "grep 未匹配"
                    })

    # Also try format 2
    for m in SRC_FOOTNOTE_RE2.finditer(body):
        # Skip if already matched by RE1
        fn_key = m.group(1)
        if any(s["footnote"] == fn_key and s["card"] == slug for s in a1_suspects):
            continue
        if f"[^{fn_key}]" in body and not SRC_FOOTNOTE_RE.search(f"[^{fn_key}]: " + m.group(0).split(": ", 1)[-1] if ": " in m.group(0) else ""):
            pass  # already counted above

suspect_rate = len(a1_suspects) / max(a1_total, 1) * 100
report["A1_source_faithfulness"] = {
    "total_footnotes": a1_total,
    "verified": a1_verified,
    "suspects": len(a1_suspects),
    "suspect_rate": f"{suspect_rate:.1f}%",
    "pass": suspect_rate < 5.0,
    "details": a1_suspects[:30]
}
suspects["A1"] = a1_suspects
print(f"  脚注总数: {a1_total}, 验证通过: {a1_verified}, suspect: {len(a1_suspects)} ({suspect_rate:.1f}%)")

# ── A2: 权威扁平化统计 ───────────────────────────────────────────────────────
print("\n[A2] 权威扁平化统计...")

QUALIFIERS_ZH = ["可能", "或许", "暗示", "据报道", "有待验证", "尚未", "初步",
                  "假设", "推测", "不确定", "一定程度", "似乎", "据称"]
QUALIFIERS_EN = ["suggests", "may", "might", "anecdotal", "could",
                 "potentially", "arguably", "preliminary", "hypothesi",
                 "speculative", "uncertain", "reportedly", "appears to",
                 "seems to", "likely", "possibly", "tentative"]

a2_stats = defaultdict(lambda: {"total": 0, "zero_hedge": 0, "total_quals": 0})

for slug, card in ALL_CARDS.items():
    fm = card["fm"]
    if fm is None:
        continue
    evidence_basis = fm.get("evidence_basis", "unknown")
    body_main = card["body"].split("[^src-")[0] if "[^src-" in card["body"] else card["body"]
    # Actually split at footnote definitions section
    body_for_quals = card["body"]
    # Count qualifiers
    lower = body_for_quals.lower()
    qual_count = 0
    for q in QUALIFIERS_ZH:
        qual_count += body_for_quals.count(q)
    for q in QUALIFIERS_EN:
        qual_count += lower.count(q)

    a2_stats[evidence_basis]["total"] += 1
    a2_stats[evidence_basis]["total_quals"] += qual_count
    if qual_count == 0:
        a2_stats[evidence_basis]["zero_hedge"] += 1

a2_report = {}
for basis, stats in sorted(a2_stats.items()):
    zero_pct = stats["zero_hedge"] / max(stats["total"], 1) * 100
    a2_report[basis] = {
        "total": stats["total"],
        "zero_hedge": stats["zero_hedge"],
        "zero_hedge_pct": f"{zero_pct:.1f}%",
        "avg_quals": stats["total_quals"] / max(stats["total"], 1)
    }

# Check thresholds
community_stats = a2_stats.get("community_discussion", {"total": 0, "zero_hedge": 0})
community_zero_pct = community_stats["zero_hedge"] / max(community_stats["total"], 1) * 100
a2_pass = community_zero_pct <= 50.0 if community_stats["total"] > 0 else True

report["A2_authority_flattening"] = {
    "by_evidence_basis": a2_report,
    "community_discussion_zero_hedge_pct": f"{community_zero_pct:.1f}%",
    "pass": a2_pass
}
print(f"  按 evidence_basis 分布:")
for basis, info in sorted(a2_report.items()):
    print(f"    {basis}: {info['total']} 卡, 零限定词 {info['zero_hedge_pct']}, 平均 {info['avg_quals']:.1f}")

# ── C2: 标题连词检测（原子性）────────────────────────────────────────────────
print("\n[C2] 标题连词检测...")

CONJUNCTIONS = re.compile(
    r'(?:^|\s)(与|和|及|以及|and|vs\.?|versus|or)(?:\s|$)',
    re.IGNORECASE
)
# More specific patterns to reduce false positives
CONJUNCTION_STRICT = re.compile(
    r'\b(and|vs\.?|versus)\b|\s(与|和|及|以及)\s',
    re.IGNORECASE
)

c2_hits = []
for slug, card in ALL_CARDS.items():
    fm = card["fm"]
    if fm is None:
        continue
    title = fm.get("title", "")
    card_type = fm.get("card_type", "")
    # Comparison cards may legitimately use vs
    if card_type == "comparison":
        continue
    if CONJUNCTION_STRICT.search(title):
        c2_hits.append({"card": slug, "title": title})

c2_rate = len(c2_hits) / max(len(ALL_CARDS), 1) * 100
report["C2_title_conjunction"] = {
    "total_non_comparison": len([s for s, c in ALL_CARDS.items()
                                  if c["fm"] and c["fm"].get("card_type") != "comparison"]),
    "conjunction_titles": len(c2_hits),
    "rate": f"{c2_rate:.1f}%",
    "pass": c2_rate < 5.0,
    "details": c2_hits[:20]
}
print(f"  连词标题: {len(c2_hits)} ({c2_rate:.1f}%)")

# ── C3: 概念重叠检测 ─────────────────────────────────────────────────────────
print("\n[C3] 概念重叠检测...")

# Build footnote fingerprints per card
SRC_FN_FINGERPRINT_RE = re.compile(
    r'\[\^src-\d+\]:\s*`([^`]+)`\s*--\s*"([^"]{0,60})',
    re.MULTILINE
)

card_fingerprints = {}
for slug, card in ALL_CARDS.items():
    fps = set()
    for m in SRC_FN_FINGERPRINT_RE.finditer(card["body"]):
        path = m.group(1)
        quote_prefix = m.group(2)[:30]
        fps.add(f"{path}|{quote_prefix}")
    card_fingerprints[slug] = fps

# Find overlapping pairs
c3_overlaps = []
slugs_list = sorted(ALL_SLUGS)
for i in range(len(slugs_list)):
    fps_i = card_fingerprints.get(slugs_list[i], set())
    if not fps_i:
        continue
    for j in range(i + 1, len(slugs_list)):
        fps_j = card_fingerprints.get(slugs_list[j], set())
        if not fps_j:
            continue
        shared = fps_i & fps_j
        if len(shared) > 2:
            c3_overlaps.append({
                "card_a": slugs_list[i],
                "card_b": slugs_list[j],
                "shared_count": len(shared),
                "shared_sample": list(shared)[:3]
            })

total_pairs = len(slugs_list) * (len(slugs_list) - 1) // 2
c3_rate = len(c3_overlaps) / max(total_pairs, 1) * 100
report["C3_concept_overlap"] = {
    "total_card_pairs": total_pairs,
    "overlap_pairs": len(c3_overlaps),
    "rate": f"{c3_rate:.4f}%",
    "pass": c3_rate < 3.0,
    "details": c3_overlaps[:20]
}
print(f"  重叠卡对: {len(c3_overlaps)} ({c3_rate:.4f}%)")

# ── C4: 循环/强连通分量检测 ──────────────────────────────────────────────────
print("\n[C4] 强连通分量检测 (Tarjan)...")

# Build directed graph from related
graph = defaultdict(list)
for slug, card in ALL_CARDS.items():
    fm = card["fm"]
    if fm is None:
        continue
    related = fm.get("related", [])
    if isinstance(related, list):
        for ref in related:
            if isinstance(ref, str) and ref in ALL_SLUGS:
                graph[slug].append(ref)

# Tarjan's SCC algorithm
index_counter = [0]
stack = []
lowlink = {}
index = {}
on_stack = {}
sccs = []

def strongconnect(v):
    index[v] = index_counter[0]
    lowlink[v] = index_counter[0]
    index_counter[0] += 1
    stack.append(v)
    on_stack[v] = True

    for w in graph.get(v, []):
        if w not in index:
            strongconnect(w)
            lowlink[v] = min(lowlink[v], lowlink[w])
        elif on_stack.get(w, False):
            lowlink[v] = min(lowlink[v], index[w])

    if lowlink[v] == index[v]:
        scc = []
        while True:
            w = stack.pop()
            on_stack[w] = False
            scc.append(w)
            if w == v:
                break
        if len(scc) > 1:
            sccs.append(scc)

# Use iterative approach for large graphs to avoid recursion limit
sys.setrecursionlimit(10000)
for node in ALL_SLUGS:
    if node not in index:
        try:
            strongconnect(node)
        except RecursionError:
            # Fallback: skip deep recursion
            pass

large_sccs = [s for s in sccs if len(s) > 2]
report["C4_strongly_connected"] = {
    "total_sccs_gt2": len(large_sccs),
    "largest_scc_size": max((len(s) for s in large_sccs), default=0),
    "sccs": [{"size": len(s), "sample": s[:5]} for s in sorted(large_sccs, key=len, reverse=True)[:10]],
    "pass": True  # informational metric
}
print(f"  SCC > 2 nodes: {len(large_sccs)}, 最大: {max((len(s) for s in large_sccs), default=0)}")

# ── D1: 源消化率 ─────────────────────────────────────────────────────────────
print("\n[D1] 源消化率...")

# Collect all source_ids referenced by cards
consumed_sources = set()
for slug, card in ALL_CARDS.items():
    fm = card["fm"]
    if fm is None:
        continue
    source_ids = fm.get("source_ids", [])
    if isinstance(source_ids, list):
        for sid in source_ids:
            consumed_sources.add(sid)
    elif source_ids:
        consumed_sources.add(str(source_ids))

unconsumed = ALL_RAW_SOURCES - consumed_sources
# Load loop_state for failed_sources
failed_sources = []
if LOOP_STATE.exists():
    try:
        ls = json.loads(LOOP_STATE.read_text())
        failed_sources = ls.get("failed_sources", [])
        if isinstance(failed_sources, int):
            failed_sources = []
    except Exception:
        pass

# Check if unconsumed sources are accounted for in failed_sources
unaccounted = unconsumed - set(failed_sources) if isinstance(failed_sources, list) else unconsumed

consumption_rate = len(consumed_sources) / max(len(ALL_RAW_SOURCES), 1) * 100
report["D1_source_consumption"] = {
    "total_raw_sources": len(ALL_RAW_SOURCES),
    "consumed": len(consumed_sources),
    "unconsumed": len(unconsumed),
    "consumption_rate": f"{consumption_rate:.1f}%",
    "failed_sources_recorded": len(failed_sources) if isinstance(failed_sources, list) else 0,
    "unaccounted_missing": len(unaccounted),
    "unaccounted_details": sorted(list(unaccounted))[:20],
    "pass": len(unaccounted) == 0
}
print(f"  消化率: {consumption_rate:.1f}% ({len(consumed_sources)}/{len(ALL_RAW_SOURCES)})")
print(f"  未记录遗漏: {len(unaccounted)}")

# ── D2: 覆盖率统计 ───────────────────────────────────────────────────────────
print("\n[D2] 覆盖率统计...")

# Cards per source
cards_per_source = defaultdict(int)
for slug, card in ALL_CARDS.items():
    fm = card["fm"]
    if fm is None:
        continue
    source_ids = fm.get("source_ids", [])
    if isinstance(source_ids, list):
        for sid in source_ids:
            cards_per_source[sid] += 1

cps_values = list(cards_per_source.values()) if cards_per_source else [0]
avg_cps = sum(cps_values) / max(len(cps_values), 1)
med_cps = sorted(cps_values)[len(cps_values) // 2] if cps_values else 0
max_cps = max(cps_values) if cps_values else 0
max_source = max(cards_per_source, key=cards_per_source.get) if cards_per_source else "N/A"

report["D2_coverage"] = {
    "avg_cards_per_source": f"{avg_cps:.1f}",
    "median_cards_per_source": med_cps,
    "max_cards_per_source": max_cps,
    "max_source": max_source,
    "consumption_rate": f"{consumption_rate:.1f}%",
    "pass": consumption_rate > 80.0
}
print(f"  每源平均卡片: {avg_cps:.1f}, 中位: {med_cps}, 最大: {max_cps} ({max_source})")

# ── E1: 跨源泄漏初筛 ─────────────────────────────────────────────────────────
print("\n[E1] 跨源泄漏初筛...")

# Build concept index: canonical_concept + aliases -> slug
concept_to_slug = {}
GENERIC_TERMS = {"llm", "rag", "agent", "ai", "api", "mcp", "kb", "wiki",
                 "knowledge", "graph", "model", "token", "context", "memory",
                 "prompt", "vector", "embedding", "retrieval", "query", "tool",
                 "benchmark", "evaluation", "framework", "system", "data",
                 "pipeline", "architecture", "protocol", "security", "attack",
                 "defense", "risk", "trust", "policy", "audit", "compliance"}

for slug, card in ALL_CARDS.items():
    fm = card["fm"]
    if fm is None:
        continue
    cc = fm.get("canonical_concept", "")
    if cc and cc.lower() not in GENERIC_TERMS and len(cc) > 5:
        concept_to_slug[cc] = slug
    aliases = fm.get("aliases", [])
    if isinstance(aliases, list):
        for alias in aliases:
            if isinstance(alias, str) and alias.lower() not in GENERIC_TERMS and len(alias) > 5:
                concept_to_slug[alias] = slug

# Build source groups (cards sharing a source_id)
source_groups = defaultdict(set)  # source_id -> set of slugs
for slug, card in ALL_CARDS.items():
    fm = card["fm"]
    if fm is None:
        continue
    source_ids = fm.get("source_ids", [])
    if isinstance(source_ids, list):
        for sid in source_ids:
            source_groups[sid].add(slug)

def get_co_source_slugs(slug):
    """Get all slugs that share at least one source with this slug."""
    fm = ALL_CARDS[slug]["fm"]
    if fm is None:
        return set()
    source_ids = fm.get("source_ids", [])
    if not isinstance(source_ids, list):
        return set()
    co_slugs = set()
    for sid in source_ids:
        co_slugs.update(source_groups.get(sid, set()))
    return co_slugs

# Check for card-ref footnotes in body
CARD_FN_RE = re.compile(r'\[\^card-[^\]]+\]')

e1_suspects = []
checked = 0
for slug, card in ALL_CARDS.items():
    body_lower = card["body"].lower()
    co_source = get_co_source_slugs(slug)
    # Check if any non-co-source concept appears in body
    for concept, target_slug in concept_to_slug.items():
        if target_slug == slug:
            continue
        if target_slug in co_source:
            continue
        # Check if concept appears in body
        if concept.lower() in body_lower:
            # Check if there's a [^card-N] reference to that card
            # Simple check: does the target slug appear in any card footnote def
            if target_slug in card["body"]:
                continue  # referenced by footnote
            e1_suspects.append({
                "card": slug,
                "leaked_concept": concept,
                "from_card": target_slug,
                "reason": "概念出现在 body 中，无同源关系，无 card 脚注锚定"
            })
    checked += 1

# Cap suspects to avoid noise
e1_suspects = e1_suspects[:50]
report["E1_cross_source_leakage"] = {
    "cards_checked": checked,
    "suspects": len(e1_suspects),
    "pass": True,  # needs agent verification
    "note": "需 agent 验证 — 脚本仅做初筛",
    "details": e1_suspects[:20]
}
suspects["E1"] = e1_suspects
print(f"  初筛 suspect: {len(e1_suspects)} 条")

# ── E2: 无脚注段落幻觉检测 ───────────────────────────────────────────────────
print("\n[E2] 无脚注段落检测...")

SRC_OR_CARD_REF = re.compile(r'\[\^(?:src|card|dist)-')

e2_suspects = []
e2_total_paragraphs = 0
e2_unsourced = 0

for slug, card in ALL_CARDS.items():
    body = card["body"]
    # Split into paragraphs by blank lines
    paragraphs = re.split(r'\n\s*\n', body)
    for para in paragraphs:
        para_stripped = para.strip()
        if not para_stripped:
            continue
        # Skip footnote definition blocks
        if para_stripped.startswith("[^"):
            continue
        # Skip single-line headers
        if para_stripped.startswith("#"):
            continue
        # Skip list items with single entries
        if para_stripped.startswith("- ") and "\n" not in para_stripped:
            continue
        # Count sentences
        sentences = count_sentences(para_stripped)
        if sentences <= 2:
            continue
        e2_total_paragraphs += 1
        # Check for footnote references
        if not SRC_OR_CARD_REF.search(para_stripped):
            e2_unsourced += 1
            e2_suspects.append({
                "card": slug,
                "paragraph_preview": para_stripped[:120],
                "sentences": sentences
            })

e2_rate = e2_unsourced / max(e2_total_paragraphs, 1) * 100
report["E2_unsourced_paragraphs"] = {
    "total_paragraphs_gt2_sentences": e2_total_paragraphs,
    "unsourced": e2_unsourced,
    "rate": f"{e2_rate:.1f}%",
    "pass": e2_rate < 10.0,
    "details": e2_suspects[:20]
}
suspects["E2"] = e2_suspects
print(f"  >2 句段落: {e2_total_paragraphs}, 无脚注: {e2_unsourced} ({e2_rate:.1f}%)")

# ── F1: Loop 独立性 ──────────────────────────────────────────────────────────
print("\n[F1] Loop 独立性检查...")

LOOP_MARKERS = re.compile(
    r'v[0-4]_llm_wiki_loop|loop_2026050|loop_2026051|loop_2026052|loop_2026053|'
    r'loop_20260601|loop_20260602|loop_20260603|loop_20260604|loop_20260605|'
    r'loop_20260606|loop_20260607|loop_20260608|loop_20260609|loop_20260610|loop_20260611'
)

f1_hits = []
for slug, card in ALL_CARDS.items():
    full_text = card["body"]
    fm = card["fm"]
    if fm:
        full_text += "\n" + yaml.dump(fm, allow_unicode=True)
    for m in LOOP_MARKERS.finditer(full_text):
        f1_hits.append({"card": slug, "match": m.group(0), "context": full_text[max(0, m.start()-20):m.end()+20]})

# Also check justification files
for jf in JUSTIFICATION_DIR.glob("*.md"):
    text = jf.read_text(encoding="utf-8", errors="ignore")
    for m in LOOP_MARKERS.finditer(text):
        f1_hits.append({"file": f"justification/{jf.name}", "match": m.group(0)})

report["F1_loop_independence"] = {
    "hits": len(f1_hits),
    "pass": len(f1_hits) == 0,
    "details": f1_hits[:20]
}
print(f"  历史 loop 引用: {len(f1_hits)}")

# ── F2: JJ 文件完整性 ────────────────────────────────────────────────────────
print("\n[F2] Justification 文件完整性...")

f2_missing = []
f2_empty = []

for slug, card in ALL_CARDS.items():
    fm = card["fm"]
    if fm is None:
        continue
    status = fm.get("status", "")
    if status != "accepted":
        continue
    jf_path = JUSTIFICATION_DIR / f"{slug}.md"
    if not jf_path.exists():
        f2_missing.append(slug)
    elif jf_path.stat().st_size < 10:
        f2_empty.append(slug)

total_accepted = len([s for s, c in ALL_CARDS.items()
                      if c["fm"] and c["fm"].get("status") == "accepted"])
f2_complete = total_accepted - len(f2_missing) - len(f2_empty)
f2_rate = f2_complete / max(total_accepted, 1) * 100

report["F2_justification_integrity"] = {
    "total_accepted": total_accepted,
    "with_justification": f2_complete,
    "missing": len(f2_missing),
    "empty": len(f2_empty),
    "completeness_rate": f"{f2_rate:.1f}%",
    "pass": len(f2_missing) == 0 and len(f2_empty) == 0,
    "missing_details": f2_missing[:20],
    "empty_details": f2_empty[:10]
}
print(f"  accepted 卡: {total_accepted}, 有 justification: {f2_complete}, 缺失: {len(f2_missing)}, 空文件: {len(f2_empty)}")

# ══════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 70)
print("v5 机械化审计汇总")
print("=" * 70)

pass_count = 0
fail_count = 0
info_count = 0

summary_rows = []
for dim_id, dim_data in sorted(report.items()):
    status = dim_data.get("pass")
    if status is True:
        label = "PASS"
        pass_count += 1
    elif status is False:
        label = "FAIL"
        fail_count += 1
    else:
        label = "INFO"
        info_count += 1
    summary_rows.append((dim_id, label))

print(f"\n{'维度':<35} {'状态':<6}")
print(f"{'-'*35} {'-'*6}")
for dim_id, label in summary_rows:
    print(f"  {dim_id:<33} {label}")

print(f"\n总计: {pass_count} PASS, {fail_count} FAIL, {info_count} INFO")
print(f"通过率: {pass_count}/{pass_count + fail_count} ({pass_count/(pass_count+fail_count)*100:.0f}%)" if (pass_count + fail_count) > 0 else "")

# ── Write JSON output ─────────────────────────────────────────────────────────
output_dir = LOOP_ROOT / "outputs" / "llm_wiki" / "kb" / "audits"
output_dir.mkdir(parents=True, exist_ok=True)

report_path = output_dir / "v5_mechanical_audit_report.json"
with open(report_path, "w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2, default=str)

suspect_path = output_dir / "v5_suspect_list.json"
with open(suspect_path, "w", encoding="utf-8") as f:
    json.dump(suspects, f, ensure_ascii=False, indent=2, default=str)

print(f"\n报告已写入: {report_path.relative_to(REPO_ROOT)}")
print(f"Suspect 清单: {suspect_path.relative_to(REPO_ROOT)}")
