---
id: memgpt-nested-kv-multi-hop
title: 嵌套 KV 基准证明"上下文内多跳"瓶颈不是上下文长度而是迭代查询
status: draft
card_type: example_pattern
tags: [#memgpt, #benchmark, #multi-hop, #nested-kv]
created_time: 2026-05-26T11:40:00+08:00
edited_time: 2026-05-26T11:40:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
provenance_card: ../provenance/memgpt-nested-kv-multi-hop.md
aliases: [nested key-value retrieval, multi-hop lookup benchmark]
related: [memgpt-function-chaining-heartbeat]
---

MemGPT 论文提出的"嵌套 KV 检索 (nested KV retrieval)"是一个**故意把全部数据塞进上下文都解不开**的基准，用来分离"上下文容量"与"多步推理调用"两种能力：

**任务设定**：
- 140 个 UUID 键值对，整批文本约 8k tokens（恰好等于 GPT-4 baseline 的上下文长度）；
- 同一 UUID 既可以是值也可以是另一个键；
- 任务给定一个起始键，要求最终查到一个"不再作为键出现"的终值；
- 嵌套层数从 0 调到 4，每层都需要做一次新查找。

**结果（论文 §experiments 给出）**：
- GPT-3.5 baseline：1 层嵌套直接掉到 0%——典型失败模式是直接返回上一层的值；
- GPT-4 / GPT-4 Turbo baseline：3 层嵌套时掉到 0%；
- **MemGPT + GPT-4**：嵌套层数不影响精度，能稳定完成 4 层 lookup；
- MemGPT + GPT-3.5 / GPT-4 Turbo：比对应 baseline 更好但仍在 2 层左右开始掉，因为函数调用可靠性不够。

为什么这个基准重要：
1. **所有数据都已经在上下文窗口里**——这不是"长上下文不够装"的问题；
2. baseline 失败说明**LLM 内部不能稳定做多跳指针追逐**，这是注意力机制本身的局限；
3. MemGPT 通过 `request_heartbeat=true` **把每次 lookup 显式成一次函数调用**，每次只关心"这次的 key 对应啥"，每次都把结果以新文本的形式刷新进 main context，相当于把 multi-hop 任务**外化成显式的串行子查询**；
4. 这种"外化"也解释了为什么 MemGPT-style agent 在 DocQA 任务上能不受 retriever top-K 截断的限制——它把"再查一次"做成一次显式动作。

操作含义：
- 不要假设"塞进上下文就能多跳"——即使全部信息在 prompt 里，模型仍会失败；
- multi-hop 任务的可靠实现需要 agent 框架把每跳显式化，并保证函数调用可靠（GPT-3.5 级别模型不够）；
- 嵌套 KV 是衡量 agent runtime 中"函数链路 + 状态保持"质量的一个简单尺子。

边界：
- 任务设计是合成的，UUID 比自然语言 entity 难——但这正是测"链路控制"的优势；
- 论文里 MemGPT + GPT-4 Turbo 反而比 MemGPT + GPT-4 差——说明更新的模型在函数协议遵守上未必更稳定（与论文一致："the most sophisticated"模型不一定带来 chaining 更可靠）。

## References

MemGPT 论文 §experiments "Nested key-value retrieval (KV)" 与图 fig:nested_kv_task_results。

- 源路径：`data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`（experiments 行 1511–1516 任务设计与结果；图 caption 行 1475–1481）。

## Footnotes

- 任务结构原文（行 1512）："In our setup, we fix the total number of UUIDs pairs to 140, corresponding to roughly 8k tokens (the context length of our GPT-4 baseline). We vary the total number of nesting levels from 0 ... to 4 ... and sample 30 different ordering configurations."
- baseline 失败模式（行 1515）："GPT-3.5 is unable to complete the nested variant of the task and has an immediate dropoff in performance, hitting 0 percent accuracy at 1 nesting level (we observe that its primary failure mode is to simply returns the original value). GPT-4 and GPT-4 Turbo are better than GPT-3.5, but also suffer from a similar dropoff, and hit 0 percent accuracy by 3 nesting levels."
- MemGPT 表现（行 1515）："MemGPT with GPT-4 on the other hand is unaffected with the number of nesting levels and is able to perform the nested lookup by accessing the key-value pairs stored in main context repeatedly via function queries."
- GPT-4 Turbo 反而较弱（图 caption 行 1478）："While GPT-4 Turbo performs better as a baseline, MemGPT with GPT-4 Turbo performs worse than MemGPT with GPT-4."
