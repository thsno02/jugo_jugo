---
schema: justification_journal.v1
card: ../cards/dual-link-format.md
created_time: 2026-06-11T10:00:00+08:00
---

## creation | 2026-06-11T10:00:00+08:00

生成方式：source extraction pass
来源：`data/raw/webpage/llm-wiki-net/markdown.md`
源证据：
- L117 — "[[wikilinks]] for Obsidian plus standard markdown links for everything else. Works in every viewer — including no viewer at all."
- L205 — "Articles use dual-link format: [[wikilink]] for Obsidian + standard markdown links for everything else."
- L300-302 — "Each topic wiki ships with its own .obsidian/ vault config... Cross-references use a dual-link format"
范围论证：双链格式是一个独立的链接兼容性设计决策，不同于主题隔离（内容组织）、零依赖（运行时约束）或多平台可移植性（分发策略）。它解决的是单一知识制品如何在异构查看环境中保持可导航性的具体问题——Obsidian 需要 wikilink 支持图谱视图，非 Obsidian 工具需要标准 markdown link。这一设计在现有卡片中未被独立论述。
