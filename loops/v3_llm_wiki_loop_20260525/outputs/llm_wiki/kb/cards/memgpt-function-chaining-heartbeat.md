---
id: memgpt-function-chaining-heartbeat
title: MemGPT 的 request_heartbeat 标志位让函数调用可以串成多步检索
status: accepted
card_type: mechanism
tags: [#memgpt, #function-calling, #control-flow, #multi-hop-retrieval]
created_time: 2026-05-26T11:35:00+08:00
edited_time: 2026-05-28T11:06:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
provenance_card: ../provenance/memgpt-function-chaining-heartbeat.md
aliases: [function chaining, heartbeat flag, MemGPT control flow]
related: [memgpt-main-vs-external-context, memgpt-nested-kv-multi-hop, memgpt-docqa-pagination-failure-mode, memgpt-virtual-context-os-analogy, langgraph-tool-runtime-store-access]
---

MemGPT 的事件驱动控制流里，**默认每次函数执行完成后控制权交还用户**（"yield"），等下一个外部事件（user message、scheduled interrupt 等）才再次推理。这对长程任务是不够的——比如分页翻 retriever 的结果、把多份文档的信息拼起来回答一个问题，都需要 LLM 自己接力调多次函数。

解决方案非常简洁：函数调用时可以带一个特殊关键字参数 **`request_heartbeat=true`**。MemGPT 看到这个 flag 就在函数 output 进入 main context 后**立即触发下一次 LLM inference**，而不是 yield 给用户。

这个机制的价值：
- **多跳检索可行**：DocQA 任务里 MemGPT 可以"先 search → 看结果 → 再 search → 直到找到 gold article"，不必把全部 page-K 一次塞进上下文；嵌套 KV 任务可以做多层 lookup（GPT-4 + MemGPT 上做到 4 层嵌套也不掉精度）。
- **保留 yield 语义**：没带 heartbeat 的函数（例如"已经准备好回答用户"的 response 函数）正常 yield，用户不会被 LLM 卡住或独白。
- **统一的事件接口**：events 是 MemGPT 推理的唯一触发源——可以是 user message、system message（内存警告）、user interaction（"用户刚登录"、"文档上传完毕"）、scheduled interrupt（定时事件）。heartbeat 是 events 的一种特殊形式（由 LLM 自身请求），让 MemGPT 能"无外部输入也继续推进"。

操作含义：
- 设计 MemGPT-style agent 时，**所有需要"看到结果再决定下一步"的函数都应该允许带 heartbeat**；
- 不带 heartbeat 的函数应该是"终结性"的——例如向用户输出最终回答；
- 系统说明里要明确告诉 LLM 何时该带 heartbeat、何时不该带，否则模型可能滥用（无限自我循环）或不用（提前 yield）。

边界：
- 没有显式硬性"最大链长"——风险是 LLM 卡在循环里持续 heartbeat。实际部署需要在 MemGPT runtime 层加入步数/预算限制；
- heartbeat 的有效性依赖底层模型对 schema 的遵守。GPT-3.5 在嵌套 KV 任务上"主要失败模式是直接返回原值"——即它没有正确触发多次 lookup，部分原因就是函数调用的可靠性不够。

## References

MemGPT 论文 §"Control flow and function chaining" 与图 1 caption 描述 heartbeat；§experiments 嵌套 KV 验证多跳能力。

- 源路径：`data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`（intro 图 caption 行 1625 描述 heartbeat；method 行 1677–1686 control flow 与 function chaining；experiments 行 1515 GPT-3.5 失败模式）。

## Footnotes

- heartbeat 与函数链原文（method 行 1683–1685）："Function chaining allows MemGPT to execute multiple function calls sequentially before returning control to the user. In MemGPT, functions can be called with a special flag that requests control be immediately returned to the processor after the requested function completes execution. If this flag is present, MemGPT will add the function output to main context and (as opposed to pausing processor execution). If this flag is not present (a yield), MemGPT will not run the LLM processor until the next external event trigger."
- 图 caption 重申（行 1625）："The LLM can request immediate follow-up LLM inference to chain function calls together by generating a special keyword argument (request_heartbeat=true) in its output; function chaining is what allows MemGPT to perform multi-step retrieval to answer user queries."
- events 类型（method 行 1679）："events are generalized inputs to MemGPT and can consist of user messages ... system messages (e.g. main context capacity warnings), user interactions ... and timed events that are run on a regular schedule."
