---
id: unified-memory-framework-three-stages
title: 长期记忆系统统一三阶段框架
status: draft
card_type: framework
tags: [long-term-memory, RAG, indexing, retrieval, reading, unified-framework]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
evidence_basis: experimental_paper
justification: ../justification/unified-memory-framework-three-stages.md
canonical_concept: unified-memory-framework
aliases: [unified memory framework, three-stage memory model, 三阶段记忆框架, indexing-retrieval-reading]
summary: >-
  unified-memory-framework 将长期记忆建模为大规模 key-value 数据存储，分解为三个阶段：indexing（将每个历史会话转换为 key-value 项）、retrieval（构建检索查询并收集最相关的 k 个项）、reading（LLM 读取检索结果生成响应）。四个控制点：value（存储粒度和格式）、key（索引键设计）、query（查询构建策略）、reading strategy（阅读策略）。该框架统一了九个现有记忆增强系统的设计视角，包括 in-context RAG、MemoryBank、LD-Agent、CoN、ChatGPT、Coze、RAPTOR、MemWalker、HippoRAG。
related: [longmemeval-benchmark-overview]
---

LongMemEval 论文提出将记忆增强聊天助手建模为大规模 key-value 数据存储 [(k1,v1), (k2,v2), ...]，其中 key 可以是异构的（离散的句子/段落/事实/实体，或连续的模型内部表示），value 可重复。[^src-1]

三个执行阶段：
1. **Indexing**：将每个历史会话 (t_i, S_i) 转换为一个或多个 key-value 项
2. **Retrieval**：构建检索查询并收集 k 个最相关项
3. **Reading**：LLM 读取检索结果并生成响应

四个控制点（CP）：
- CP1 Value：存储格式和粒度（session / round / compressed facts）
- CP2 Key：索引键设计（value 本身 / 扩展键）
- CP3 Query：查询构建策略（直接 / 时间感知扩展）
- CP4 Reading Strategy：阅读策略（direct / Chain-of-Note / interactive）

该框架将九个现有系统视为其实例化，包括 in-context RAG、MemoryBank、LD-Agent、CoN、ChatGPT、Coze、RAPTOR、MemWalker、HippoRAG。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/4_methodology.tex" -- "We formulate long-term memory as a massive key-value datastore"
[^src-2]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "tables/memory_system_dimensions_comp.tex" -- "A comparison of nine memory-augmented frameworks through the lens of the proposed unified framework"
