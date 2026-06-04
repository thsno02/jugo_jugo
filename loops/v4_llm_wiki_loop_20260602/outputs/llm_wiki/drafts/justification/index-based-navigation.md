---
schema: justification_journal.v1
card: ../cards/index-based-navigation.md
created_time: 2026-06-04T22:30:00+08:00
---

## creation | 2026-06-04T22:30:00+08:00

生成方式：Mode A questioning loop, round 1
问题：index.md 在什么规模下有效？超出后有什么替代方案？
来源：`data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`

源证据：
- "Indexing and logging" — "This works surprisingly well at moderate scale (~100 sources, ~hundreds of pages)"
- "Optional: CLI tools" — "qmd is a good option: it's a local search engine..."
- "Indexing and logging > log.md" — "It's an append-only record"

范围论证：本卡覆盖 wiki 导航的核心机制（index.md）、规模边界、
替代工具（qmd）和辅助文件（log.md）。
