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
related: [audit-provenance-tracing, compilation-gap, lossy-compression-citation-tradeoff, memory-overwrite-vs-omission-failure]
  - temporal-knowledge-graph-three-tier
  - episodic-semantic-memory-duality
---

Graphiti 的 episode 子图被设计为一个无损数据存储（non-lossy data store），从中提取语义实体和关系，但原始数据始终保留 [^src-1]。

**双向索引**：Episode 与其派生的语义边之间维护双向索引，追踪边与源 episode 之间的关系 [^src-2]。这种设计支持两个方向的遍历：
- **正向**：从 episode 快速检索其相关实体和事实
- **反向**：从语义制品追溯到源 episode，用于引用（citation）或引述（quotation）

**非破坏性更新**：这种设计与边失效机制配合——旧的事实不被删除而是标记为失效，episode 原始数据也不被修改。整个知识图谱以"动态添加新信息的非损失方式"更新 [^src-3]。

论文注意到，虽然这些双向连接在当前实验中未被直接检验，但将在未来工作中探索 [^src-4]。

这种无损设计与知识压缩领域普遍存在的有损性形成鲜明对比：段落级摘要压缩会损害引用质量[^dist-1]，文档级编译会灾难性丢弃事实[^dist-2]，商业记忆系统的压缩策略导致覆写和遗漏两种失败模式[^dist-3]。

与 LLM Wiki 的审计溯源相比，Graphiti 的溯源是内建的——在数据写入时即建立双向索引，而非事后沿制品图遍历[^card-1]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2 (Knowledge Graph Construction) -- "Episodes serve as a non-lossy data store from which semantic entities and relations are extracted."
[^src-2]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.1 (Episodes) -- "Episodes and their derived semantic edges maintain bidirectional indices that track the relationships between edges and their source episodes... semantic artifacts can be traced to their sources for citation or quotation, while episodes can quickly retrieve their relevant entities and facts."
[^src-3]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 1 -- "The Graphiti KG engine dynamically updates the knowledge graph with new information in a non-lossy manner"
[^dist-1]: [有损压缩的引用权衡](lossy-compression-citation-tradeoff.md) -- 本卡主张通过保留原始数据实现无损存储与溯源，该卡展示有损压缩在提升效率的同时不可避免地损害引用质量，区分点在于是否以牺牲信息完整性换取压缩效率
[^dist-2]: [编译缺口](compilation-gap.md) -- 本卡提出保留原始episode的无损架构，该卡量化编译过程中53-60%的灾难性事实丢失，区分点在于Graphiti通过"保留原始+提取语义"的双层设计绕过了编译的有损性
[^dist-3]: [记忆覆写与遗漏两种失败模式](memory-overwrite-vs-omission-failure.md) -- 本卡的无损设计（episode不被修改、旧事实标记失效而非删除）直接回应该卡诊断的两种失败模式：覆写（通过非破坏性更新避免）和遗漏（通过保留全部输入避免）

[^card-1]: [审计与溯源追踪](audit-provenance-tracing.md) -- 本卡通过内建双向索引实现写入时溯源，该卡采取事后沿制品图遍历（output->wiki->raw）的审计策略，两者代表内建溯源与事后追踪的架构区分
[^src-4]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- Section 2.1 -- "While these connections are not directly examined in this paper's experiments, they will be explored in future work."
