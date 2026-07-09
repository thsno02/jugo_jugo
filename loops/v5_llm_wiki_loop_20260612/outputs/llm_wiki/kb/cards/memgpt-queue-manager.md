---
id: memgpt-queue-manager
title: MemGPT 队列管理器与驱逐策略
status: accepted
card_type: mechanism
tags:
- llm-memory
- context-eviction
- summarization
- fifo
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-memgpt
evidence_basis: experimental_paper
justification: ../justification/memgpt-queue-manager.md
canonical_concept: memgpt-queue-manager
aliases:
- MemGPT queue manager
- 队列管理器
- queue eviction policy
- memory pressure warning
summary: 'MemGPT memgpt-queue-manager 队列管理器 管理FIFO队列和recall storage之间的消息流动。 当prompt tokens超过warning token count(如70%上下文窗口)时插入memory pressure警告, 让LLM有机会保存重要信息; 当超过flush token count(如100%)时执行队列驱逐: 驱逐约50%消息,
  生成新的递归摘要, 被驱逐消息存入recall storage可通过函数调用检索。'
related:
- memgpt-main-context-structure
- memgpt-function-chaining
- memgpt-archival-recall-storage
- memgpt-event-driven-control-flow
---
Queue Manager (队列管理器) 负责管理 **recall storage** (消息数据库) 和 **FIFO 队列**之间的消息流动。[^src-1]

**正常流程**: 当新消息到达系统时，queue manager 将其追加到 FIFO 队列，拼接 prompt tokens 并触发 LLM 推理。Queue manager 同时将传入消息和生成的 LLM 输出写入 recall storage。当通过函数调用检索 recall storage 中的消息时，queue manager 将它们追加到队列尾部以重新插入 LLM 上下文窗口。[^src-1]

**驱逐策略** (queue eviction policy): 采用两阶段触发机制 -- [^src-1]
1. **Warning 阶段**: 当 prompt tokens 超过底层 LLM 上下文窗口的 "warning token count"（如 70%）时，queue manager 插入一条系统消息警告 LLM 即将发生队列驱逐（"memory pressure" 警告），允许 LLM 使用函数将 FIFO 队列中的重要信息存储到 working context 或 archival storage。
2. **Flush 阶段**: 当 prompt tokens 超过 "flush token count"（如 100%）时，queue manager 执行队列刷新 -- 驱逐特定数量的消息（如 50%），并使用已有的递归摘要加上被驱逐消息生成新的递归摘要。被驱逐的消息不再 in-context，但永久存储在 recall storage 中，可通过函数调用读取。

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/method_rewrite.tex" -- "The queue manager is also responsible for controlling context overflow via a queue eviction policy. When the prompt tokens exceed the 'warning token count'..."
[^card-1]: [memgpt-main-context-structure] FIFO 队列是主上下文的第三段
