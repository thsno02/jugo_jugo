---
id: memgpt-queue-eviction-policy
title: MemGPT 两阶段队列驱逐策略
status: draft
card_type: mechanism
tags: [memgpt, eviction-policy, memory-pressure, queue-manager, context-overflow]
created_time: 2026-06-12T10:02:00+08:00
edited_time: 2026-06-12T10:02:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: peer-reviewed
justification: ../justification/experiment/memgpt-queue-eviction-policy.md
canonical_concept: queue-eviction-policy
aliases: [队列驱逐策略, eviction policy, memory pressure warning, context flush]
summary: >-
  MemGPT queue-eviction-policy 采用 warning（~70%占用）+ flush（~100%占用）两阶段策略管理上下文溢出：先警告 LLM 主动保存重要信息，再强制驱逐并生成 recursive summary。
related: [memgpt-main-context-structure, memgpt-recursive-summary-limitations]
---

MemGPT 的 Queue Manager 通过两阶段策略管理 FIFO Queue 的上下文溢出：

**阶段 1 — Memory Pressure Warning**：当 prompt tokens 超过底层 LLM 上下文窗口的 "warning token count"（如 70%）时，queue manager 向队列插入一条系统消息警告 LLM 即将发生驱逐，允许 LLM 使用函数调用将队列中的重要信息主动保存到 working context 或 archival storage。[^src-1]

**阶段 2 — Flush**：当 prompt tokens 超过 "flush token count"（如 100%）时，queue manager 强制驱逐特定数量的消息（如占上下文窗口 50% 的消息），并使用"现有 recursive summary + 被驱逐消息"生成新的 recursive summary。被驱逐消息不再 in-context，但永久存储于 recall storage，可通过函数调用读取。[^src-1]

然而，这一策略的有效性依赖 LLM 在收到 warning 后的响应质量——如果 LLM 未能在 flush 前正确识别和保存关键信息，这些信息将仅以有损 summary 形式存在。论文中 DMR baseline 使用的"lossy summarization"性能远低于 MemGPT，间接说明 summary 的信息损失是显著的，但 MemGPT 自身的 recursive summary 也面临同样的信息压缩 tradeoff。[^src-2]

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Queue Manager -- "When the prompt tokens exceed the 'warning token count'... the queue manager inserts a system message into the queue warning the LLM of an impending queue eviction"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: DMR -- "The baselines are able to see a lossy summarization of the past five conversations"
[^card-1]: -> memgpt-recursive-summary-limitations -- 本卡聚焦驱逐策略的两阶段流程，该卡聚焦 recursive summary 的信息损失问题
[^card-2]: -> memgpt-main-context-structure -- 本卡描述 queue 溢出的动态管理，该卡描述 main context 的静态结构
