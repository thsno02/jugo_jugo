---
id: dual-retrieval-entity-semantic
title: 双路检索策略（实体锚定 + 语义三元组）
status: accepted
card_type: mechanism
tags: [knowledge_graph, retrieval, entity_resolution, semantic_search, Mem0]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0]
justification: ../justification/dual-retrieval-entity-semantic.md
canonical_concept: dual-retrieval-entity-semantic
aliases: [双路检索, dual retrieval strategy, entity-centric + semantic triplet retrieval]
summary: >-
  dual-retrieval-entity-semantic（双路检索 / entity-centric + semantic triplet retrieval）Mem0^g 实现两种互补检索路径：实体锚定法先识别查询中的实体再探索其关系子图；语义三元组法将整个查询编码为向量与所有关系三元组做细粒度相似度匹配，前者适合定向实体查询后者适合宽泛概念查询
related: [graph-memory-temporal-advantage, index-based-navigation, cross-tool-entity-resolution]
---

Mem0^g 的记忆检索实现了双路策略，以应对不同类型查询的需求 [^src-1]：

**实体锚定法（Entity-centric method）**：首先识别查询中的关键实体，然后利用语义相似度在知识图谱中定位对应节点。以这些锚定节点为起点，系统性地探索其入边和出边关系，构建一个包含相关上下文信息的综合子图 [^src-2]。

**语义三元组法（Semantic triplet approach）**：采用更全局性的视角，将整个查询编码为稠密嵌入向量，然后与知识图谱中每个关系三元组的文本编码进行匹配。系统计算查询与所有可用三元组之间的细粒度相似度分数，仅返回超过可配置相关性阈值的结果，并按相似度降序排列 [^src-3]。

这种双路机制的设计意图是：实体锚定法擅长处理"针对性的实体聚焦问题"，而语义三元组法能有效处理"更宽泛的概念性查询" [^src-4]。两种路径互补而非替代，使系统能够同时处理精确检索和模糊检索的需求。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/proposed_work.tex -- "The memory retrieval functionality in Mem0^g implements a dual-approach strategy for optimal information access."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/proposed_work.tex -- "The entity-centric method first identifies key entities within a query, then leverages semantic similarity to locate corresponding nodes in the knowledge graph. It systematically explores both incoming and outgoing relationships from these anchor nodes"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/proposed_work.tex -- "the semantic triplet approach takes a more holistic view by encoding the entire query as a dense embedding vector. This query representation is then matched against textual encodings of each relationship triplet in the knowledge graph."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/proposed_work.tex -- "This dual retrieval mechanism enables Mem0^g to handle both targeted entity-focused questions and broader conceptual queries with equal effectiveness."
