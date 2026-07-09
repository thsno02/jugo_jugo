---
id: memgpt-function-chaining
title: MemGPT 函数链与心跳机制
status: draft
card_type: mechanism
tags: [llm-agent, function-calling, control-flow, multi-step-retrieval]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: experimental_paper
justification: ../justification/memgpt-function-chaining.md
canonical_concept: memgpt-function-chaining
aliases: [function chaining, request_heartbeat, 函数链, heartbeat mechanism, 心跳机制]
summary: >-
  MemGPT memgpt-function-chaining 函数链 request_heartbeat 心跳机制允许LLM在单次用户交互中
  连续执行多个函数调用而不将控制权交还用户。LLM在函数输出中附带request_heartbeat=true标志时,
  系统将函数结果追加到主上下文后立即触发下一轮LLM推理; 不带该标志则yield,
  等待下一个外部事件。该机制使多步检索(如翻页、跨文档聚合)成为可能。
related: [memgpt-queue-manager, memgpt-self-directed-memory]
---

MemGPT 中的函数链 (function chaining) 机制允许系统在返回控制权给用户之前，连续执行多个函数调用。这对于许多实际任务至关重要，例如在单次查询中翻阅多页结果，或从不同文档中聚合主上下文中的数据。[^src-1]

实现方式：MemGPT 的函数可以附带一个特殊标志 (`request_heartbeat=true`) 来请求在函数执行完成后立即将控制权返回给 LLM processor。如果该标志存在，MemGPT 将函数输出添加到主上下文后立即触发下一轮推理（而非暂停执行）。如果该标志不存在（即 yield），MemGPT 不会运行 LLM processor 直到下一个外部事件触发（如用户消息或定时中断）。[^src-1]

该机制使 MemGPT 能执行多步检索来回答用户查询，是其在嵌套 KV 检索和文档 QA 任务中表现优异的关键能力。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/method_rewrite.tex" -- "Function chaining allows MemGPT to execute multiple function calls sequentially before returning control to the user...functions can be called with a special flag that requests control be immediately returned to the processor after the requested function completes execution"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "Figure 3 caption" -- "The LLM can request immediate follow-up LLM inference to chain function calls together by generating a special keyword argument (request_heartbeat=true) in its output; function chaining is what allows MemGPT to perform multi-step retrieval to answer user queries"
[^card-1]: [memgpt-queue-manager] 函数链的输出经由 queue manager 追加到 FIFO 队列
