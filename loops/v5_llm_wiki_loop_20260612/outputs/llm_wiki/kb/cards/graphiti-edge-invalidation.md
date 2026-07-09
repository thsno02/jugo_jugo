---
id: graphiti-edge-invalidation
title: Graphiti 边失效与动态知识更新
status: accepted
card_type: mechanism
tags:
- knowledge-graph
- temporal-reasoning
- contradiction-detection
- dynamic-update
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-zep
evidence_basis: experimental_paper
justification: ../justification/graphiti-edge-invalidation.md
canonical_concept: graphiti-edge-invalidation
aliases:
- edge invalidation
- temporal extraction
- fact invalidation
- 边失效机制
summary: Graphiti 通过 LLM 对新边与已有语义相关边进行矛盾检测来实现 edge invalidation。 当发现时间重叠的矛盾时，旧边的 t_invalid 被设为新边的 t_valid。系统按 T' 时间线 始终优先新信息。此机制使知识图谱能在对话演化时动态更新，同时保留历史关系记录， 实现非损失性的事实更替。
related:
- graphiti-bi-temporal-model
- graphiti-entity-fact-extraction
---

Graphiti 的 edge invalidation 机制是其处理动态信息更新的关键区分特性。[^src-1]

当新边被加入图谱时，系统使用 LLM 将新边与语义相关的已有边进行比较，识别潜在矛盾。若系统发现时间上存在重叠的矛盾关系，则将被影响的旧边的 t_invalid 设置为新（invalidating）边的 t_valid。[^src-1]

遵循事务时间线 T' 的逻辑，Graphiti 在判断边失效时始终优先新信息——即后摄入的信息在矛盾时覆盖先摄入的信息。[^src-1]

这种方法使得数据可以随对话演化动态添加到 Graphiti 中，同时维护当前关系状态和关系历史演化记录。旧事实不被删除，仅被标记为失效，保留了完整的时间线供审计或历史查询。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Temporal Extraction and Edge Invalidation" P2 -- "The system employs an LLM to compare new edges against semantically related existing edges to identify potential contradictions"
[^src-2]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Temporal Extraction and Edge Invalidation" P3 -- "This comprehensive approach enables the dynamic addition of data to Graphiti as conversations evolve, while maintaining both current relationship states and historical records"
[^card-1]: [graphiti-bi-temporal-model] -- edge invalidation 依赖双时间线的四个时间戳
