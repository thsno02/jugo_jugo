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
related: [alias-cross-language-dedup, cross-tool-entity-resolution, wiki-deduplication-fragility]
  - temporal-knowledge-graph-three-tier
  - hybrid-triple-search-complementarity
---

Graphiti 对从 episode 中提取的实体进行多步消解以避免重复 [^src-1]：

**实体提取**：处理当前消息和最近 n=4 条消息（两轮完整对话）以提供命名实体识别的上下文。说话者自动作为实体提取。系统使用受 reflexion 启发的反思技术来减少幻觉并增强提取覆盖率 [^src-2]。

**候选检索**：将每个实体名称嵌入到 1024 维向量空间中，通过余弦相似度搜索在已有图实体节点中检索相似节点。同时对已有实体名称和摘要执行全文搜索以识别额外候选节点 [^src-3]。

**LLM 消解**：将候选节点和 episode 上下文一起传入 LLM，通过实体消解提示判断是否为重复实体。若识别为重复，则生成更新后的名称和摘要 [^src-4]。

**图写入**：使用预定义的 Cypher 查询（而非 LLM 生成的数据库查询）将数据写入知识图谱，以确保一致的 schema 格式并减少幻觉风险 [^src-5]。

事实（fact/edge）的去重采用类似流程，但搜索空间被限制在相同实体对之间的已有边上，既防止不同实体间的相似边被错误合并，也显著降低了计算复杂度 [^src-6]。

与别名精确匹配方案[^card-1]不同，混合检索路径不依赖预定义别名，而是通过嵌入空间的近邻搜索发现语义等价实体。然而，最终裁决仍依赖 LLM，与确定性去重保护机制的诉求之间存在张力[^dist-1]。该管线虽针对单数据源设计，其候选检索思路同样适用于跨工具实体解析场景[^card-2]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.1 (Entities) -- "Following initial entity extraction, we employ a reflection technique"
[^src-2]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.1 -- "the system processes both the current message content and the last n messages to provide context for named entity recognition. For this paper... n=4"
[^src-3]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.1 -- "the system embeds each entity name into a 1024-dimensional vector space. This embedding enables the retrieval of similar nodes through cosine similarity search... The system also performs a separate full-text search on existing entity names and summaries"
[^src-4]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.1 -- "These candidate nodes, together with the episode context, are then processed through an LLM using our entity resolution prompt. When the system identifies a duplicate entity, it generates an updated name and summary."
[^src-5]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.1 -- "We chose this approach over LLM-generated database queries to ensure consistent schema formats and reduce the potential for hallucinations."
[^src-6]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.2.2 (Facts) -- "The hybrid search for relevant edges is constrained to edges existing between the same entity pairs as the proposed new edge."
[^card-1]: [别名系统与跨语言去重](alias-cross-language-dedup.md) -- 本卡依赖向量嵌入+全文搜索做候选检索，该卡依赖别名精确匹配做第一层去重
[^card-2]: [跨工具实体解析](cross-tool-entity-resolution.md) -- 本卡描述单数据源内的实体消解管线，该卡将实体解析范围扩展到跨工具/跨系统
[^dist-1]: [Wiki 去重的脆弱性](wiki-deduplication-fragility.md) -- 本卡的混合检索增强了候选质量但最终仍依赖 LLM 裁决，该卡主张缺乏确定性保护机制时 LLM 去重必然脆弱，区分点在于：统计检索信号是否足以替代确定性规则保护
