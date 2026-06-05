---
id: graphrag-global-sensemaking
title: GraphRAG 全局语义理解方法
status: accepted
card_type: mechanism
tags: [graphrag, rag, sensemaking, knowledge-graph, community-summarization]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
justification: ../justification/graphrag-global-sensemaking.md
canonical_concept: graphrag-global-sensemaking
aliases: [Graph RAG, 图谱RAG, 全局意义建构RAG]
summary: >-
  graphrag-global-sensemaking（Graph RAG / 图谱RAG）通过 LLM 构建实体知识图谱并预生成层级社区摘要，以 map-reduce 方式回答传统向量 RAG 无法处理的全局语义理解（sensemaking）查询
related: [graphrag-community-hierarchy, graphrag-map-reduce-query, sensemaking-vs-retrieval-query]
---

GraphRAG 是一种基于图的 RAG 方法，用于解决传统向量 RAG 在全局问题上的根本失败。传统 RAG 通过向量相似性检索局部相关的文本片段，但面对"这个数据集的主要主题是什么？"之类需要理解整个语料库的查询时，本质上这是一个查询聚焦摘要（QFS）任务，而非显式检索任务 [^src-1]。

GraphRAG 的核心思路是用 LLM 分两阶段构建图索引：首先从源文档中提取实体知识图谱，然后为所有紧密相关实体群预生成社区摘要 [^src-2]。给定一个查询，每个社区摘要被用来生成部分响应，最终所有部分响应再被汇总为返回给用户的最终回答。

GraphRAG 与此前基于图的 RAG 方法的关键区别在于：它聚焦于图固有的模块性（modularity）以及将图分割为嵌套模块化社区的能力 [^src-3]。该方法递归地利用 LLM 创建跨越社区层级的越来越全局的摘要。

在百万 token 规模的数据集上，GraphRAG 在回答全局意义建构（sensemaking）问题时，在全面性和多样性两个维度上均大幅优于传统 RAG 基线 [^src-4]。然而，该管道对实体提取阶段的投毒攻击高度敏感——仅需修改源文本中极少量词语即可显著扭曲知识图谱并误导下游推理[^card-graphrag-knowledge-poisoning-attack]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Abstract (graph_rag.tex) -- "RAG fails on global questions directed at an entire text corpus, such as 'What are the main themes in the dataset?', since this is inherently a query-focused summarization (QFS) task, rather than an explicit retrieval task."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Abstract (graph_rag.tex) -- "Our approach uses an LLM to build a graph index in two stages: first, to derive an entity knowledge graph from the source documents, then to pregenerate community summaries for all groups of closely related entities."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 2.2 (graph_rag.tex) -- "GraphRAG contrasts with these approaches by focusing on a previously unexplored quality of graphs in this context: their inherent modularity and the ability to partition graphs into nested modular communities of closely related nodes"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Abstract (graph_rag.tex) -- "we show that GraphRAG leads to substantial improvements over a conventional RAG baseline for both the comprehensiveness and diversity of generated answers"
[^card-graphrag-knowledge-poisoning-attack]: [GraphRAG 知识投毒攻击](graphrag-knowledge-poisoning-attack.md) -- 知识投毒攻击（KPA）以极低修改量操纵 GraphRAG 的实体提取过程，揭示全局 sensemaking 管道在安全性上的已知空白
