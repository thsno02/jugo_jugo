---
id: memgpt-function-chaining
title: MemGPT 函数链与心跳标志机制
status: draft
card_type: mechanism
tags: [memgpt, function-chaining, heartbeat, multi-step-retrieval, control-flow]
created_time: 2026-06-12T10:07:00+08:00
edited_time: 2026-06-12T10:07:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: peer-reviewed
justification: ../justification/experiment/memgpt-function-chaining.md
canonical_concept: function-chaining-heartbeat
aliases: [函数链, function chaining, heartbeat flag, request_heartbeat, multi-step retrieval]
summary: >-
  MemGPT function-chaining-heartbeat 通过 request_heartbeat=true 标志实现多步函数调用：flag 存在时函数完成后立即触发下一次 LLM 推理而非暂停，flag 不存在（yield）则等待下一外部事件。
related: [memgpt-virtual-context-management, memgpt-event-driven-control-flow, memgpt-nested-kv-retrieval]
---

MemGPT 的函数链（function chaining）机制允许 LLM processor 在返回用户响应之前连续执行多个函数调用：

- 函数调用时附带特殊 keyword argument `request_heartbeat=true`，请求函数执行完毕后立即将控制权返回 LLM processor（而非暂停等待外部事件）[^src-1]
- 若 flag 存在，MemGPT 将函数输出加入 main context 并立即触发新一轮 LLM 推理
- 若 flag 不存在（yield），MemGPT 不运行 processor 直到下一个外部事件触发（如用户消息或定时中断）

这一机制使得需要多步操作的任务成为可能：翻页浏览检索结果、从不同文档拼凑信息、nested KV lookup 中的迭代查询。[^src-1] 论文 Figure 2 展示了 MemGPT 通过多次 archival storage 查询来回答问题的流程。

然而，function chaining 的实际有效性受限于 LLM 是否"愿意"持续链式调用。论文在 nested KV 任务中观察到 MemGPT+GPT-4 Turbo 和 GPT-3.5 "failing to perform enough lookups"——说明 LLM 可能在应该继续链式调用时提前 yield，导致任务失败。[^src-2]

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Control flow and function chaining -- "Function chaining allows MemGPT to execute multiple function calls sequentially before returning control to the user."
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Nested KV -- "still begin to drop off in performance at 2 nesting levels as a result of failing to perform enough lookups"
[^card-1]: -> memgpt-event-driven-control-flow -- 本卡聚焦函数链的连续调用机制，该卡描述触发 LLM 推理的事件类型
[^card-2]: -> memgpt-nested-kv-retrieval -- 本卡描述函数链的通用机制，该卡展示函数链在 nested KV 任务中的具体应用
