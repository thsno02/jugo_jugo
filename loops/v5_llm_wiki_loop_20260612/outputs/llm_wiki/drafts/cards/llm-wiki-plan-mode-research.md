---
id: llm-wiki-plan-mode-research
title: Plan 模式并行路径研究
status: draft
card_type: mechanism
tags: [llm-wiki, plan-mode, parallel-paths, research-decomposition]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
evidence_basis: documentation
justification: ../justification/llm-wiki-plan-mode-research.md
canonical_concept: plan-mode-research
aliases: [plan mode, --plan, research plan decomposition, 计划模式]
summary: >-
  plan-mode-research 模式：--plan 将广泛主题分解为独立路径并行运行，每路径独立 5-agent 群，各路径并行摄取写唯一文件，单次编译跨路径合成，可与 --deep --min-time --new-topic 组合
related: [llm-wiki-parallel-multi-agent-research, llm-wiki-gap-report-iterative]
---

对于广泛主题，--plan 标志将研究分解为独立路径并全部并行运行。Agent 生成研究计划（列出路径及各路径关注点），用户确认后启动。[^src-1]

每条路径运行自己的 5-agent 群（使用 --deep 则为 8 agents/路径）。各路径并行摄取源（每路径写唯一文件避免冲突），完成后单次编译 pass 看到所有源，进行跨路径合成。[^src-2]

可与其他标志组合：--plan --deep（8 agents/路径）、--plan --min-time 2h（多次计划-分发-编译循环）、--plan --new-topic（创建 wiki 同时研究）。[^src-3]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Plan Mode" P236 -- "For broad topics, --plan decomposes your research into independent paths and runs them all in parallel"
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Plan Mode" P246 -- "Each path runs its own 5-agent swarm. Sources are ingested in parallel (each path writes unique files), then a single compilation pass sees all sources at once for cross-path synthesis."
[^src-3]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Plan Mode" P253-255 -- "--plan --deep, --plan --min-time 2h, --plan --new-topic"
