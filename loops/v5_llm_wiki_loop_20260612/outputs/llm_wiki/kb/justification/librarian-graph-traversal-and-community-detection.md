# Justification: librarian-graph-traversal-and-community-detection

## 为什么值得建卡

知识图谱遍历与社区检测是 Librarian 区别于其他 markdown 工具的核心技术能力，也是 LLM Wiki 模式中"结构化涌现"的工程实现。Louvain + PageRank + BFS 的组合使 LLM 能感知 vault 的拓扑结构。

## evidence_basis 选择: code_implementation

README 描述的是已实现并可调用的 MCP tools（library_traverse, library_shortest_path, library_graph_analysis, library_cluster），属于代码实现级别证据。

## 原子性检验

本卡将图遍历和社区检测合并，因为两者共享同一双向图数据结构且在功能上互补（遍历是局部探索，社区检测是全局结构）。自动 wikilink 机制独立拆卡。
