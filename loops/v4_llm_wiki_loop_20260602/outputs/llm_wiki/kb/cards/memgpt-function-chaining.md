---
id: memgpt-function-chaining
title: MemGPT 函数链与心跳机制
status: accepted
card_type: mechanism
tags: [LLM, function_calling, control_flow, multi_step_retrieval, MemGPT]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
justification: ../justification/memgpt-function-chaining.md
canonical_concept: memgpt-function-chaining
aliases: [函数链, function chaining, request_heartbeat, 心跳标志, yield]
summary: >-
  memgpt-function-chaining（函数链, request_heartbeat）通过 request_heartbeat=true 标志让函数执行后立即将控制权交回 LLM 处理器而非等待下一个外部事件，实现多步连续函数调用，支持分页浏览搜索结果和跨文档信息汇集
related: [memgpt-event-driven-control-flow, memgpt-nested-kv-retrieval, memgpt-self-directed-memory]
---

MemGPT 的函数链（function chaining）机制解决了许多实际任务需要连续调用多个函数的需求，例如浏览搜索结果的多个分页，或从不同文档中汇集信息 [^src-1]。

实现方式：函数可以附带一个特殊标志（request_heartbeat=true），请求在函数执行完成后将控制权立即交回 LLM 处理器。如果该标志存在，MemGPT 将函数输出追加到主上下文并立即触发下一次 LLM 推理（而非暂停执行）[^src-2]。如果该标志不存在（即"yield"），MemGPT 不会运行 LLM 处理器，直到下一个外部事件触发（例如用户消息或定时中断）[^src-3]。

这一机制是 MemGPT 能够执行多步检索回答用户查询的关键：LLM 可以在一次用户交互中连续发起多次搜索、翻页、比较和整合信息，最终才将控制权交还给用户 [^src-4]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/method_rewrite.tex -- "Many practical tasks require calling multiple functions in sequence, for example, navigating through multiple pages of results from a single query or collating data from different documents"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/method_rewrite.tex -- "In MemGPT, functions can be called with a special flag that requests control be immediately returned to the processor after the requested function completes execution."
[^src-3]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/method_rewrite.tex -- "If this flag is not present (a yield), MemGPT will not run the LLM processor until the next external event trigger"
[^src-4]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Figure 2 caption -- "The LLM can request immediate follow-up LLM inference to chain function calls together by generating a special keyword argument (request_heartbeat=true)...function chaining is what allows MemGPT to perform multi-step retrieval to answer user queries."
