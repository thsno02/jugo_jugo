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
related: [bi-temporal-fact-model, contradiction-as-asset, minority-pressure-promotion, temporal-event-graph-grounding, temporal-knowledge-graph-three-tier]
---

Graphiti 的一项关键区分特性是其通过时间提取与边失效过程管理动态信息更新的能力 [^src-1]。

**矛盾检测**：当新边（fact）被引入时，系统使用 LLM 将新边与语义相关的已有边进行比较，以识别潜在矛盾 [^src-2]。

**失效处理**：当系统识别出时间上重叠的矛盾时，将受影响边的 t_invalid 设置为导致失效的新边的 t_valid。沿着事务时间线 T'，Graphiti 在确定边失效时始终优先采纳新信息 [^src-3]。

**非破坏性更新**：旧的边并不被删除，而是通过 t_invalid 标记为失效。这使得知识图谱既维护当前关系状态，也保留关系随时间演变的历史记录 [^src-4]。

这种机制使得数据可以随着对话演进而动态添加到 Graphiti 中，同时不丢失历史信息。这一失效流程直接操作双时间线事实模型中的时间戳字段（尤其是 t_invalid 和 t_valid），是双时间线建模在矛盾解决场景中的具体应用[^card-2]。

与 LLM Wiki 中「矛盾即资产」的保留策略不同，边失效机制对矛盾采取不对称处理：始终优先新信息，将旧边标记为失效[^dist-1]。伴侣记忆框架的少数派压力提升机制则选择了第三条路径：既不对等保留，也不立即失效，而是让少数派假设在缓冲区跨周期积累压力，达到阈值后才能挑战主导解释[^dist-2]。

LoCoMo 的时序事件图从另一个方向处理类似的时序演变问题：它通过构建含日期和因果连接的事件图来锚定对话叙事，而 Graphiti 的边失效机制则侧重于已有知识的动态更新与矛盾解决[^card-1]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.3 (Temporal Extraction and Edge Invalidation) -- "A key differentiating feature of Graphiti compared to other knowledge graph engines is its capacity to manage dynamic information updates through temporal extraction and edge invalidation processes."
[^src-2]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.3 -- "The system employs an LLM to compare new edges against semantically related existing edges to identify potential contradictions."
[^src-3]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.3 -- "When the system identifies temporally overlapping contradictions, it invalidates the affected edges by setting their t_invalid to the t_valid of the invalidating edge. Following the transactional timeline T', Graphiti consistently prioritizes new information when determining edge invalidation."
[^src-4]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.3 -- "This comprehensive approach enables the dynamic addition of data to Graphiti as conversations evolve, while maintaining both current relationship states and historical records of relationship evolution over time."
[^card-1]: [时序事件图作为对话锚定机制](temporal-event-graph-grounding.md) -- LoCoMo 的时序事件图通过因果连接锚定对话叙事，与 Graphiti 的边失效机制互补：前者构建时序结构，后者管理时序知识的动态更新与矛盾解决
[^card-2]: [双时间线事实建模](bi-temporal-fact-model.md) -- 本卡聚焦基于时间戳的矛盾检测与失效处理流程，该卡聚焦底层四时间戳数据模型，边失效是双时间线建模在矛盾解决中的具体应用
[^dist-1]: [矛盾作为知识资产](contradiction-as-asset.md) -- 本卡通过边失效优先采纳新信息解决矛盾，该卡主张矛盾双方对等保留，区分点在于新旧信息是否平等对待
[^dist-2]: [少数派压力提升机制](minority-pressure-promotion.md) -- 本卡通过即时边失效（新信息立即胜出）解决矛盾，该卡通过多周期缓冲区压力积累解决矛盾，区分点在于矛盾解决的时间尺度：即时 vs. 跨周期积累
