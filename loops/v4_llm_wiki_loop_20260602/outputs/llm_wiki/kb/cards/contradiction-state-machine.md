---
id: contradiction-state-machine
title: 矛盾状态机
status: accepted
card_type: mechanism
tags: [llm-wiki, contradiction, state-machine, maintenance, quality]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
justification: ../justification/contradiction-state-machine.md
canonical_concept: contradiction-state-machine
aliases: [矛盾状态机, contradiction tracking, 矛盾检测与解决, contradiction state machine]
summary: >-
  contradiction-state-machine（矛盾状态机 / contradiction tracking / 矛盾检测与解决）
  是 LLM Wiki 插件中跟踪知识矛盾的状态机制：detected -> review_ok -> resolved（AI 修复）
  或 detected -> pending_fix（手动修复），矛盾在多源融合时带归因保留而非自动消除
related:
  - lint-operation
  - source-faithfulness-risk
---

Karpathy LLM Wiki 插件实现了一套**矛盾状态机**（Contradiction State Machine），用于系统性地跟踪和处理 Wiki 中的知识矛盾[^src-1]。

**状态转换路径**有两条[^src-1]：
- **AI 修复路径**：`detected` -> `review_ok` -> `resolved` -- 矛盾被检测到后，经人类确认可由 AI 修复，标记为已解决
- **手动修复路径**：`detected` -> `pending_fix` -- 矛盾被检测到后，标记为等待人工手动处理

**矛盾的来源**：当多个资料对同一知识点存在冲突时，插件的智能知识融合机制不会自动消除矛盾，而是**保留矛盾并附带归因**[^src-2]。这意味着系统承认矛盾的合理性——不同来源可能确实对同一问题持不同立场。

**矛盾检测**作为巡检（Lint）操作的一部分被执行，在健康扫描报告中与重复页、死链、空页、孤立页、缺失别名并列呈现[^src-3]。代码层面，矛盾检测有独立模块 `contradictions.ts` 负责[^src-4]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/obsidian-community-plugin/text.txt` -- "Maintenance" L284 -- "Contradiction State Machine — detected → review_ok → resolved (AI fix) or detected → pending_fix (manual)"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/obsidian-community-plugin/text.txt` -- "Knowledge Quality" L267 -- "Smart Knowledge Fusion — Multi-source updates merge new info without redundancy, contradictions preserved with attribution, reviewed: true pages protected from overwrite"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/obsidian-community-plugin/text.txt` -- "Maintenance" L274 -- "Lint Health Scan — Detects duplicates, dead links, empty pages, orphans, missing aliases, and contradictions in one comprehensive report"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/obsidian-community-plugin/text.txt` -- "Codebase" L381 -- "contradictions.ts # Contradiction detection"
