---
id: contradiction-state-machine
title: 矛盾检测状态机
status: draft
card_type: mechanism
tags: [llm-wiki, contradiction, state-machine, knowledge-integrity]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
evidence_basis: documentation
justification: ../justification/contradiction-state-machine.md
canonical_concept: contradiction-state-machine
aliases: [contradiction detection, 矛盾检测, contradiction state machine]
summary: >-
  矛盾状态机：detected → review_ok → resolved（AI修复），或 detected → pending_fix（手动处理）。
  多源更新时保留矛盾并附带归因（attribution）。标记 reviewed:true 的页面受保护不被覆盖。
  Lint 扫描可检测矛盾。
related: [smart-knowledge-fusion, karpathy-llm-wiki-concept]
---

该插件实现矛盾检测状态机，处理多源知识冲突：[^src-1]

状态转换路径：
- detected → review_ok → resolved（AI 自动修复）
- detected → pending_fix（等待手动处理）

多源更新合并新信息时，矛盾被保留并附带归因（attribution），不会静默覆盖。用户可在 frontmatter 中设置 `reviewed: true` 保护页面不被后续 ingest 覆盖。[^src-2] [^card-1]

[^src-1]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Features" P1 -- "Contradiction State Machine — detected → review_ok → resolved(AI fix) or detected → pending_fix(manual)"
[^src-2]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Features" P1 -- "Smart Knowledge Fusion — Multi-source updates merge new info without redundancy, contradictions preserved with attribution, reviewed: true pages protected from overwrite"
[^card-1]: 参见 [[smart-knowledge-fusion]] 了解多源合并机制
