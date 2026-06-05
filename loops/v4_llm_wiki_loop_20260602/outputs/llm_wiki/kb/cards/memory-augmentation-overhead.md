---
id: memory-augmentation-overhead
title: LLM 记忆系统的开销问题
status: accepted
card_type: source_claim
tags: [memory-system, overhead, efficiency, llm-limitation, stateless-interaction]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-lightmem]
justification: ../justification/memory-augmentation-overhead.md
canonical_concept: memory-augmentation-overhead
aliases: [记忆系统开销, memory system overhead, 记忆增强计算代价]
summary: >-
  memory-augmentation-overhead（记忆系统开销, memory system overhead, 记忆增强计算代价）现有 LLM 记忆系统虽使模型超越无状态交互，但普遍引入大量时间和计算开销，成为记忆增强生成的核心瓶颈。
related: [lightmem-three-stage-memory, sleep-time-memory-consolidation, context-window-degradation]
---

大语言模型在动态和复杂环境中难以有效利用历史交互信息 [^src-1]。记忆系统（memory systems）的引入使 LLM 能够超越无状态交互（stateless interactions），提供持久化的信息存储、检索和利用机制 [^src-2]。

然而，现有的记忆系统普遍带来显著的时间和计算开销（substantial time and computational overhead）[^src-3]。这一开销问题构成了记忆增强生成领域的核心瓶颈：系统在提升模型利用历史信息能力的同时，也大幅增加了推理成本。

LightMem 的实验数据从侧面量化了这一问题的严重程度：与 strong baselines 相比，LightMem 在保持甚至提升准确率的前提下，将 token 使用量降低了最多 38 倍，API 调用次数降低了最多 55.5 倍 [^src-4]。这意味着此前的基线系统在 token 消耗和 API 调用上存在一到两个数量级的冗余。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-lightmem/text.txt` -- Abstract -- "Large Language Models (LLMs) struggle to effectively leverage historical interaction information in dynamic and complex environments"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-lightmem/text.txt` -- Abstract -- "Memory systems enable LLMs to move beyond stateless interactions by introducing persistent information storage, retrieval, and utilization mechanisms"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-lightmem/text.txt` -- Abstract -- "existing memory systems often introduce substantial time and computational overhead"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-lightmem/text.txt` -- Abstract -- "reducing total token usage by up to 38x / 20.9x and API calls by up to 30x / 55.5x"
