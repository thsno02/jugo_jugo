---
id: memgpt-archival-recall-storage
title: MemGPT 外部存储双系统
status: accepted
card_type: system-component
tags:
- llm-memory
- external-storage
- database
- archival
- recall
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-memgpt
evidence_basis: experimental_paper
justification: ../justification/memgpt-archival-recall-storage.md
canonical_concept: memgpt-archival-recall-storage
aliases:
- archival storage
- recall storage
- 归档存储
- 回忆存储
- MemGPT external context databases
summary: 'MemGPT memgpt-archival-recall-storage 外部存储双系统 将外部上下文(external context) 分为两个数据库: archival storage(读写数据库, 存储任意长度文本对象, 用于文档/知识持久存储, 支持向量搜索)和recall storage(消息数据库, 存储所有历史消息含函数IO, 支持通过搜索重新调入上下文)。archival类比长期磁盘文件,
  recall类比swap/日志。 两者均通过MemGPT函数调用访问, 数据必须显式移入主上下文才可被LLM推理使用。'
related:
- memgpt-memory-hierarchy
- memgpt-queue-manager
---

MemGPT 的外部上下文 (external context) 由两个独立的数据库系统组成：[^src-1]

**Archival Storage (归档存储)**:
- 读写数据库，存储任意长度的文本对象
- 在文档分析场景中存储整个文档语料库（如 Wikipedia 嵌入）
- 在对话场景中用于存储重要信息（当 working context 空间不足时）
- 支持向量搜索（论文实验中使用 PostgreSQL + pgvector + HNSW 索引）
- 类比：长期磁盘文件系统 [^src-2]

**Recall Storage (回忆存储)**:
- MemGPT 的消息数据库
- 存储所有传入消息和 LLM 生成的输出
- 包含对话消息、系统消息、函数调用的输入输出
- 被 queue manager 驱逐的消息永久存储在此
- 可通过 MemGPT 函数调用搜索并重新插入 FIFO 队列
- 类比：swap 空间 / 系统日志 [^src-1]

两个存储系统均通过 MemGPT 函数调用接口访问，数据必须被显式移入主上下文后才能在推理时被 LLM processor 使用。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/method_rewrite.tex" -- "the queue manager appends them to the back of the queue to reinsert them into the LLM's context window...archival storage (a read/write database storing arbitrary length text objects)"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/experiments.tex" -- "We use MemGPT's default storage settings which uses PostgreSQL for archival memory storage with vector search enabled via the pgvector extension"
[^src-3]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/method_rewrite.tex" -- "External context refers to any information that is held outside of the LLMs fixed context window. This out-of-context data must always be explicitly moved into main context"
[^card-1]: [memgpt-memory-hierarchy] archival 和 recall 构成内存层级中的"外部上下文"层
[^card-2]: [memgpt-queue-manager] queue manager 管理 recall storage 与 FIFO 队列之间的数据流
