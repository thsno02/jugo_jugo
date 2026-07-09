---
id: zep-dmr-benchmark-results
title: Zep 在 DMR 基准上的实验结果与批评
status: draft
card_type: empirical-finding
tags: [benchmark, DMR, MemGPT, evaluation, agent-memory]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
evidence_basis: experimental_paper
justification: ../justification/zep-dmr-benchmark-results.md
canonical_concept: zep-dmr-benchmark-results
aliases: [Deep Memory Retrieval, DMR benchmark, DMR evaluation]
summary: >-
  Zep 在 DMR benchmark 上达到 94.8%（gpt-4-turbo）/98.2%（gpt-4o-mini），优于 MemGPT
  的 93.4%。但论文同时批评 DMR 的局限：每对话仅 60 条消息可完全放入上下文窗口，仅含
  单轮事实检索问题，措辞模糊，不代表企业用例。Full-context baseline 已达 94.4%/98.0%，
  凸显该基准对记忆系统评估的不充分性。
related: [zep-temporal-knowledge-graph-architecture, zep-longmemeval-results]
---

Zep 在 Deep Memory Retrieval (DMR) 基准上的结果：gpt-4-turbo 下 94.8%（vs MemGPT 93.4%），gpt-4o-mini 下 98.2%（vs full-context baseline 98.0%）。[^src-1]

然而论文对 DMR 基准本身提出了明确批评：[^src-2]

- **规模不足**：每个对话仅含约 60 条消息（5 sessions x 12 messages），完全可以放入当前 LLM 的上下文窗口
- **评估维度单一**：仅包含单轮事实检索问题，无法评估复杂记忆理解能力
- **措辞模糊**：问题引用如"favorite drink to relax with"等概念，但对话中从未如此明确表述
- **代表性差**：不能代表真实企业 LLM Agent 用例

Full-context 方法在 gpt-4-turbo/gpt-4o-mini 上分别达到 94.4%/98.0%，进一步证明该基准对记忆系统评估的不充分。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Deep Memory Retrieval (DMR)" P2 -- "Zep achieved 94.8% accuracy with gpt-4-turbo and 98.2% with gpt-4o-mini"
[^src-2]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Deep Memory Retrieval (DMR)" P3 -- "Our analysis revealed significant weaknesses in the benchmark's design"
[^card-1]: [zep-temporal-knowledge-graph-architecture] -- DMR 是 Zep 系统验证的第一个基准
