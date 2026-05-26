---
schema: draft_card_provenance.v3
draft_card: ../cards/zep-bi-temporal-edges.md
material_id: arxiv-zep
digest_id: digest_arxiv-zep
source_paths:
  - data/raw/arxiv/arxiv-zep/agent_source_bundle.txt
created_time: 2026-05-26T11:05:00+08:00
edited_time: 2026-05-26T11:05:00+08:00
edited_entity: llm
---

## 源证据

- main.tex 行 120：「Zep implements a bi-temporal model, where timeline T represents the chronological ordering of events, and timeline T' represents the transactional order of Zep's data ingestion.」
- main.tex 行 142：「the system tracks four timestamps: $t'_\text{created}$ and $t'_\text{expired} \in T'$ monitor when facts are created or invalidated in the system, while $t_\text{valid}$ and $t_\text{invalid} \in T$ track the temporal range during which facts held true.」
- main.tex 行 144：「When the system identifies temporally overlapping contradictions, it invalidates the affected edges by setting their $t_\text{invalid}$ to the $t_\text{valid}$ of the invalidating edge. Following the transactional timeline $T'$, Graphiti consistently prioritizes new information when determining edge invalidation.」
- main.tex 行 165–179：sample context template 显示 "FACT (Date range: from - to)"，证明时间区间会进入 prompt。
- main.tex 行 137：「The hybrid search for relevant edges is constrained to edges existing between the same entity pairs as the proposed new edge.」——确认失效检测的范围限制。
- main.tex 行 291：「additional development may be needed to improve less capable models' understanding of Zep's temporal data.」

## 卡片范围是否成立

本卡聚焦"双时间线 + 边失效"这一机制，所有四个时间戳、失效如何触发、新边优先级都直接来自 §2.2.3。卡里对 "knowledge-update / temporal-reasoning 可解" 的引申是基于实验结果（§4.3）的一个连接性陈述，不是原文直接断言；如需更稳保守可去掉，但属于合理推论。其他主张（如失效范围限同 entity pair、弱模型 gap）有原文支持。

## 发表门控结果

本轮未运行。

## 备注

- 与 zep-graphiti-three-tier-graph 是兄弟卡，引用相同源材料但不同章节，互不重复。
- v2 若已有 "temporal knowledge graph" 通用卡，应在 comparison 阶段评估边界。
