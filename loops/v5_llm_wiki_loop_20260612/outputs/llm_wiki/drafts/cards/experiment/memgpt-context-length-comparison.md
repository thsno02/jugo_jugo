---
id: memgpt-context-length-comparison
title: 主流模型上下文长度对比与 MemGPT 的意义
status: draft
card_type: context
tags: [memgpt, context-length, llama, gpt-4, gpt-3.5, model-comparison]
created_time: 2026-06-12T10:30:00+08:00
edited_time: 2026-06-12T10:30:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: peer-reviewed
justification: ../justification/experiment/memgpt-context-length-comparison.md
canonical_concept: context-length-landscape
aliases: [上下文长度对比, context length comparison, token limits, message capacity]
summary: >-
  MemGPT context-length-landscape 论文统计主流模型上下文（2024年初数据）：Llama1 2k至GPT-4 Turbo 128k至Yi-34B 200k；按50 token/消息估算，8k窗口仅支持~140条消息，凸显长对话场景的固定上下文瓶颈。
related: [memgpt-lost-in-middle-motivation, memgpt-virtual-context-management]
---

论文通过对比主流模型上下文窗口大小来论证 MemGPT 的必要性（数据截至 2024 年 1 月）：

| 模型 | 开源? | Context (tokens) | ~消息数* |
|------|-------|-----------------|----------|
| Llama 1 | Yes | 2k | 20 |
| Llama 2 | Yes | 4k | 60 |
| Mistral 7B | Yes | 8k | 140 |
| GPT-4 (release) | No | 8k | 140 |
| GPT-3.5 Turbo | No | 16k | 300 |
| GPT-4 Turbo | No | 128k | ~2600 |
| Yi-34B-200k | Yes | 200k | ~4000 | [^src-1]

*消息数假设 1k token preprompt + ~50 token/消息（~250 字符）

**论证逻辑**：即使最大的 128k-200k 窗口，在长期对话（数周/数月交互）或大型文档分析（SEC 10-K 可超百万 token）场景下也远远不够。且许多任务需要跨多个长文档推理。[^src-2]

然而，该对比表的时效性有限——论文发表后 Gemini 1.5 Pro 等模型已达到 1M+ context。MemGPT 的价值需要在不断增长的原生上下文能力背景下重新评估。但论文的核心论点（"盲目扩展上下文不是解决方案"，基于 lost-in-the-middle 等 evidence）仍有独立价值。[^src-2]

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Table: context-length-comparison -- context window data for major models
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Document analysis -- "legal or financial documents such as Annual Reports (SEC Form 10-K) can easily pass the million token mark... it becomes difficult to envision blindly scaling up context as a solution"
[^card-1]: -> memgpt-lost-in-middle-motivation -- 本卡提供定量上下文限制数据，该卡补充"即使扩展上下文也不够"的定性论据
