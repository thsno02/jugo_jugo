---
id: graphrag-global-sensemaking
title: GraphRAG 解决全局 sensemaking 问题
status: accepted
card_type: problem-solution
tags:
- graphrag
- sensemaking
- vector-rag
- global-query
- modularity
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-graphrag
evidence_basis: experimental_paper
justification: ../justification/graphrag-global-sensemaking.md
canonical_concept: graphrag-global-sensemaking
aliases:
- GraphRAG sensemaking
- GraphRAG global query
- 全局 sensemaking
summary: GraphRAG graphrag-global-sensemaking 针对 vector RAG 无法回答全局性 sensemaking 问题的痛点，利用知识图谱的固有模块性 modularity 通过 Leiden 层级社区检测将图划分为密切关联节点群，预生成社区摘要后以 map-reduce 聚合实现全语料覆盖。Sensemaking 定义为推理 connections among
  people places events 以预测轨迹并有效行动。Vector RAG 仅检索局部语义相似片段无法覆盖全局主题趋势。
related:
- graphrag-pipeline-architecture
- graphrag-adaptive-benchmarking
- graphrag-community-hierarchy-cost-performance
- graphrag-limitations-and-future-directions
---
**问题**: Vector RAG 通过 embedding 检索与查询语义相似的少量文本片段，对 "What are the main themes in the dataset?" 类需要全语料理解的 sensemaking 问题无法提供答案——这本质上是 query-focused summarization (QFS) 任务而非检索任务。

**Sensemaking 定义**: "reasoning over connections (which can be among people, places, and events) in order to anticipate their trajectories and act effectively" (Klein et al., 2006)。

**GraphRAG 核心洞察**: 图具有固有模块性（modularity）——可被划分为层级化的嵌套社区。通过对每个社区预生成 LLM 摘要，查询时对所有相关社区摘要进行 map-reduce 聚合，即可实现全语料的全局覆盖，无需将全部文本放入单个 context window。

**与先前 graph+RAG 方法的区别**: 此前方法使用子图/图元素直接填充 prompt 或增强检索（如动态遍历文档图），GraphRAG 独特地利用图的社区结构——这是一个在此背景下此前未被探索的图属性。

[^src-1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Introduction" -- "RAG fails on global questions directed at an entire text corpus...since this is inherently a query-focused summarization (QFS) task"
[^src-2]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Using Knowledge Graphs with LLMs and RAG" (Section 2.2) -- "GraphRAG contrasts with these approaches by focusing on a previously unexplored quality of graphs in this context: their inherent modularity"
[^card-1]: [graphrag-pipeline-architecture] 流水线实现细节
