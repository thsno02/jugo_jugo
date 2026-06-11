---
schema: justification_journal.v1
card: ../cards/scale-tiered-tooling-decision.md
created_time: 2026-06-11T10:00:00+08:00
---

## creation | 2026-06-11T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/openaitoolshub-six-months/markdown.md`
源证据：
- L47-54 — 完整比较表：v1 / Rohit v2 / GBrain / 实际运行方案的五维对比（Storage, Search, Lint, Originals, Best for, Maintenance）
- L7 — "Skip the Postgres + Dream Cycle stuff (GBrain) until your wiki crosses ~500 pages. At 35, plain markdown + grep is faster."
- L42 — "At 35 pages, grep -r 'keyword' wiki/ returns in 40ms."
- L43 — "GBrain's Postgres + Dream Cycle. Garry Tan's GBrain stack deploys at 14,700+ files with nightly cron consolidation."
- L90 — "I'll switch when my page count crosses ~500 and grep starts feeling slow."
范围论证：llm-wiki-scale-boundary 从法语社区来源得出「10 至数百篇文档」的理论边界，本卡的独特贡献是：(1) 从同一实践者对比运行三个方案变体的实践经验出发；(2) 给出具体的维护时间数据（5/10/0/15 min/day）；(3) 提供明确的升级触发点（~500 页 + grep 变慢）。这一结构化比较表和分层决策逻辑在知识库中唯一。
