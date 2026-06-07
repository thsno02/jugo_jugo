---
schema: justification_journal.v1
card: ../cards/fuzzy-intent-router.md
created_time: 2026-06-08T10:00:00+08:00
---

## creation | 2026-06-08T10:00:00+08:00

生成方式：Mode A extraction from repo source bundle
来源：`data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt`
源证据：
- FILE: claude-plugin/commands/wiki.md — "If $ARGUMENTS is freeform text... Detect their intent and route to the right subcommand" + 完整 20 级优先级表
- FILE: claude-plugin/commands/wiki.md — "Confidence routing: High confidence... route directly... Low confidence... present top 2-3 matching options"
- FILE: claude-plugin/commands/wiki.md — "Never guess when ambiguous. A quick menu is faster than undoing the wrong action."
- FILE: claude-plugin/commands/research.md — "Input Detection: Topic vs Question vs Thesis"
范围论证：模糊意图路由器是 llm-wiki 的用户交互入口设计，包含 20 级优先级匹配、置信度分流策略和输入三分法。这与并行研究（如何执行研究）和 Hub 解析（如何找到数据）是不同层面的关注点。现有卡片均未覆盖自然语言命令路由这一用户体验层面的机制。
