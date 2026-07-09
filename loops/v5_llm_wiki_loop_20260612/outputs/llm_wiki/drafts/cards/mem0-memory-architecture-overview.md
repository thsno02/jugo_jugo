---
id: mem0-memory-architecture-overview
title: Mem0 记忆架构总览
status: draft
card_type: system-architecture
tags: [memory, llm-agent, long-term-memory, conversational-ai]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0]
evidence_basis: experimental_paper
justification: ../justification/mem0-memory-architecture-overview.md
canonical_concept: mem0-memory-architecture
aliases: [Mem0, mem-zero, mem0 system, memory-centric architecture]
summary: >-
  Mem0 mem-zero 是一种可扩展的记忆中心架构 memory-centric architecture，通过动态提取 extraction、整合 consolidation 和检索 retrieval 对话中的显著信息来克服 LLM 固定上下文窗口限制。系统处理消息对 message pairs，包含 extraction phase 和 update phase 两个阶段，使用 GPT-4o-mini 作为推理引擎，向量数据库存储稠密嵌入。在 LOCOMO benchmark 上，Mem0 在 single-hop、multi-hop、temporal 问题类型上达到 SOTA。
related: []
---

Mem0（发音为 mem-zero）是一种可扩展的记忆中心架构，旨在为 AI agent 提供持久化长期记忆能力。该系统采用增量处理范式（incremental processing paradigm），能够在持续对话中无缝运作。[^src-1]

其完整管线架构由两个阶段组成：提取阶段（extraction phase）和更新阶段（update phase）。系统处理的基本单元是消息对 $(m_{t-1}, m_t)$，通常由用户消息和助手响应构成。所有语言模型操作使用 GPT-4o-mini 作为推理引擎，向量数据库采用稠密嵌入实现高效相似性搜索。[^src-2]

在 LOCOMO benchmark 上的综合评估表明，Mem0 在 single-hop、multi-hop 和 temporal 推理任务上一致优于现有记忆系统，包括记忆增强架构、RAG 方法以及开源和商业方案。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/proposed_work.tex" P1139 -- "Our architecture follows an incremental processing paradigm, enabling it to operate seamlessly within ongoing conversations."
[^src-2]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/proposed_work.tex" P1158 -- "All language model operations utilized GPT-4o-mini as the inference engine. The vector database employs dense embeddings to facilitate efficient similarity search during the update phase."
[^src-3]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/intro.tex" P1127 -- "Our experimental results on the LOCOMO benchmark demonstrate that our approaches consistently outperform existing memory systems"
