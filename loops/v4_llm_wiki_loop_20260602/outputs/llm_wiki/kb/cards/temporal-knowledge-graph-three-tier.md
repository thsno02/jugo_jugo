---
id: temporal-knowledge-graph-three-tier
title: 时序知识图谱的三层子图架构
status: accepted
card_type: mechanism
tags: [knowledge_graph, agent_memory, graph_architecture, Zep, Graphiti]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
justification: ../justification/temporal-knowledge-graph-three-tier.md
canonical_concept: temporal-knowledge-graph-three-tier
aliases: [三层知识图谱, three-tier KG, Graphiti三层架构, episode-semantic-community hierarchy]
summary: >-
  temporal-knowledge-graph-three-tier（三层知识图谱, three-tier KG）Zep/Graphiti 将 agent 记忆组织为 episode 子图（原始数据）、semantic entity 子图（提取的实体与关系）、community 子图（聚类摘要）三层递进结构
related:
  - episodic-semantic-memory-duality
  - dynamic-community-detection
---

Zep 的核心组件 Graphiti 将知识图谱 G=(N, E, phi) 组织为三层层次化子图 [^src-1]：

**Episode 子图 (G_e)**：存储原始输入数据（消息、文本、JSON），作为无损数据源。Episode 节点通过 episodic edge 连接到所提取的 semantic entity 节点，支持双向追溯——从语义制品回溯到源数据用于引用，或从 episode 快速检索相关实体与事实 [^src-2]。

**Semantic Entity 子图 (G_s)**：在 episode 子图之上构建。实体节点代表从 episode 中提取并与已有图实体完成消解的实体；语义边代表实体间的关系（即事实/fact）。这是知识图谱中承载结构化知识的核心层 [^src-3]。

**Community 子图 (G_c)**：最高层级。通过社区检测算法将强连接的实体聚类，生成高层摘要。Community 节点提供对 semantic entity 子图结构的更全面、互联的视角 [^src-4]。

这种从 episode 到 fact 到 entity 到 community 的层次化组织，扩展了已有的分层 RAG 策略 [^src-5]。

LoCoMo 的时序事件图是一种更轻量的对应物：它以事件节点和因果连接构建对话锚定图，功能上对应于 Graphiti 的 semantic entity 子图层，但不具备 episode 溯源和 community 聚类能力[^card-1]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2 (Knowledge Graph Construction) -- "memory is powered by a temporally-aware dynamic knowledge graph G=(N, E, phi)... This graph comprises three hierarchical tiers of subgraphs: an episode subgraph, a semantic entity subgraph, and a community subgraph."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.1 (Episodes) -- "semantic artifacts can be traced to their sources for citation or quotation, while episodes can quickly retrieve their relevant entities and facts"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2 -- "Entity nodes... represent entities extracted from episodes and resolved with existing graph entities. Entity edges... represent relationships between entities extracted from episodes."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2 -- "Community nodes... represent clusters of strongly connected entities. Communities contain high-level summarizations of these clusters"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2 -- "The resulting hierarchical organization—from episodes to facts to entities to communities—extends existing hierarchical RAG strategies"
[^card-1]: [时序事件图作为对话锚定机制](temporal-event-graph-grounding.md) -- LoCoMo 的时序事件图是三层架构中 semantic entity 子图的轻量对应物，以事件节点和因果连接构建对话锚定
