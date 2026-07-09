---
id: librarian-graph-traversal-and-community-detection
title: Librarian 提供 BFS 图遍历与 Louvain 社区检测
status: accepted
card_type: mechanism
tags:
- knowledge-graph
- bfs
- louvain
- community-detection
- pagerank
- centrality
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- repo-ngmeyer-librarian-mcp
evidence_basis: code_implementation
justification: ../justification/librarian-graph-traversal-and-community-detection.md
canonical_concept: librarian-graph-community-detection
aliases:
- library_traverse
- library_shortest_path
- library_graph_analysis
- library_cluster
- Louvain modularity
- BFS traversal
- community detection
summary: Librarian 从 vault 的 [[wikilinks]] 构建双向图，提供三种图遍历工具：BFS N-hop 遍历（library_traverse）、最短路径（library_shortest_path）、图分析（library_graph_analysis，含连通分量/hub/bridge/orphan）。社区检测使用 Louvain modularity optimization（library_cluster），结合
  betweenness centrality 和 PageRank 排序 god nodes（结构重要笔记）并发现跨社区连接。librarian graph-traversal louvain community-detection bfs pagerank。
related:
- librarian-mcp-as-llm-wiki-productization
- graphiti-community-detection
---

Librarian 从 vault 中所有 `[[wikilinks]]` 构建双向图，并暴露三种图遍历工具[^src-1]：

1. **Traverse (BFS)** — 从任意笔记出发，N-hop 深度广度优先遍历，展示主题邻域
2. **Shortest path** — 找到两笔记之间的最短链接链，揭示概念间连接路径
3. **Graph analysis** — 连通分量、hub 笔记、bridge 笔记、孤立笔记的结构分析

社区检测使用 Louvain modularity optimization 算法识别 vault 中的主题聚类[^src-2]。结合 betweenness centrality 和 PageRank，report 工具能排序"god nodes"（结构上最重要的笔记）并发现意外的跨社区连接。

这些能力使 LLM 不仅能读写笔记，还能理解 vault 的拓扑结构——哪些是知识枢纽、哪些是桥接不同主题的关键笔记、哪些是被遗忘的孤立节点。

[^card-1]: [[librarian-mcp-as-llm-wiki-productization]] — Librarian 整体架构
[^src-1]: `data/raw/github_repo/repo-ngmeyer-librarian-mcp/repo/README.md` -- "Knowledge graph traversal" P1 -- "Librarian builds a bidirectional graph from your vault's [[wikilinks]] and exposes three graph tools"
[^src-2]: `data/raw/github_repo/repo-ngmeyer-librarian-mcp/repo/README.md` -- "Community detection" P1 -- "Louvain modularity optimization identifies topic clusters in your vault. Combined with betweenness centrality and PageRank"
