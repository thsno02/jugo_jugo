---
schema: justification_journal.v1
card: ../cards/log-file.md
created_time: 2026-06-05T00:00:00+08:00
---

## creation | 2026-06-05T00:00:00+08:00

生成方式：Mode A questioning loop, round 1 拆卡（从 index-based-navigation 拆出）
问题：index.md 和 log.md 各自的角色是什么？
来源：`data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`

源证据：
- "Indexing and logging > log.md" P1 — "It's an append-only record of what happened and when"
- "Indexing and logging > log.md" P1 — "The log gives you a timeline of the wiki's evolution"

范围论证：从 index-based-navigation 卡拆出。原卡覆盖了 index.md、log.md 和 qmd 三个不同组件，
违反原子性。本卡聚焦 log.md 的时间线角色和 unix 可解析性。
