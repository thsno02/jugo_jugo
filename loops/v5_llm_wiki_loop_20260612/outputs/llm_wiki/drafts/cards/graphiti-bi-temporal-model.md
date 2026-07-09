---
id: graphiti-bi-temporal-model
title: Graphiti 双时间线模型
status: draft
card_type: mechanism
tags: [temporal-modeling, knowledge-graph, bi-temporal, agent-memory]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
evidence_basis: experimental_paper
justification: ../justification/graphiti-bi-temporal-model.md
canonical_concept: graphiti-bi-temporal-model
aliases: [bi-temporal model, dual timeline, 双时间线, T and T' timelines]
summary: >-
  Graphiti 实现 bi-temporal model：timeline T 为事件发生的实际时间顺序（chronological），
  timeline T' 为系统摄入数据的事务顺序（transactional）。每条 edge 存储四个时间戳：
  t'_created/t'_expired (T') 和 t_valid/t_invalid (T)。T' 用于数据库审计，T 为对话数据
  的动态演化建模。论文称此为 LLM-based KG construction 的新颖贡献。
related: [zep-temporal-knowledge-graph-architecture, graphiti-edge-invalidation]
---

Graphiti 的双时间线（bi-temporal）模型区分两个时间维度：[^src-1]

- **Timeline T（chronological）**：事件在现实世界中实际发生的时间顺序。表示事实何时为真（t_valid）以及何时不再为真（t_invalid）。
- **Timeline T'（transactional）**：数据被系统摄入和处理的事务时间顺序。记录事实何时被创建在系统中（t'_created）以及何时被系统标记为过期（t'_expired）。

这种双时间线设计使得知识图谱不仅知道"Alan Turing was born on June 23, 1912"中事实成立的时间点，也能正确处理"I started my new job two weeks ago"这类相对时间引用（基于 reference timestamp 计算）。[^src-2]

论文将此双时间线方法称为 LLM-based 知识图谱构建中的新颖贡献，是 Zep 相对于先前 graph-based RAG 提案的独特能力基础。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Episodes" P2 -- "Zep implements a bi-temporal model...This bi-temporal approach represents a novel advancement in LLM-based knowledge graph construction"
[^src-2]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Temporal Extraction and Edge Invalidation" P1 -- "enables accurate extraction and datetime representation of both absolute timestamps...and relative timestamps"
[^card-1]: [zep-temporal-knowledge-graph-architecture] -- 双时间线是 Zep 架构的核心时间建模基础
