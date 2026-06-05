---
schema: justification_journal.v1
card: ../cards/entity-resolution-hybrid-search.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt`
源证据：
- Section 2.2.1 — "the system embeds each entity name into a 1024-dimensional vector space... also performs a separate full-text search"
- Section 2.2.1 — "We chose this approach over LLM-generated database queries to ensure consistent schema formats and reduce the potential for hallucinations."
范围论证：实体消解流程是 Graphiti 知识图谱构建中的关键工程步骤，包含多个技术决策（混合搜索、LLM 判定、预定义 Cypher 查询）。它独立于三层架构的宏观设计，是一个可操作层面的具体机制。
