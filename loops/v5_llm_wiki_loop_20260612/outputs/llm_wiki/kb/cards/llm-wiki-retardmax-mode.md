---
id: llm-wiki-retardmax-mode
title: Retardmax 快速出稿模式
status: accepted
card_type: mechanism
tags:
- llm-wiki
- retardmax
- rapid-research
- aggressive-ingestion
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- llm-wiki-net
evidence_basis: documentation
justification: ../justification/llm-wiki-retardmax-mode.md
canonical_concept: retardmax-mode
aliases:
- retardmax
- retardmaxxing
- --retardmax
- 快速出稿模式
summary: retardmax-mode：灵感来自 Elisha Long 的 retardmaxxing 哲学（先行动后思考），十个并行 agents 跳过规划撒最广的网，激进摄取快速编译后续再
  lint，可用于 research 和 output 命令
related:
- multi-agent-parallel-research-pipeline
---

Retardmax 是 llm-wiki 的一种快速出稿研究模式，灵感来自 Elisha Long 的 retardmaxxing 哲学——先行动后思考（act first, think later）。[^src-1]

该模式部署十个并行 agents，跳过规划阶段，撒最广的搜索网，激进摄取，快速编译，后续再通过 lint 清理。可用于 `/wiki:research --retardmax` 和 `/wiki:output --retardmax`。[^src-2]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Retardmax" P303 -- "A research mode inspired by Elisha Long's retardmaxxing philosophy — act first, think later."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Retardmax" P303 -- "Ten parallel agents, skip planning, cast the widest net, ingest aggressively, compile fast, lint later."
