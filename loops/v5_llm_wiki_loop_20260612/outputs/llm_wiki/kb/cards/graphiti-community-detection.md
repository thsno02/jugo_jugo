---
id: graphiti-community-detection
title: Graphiti 社区检测与动态扩展
status: accepted
card_type: mechanism
tags:
- knowledge-graph
- community-detection
- label-propagation
- GraphRAG
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-zep
evidence_basis: experimental_paper
justification: ../justification/graphiti-community-detection.md
canonical_concept: graphiti-community-detection
aliases:
- community subgraph
- label propagation in Graphiti
- community detection
- 社区检测
summary: Graphiti 使用 label propagation（而非 Leiden 算法）进行社区检测，因其支持直接的 动态扩展：新节点加入时调查邻居社区归属，分配给多数社区并更新摘要。这显著降低 延迟和 LLM 推理成本，但结果会逐渐偏离完整 label propagation，仍需定期刷新。 社区节点含 map-reduce 风格的成员摘要，社区名包含关键词以支持 cosine similarity
  搜索。
related:
- zep-temporal-knowledge-graph-architecture
- zep-hybrid-retrieval-pipeline
- librarian-graph-traversal-and-community-detection
---

Graphiti 选择 label propagation 算法（而非 GraphRAG 使用的 Leiden 算法）进行社区检测，主要原因是 label propagation 具有直接的动态扩展能力。[^src-1]

**动态扩展逻辑**：实现 label propagation 的单个递归步骤。当新实体节点加入图谱时，系统调查其邻居节点的社区归属，将新节点分配给邻居中占多数（plurality）的社区，随后更新社区摘要和图结构。这是一种实用的启发式方法，显著降低了延迟和 LLM 推理成本。[^src-1]

**局限性**：动态更新的结果会逐渐偏离完整 label propagation 运行产生的社区划分，因此仍然需要定期进行完整的社区刷新。[^src-1]

**社区摘要**：沿用 GraphRAG 的做法，社区节点包含通过迭代 map-reduce 风格摘要生成的成员汇总。社区名包含关键术语和相关主题，嵌入存储后支持 cosine similarity 搜索。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Communities" P1 -- "we employ a label propagation algorithm rather than the Leiden algorithm...dynamic extension implements the logic of a single recursive step"
[^src-2]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Communities" P2 -- "our community nodes contain summaries derived through an iterative map-reduce-style summarization...we generate community names containing key terms"
[^card-1]: [zep-temporal-knowledge-graph-architecture] -- 社区子图为三层架构的最高层
