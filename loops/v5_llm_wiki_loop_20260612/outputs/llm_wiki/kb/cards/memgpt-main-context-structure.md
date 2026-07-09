---
id: memgpt-main-context-structure
title: MemGPT 主上下文三段式结构
status: accepted
card_type: system-component
tags:
- llm-memory
- prompt-engineering
- context-management
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-memgpt
evidence_basis: experimental_paper
justification: ../justification/memgpt-main-context-structure.md
canonical_concept: memgpt-main-context-structure
aliases:
- MemGPT main context
- MemGPT prompt tokens structure
- 主上下文结构
summary: 'MemGPT memgpt-main-context-structure 主上下文三段式结构 将prompt tokens划分为三个连续段: (1) system instructions(只读/静态, 含控制流说明和函数schema), (2) working context(固定大小读写块, 仅通过函数调用写入, 存储关键事实和偏好), (3) FIFO queue(滚动消息历史,
  含对话/系统消息/函数IO, 首位存递归摘要)。'
related:
- memgpt-memory-hierarchy
- memgpt-queue-manager
- memgpt-conversation-opener-engagement
---
MemGPT 的主上下文 (prompt tokens) 被划分为三个连续段落 (contiguous sections)：[^src-1]

1. **System Instructions** (系统指令) -- 只读/静态区域，包含 MemGPT 控制流信息、不同内存层级的预期用法说明，以及函数 schema（含自然语言描述）的使用指引。[^src-1]

2. **Working Context** (工作上下文) -- 固定大小的读写块，存储非结构化文本，仅可通过 MemGPT 函数调用进行写入。在对话场景中，该区域用于存储关于用户和 agent 所扮演角色的关键事实、偏好和其他重要信息，使 agent 能流畅地与用户对话。[^src-1]

3. **FIFO Queue** (先进先出队列) -- 存储滚动消息历史，包括 agent 与用户之间的消息、系统消息（如内存警告）以及函数调用的输入输出。队列的第一个索引位置存储一条系统消息，包含被驱逐消息的递归摘要。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/method_rewrite.tex" -- "The prompt tokens in MemGPT are split into three contiguous sections: the system instructions, working context, and FIFO Queue"
[^card-1]: [memgpt-memory-hierarchy] 主上下文是内存层级中的"主内存"层
