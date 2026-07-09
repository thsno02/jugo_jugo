---
id: mem0-graph-memory-architecture
title: Mem0 图记忆架构
status: accepted
card_type: system-architecture
tags:
- graph-memory
- knowledge-graph
- neo4j
- entity-extraction
- relationship-triplet
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-mem0
evidence_basis: experimental_paper
justification: ../justification/mem0-graph-memory-architecture.md
canonical_concept: mem0-graph-memory
aliases:
- Mem0^g
- Mem0 graph memory
- 图记忆
- graph-based memory
- mem0p
summary: Mem0^g mem0p 图记忆架构将记忆表示为有向标记图 directed labeled graph G=(V,E,L)，节点为实体 entities，边为关系
  relationships，标签为语义类型。采用 entity extractor + relationship generator 两阶段 LLM 管线将非结构化文本转为结构化图表示。使用
  Neo4j 图数据库，通过 conflict detection 和 update resolver 维护一致性。支持 entity-centric 和 semantic
  triplet 双重检索策略。
related:
- mem0-memory-architecture-overview
- mem0-graph-temporal-advantage
- graphiti-episodic-semantic-memory-analogy
- mem0-update-phase-operations
---

Mem0^g（Mem0 with graph memory）扩展了基础 Mem0 架构，引入图记忆表示以捕获对话元素间的复杂关系结构。记忆被表示为有向标记图 $G = (V, E, L)$：[^src-1]

- **节点** $V$：实体（如 Alice、San_Francisco）
- **边** $E$：实体间关系（如 lives_in）
- **标签** $L$：语义类型分配（如 Person、City）

每个实体节点包含三个组件：实体类型分类、嵌入向量 $e_v$、创建时间戳 $t_v$ 等元数据。关系结构为三元组 $(v_s, r, v_d)$。[^src-2]

提取过程采用两阶段 LLM 管线：首先 **entity extractor** 识别实体及其类型，然后 **relationship generator** 推导实体间有意义的连接，建立关系三元组。整合新信息时，系统计算源/目标实体嵌入，搜索语义相似度超过阈值 $t$ 的现有节点，并通过 **conflict detection** 机制和 **update resolver** 维护知识图一致性（将过时关系标记为无效而非物理删除，以支持时间推理）。[^src-3]

检索功能实现双重策略：entity-centric 方法从锚点节点探索关系子图，semantic triplet 方法对查询编码为稠密向量匹配三元组文本编码。系统使用 Neo4j 作为底层图数据库。[^src-4]

[^card-1]: [[mem0-memory-architecture-overview]] 描述了 Mem0 基础架构

[^src-1]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/proposed_work.tex" P1164 -- "memories are represented as a directed labeled graph G = (V, E, L)"
[^src-2]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/proposed_work.tex" P1172 -- "Each entity node v in V contains three components: (1) an entity type classification... (2) an embedding vector e_v... (3) metadata including a creation timestamp t_v"
[^src-3]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/proposed_work.tex" P1184 -- "we implement a conflict detection mechanism that identifies potentially conflicting existing relationships when new information arrives. An LLM-based update resolver determines if certain relationships should be obsolete, marking them as invalid rather than physically removing them"
[^src-4]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/proposed_work.tex" P1188 -- "the system utilizes Neo4j as the underlying graph database"
