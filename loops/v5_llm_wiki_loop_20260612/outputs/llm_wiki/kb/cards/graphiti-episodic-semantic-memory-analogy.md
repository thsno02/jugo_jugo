---
id: graphiti-episodic-semantic-memory-analogy
title: Graphiti 的 episodic/semantic memory 心理学类比
status: accepted
card_type: design-rationale
tags:
- episodic-memory
- semantic-memory
- cognitive-model
- knowledge-graph
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-zep
evidence_basis: experimental_paper
justification: ../justification/graphiti-episodic-semantic-memory-analogy.md
canonical_concept: graphiti-episodic-semantic-memory-analogy
aliases:
- episodic vs semantic memory in Graphiti
- dual memory model
- 情节记忆与语义记忆类比
summary: Graphiti 的 episode 子图与 semantic entity 子图的双重存储类比心理学中 episodic memory （表征独立事件）与
  semantic memory（捕获概念间关联及含义）的区分。这种设计使 LLM Agent 发展出更贴近人类记忆系统的分层记忆结构。类似方法见 AriGraph。
related:
- zep-temporal-knowledge-graph-architecture
- graphiti-episode-subgraph
- mem0-graph-memory-architecture
---

Graphiti 将原始对话数据（episode 子图）与从中提取的语义知识（semantic entity 子图）分别存储，这种双重存储设计有意类比心理学中对人类记忆系统的建模。[^src-1]

心理学模型区分：
- **Episodic memory**：表征独立事件的记忆
- **Semantic memory**：捕获概念之间的关联及其含义

通过在知识图谱中实现这种区分，使用 Zep 的 LLM Agent 可以发展出更为精细和层次化的记忆结构，更贴近我们对人类记忆系统的理解。[^src-1]

论文指出知识图谱为表征这些记忆结构提供了有效介质，其 episodic/semantic 子图的分离实现借鉴了 AriGraph 中的类似方法。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` -- "Knowledge Graph Construction" P2 -- "The dual storage of both raw episodic data and derived semantic entity information mirrors psychological models of human memory"
[^card-1]: [graphiti-episode-subgraph] -- episode 子图是 episodic memory 的实现载体
[^card-2]: [zep-temporal-knowledge-graph-architecture] -- 此心理学类比是三层架构的设计动机
