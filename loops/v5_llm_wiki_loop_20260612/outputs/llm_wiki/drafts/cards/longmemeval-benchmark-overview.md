---
id: longmemeval-benchmark-overview
title: LongMemEval 长期记忆基准概览
status: draft
card_type: benchmark
tags: [long-term-memory, chat-assistant, evaluation, benchmark, ICLR-2025]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-longmemeval]
evidence_basis: code_implementation
justification: ../justification/longmemeval-benchmark-overview.md
canonical_concept: longmemeval-benchmark
aliases: [LongMemEval, long-mem-eval, LongMemEval benchmark]
summary: >-
  LongMemEval (longmemeval-benchmark) 是一个测试对话助手长期记忆能力的综合基准,
  发表于 ICLR 2025, 包含 500 道高质量问题, 测试五种核心能力: Information Extraction,
  Multi-Session Reasoning, Knowledge Updates, Temporal Reasoning, Abstention.
  受 needle-in-a-haystack 启发设计属性控制管线编排可扩展带时间戳对话历史.
related: [longmemeval-five-memory-abilities, longmemeval-dataset-variants]
---

LongMemEval 是一个综合、高难度、可扩展的基准，用于测试对话助手的长期记忆能力。[^src-1]

该基准包含 500 道高质量问题，覆盖五种核心长期记忆能力：Information Extraction、Multi-Session Reasoning、Knowledge Updates、Temporal Reasoning 和 Abstention。[^src-2]

受 needle-in-a-haystack 测试启发，LongMemEval 设计了属性控制管线（attribute-controlled pipeline）编排连贯、可扩展、带时间戳的对话历史。系统要求聊天系统在线解析动态交互以进行记忆存储，并在所有交互会话结束后回答问题。[^src-3]

该工作由 Di Wu、Hongwei Wang、Wenhao Yu、Yuwei Zhang、Kai-Wei Chang 和 Dong Yu 完成，被 ICLR 2025 接收。[^src-4]

[^src-1]: data/raw/github_repo/repo-longmemeval/repo/README.md -- "LongMemEval Overview" P1 -- "We introduce LongMemEval, a comprehensive, challenging, and scalable benchmark for testing the long-term memory of chat assistants."
[^src-2]: data/raw/github_repo/repo-longmemeval/repo/README.md -- "LongMemEval Overview" P2 -- "We release 500 high quality questions to test five core long-term memory abilities"
[^src-3]: data/raw/github_repo/repo-longmemeval/repo/README.md -- "LongMemEval Overview" P3 -- "Inspired by the 'needle-in-a-haystack' test, we design an attribute-controlled pipeline to compile a coherent, extensible, and timestamped chat history for each question."
[^src-4]: data/raw/github_repo/repo-longmemeval/repo/README.md -- "News" P1 -- "LongMemEval is accepted at ICLR 2025."
