---
id: memgpt-queue-eviction-policy
title: MemGPT 队列驱逐与内存压力机制
status: accepted
card_type: mechanism
tags: [LLM, context_overflow, eviction_policy, memory_pressure, recursive_summary, MemGPT]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
justification: ../justification/memgpt-queue-eviction-policy.md
canonical_concept: memgpt-queue-eviction-policy
aliases: [队列驱逐策略, memory pressure warning, 内存压力警告, queue manager, 队列管理器]
summary: >-
  memgpt-queue-eviction-policy（队列驱逐策略, memory pressure warning, queue manager）在 prompt tokens 达到 warning token count（如 70%）时插入内存压力系统消息让 LLM 主动保存重要信息，达到 flush token count（如 100%）时驱逐消息并生成递归摘要，被驱逐消息存入 recall storage 可后续检索
related: [archive-lifecycle, memgpt-main-context-structure, memgpt-memory-hierarchy, memgpt-self-directed-memory, virtual-context-management]
---

MemGPT 的队列管理器（queue manager）负责处理上下文溢出，采用两阶段驱逐策略 [^src-1]：

**阶段一：内存压力警告。** 当 prompt tokens 超过底层 LLM 上下文窗口的"警告 token 数"（例如上下文窗口的 70%）时，队列管理器向 FIFO 队列插入一条系统消息，警告 LLM 即将发生队列驱逐（"memory pressure" 警告）。这给予 LLM 使用函数调用将 FIFO 队列中的重要信息保存到 working context 或 archival storage 的机会 [^src-1]。

**阶段二：队列刷新。** 当 prompt tokens 超过"刷新 token 数"（例如上下文窗口的 100%）时，队列管理器执行刷新操作：驱逐特定数量的消息（例如上下文窗口的 50%），使用已有的递归摘要和被驱逐消息生成新的递归摘要。被驱逐的消息不再 in-context，但会被无限期存储在 recall storage 中，可通过函数调用读取 [^src-1]。

队列管理器同时负责日常消息管理：接收新消息时追加到 FIFO 队列、触发 LLM 推理、并将消息写入 recall storage（消息数据库）。通过 recall storage 检索的消息会被重新追加到队列末尾，重新进入 LLM 的上下文窗口 [^src-2]。

从 OS 类比角度看，队列驱逐策略是虚拟上下文管理中"分页到磁盘"操作的具体实现[^card-2]。值得注意的是，LLM Wiki 的归档生命周期在知识库层面采用了结构相似的模式——将不活跃的主题移至冷存储并保留检索入口[^card-1]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/method_rewrite.tex -- "When the prompt tokens exceed the 'warning token count'...the queue manager inserts a system message into the queue warning the LLM of an impending queue eviction (a 'memory pressure' warning)...When the prompt tokens exceed the 'flush token count'...the queue manager flushes the queue to free up space"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/method_rewrite.tex -- "When a new message is received by the system, the queue manager appends the incoming messages to the FIFO queue...When messages in recall storage are retrieved via a MemGPT function call, the queue manager appends them to the back of the queue to reinsert them into the LLM's context window."
[^card-1]: [主题归档生命周期](archive-lifecycle.md) -- 本卡在 LLM 运行时上下文层面实现"驱逐到冷存储并保留检索入口"，该卡在知识库主题层面实现类似的分层存储模式
[^card-2]: [虚拟上下文管理](virtual-context-management.md) -- 本卡是虚拟上下文管理的具体驱逐策略实现，该卡是上层的 OS 分页类比概念
