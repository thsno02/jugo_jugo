---
id: zep-temporal-knowledge-graph-architecture
title: Zep 时序知识图谱架构总览
status: draft
card_type: system-architecture
tags: [knowledge-graph, agent-memory, temporal-reasoning, RAG]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
evidence_basis: experimental_paper
justification: ../justification/zep-temporal-knowledge-graph-architecture.md
canonical_concept: zep-temporal-knowledge-graph-architecture
aliases: [Zep, Zep memory layer, Zep AI memory service]
summary: >-
  Zep 是一种基于时序知识图谱的 AI Agent 记忆层服务，核心引擎为 Graphiti。其知识图谱
  G=(N,E,phi) 包含三层子图：episode subgraph（原始消息）、semantic entity subgraph
  （提取的实体与事实）、community subgraph（聚类摘要）。采用 bi-temporal model 双时间线
  追踪事实的现实有效期（T）与系统记录期（T'）。在 DMR benchmark 上 94.8% vs MemGPT 93.4%，
  在 LongMemEval 上准确率提升最高 18.5% 且延迟降低约 90%。
related: []
---

Zep 是由 Zep AI 提出的 AI Agent 记忆层服务，旨在解决传统 RAG 仅适用于静态文档、不适合动态对话记忆的局限。其核心由 Graphiti 时序知识图谱引擎驱动。[^src-1]

知识图谱 G=(N, E, phi) 由三个层次化子图组成：Episode 子图存储非损失性原始数据，Semantic Entity 子图存储提取和消解后的实体与关系（facts），Community 子图通过社区检测提供高层摘要。这种分层设计类比人类记忆中 episodic memory 与 semantic memory 的区分。[^src-2]

系统实现了 bi-temporal model：时间线 T 追踪事实在现实世界中的有效期，时间线 T' 追踪系统的数据摄入事务。这使得图谱能同时表达"事实何时为真"和"系统何时知道该事实"。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Abstract" P1 -- "We introduce Zep, a novel memory layer service for AI agents that outperforms the current state-of-the-art system, MemGPT"
[^src-2]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Knowledge Graph Construction" P1 -- "memory is powered by a temporally-aware dynamic knowledge graph G=(N, E, phi)...comprises three hierarchical tiers of subgraphs"
[^src-3]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Episodes" P2 -- "Zep implements a bi-temporal model, where timeline T represents the chronological ordering of events, and timeline T' represents the transactional order"
