---
id: llm-wiki-gap-report-iterative
title: Gap Report 与迭代研究
status: accepted
card_type: mechanism
tags:
- llm-wiki
- gap-report
- iterative-research
- follow-up
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- llm-wiki-net
evidence_basis: documentation
justification: ../justification/llm-wiki-gap-report-iterative.md
canonical_concept: gap-report-iterative-research
aliases:
- gap report
- gap drilling
- iterative research
- 知识空白报告
summary: gap-report-iterative-research 机制：每轮研究后展示已覆盖内容和缺失内容及建议后续，2+ gaps 时提供交互选择并行关闭，--min-time
  支持多轮 gap drilling 每轮钻入前轮发现的空白
related:
- llm-wiki-plan-mode-research
- llm-wiki-thesis-mode
- multi-agent-parallel-research-pipeline
---
llm-wiki 的研究流程内置了 gap report 迭代机制。每轮研究结束后，系统展示已覆盖内容、仍缺失内容和建议的后续方向。[^src-1]

当存在 2 个或更多 gap 时，用户被提供交互选择（输入编号、"all"或"skip"），选中的 gap 作为另一批并行任务启动。[^src-2]

配合 --min-time（如 2h）使用时，研究自动进行多轮，每轮钻入上轮发现的空白，形成渐进式知识积累。[^src-3]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Research Workflow Stage 4" P189 -- "After each round, you see what's covered, what's still missing, and suggested follow-ups."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Research Workflow Stage 4" P189-193 -- "If 2+ gaps remain, you're offered to close them in parallel"
[^src-3]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Plan Mode" P194 -- "Multi-round research: Add --min-time 2h to keep researching in rounds, each drilling into gaps the previous round found."
