---
id: memgpt-self-directed-memory
title: MemGPT 自主内存编辑机制
status: accepted
card_type: mechanism
tags:
- llm-agent
- self-editing
- function-calling
- autonomous-memory
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-memgpt
evidence_basis: experimental_paper
justification: ../justification/memgpt-self-directed-memory.md
canonical_concept: memgpt-self-directed-memory
aliases:
- self-directed memory editing
- 自主内存编辑
- self-directed memory management
- MemGPT function executor
summary: 'MemGPT memgpt-self-directed-memory 自主内存编辑 通过函数执行器(function executor) 实现LLM对自身内存的完全自主管理: LLM processor生成的输出被解析为函数调用, 执行后结果反馈给processor形成闭环。系统指令中提供内存层级描述和函数schema引导LLM使用内存。 运行时错误(如上下文已满)也作为反馈返回,
  使系统能从自身行为中学习调整。 内存编辑完全自我驱动, 无需用户干预。'
related:
- memgpt-function-chaining
- memgpt-memory-hierarchy
- memgpt-deep-memory-retrieval
- memgpt-doc-qa-context-invariance
---
MemGPT 通过函数执行器 (function executor) 实现完全自我驱动的内存管理机制。在每个推理周期中，LLM processor 将主上下文作为输入生成输出字符串，该字符串被 MemGPT 解析以确保正确性，验证通过后执行对应函数。[^src-1]

内存编辑和检索完全是自我导向的（self-directed）：MemGPT 基于当前上下文自主更新和搜索其内存。例如，它可以在对话历史过长时决定在上下文之间移动数据项，也可以修改其主上下文以更好地反映其对当前目标和职责的理解。[^src-1]

实现自我导向编辑的关键是系统指令中的两个组成部分：
1. 内存层级及其用途的详细描述
2. 函数 schema（含自然语言描述），系统可通过调用这些函数访问或修改内存 [^src-1]

执行结果（包括运行时错误，如尝试向已满的主上下文添加内容）被反馈给 processor，形成闭环学习。MemGPT 还通过 token 限制警告提示 processor 进行内存管理决策，检索机制实现了分页以防止单次检索溢出上下文窗口。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/method_rewrite.tex" -- "Memory edits and retrieval are entirely self-directed: MemGPT autonomously updates and searches through its own memory based on the current context"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/method_rewrite.tex" -- "The results, including any runtime errors that occur (e.g. trying to add to main context when it is already at maximum capacity), are then fed back to the processor by MemGPT. This feedback loop enables the system to learn from its actions and adjust its behavior accordingly"
[^card-1]: [memgpt-memory-hierarchy] 自主编辑操作的目标是内存层级中的各个层
[^card-2]: [memgpt-function-chaining] 函数链机制使多步自主编辑成为可能
