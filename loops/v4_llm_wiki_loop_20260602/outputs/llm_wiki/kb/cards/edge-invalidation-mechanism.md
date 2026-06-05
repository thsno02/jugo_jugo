---
id: edge-invalidation-mechanism
title: 边失效与动态知识更新机制
status: accepted
card_type: mechanism
tags: [knowledge_graph, temporal_reasoning, contradiction_handling, Graphiti, dynamic_update]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
justification: ../justification/edge-invalidation-mechanism.md
canonical_concept: edge-invalidation-mechanism
aliases: [边失效机制, edge invalidation, 时序边失效, temporal edge invalidation]
summary: >-
  edge-invalidation-mechanism（边失效机制, edge invalidation）Graphiti 通过 LLM 比较新边与已有语义相关边来检测矛盾，当发现时间重叠的矛盾时，将旧边的 t_invalid 设为新边的 t_valid，始终优先采纳新信息
related:
  - bi-temporal-fact-model
  - temporal-knowledge-graph-three-tier
---

Graphiti 的一项关键区分特性是其通过时间提取与边失效过程管理动态信息更新的能力 [^src-1]。

**矛盾检测**：当新边（fact）被引入时，系统使用 LLM 将新边与语义相关的已有边进行比较，以识别潜在矛盾 [^src-2]。

**失效处理**：当系统识别出时间上重叠的矛盾时，将受影响边的 t_invalid 设置为导致失效的新边的 t_valid。沿着事务时间线 T'，Graphiti 在确定边失效时始终优先采纳新信息 [^src-3]。

**非破坏性更新**：旧的边并不被删除，而是通过 t_invalid 标记为失效。这使得知识图谱既维护当前关系状态，也保留关系随时间演变的历史记录 [^src-4]。

这种机制使得数据可以随着对话演进而动态添加到 Graphiti 中，同时不丢失历史信息。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.3 (Temporal Extraction and Edge Invalidation) -- "A key differentiating feature of Graphiti compared to other knowledge graph engines is its capacity to manage dynamic information updates through temporal extraction and edge invalidation processes."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.3 -- "The system employs an LLM to compare new edges against semantically related existing edges to identify potential contradictions."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.3 -- "When the system identifies temporally overlapping contradictions, it invalidates the affected edges by setting their t_invalid to the t_valid of the invalidating edge. Following the transactional timeline T', Graphiti consistently prioritizes new information when determining edge invalidation."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.3 -- "This comprehensive approach enables the dynamic addition of data to Graphiti as conversations evolve, while maintaining both current relationship states and historical records of relationship evolution over time."
