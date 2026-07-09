---
id: memgpt-archival-vs-recall-storage
title: MemGPT 归档存储与回忆存储的区分
status: draft
card_type: distinction
tags: [memgpt, archival-storage, recall-storage, external-context, memory-hierarchy]
created_time: 2026-06-12T10:05:00+08:00
edited_time: 2026-06-12T10:05:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: peer-reviewed
justification: ../justification/experiment/memgpt-archival-vs-recall-storage.md
canonical_concept: archival-vs-recall-storage
aliases: [归档存储, 回忆存储, archival storage, recall storage, external context]
summary: >-
  MemGPT archival-vs-recall-storage 区分两种外部存储：recall storage 专存消息历史（自动写入），archival storage 存储任意长度文本对象（显式读写），两者共同构成 external context。
related: [memgpt-main-context-structure, memgpt-virtual-context-management, memgpt-document-qa-pagination]
---

MemGPT 的 external context（类比 OS 磁盘存储）包含两个功能不同的存储层：

**Recall Storage（回忆存储）**：消息数据库，自动存储所有经过 MemGPT 系统的消息——包括用户消息、agent 回复、系统消息、函数调用记录。当消息被 FIFO queue 驱逐后仍永久保存于此。通过 conversation_search 函数检索，检索结果被 queue manager 追加到队列尾部重新进入上下文。[^src-1]

**Archival Storage（归档存储）**：读写数据库，存储任意长度的文本对象，不限于消息——可存放文档、用户上传数据、LLM 主动存储的重要信息等。通过 archival_memory_insert/search 函数操作。在文档分析场景中使用 PostgreSQL + pgvector 扩展（HNSW 索引）实现近似亚秒级向量搜索。[^src-2]

两者的关键区别在于写入方式：recall storage 由系统自动写入（每条消息都存），archival storage 需要 LLM 或用户显式操作。然而，这意味着重要信息如果仅存在于消息流中而未被 LLM 主动转存到 archival storage，其可检索性仅依赖 recall storage 的搜索能力——论文未明确说明 recall storage 是否也支持向量搜索或仅支持关键词匹配。[^src-1]

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Queue Manager -- "The queue manager writes both the incoming message and the generated LLM output to recall storage (the MemGPT message database)."
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Multi-document QA -- "MemGPT's default storage settings which uses PostgreSQL for archival memory storage with vector search enabled via the pgvector extension"
[^card-1]: -> memgpt-main-context-structure -- 本卡聚焦外部存储的两种类型及其区别，该卡聚焦内部 main context 的结构
