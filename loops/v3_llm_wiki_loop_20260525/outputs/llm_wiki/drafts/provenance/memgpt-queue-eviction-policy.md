---
schema: draft_card_provenance.v3
draft_card: ../cards/memgpt-queue-eviction-policy.md
material_id: arxiv-memgpt
digest_id: digest_arxiv-memgpt
source_paths:
  - data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt
created_time: 2026-05-26T11:30:00+08:00
edited_time: 2026-05-26T11:30:00+08:00
edited_entity: llm
---

## 源证据

- method 行 1646："The queue manager manages messages in recall storage and the FIFO queue. When a new message is received ... the queue manager writes both the incoming message and the generated LLM output to recall storage."
- method 行 1648（完整一段）："The queue manager is also responsible for controlling context overflow via a queue eviction policy. When the prompt tokens exceed the 'warning token count' of the underlying LLM's context window (e.g. 70% of the context window), the queue manager inserts a system message into the queue warning the LLM of an impending queue eviction (a 'memory pressure' warning) ... When the prompt tokens exceed the 'flush token count' (e.g. 100% of the context window), the queue manager flushes the queue to free up space in the context window: the queue manager evicts a specific count of messages (e.g. 50% of the context window), generates a new recursive summary using the existing recursive summary and evicted messages. Once the queue is flushed, the evicted messages are no longer in-context and immediately viewable to the LLM, however they are stored indefinitely in recall storage and readable via MemGPT function calls."
- 行 1642："The first index in the FIFO queue stores a system message containing a recursive summary of messages that have been evicted from the queue."（递归摘要槽位的位置约束）

## 卡片范围是否成立

本卡聚焦"queue manager 的驱逐策略 = 警告水位 + flush 水位 + 递归摘要"。完整流程逐字来自 method 行 1646–1648。"两段式水位避免突然失忆" / "驱逐数量是可调的折中" 是把论文给的"e.g."参数化扩展，仍是论文意图内的工程性表达。"摘要漂移"是基于 recursive summarization 在通用领域已知的限制（且论文也在 introduction 行 1535 引用"baseline 用 recursive summarization 表现差"），不偏离原文。

## 发表门控结果

本轮未运行。

## 备注

- 该卡机制层与 memgpt-main-vs-external-context 互补（结构 vs 流程）。
- 与 v2 可能已有的"context window management"通用卡有重叠，但本卡是 MemGPT 具体实现，应保留。
