---
id: zep-hybrid-retrieval-pipeline
title: Zep 混合检索管线
status: accepted
card_type: mechanism
tags:
- retrieval
- hybrid-search
- cosine-similarity
- BM25
- BFS
- knowledge-graph
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-zep
evidence_basis: experimental_paper
justification: ../justification/zep-hybrid-retrieval-pipeline.md
canonical_concept: zep-hybrid-retrieval-pipeline
aliases:
- Zep memory retrieval
- graph search API
- hybrid search in Zep
- 混合检索
summary: Zep 记忆检索实现 f(alpha)=chi(rho(phi(alpha)))=beta 三步管线：Search phi 通过 cosine similarity（语义相似）、BM25 full-text（词汇相似）、BFS（上下文/图距离相似） 三种方法识别候选 edges/entities/communities；Reranker rho 重排序结果；Constructor chi
  将图元素转为文本上下文字符串。BFS 可用 recent episodes 作为种子，将近期上下文纳入检索。
related:
- zep-temporal-knowledge-graph-architecture
- zep-reranker-strategies
- graphiti-community-detection
---
Zep 的记忆检索被形式化为函数 f: S -> S，将文本查询 alpha 映射为文本上下文 beta，由三个组件的组合实现：f(alpha) = chi(rho(phi(alpha))) = beta。[^src-1]

**Search (phi)**：系统实现三种搜索函数：
1. **Cosine semantic similarity (phi_cos)**：捕获语义相似性
2. **BM25 full-text search (phi_bm25)**：识别词汇相似性
3. **Breadth-first search (phi_bfs)**：揭示上下文相似性——图中距离更近的节点出现在更相似的对话上下文中

三种方法分别作用于不同对象：edges 搜索 fact 字段，entity nodes 搜索 name 字段，community nodes 搜索 community name（含关键词和短语）。[^src-2]

BFS 还接受节点作为参数，特别适合用 recent episodes 作为种子，将近期提及的实体和关系纳入检索上下文。[^src-2]

**Constructor (chi)**：将结果转为文本——每条 edge 返回 fact + t_valid/t_invalid，每个 entity node 返回 name + summary，每个 community node 返回 summary。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Memory Retrieval" P1 -- "The process f(alpha)->beta comprises three distinct steps...Search, Reranker, Constructor"
[^src-2]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Search" P1 -- "Zep implements three search functions: cosine semantic similarity search, Okapi BM25 full-text search, and breadth-first search"
[^card-1]: [zep-temporal-knowledge-graph-architecture] -- 检索管线是 Zep 作为记忆服务的核心产出接口
