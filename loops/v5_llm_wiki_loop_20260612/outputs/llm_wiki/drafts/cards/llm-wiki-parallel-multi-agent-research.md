---
id: llm-wiki-parallel-multi-agent-research
title: 并行多 Agent 研究机制
status: superseded
superseded_by: multi-agent-parallel-research-pipeline
card_type: mechanism
tags: [llm-wiki, multi-agent, parallel-research, web-search]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
evidence_basis: documentation
justification: ../justification/llm-wiki-parallel-multi-agent-research.md
canonical_concept: parallel-multi-agent-research
aliases: [parallel agents, multi-agent research, 并行研究, parallel research swarm]
summary: >-
  parallel-multi-agent-research 机制：标准 5 agents / deep 8 / retardmax 10 从学术技术应用新闻反面角度并行搜索，每 agent 2-3 次 web search 加全文获取加质量评分 1-5，可信度去重后摄取，--min-time 支持多轮 gap drilling
related: [llm-wiki-thesis-mode, llm-wiki-plan-mode-research, llm-wiki-gap-report-iterative]
---

llm-wiki 的核心研究能力基于并行多 agent 架构。标准模式部署 5 个 agents，--deep 模式 8 个，--retardmax 模式 10 个，各自从不同角度同时搜索：学术、技术、应用、新闻和反面（contrarian）。[^src-1]

每个 agent 执行 2-3 次 web search，进行全内容获取，并以 1-5 分质量评分。摄取前进行可信度去重（credibility pass）。[^src-2]

使用 --min-time 参数（如 --min-time 2h）可让研究持续多轮运行，每轮钻入前一轮发现的知识空白。[^src-3]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Research" P2 -- "5–10 parallel agents search academic, technical, applied, news, and contrarian angles."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Research Workflow Stage 2" P185 -- "5 agents (8 with --deep, 10 with --retardmax) search simultaneously from different angles — 2-3 web searches each, full-content fetch, quality scoring (1-5). A credibility pass deduplicates before ingestion."
[^src-3]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Research" P27 -- "--min-time 2h keeps going in rounds, drilling into gaps each round finds."
