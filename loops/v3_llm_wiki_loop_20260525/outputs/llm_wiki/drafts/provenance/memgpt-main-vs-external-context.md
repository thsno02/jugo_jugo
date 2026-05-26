---
schema: draft_card_provenance.v3
draft_card: ../cards/memgpt-main-vs-external-context.md
material_id: arxiv-memgpt
digest_id: digest_arxiv-memgpt
source_paths:
  - data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt
created_time: 2026-05-26T11:25:00+08:00
edited_time: 2026-05-26T11:25:00+08:00
edited_entity: llm
---

## 源证据

- method 行 1633–1637：定义 main context 与 external context、in-context 与 out-of-context 的区分。
- 行 1641："The prompt tokens in MemGPT are split into three contiguous sections: the system instructions, working context, and FIFO Queue. The system instructions are read-only (static) ... Working context is a fixed-size read/write block of unstructured text, writeable only via MemGPT function calls."
- 行 1642："The FIFO queue stores a rolling history of messages ... The first index in the FIFO queue stores a system message containing a recursive summary of messages that have been evicted from the queue."
- 行 1646："The queue manager writes both the incoming message and the generated LLM output to recall storage (the MemGPT message database). When messages in recall storage are retrieved via a MemGPT function call, the queue manager appends them to the back of the queue to reinsert them into the LLM's context window."
- 行 1648：archival storage 定义—"a read/write database storing arbitrary length text objects."
- 行 1460：实际部署用 PostgreSQL + pgvector + HNSW。
- 行 1637："MemGPT provides function calls that the LLM processor to manage its own memory without any user intervention."——验证 external 必须通过函数访问的硬约束。

## 卡片范围是否成立

本卡范围是"5 个具名内存区的角色与写规则"，独立于 OS 类比卡和队列驱逐卡。所有具名区与写规则有原文逐字定义。"两类写法的语义不同"是把 §2 描述总结成可操作的工程区分，仍受原文支撑。

## 发表门控结果

本轮未运行。

## 备注

- 与 memgpt-virtual-context-os-analogy 互补：前者是哲学/范式，本卡是结构/规则。
- 与 memgpt-queue-eviction-policy 共用 FIFO/recall 概念，但本卡只描述区是什么，不展开驱逐策略。
