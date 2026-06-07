---
id: memgpt-main-context-structure
title: MemGPT 主上下文三段式结构
status: accepted
card_type: mechanism
tags: [LLM, prompt_engineering, system_instructions, working_context, FIFO_queue, MemGPT]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
justification: ../justification/memgpt-main-context-structure.md
canonical_concept: memgpt-main-context-structure
aliases: [主上下文结构, prompt tokens三段, system instructions + working context + FIFO queue]
summary: >-
  memgpt-main-context-structure（主上下文三段式结构）将 LLM prompt tokens 分为 system instructions（只读，控制流与函数说明）、working context（固定大小读写块，存储关键事实）、FIFO queue（滚动消息历史，首位存递归摘要），三者拼接为单一输入
related: [memgpt-memory-hierarchy, memgpt-queue-eviction-policy]
---

MemGPT 将主上下文（prompt tokens）划分为三个连续段 [^src-1]：

1. **系统指令（system instructions）**：只读（静态）区域，包含 MemGPT 控制流信息、各内存层级的预期用途说明、以及如何使用 MemGPT 函数（例如如何检索 out-of-context 数据）的指令 [^src-1]。

2. **工作上下文（working context）**：固定大小的读写块，存储非结构化文本，仅可通过 MemGPT 函数调用写入。在对话场景中，用于存储关于用户和 agent 角色的关键事实、偏好和其他重要信息，使 agent 能够流畅地与用户对话 [^src-1]。

3. **FIFO 队列（FIFO queue）**：存储滚动的消息历史，包括 agent-用户消息、系统消息（如内存警告）、以及函数调用的输入和输出。队列的第一个位置存储一条系统消息，包含已从队列中被驱逐的消息的递归摘要 [^src-2]。

每次推理时，这三个部分被拼接为单一字符串作为 LLM 处理器的输入 [^src-3]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/method_rewrite.tex -- "The prompt tokens in MemGPT are split into three contiguous sections: the system instructions, working context, and FIFO Queue."
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/method_rewrite.tex -- "The first index in the FIFO queue stores a system message containing a recursive summary of messages that have been evicted from the queue."
[^src-3]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/method_rewrite.tex -- "During each inference cycle, LLM processor takes main context (concatenated into a single string) as input"
