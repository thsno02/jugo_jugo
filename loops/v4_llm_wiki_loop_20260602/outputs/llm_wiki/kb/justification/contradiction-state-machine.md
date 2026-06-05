---
schema: justification_journal.v1
card: ../cards/contradiction-state-machine.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/obsidian-community-plugin/text.txt`
源证据：
- L284 — "Contradiction State Machine — detected → review_ok → resolved (AI fix) or detected → pending_fix (manual)"
- L267 — "Smart Knowledge Fusion — Multi-source updates merge new info without redundancy, contradictions preserved with attribution"
- L274 — "Lint Health Scan — Detects duplicates, dead links, empty pages, orphans, missing aliases, and contradictions"
- L381 — "contradictions.ts # Contradiction detection"
范围论证：现有 lint-operation 卡列出矛盾检测为巡检项之一，但未展开其跟踪机制；该卡记录插件实现的具体状态机（detected/review_ok/resolved/pending_fix）及其设计哲学（保留矛盾而非消除），是独立的 mechanism 概念
