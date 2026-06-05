---
schema: justification_journal.v1
card: ../cards/edge-invalidation-mechanism.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-zep/agent_source_bundle.txt`
源证据：
- Section 2.2.3 — "A key differentiating feature of Graphiti compared to other knowledge graph engines is its capacity to manage dynamic information updates through temporal extraction and edge invalidation processes."
- Section 2.2.3 — "Graphiti consistently prioritizes new information when determining edge invalidation."
范围论证：边失效机制是 Graphiti 处理动态、演变知识的核心手段，与双时间线模型配合但逻辑独立——前者是时间标记的数据模型，后者是基于 LLM 的矛盾检测与失效流程。已有卡 contradiction-state-machine 关注矛盾状态机的一般概念，本卡聚焦 Graphiti 特定的边失效实现。
