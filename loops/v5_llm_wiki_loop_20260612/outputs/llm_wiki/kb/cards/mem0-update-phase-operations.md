---
id: mem0-update-phase-operations
title: Mem0 更新阶段与记忆操作分类
status: accepted
card_type: mechanism
tags:
- memory-update
- tool-call
- semantic-similarity
- knowledge-base-maintenance
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-mem0
evidence_basis: experimental_paper
justification: ../justification/mem0-update-phase-operations.md
canonical_concept: mem0-update-phase-operations
aliases:
- update phase
- memory update operations
- ADD UPDATE DELETE NOOP
- 更新阶段
- memory management operations
summary: Mem0 update phase 更新阶段对每个候选事实评估四种操作：ADD（新信息无语义等价记忆时创建）、UPDATE（用互补信息增强现有记忆）、DELETE（移除被新信息矛盾的记忆）、NOOP（无需修改）。系统检索
  top s=10 语义相似记忆，通过 LLM function-calling tool call 接口直接选择操作，无需独立分类器。维护知识库一致性和时间一致性。
related:
- mem0-memory-architecture-overview
- mem0-extraction-phase
- mem0-graph-memory-architecture
---

Mem0 的更新阶段（update phase）在提取完成后评估每个候选事实与现有记忆的关系，以维护一致性并避免冗余。对每个提取的事实 $\omega_i \in \Omega$，系统首先使用向量嵌入从数据库检索 top $s$（实验中设为 10）个语义相似记忆。[^src-1]

检索到的记忆连同候选事实通过 function-calling 接口（称为 tool call）呈现给 LLM。LLM 自身决定执行四种操作之一：[^src-2]

- **ADD**：当不存在语义等价记忆时，为新信息创建记忆
- **UPDATE**：用互补信息增强现有记忆（当新信息内容量 > 现有记忆时替换）
- **DELETE**：移除被新信息矛盾的记忆
- **NOOP**：候选事实已存在或不相关，无需修改知识库

系统不使用独立分类器，而是利用 LLM 的推理能力基于候选事实与现有记忆之间的语义关系直接选择适当操作。操作执行后维护知识库的连贯性和时间一致性。[^src-3]

[^card-1]: [[mem0-memory-architecture-overview]] 提供了 Mem0 系统的整体架构上下文
[^card-2]: [[mem0-extraction-phase]] 描述了产出候选事实集合 Omega 的前置阶段

[^src-1]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/proposed_work.tex" P1155 -- "the system first retrieves the top s semantically similar memories using vector embeddings from the database"
[^src-2]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/proposed_work.tex" P1155 -- "ADD for creation of new memories when no semantically equivalent memory exists; UPDATE for augmentation of existing memories with complementary information; DELETE for removal of memories contradicted by new information; and NOOP when the candidate fact requires no modification"
[^src-3]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/proposed_work.tex" P1155 -- "Rather than using a separate classifier, we leverage the LLM's reasoning capabilities to directly select the appropriate operation"
