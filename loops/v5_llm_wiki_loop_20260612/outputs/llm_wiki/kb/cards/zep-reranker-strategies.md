---
id: zep-reranker-strategies
title: Zep 重排序策略
status: accepted
card_type: mechanism
tags:
- reranking
- RRF
- MMR
- cross-encoder
- retrieval
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-zep
evidence_basis: experimental_paper
justification: ../justification/zep-reranker-strategies.md
canonical_concept: zep-reranker-strategies
aliases:
- Zep reranker
- episode-mentions reranker
- node distance reranker
- 重排序策略
summary: Zep 支持多种 reranker：RRF（多结果融合）、MMR（多样性重排序）、episode-mentions reranker（按实体/事实在对话中被提及频率排序，频繁引用的信息更易获取）、node distance reranker（按图距离从中心节点排序，提供局部化上下文）、cross-encoder（LLM 生成相关性 分数，精度最高但计算代价最大）。初始搜索追求高 recall，reranker
  追求高 precision。
related:
- zep-hybrid-retrieval-pipeline
---

Zep 的 reranker 组件 (rho) 在初始搜索结果基础上提升精度（precision），而搜索阶段侧重召回率（recall）。[^src-1]

支持的重排序策略包括：[^src-1]

1. **Reciprocal Rank Fusion (RRF)**：融合多个检索方法的排序结果
2. **Maximal Marginal Relevance (MMR)**：兼顾相关性和多样性的重排序
3. **Episode-mentions reranker**：按实体或事实在对话中被提及的频率进行优先排序，使频繁引用的信息更容易被访问
4. **Node distance reranker**：基于结果与指定中心节点（centroid）之间的图距离进行重排序，提供局部化的上下文
5. **Cross-encoder**：使用 LLM 通过 cross-attention 对 node/edge-query 对生成相关性分数，精度最高但计算成本也最高

[^src-1]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Reranker" P1 -- "Zep supports existing reranking approaches such as Reciprocal Rank Fusion (RRF) and Maximal Marginal Relevance (MMR)...Additionally, Zep implements a graph-based episode-mentions reranker"
[^card-1]: [zep-hybrid-retrieval-pipeline] -- reranker 是三步检索管线的第二步
