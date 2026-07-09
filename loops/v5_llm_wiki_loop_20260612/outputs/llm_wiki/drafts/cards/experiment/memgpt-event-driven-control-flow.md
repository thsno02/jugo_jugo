---
id: memgpt-event-driven-control-flow
title: MemGPT 事件驱动控制流
status: draft
card_type: mechanism
tags: [memgpt, event-driven, control-flow, system-events, timed-events]
created_time: 2026-06-12T10:08:00+08:00
edited_time: 2026-06-12T10:08:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: peer-reviewed
justification: ../justification/experiment/memgpt-event-driven-control-flow.md
canonical_concept: event-driven-control-flow
aliases: [事件驱动控制流, event-driven control flow, event triggers, timed events]
summary: >-
  MemGPT event-driven-control-flow 定义四类事件触发 LLM 推理：用户消息、系统消息（如 memory pressure）、用户交互事件（登录/上传）、定时事件（允许无用户干预的主动运行）。
related: [memgpt-function-chaining, memgpt-queue-eviction-policy]
---

MemGPT 中 LLM 推理由事件（events）触发，事件是系统的广义输入，包含四类：

1. **用户消息**：chat 应用中的用户输入[^src-1]
2. **系统消息**：如 memory pressure warning（上下文即将溢出的警告）[^src-1]
3. **用户交互事件**：如用户登录提醒、文档上传完成通知[^src-1]
4. **定时事件**：按固定时间表运行，允许 MemGPT 在无用户干预情况下"主动"执行操作（unprompted execution）[^src-1]

所有事件经 parser 转换为纯文本消息后追加到 main context，最终作为 LLM processor 的输入。这种统一的事件抽象使得 MemGPT 不仅是被动响应用户的系统，还能主动进行内存维护、数据整理等后台任务。

然而，定时事件机制意味着额外的 LLM 推理成本——每次定时触发都消耗一次完整的 LLM 调用。论文未讨论定时事件的频率设置、成本优化或在实验中的具体使用情况，这些实现细节对实际部署的 cost-effectiveness 至关重要。[^src-1]

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Control flow and function chaining -- "events are generalized inputs to MemGPT and can consist of user messages... system messages... user interactions... and timed events that are run on a regular schedule"
[^card-1]: -> memgpt-function-chaining -- 本卡描述触发推理的事件类型，该卡聚焦推理后函数调用的链式执行机制
