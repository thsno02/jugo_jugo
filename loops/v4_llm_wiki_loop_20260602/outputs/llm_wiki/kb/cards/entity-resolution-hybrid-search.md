---
id: entity-resolution-hybrid-search
title: 混合搜索实体消解流程
status: accepted
card_type: mechanism
tags: [entity_resolution, knowledge_graph, deduplication, embedding, Graphiti]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
justification: ../justification/entity-resolution-hybrid-search.md
canonical_concept: entity-resolution-hybrid-search
aliases: [混合搜索实体消解, entity resolution via hybrid search, 实体去重管线]
summary: >-
  entity-resolution-hybrid-search（混合搜索实体消解, entity resolution pipeline）Graphiti 的实体消解分三步：1024维向量嵌入余弦相似度搜索 + 全文搜索找候选、LLM 判定是否重复、预定义 Cypher 查询写入图（避免 LLM 生成查询的幻觉风险）
related:
  - temporal-knowledge-graph-three-tier
  - hybrid-triple-search-complementarity
---

Graphiti 对从 episode 中提取的实体进行多步消解以避免重复 [^src-1]：

**实体提取**：处理当前消息和最近 n=4 条消息（两轮完整对话）以提供命名实体识别的上下文。说话者自动作为实体提取。系统使用受 reflexion 启发的反思技术来减少幻觉并增强提取覆盖率 [^src-2]。

**候选检索**：将每个实体名称嵌入到 1024 维向量空间中，通过余弦相似度搜索在已有图实体节点中检索相似节点。同时对已有实体名称和摘要执行全文搜索以识别额外候选节点 [^src-3]。

**LLM 消解**：将候选节点和 episode 上下文一起传入 LLM，通过实体消解提示判断是否为重复实体。若识别为重复，则生成更新后的名称和摘要 [^src-4]。

**图写入**：使用预定义的 Cypher 查询（而非 LLM 生成的数据库查询）将数据写入知识图谱，以确保一致的 schema 格式并减少幻觉风险 [^src-5]。

事实（fact/edge）的去重采用类似流程，但搜索空间被限制在相同实体对之间的已有边上，既防止不同实体间的相似边被错误合并，也显著降低了计算复杂度 [^src-6]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.1 (Entities) -- "Following initial entity extraction, we employ a reflection technique"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.1 -- "the system processes both the current message content and the last n messages to provide context for named entity recognition. For this paper... n=4"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.1 -- "the system embeds each entity name into a 1024-dimensional vector space. This embedding enables the retrieval of similar nodes through cosine similarity search... The system also performs a separate full-text search on existing entity names and summaries"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.1 -- "These candidate nodes, together with the episode context, are then processed through an LLM using our entity resolution prompt. When the system identifies a duplicate entity, it generates an updated name and summary."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.1 -- "We chose this approach over LLM-generated database queries to ensure consistent schema formats and reduce the potential for hallucinations."
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.2 (Facts) -- "The hybrid search for relevant edges is constrained to edges existing between the same entity pairs as the proposed new edge."
