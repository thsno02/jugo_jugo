---
id: hybrid-triple-search-complementarity
title: 三种互补搜索方法的混合检索
status: accepted
card_type: mechanism
tags: [search, retrieval, cosine_similarity, BM25, BFS, knowledge_graph, Zep]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
justification: ../justification/hybrid-triple-search-complementarity.md
canonical_concept: hybrid-triple-search-complementarity
aliases: [三种搜索互补, triple search methods, cosine-BM25-BFS hybrid]
summary: >-
  hybrid-triple-search-complementarity（三种搜索互补, cosine-BM25-BFS hybrid）Zep 组合三种搜索方法：余弦相似度（语义相似）、BM25 全文搜索（词汇相似）、广度优先图搜索（上下文相似），分别捕获不同维度的相关性
related:
  - search-rerank-construct-pipeline
  - temporal-knowledge-graph-three-tier
---

Zep 实现了三种搜索函数，各自捕获不同维度的相似性 [^src-1]：

**余弦语义相似度搜索 (phi_cos)**：基于向量嵌入的语义相似度，捕获语义层面的相似性 [^src-2]。

**BM25 全文搜索 (phi_bm25)**：基于 Okapi BM25 算法，捕获词汇层面的相似性。两者均使用 Neo4j 的 Lucene 实现 [^src-3]。

**广度优先搜索 (phi_bfs)**：在知识图谱上进行 n 跳扩展，捕获上下文相似性——图中距离更近的节点和边出现在更相似的对话上下文中。BFS 在 RAG 领域中较少被关注，但具有独特价值：它可以接受节点作为搜索参数（而非仅文本查询），特别适合使用最近的 episode 作为种子来将近期提及的实体和关系纳入检索上下文 [^src-4]。

三种方法的搜索字段也因对象类型而异：对语义边搜索 fact 字段，对实体节点搜索 entity name，对社区节点搜索 community name（包含社区中的关键词和短语）[^src-5]。

论文作者总结："全文搜索识别词汇相似性，余弦相似度捕获语义相似性，广度优先搜索揭示上下文相似性"[^src-6]。

Mem0^g 的知识图谱检索采用了类似的双路互补设计（实体锚定 + 语义三元组），从不同角度印证了多路检索的互补价值 [^card-1]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 3.1 (Search) -- "Zep implements three search functions: cosine semantic similarity search, Okapi BM25 full-text search, and breadth-first search."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 3.1 -- "cosine similarity captures semantic similarities"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 3.1 -- "The first two functions utilize Neo4j's implementation of Lucene"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 3.1 -- "breadth-first search over knowledge graphs has received limited attention in the RAG domain... phi_bfs can accept nodes as parameters for the search... This functionality proves particularly valuable when using recent episodes as seeds for the breadth-first search"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 3.1 -- "The search field varies across the three object types: for E_s, we search the fact field; for N_s, the entity name; and for N_c, the community name"
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 3.1 -- "full-text search identifies word similarities, cosine similarity captures semantic similarities, and breadth-first search reveals contextual similarities"
[^card-1]: [双路检索策略（实体锚定 + 语义三元组）](dual-retrieval-entity-semantic.md) -- Mem0^g 从实体锚定和语义三元组两个路径实现知识图谱检索，与 Zep 的三路方法互为补充
