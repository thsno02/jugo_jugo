---
id: memgpt-main-vs-external-context
title: MemGPT 的"内存分层"由 3+2 五个具名区组成，每个区角色和写规则都不同
status: accepted
card_type: mechanism
tags: [#memgpt, #memory-hierarchy, #working-context, #archival-storage]
created_time: 2026-05-26T11:25:00+08:00
edited_time: 2026-05-28T11:02:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
provenance_card: ../provenance/memgpt-main-vs-external-context.md
aliases: [main context, external context, recall storage, archival storage]
related: [memgpt-virtual-context-os-analogy, memgpt-queue-eviction-policy, memgpt-function-chaining-heartbeat, memgpt-dmr-task-evaluation, lightmem-three-stage-atkinson-shiffrin, langgraph-store-namespace-key-json-model]
---

MemGPT 把"LLM 看得到的所有信息"分成两大类，五个具名区，每一区的角色、写入方式、是否可被 LLM 直接读都不同：

**Main context（prompt tokens，等同 RAM，分三段，顺序拼成 prompt）**

1. **System instructions**——只读静态段。包含控制流说明、各内存层的用途、所有 MemGPT 函数的 schema。这里相当于"内核 ABI 文档"，告诉 LLM 怎样发"系统调用"。
2. **Working context**——固定大小的可读可写文本块，**只能通过 MemGPT 函数修改**，不能在普通生成里直接覆盖。在对话场景里用于存"关于用户的关键事实、偏好、当前 persona"。这是 MemGPT 唯一一个**持久驻留 prompt** 的语义记忆区。
3. **FIFO queue**——滚动消息历史（user/agent 消息、系统消息、函数调用 I/O）。**第一条永远是"已被驱逐消息的递归摘要"系统消息**，保证 LLM 永远有一个 lossy 的全局视角。

**External context（out-of-context，两类数据库，需显式 page in）**

4. **Recall storage**——message database。所有进出的消息（包括 FIFO 已驱逐的）都被队列管理器写到这里；可被 MemGPT 函数检索回来，检索到的消息**会被追加到 FIFO 队尾重新进入上下文**。
5. **Archival storage**——任意长度文本对象的读写数据库。论文实现用 PostgreSQL + pgvector + HNSW 做向量检索；用于长文档/大知识库（如 Wikipedia dump）。

机制含义与写规则边界：
- "想让某事不被忘"有两个槽位：写进 working context（保证每次 prompt 都看到），或写进 archival（需要时主动 search）。**两者语义不同**——前者是 prompt-resident 长期事实，后者是 demand-paged 大语料。
- recall ≠ archival：recall 是"会话历史的可逆驱逐缓存"，archival 是"任意文本的命中性数据库"。论文里这种区分被反复用：例如 DMR 对话评估靠 recall；DocQA 任务靠 archival 上 OpenAI embedding。
- LLM **无法**绕过函数直接读 external context——任何外部数据进入 LLM 视野必须有显式函数调用。这一硬约束让"调度行为 ↔ 实际看到的内容"始终可解释。

误用：把所有用户事实直接堆进 working context 会迅速吃满 prompt；把高频引用事实放进 archival 又会增加每次 query 的 LLM 调用与延迟。正确分层依赖于"事实频率 + 持久性"判断。

## References

MemGPT 论文 §2 (MemGPT 节) 子节 "Main context" 与"Function executor"明确分区与写规则；§intro 图 7 系统流图也展示这五个区。

- 源路径：`data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`（method 行 1633–1648 main/external 与 working context；行 1639–1642 三段主上下文；行 1646 第一条总是 recursive summary；DocQA archival 用 pgvector 行 1460）。

## Footnotes

- 三段定义原文（行 1641）："The prompt tokens in MemGPT are split into three contiguous sections: the system instructions, working context, and FIFO Queue."
- working context 只能函数写（行 1641）："Working context is a fixed-size read/write block of unstructured text, writeable only via MemGPT function calls."
- recursive summary 永远占位（行 1642）："The first index in the FIFO queue stores a system message containing a recursive summary of messages that have been evicted from the queue."
- archival 用 PG + pgvector + HNSW（行 1460）："We use MemGPT's default storage settings which uses PostgreSQL for archival memory storage with vector search enabled via the pgvector extention. We pre-compute embeddings and load them into the database, which uses an HNSW index to enable approximate, sub-second query times."
