---
id: non-lossy-episodic-store
title: 无损 Episode 数据存储与双向溯源
status: accepted
card_type: operational_rule
tags: [data_integrity, provenance, episodic_memory, knowledge_graph, Graphiti]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
justification: ../justification/non-lossy-episodic-store.md
canonical_concept: non-lossy-episodic-store
aliases: [无损Episode存储, non-lossy data store, 双向索引溯源]
summary: >-
  non-lossy-episodic-store（无损Episode存储, non-lossy data store）Graphiti 的 episode 子图作为无损数据存储保留所有原始输入，并通过双向索引支持正向/反向遍历：语义制品可追溯到源 episode 用于引用，episode 可快速检索其相关实体
related:
  - temporal-knowledge-graph-three-tier
  - episodic-semantic-memory-duality
---

Graphiti 的 episode 子图被设计为一个无损数据存储（non-lossy data store），从中提取语义实体和关系，但原始数据始终保留 [^src-1]。

**双向索引**：Episode 与其派生的语义边之间维护双向索引，追踪边与源 episode 之间的关系 [^src-2]。这种设计支持两个方向的遍历：
- **正向**：从 episode 快速检索其相关实体和事实
- **反向**：从语义制品追溯到源 episode，用于引用（citation）或引述（quotation）

**非破坏性更新**：这种设计与边失效机制配合——旧的事实不被删除而是标记为失效，episode 原始数据也不被修改。整个知识图谱以"动态添加新信息的非损失方式"更新 [^src-3]。

论文注意到，虽然这些双向连接在当前实验中未被直接检验，但将在未来工作中探索 [^src-4]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2 (Knowledge Graph Construction) -- "Episodes serve as a non-lossy data store from which semantic entities and relations are extracted."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.1 (Episodes) -- "Episodes and their derived semantic edges maintain bidirectional indices that track the relationships between edges and their source episodes... semantic artifacts can be traced to their sources for citation or quotation, while episodes can quickly retrieve their relevant entities and facts."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 1 -- "The Graphiti KG engine dynamically updates the knowledge graph with new information in a non-lossy manner"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.1 -- "While these connections are not directly examined in this paper's experiments, they will be explored in future work."
