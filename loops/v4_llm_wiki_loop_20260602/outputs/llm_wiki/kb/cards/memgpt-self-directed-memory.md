---
id: memgpt-self-directed-memory
title: MemGPT 自主内存编辑与检索
status: accepted
card_type: mechanism
tags: [LLM, self_directed, memory_editing, function_calling, feedback_loop, MemGPT]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
justification: ../justification/memgpt-self-directed-memory.md
canonical_concept: memgpt-self-directed-memory
aliases: [自主内存管理, self-directed memory editing, LLM自编辑内存]
summary: >-
  memgpt-self-directed-memory（自主内存编辑, self-directed memory editing）LLM 处理器输出被解析为函数调用，自主决定何时在上下文层级间移动数据、更新 working context、搜索 archival/recall storage；函数执行结果（含运行时错误）反馈回 LLM 形成闭环，分页机制防止检索溢出
related: [memgpt-memory-hierarchy, memgpt-function-chaining, memgpt-queue-eviction-policy]
---

MemGPT 中的内存编辑和检索完全由 LLM 自主驱动（self-directed）：MemGPT 基于当前上下文自主地更新和搜索自己的内存 [^src-1]。

**实现方式**：在每个推理周期中，LLM 处理器以主上下文（拼接为单一字符串）作为输入，生成输出字符串。该输出被 MemGPT 解析以确保正确性；如果解析器验证了函数参数，则执行该函数。执行结果（包括运行时错误，例如尝试在主上下文已满时添加内容）被反馈给处理器，形成闭环，使系统能够从自己的行为中学习并相应调整 [^src-2]。

**指导机制**：通过在系统指令中提供两个主要组件来实现自主编辑和检索：(1) 内存层次结构及其各自用途的详细描述；(2) 函数 schema（附带自然语言描述），系统可调用这些函数来访问或修改内存 [^src-3]。

**溢出保护**：内存检索机制设计为感知 token 限制，并实现分页（pagination）以防止检索调用溢出上下文窗口 [^src-4]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/method_rewrite.tex -- "Memory edits and retrieval are entirely self-directed: MemGPT autonomously updates and searches through its own memory based on the current context."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/method_rewrite.tex -- "The results, including any runtime errors that occur (e.g. trying to add to main context when it is already at maximum capacity), are then fed back to the processor by MemGPT. This feedback loop enables the system to learn from its actions and adjust its behavior accordingly."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/method_rewrite.tex -- "We implement self-directed editing and retrieval by providing explicit instructions within the system instructions that guide the LLM on how to interact with the MemGPT memory systems."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/method_rewrite.tex -- "our memory retrieval mechanisms are designed to be cognizant of these token constraints and implement pagination to prevent retrieval calls from overflowing the context window."
