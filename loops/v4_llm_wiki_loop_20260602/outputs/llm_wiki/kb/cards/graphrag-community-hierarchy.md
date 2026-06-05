---
id: graphrag-community-hierarchy
title: GraphRAG 层级社区检测与摘要机制
status: accepted
card_type: mechanism
tags: [graphrag, community-detection, leiden, hierarchy, summarization]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
justification: ../justification/graphrag-community-hierarchy.md
canonical_concept: graphrag-community-hierarchy
aliases: [社区层级摘要, hierarchical community summarization, 图社区层级]
summary: >-
  graphrag-community-hierarchy（社区层级摘要 / hierarchical community summarization）使用 Leiden 算法递归检测知识图谱中的层级社区，每层覆盖互斥穷尽的节点分区，LLM 自底向上生成社区摘要实现分治式全局理解
related: [dynamic-community-detection, graph-modularity-for-summarization, graphrag-community-level-tradeoff, graphrag-global-sensemaking, graphrag-map-reduce-query]
---

GraphRAG 的核心机制是对 LLM 构建的知识图谱进行层级社区检测。论文使用 Leiden 社区检测算法，以层级方式递归检测社区内部的子社区，直到达到无法再分割的叶节点社区 [^src-1]。

层级结构的关键性质是：每一层级提供一个覆盖图中所有节点的互斥且穷尽的社区分区，从而实现分治式的全局摘要 [^src-2]。

社区摘要的生成采用自底向上的方式：

- **叶节点社区**：按边的源节点和目标节点的联合度数（degree）降序排列，依次添加节点描述、边描述和相关声明到上下文窗口，直至 token 上限 [^src-3]。
- **高层社区**：如果所有元素摘要能放入上下文窗口，按叶节点方式处理。否则，按子社区元素摘要 token 数降序排列，用更短的子社区摘要迭代替换更长的元素摘要，直到能放入上下文窗口 [^src-4]。

这些社区摘要本身就有独立价值——用户可以扫描某一层级的社区摘要寻找感兴趣的主题，然后阅读更低层级的链接报告获取子主题的详细信息 [^src-5]。

此机制的概念基础——图的固有模块性——是 GraphRAG 区别于此前图+RAG 方法的关键洞察[^card-1]。

**替代方案**：Graphiti（Zep）选择标签传播算法替代 Leiden，以支持新实体加入时的单步动态社区分配，用全局最优性换取增量更新的低延迟[^card-dynamic-community-detection]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 1.1.4 (graph_rag.tex) -- "we use Leiden community detection in a hierarchical manner, recursively detecting sub-communities within each detected community until reaching leaf communities that can no longer be partitioned"
[^src-2]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 1.1.4 (graph_rag.tex) -- "Each level of this hierarchy provides a community partition that covers the nodes of the graph in a mutually exclusive, collectively exhaustive way, enabling divide-and-conquer global summarization."
[^src-3]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 1.1.5 (graph_rag.tex) -- "for each community edge in decreasing order of combined source and target node degree (i.e., overall prominence), add descriptions of the source node, target node, the edge itself, and related claims"
[^src-4]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 1.1.5 (graph_rag.tex) -- "rank sub-communities in decreasing order of element summary tokens and iteratively substitute sub-community summaries (shorter) for their associated element summaries (longer) until they fit within the context window"
[^src-5]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Section 1.1.5 (graph_rag.tex) -- "a user may scan through community summaries at one level looking for general themes of interest, then read linked reports at a lower level that provide additional details for each subtopic"
[^card-dynamic-community-detection]: [标签传播动态社区检测](dynamic-community-detection.md) -- Graphiti 用标签传播替代 Leiden 以支持动态增量更新，代表了与 GraphRAG 层级检测互补的另一种社区检测范式
[^card-1]: [图模块性作为层级摘要的结构基础](graph-modularity-for-summarization.md) -- 本卡聚焦层级社区检测的具体机制（Leiden 递归分区与自底向上摘要），该卡聚焦此机制背后的概念基础——图的固有模块性
