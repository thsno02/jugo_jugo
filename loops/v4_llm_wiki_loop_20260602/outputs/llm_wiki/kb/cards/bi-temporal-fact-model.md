---
id: bi-temporal-fact-model
title: 双时间线事实建模
status: accepted
card_type: mechanism
tags: [temporal_modeling, knowledge_graph, bi-temporal, Graphiti, agent_memory]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
justification: ../justification/bi-temporal-fact-model.md
canonical_concept: bi-temporal-fact-model
aliases: [双时间线模型, bi-temporal model, 事件时间线与摄入时间线]
summary: >-
  bi-temporal-fact-model（双时间线模型, bi-temporal model）Graphiti 对每条 edge/fact 维护两条时间线：事件时间线 T（事实何时为真）和事务时间线 T'（数据何时被摄入系统），通过四个时间戳实现动态对话数据的时序建模
related:
  - temporal-knowledge-graph-three-tier
  - edge-invalidation-mechanism
---

Graphiti 引入了一种双时间线（bi-temporal）建模方法，这在基于 LLM 的知识图谱构建中被论文作者认为是一项新进展 [^src-1]。

**时间线 T（事件时间线）**：表示事件的时间顺序——事实在现实世界中何时为真。每条消息附带参考时间戳 t_ref，使系统能够准确提取消息中的相对或部分日期（如"下周四"、"两周后"、"去年夏天"）[^src-2]。

**时间线 T'（事务时间线）**：表示 Zep 数据摄入的事务顺序，服务于传统的数据库审计目的 [^src-3]。

每条语义边（fact）上存储四个时间戳 [^src-4]：
- t'_created / t'_expired（属于 T'）：记录 fact 在系统中创建或失效的时间
- t_valid / t_invalid（属于 T）：追踪 fact 在现实世界中为真的时间范围

这种双时间线设计使知识图谱能够表达一个复杂、不断演变的世界 [^src-5]，同时为后续的 edge invalidation 机制提供了基础。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.1 (Episodes) -- "This bi-temporal approach represents a novel advancement in LLM-based knowledge graph construction and underlies much of Zep's unique capabilities compared to previous graph-based RAG proposals."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.1 -- "This temporal information enables Zep to accurately identify and extract relative or partial dates mentioned in the message content (e.g., 'next Thursday,' 'in two weeks,' or 'last summer')."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.1 -- "timeline T' represents the transactional order of Zep's data ingestion"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.3 (Temporal Extraction and Edge Invalidation) -- "the system tracks four timestamps: t'_created and t'_expired in T' monitor when facts are created or invalidated in the system, while t_valid and t_invalid in T track the temporal range during which facts held true"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 1 (Introduction) -- "The Graphiti KG engine dynamically updates the knowledge graph with new information in a non-lossy manner, maintaining a timeline of facts and relationships, including their periods of validity."
