---
schema: accepted_card_provenance.v3
card: ../cards/memgpt-queue-eviction-policy.md
material_id: arxiv-memgpt
digest_id: digest_arxiv-memgpt
source_paths:
  - data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt
draft_card: ../../drafts/cards/memgpt-queue-eviction-policy.md
draft_provenance: ../../drafts/provenance/memgpt-queue-eviction-policy.md
similarity_result: ../../drafts/similarity/memgpt-queue-eviction-policy.json
comparison_provenance: ../../drafts/comparison/memgpt-queue-eviction-policy.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:40:00+08:00
  gate_notes: 6/6 项通过；三段策略与水位参数有 verbatim 出处。
created_time: 2026-05-26T11:30:00+08:00
edited_time: 2026-05-27T14:40:00+08:00
edited_entity: llm
---

## 源证据

- method 行 1646："The queue manager manages messages in recall storage and the FIFO queue. When a new message is received ... the queue manager writes both the incoming message and the generated LLM output to recall storage."
- method 行 1648（完整一段）："The queue manager is also responsible for controlling context overflow via a queue eviction policy. When the prompt tokens exceed the 'warning token count' of the underlying LLM's context window (e.g. 70% of the context window), the queue manager inserts a system message into the queue warning the LLM of an impending queue eviction (a 'memory pressure' warning) ... When the prompt tokens exceed the 'flush token count' (e.g. 100% of the context window), the queue manager flushes the queue to free up space in the context window: the queue manager evicts a specific count of messages (e.g. 50% of the context window), generates a new recursive summary using the existing recursive summary and evicted messages. Once the queue is flushed, the evicted messages are no longer in-context and immediately viewable to the LLM, however they are stored indefinitely in recall storage and readable via MemGPT function calls."
- 行 1642："The first index in the FIFO queue stores a system message containing a recursive summary of messages that have been evicted from the queue."（递归摘要槽位的位置约束）

## 卡片范围是否成立

本卡聚焦"queue manager 的驱逐策略 = 警告水位 + flush 水位 + 递归摘要"。完整流程逐字来自 method 行 1646–1648。"两段式水位避免突然失忆" / "驱逐数量是可调的折中" 是把论文给的"e.g."参数化扩展，仍是论文意图内的工程性表达。"摘要漂移"是基于 recursive summarization 在通用领域已知的限制（且论文也在 introduction 行 1535 引用"baseline 用 recursive summarization 表现差"），不偏离原文。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:40:00+08:00
- 检查要点：
  - 标题已是 operational rule 概念串。
  - 知识密度足：3 步流程、设计动因、操作含义、边界。
  - 源支撑：method 行 1646–1648 verbatim 引用。
  - References + Footnotes 双在；Footnotes 3 条 verbatim。
  - frontmatter 完整；related 含同系列与 LightMem、metabolism 邻接。

## 备注

- 该卡机制层与 memgpt-main-vs-external-context 互补（结构 vs 流程）。
- 与 v2 可能已有的"context window management"通用卡有重叠，但本卡是 MemGPT 具体实现，应保留。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/memgpt-queue-eviction-policy.md`
- draft provenance: `../../drafts/provenance/memgpt-queue-eviction-policy.md`
- similarity: `../../drafts/similarity/memgpt-queue-eviction-policy.json`
- comparison provenance: `../../drafts/comparison/memgpt-queue-eviction-policy.md`
