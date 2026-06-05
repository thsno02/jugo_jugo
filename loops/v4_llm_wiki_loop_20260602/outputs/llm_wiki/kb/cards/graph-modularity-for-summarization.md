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
related: [graphrag-community-hierarchy, graphrag-global-sensemaking]
---

GraphRAG 与此前图+RAG 方法的关键区别在于它聚焦的图属性。此前的方法或者直接在 prompt 中使用子图/图元素/图结构属性 [^src-1]，或者用知识图谱作为事实基础 [^src-2]，或者用 LLM 代理在查询时动态遍历图 [^src-3]。

GraphRAG 则聚焦于一个此前在这一场景中未被探索的图属性：图固有的模块性（modularity）——即将图分割为紧密连接节点的嵌套模块化社区的能力 [^src-4]。

模块性是网络科学中的经典概念，指网络中节点倾向于形成内部连接紧密、外部连接稀疏的群组的特性。GraphRAG 利用这一特性，通过社区检测算法（如 Leiden、Louvain）自动发现实体知识图谱中的主题聚类，然后递归地利用 LLM 创建跨越社区层级的越来越全局的摘要 [^src-5]。

这意味着图的结构本身提供了一种自然的主题分组方式，无需人工分类或预定义的层次结构。图的模块性越强，社区检测产生的分组就越有意义，社区摘要对全局 sensemaking 的支持就越好。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 2.2 (graph_rag.tex) -- "Some techniques use subgraphs, elements of the graph, or properties of the graph structure directly in the prompt"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 2.2 (graph_rag.tex) -- "or as factual grounding for generated outputs"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 2.2 (graph_rag.tex) -- "use the knowledge graph to enhance retrieval, where at query time an LLM-based agent dynamically traverses a graph"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 2.2 (graph_rag.tex) -- "GraphRAG contrasts with these approaches by focusing on a previously unexplored quality of graphs in this context: their inherent modularity and the ability to partition graphs into nested modular communities of closely related nodes"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 2.2 (graph_rag.tex) -- "Specifically, GraphRAG recursively creates increasingly global summaries by using the LLM to create summaries spanning this community hierarchy."
