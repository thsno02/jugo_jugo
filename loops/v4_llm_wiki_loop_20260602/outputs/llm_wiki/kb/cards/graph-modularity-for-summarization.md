---
id: graph-modularity-for-summarization
title: 图模块性作为层级摘要的结构基础
status: accepted
card_type: concept
tags: [modularity, graph-structure, community-detection, summarization, graphrag]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
justification: ../justification/graph-modularity-for-summarization.md
canonical_concept: graph-modularity-for-summarization
aliases: [graph modularity, 图模块性, 图的社区可分性]
summary: >-
  graph-modularity-for-summarization（graph modularity / 图模块性）GraphRAG 利用知识图谱固有的模块性——将图分割为嵌套模块化社区的能力——作为层级摘要的结构基础，这是此前图+RAG 方法未曾探索的图属性
related: [dynamic-community-detection, graphrag-community-hierarchy, graphrag-global-sensemaking, memory-gravity]
---

GraphRAG 与此前图+RAG 方法的关键区别在于它聚焦的图属性。此前的方法或者直接在 prompt 中使用子图/图元素/图结构属性 [^src-1]，或者用知识图谱作为事实基础 [^src-2]，或者用 LLM 代理在查询时动态遍历图 [^src-3]。

GraphRAG 则聚焦于一个此前在这一场景中未被探索的图属性：图固有的模块性（modularity）——即将图分割为紧密连接节点的嵌套模块化社区的能力 [^src-4]。

模块性是网络科学中的经典概念，指网络中节点倾向于形成内部连接紧密、外部连接稀疏的群组的特性。GraphRAG 利用这一特性，通过社区检测算法（如 Leiden、Louvain）自动发现实体知识图谱中的主题聚类，然后递归地利用 LLM 创建跨越社区层级的越来越全局的摘要 [^src-5]。

这意味着图的结构本身提供了一种自然的主题分组方式，无需人工分类或预定义的层次结构。图的模块性越强，社区检测产生的分组就越有意义，社区摘要对全局 sensemaking 的支持就越好。

GraphRAG 利用此模块性的具体机制——Leiden 算法递归检测层级社区并自底向上生成摘要——见社区层级卡[^card-1]。Graphiti 则用标签传播实现同一模块性属性的动态增量检测[^card-2]。值得注意的是，模块性是群组层的图属性，与节点层的中心性属性服务于不同的知识管理目的[^dist-1]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 2.2 (graph_rag.tex) -- "Some techniques use subgraphs, elements of the graph, or properties of the graph structure directly in the prompt"
[^src-2]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 2.2 (graph_rag.tex) -- "or as factual grounding for generated outputs"
[^src-3]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 2.2 (graph_rag.tex) -- "use the knowledge graph to enhance retrieval, where at query time an LLM-based agent dynamically traverses a graph"
[^src-4]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 2.2 (graph_rag.tex) -- "GraphRAG contrasts with these approaches by focusing on a previously unexplored quality of graphs in this context: their inherent modularity and the ability to partition graphs into nested modular communities of closely related nodes"
[^src-5]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 2.2 (graph_rag.tex) -- "Specifically, GraphRAG recursively creates increasingly global summaries by using the LLM to create summaries spanning this community hierarchy."
[^card-1]: [GraphRAG 层级社区检测与摘要机制](graphrag-community-hierarchy.md) -- 本卡聚焦图模块性这一概念属性，该卡详述利用此属性的具体机制——Leiden 算法递归检测层级社区并自底向上生成摘要
[^card-2]: [标签传播动态社区检测](dynamic-community-detection.md) -- 本卡论述图模块性作为摘要的结构基础，该卡展示 Graphiti 如何用标签传播实现同一模块性属性的动态增量检测
[^dist-1]: [记忆引力](memory-gravity.md) -- 本卡利用图的模块性进行主题聚类与摘要，该卡利用图的中心性进行记忆保留决策；区分点在于模块性是群组层属性（节点如何聚为社区），中心性是节点层属性（单节点的结构承重），两者代表图结构服务知识管理的不同粒度
