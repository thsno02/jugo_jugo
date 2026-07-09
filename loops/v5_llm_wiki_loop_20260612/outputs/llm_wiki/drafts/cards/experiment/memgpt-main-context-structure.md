---
id: memgpt-main-context-structure
title: MemGPT 主上下文三段结构
status: draft
card_type: architecture
tags: [memgpt, main-context, system-instructions, working-context, fifo-queue]
created_time: 2026-06-12T10:01:00+08:00
edited_time: 2026-06-12T10:01:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: peer-reviewed
justification: ../justification/experiment/memgpt-main-context-structure.md
canonical_concept: memgpt-main-context
aliases: [主上下文, main context, prompt tokens structure]
summary: >-
  MemGPT memgpt-main-context 将 prompt tokens 分为 system instructions（只读）、working context（固定大小读写块）、FIFO queue（滚动消息历史+recursive summary）三个连续区段。
related: [memgpt-virtual-context-management, memgpt-working-context-usage, memgpt-queue-eviction-policy]
---

MemGPT 的 main context（即 LLM 的 prompt tokens）被划分为三个连续区段：

1. **System instructions**（只读/静态）：包含 MemGPT 控制流描述、内存层级用途说明、函数 schema 及其自然语言描述。为 LLM 提供如何与内存系统交互的指导。[^src-1]

2. **Working context**（固定大小 read/write 块）：仅通过 MemGPT 函数调用可写入的非结构化文本区域。在对话场景中存储关于用户和 agent persona 的关键事实、偏好等。[^src-1]

3. **FIFO Queue**（滚动消息历史）：存储用户消息、agent 回复、系统消息、函数调用输入输出。队列第一个 index 始终存放一条包含已驱逐消息的 recursive summary 的系统消息。[^src-1]

然而，这种固定分区设计存在 tradeoff：system instructions 占据的 token 是固定开销（论文未量化但暗示非平凡），working context 大小固定意味着可存储的关键信息量有上限——若用户交互信息超出 working context 容量，LLM 需要将溢出信息转存到 archival storage，增加了后续检索的复杂性和延迟。[^src-2]

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Main context (prompt tokens) -- "The prompt tokens in MemGPT are split into three contiguous sections: the system instructions, working context, and FIFO Queue."
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Function executor -- "runtime errors that occur (e.g. trying to add to main context when it is already at maximum capacity)"
[^card-1]: -> memgpt-virtual-context-management -- 本卡聚焦 main context 内部结构，该卡聚焦虚拟上下文管理的整体数据流动机制
[^card-2]: -> memgpt-queue-eviction-policy -- 本卡描述 FIFO queue 的静态结构，该卡聚焦 queue 溢出时的动态驱逐策略
