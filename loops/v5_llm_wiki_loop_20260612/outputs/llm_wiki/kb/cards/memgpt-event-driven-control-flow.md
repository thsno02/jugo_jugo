---
id: memgpt-event-driven-control-flow
title: MemGPT 事件驱动控制流
status: accepted
card_type: mechanism
tags:
- llm-agent
- event-driven
- control-flow
- system-architecture
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-memgpt
evidence_basis: experimental_paper
justification: ../justification/memgpt-event-driven-control-flow.md
canonical_concept: memgpt-event-driven-control-flow
aliases:
- event-driven control flow
- 事件驱动控制流
- MemGPT events
- MemGPT interrupt system
summary: MemGPT memgpt-event-driven-control-flow 事件驱动控制流 以事件(events)作为触发LLM推理的广义输入, 包括用户消息、系统消息(如上下文容量警告)、用户交互(登录/文档上传提醒)和定时事件(允许无用户干预运行)。 事件经解析器转换为纯文本消息后追加到主上下文。这种设计类比OS中断系统, 使MemGPT能在非用户主动触发时也执行内存管理操作。
related:
- memgpt-function-chaining
- memgpt-queue-manager
---

在 MemGPT 中，**事件** (events) 触发 LLM 推理。事件是 MemGPT 的广义输入，包含多种类型：[^src-1]

- **用户消息** (user messages) -- 聊天应用中的用户输入
- **系统消息** (system messages) -- 如主上下文容量警告（memory pressure warning）
- **用户交互** (user interactions) -- 如用户刚登录的提醒，或完成文档上传的通知
- **定时事件** (timed events) -- 按固定调度运行，允许 MemGPT 在无用户干预下"自发"执行

MemGPT 通过解析器处理事件，将其转换为纯文本消息后追加到主上下文，最终作为输入传递给 LLM processor。[^src-1]

这种事件驱动设计类比于操作系统中的中断系统：不仅用户输入（类比用户态程序请求）触发处理，系统自身的状态变化（类比硬件中断）和定时调度（类比时钟中断）也能触发 LLM 执行。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/method_rewrite.tex" -- "In MemGPT, events trigger LLM inference: events are generalized inputs to MemGPT and can consist of user messages (in chat applications), system messages (e.g. main context capacity warnings), user interactions (e.g. an alert that a user just logged in), and timed events that are run on a regular schedule (allowing MemGPT to run 'unprompted' without user intervention)"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/intro.tex" -- "The combined use of a memory-hierarchy, OS functions and event-based control flow allow MemGPT to handle unbounded context using LLMs that have finite context windows"
[^card-1]: [memgpt-function-chaining] 事件驱动确定何时触发推理，函数链确定单次触发内的多步执行
