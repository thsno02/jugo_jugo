---
id: memgpt-nested-kv-retrieval
title: MemGPT 嵌套键值检索与多跳能力
status: accepted
card_type: source_claim
tags: [LLM, evaluation, multi_hop, nested_kv, document_analysis, MemGPT]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
justification: ../justification/memgpt-nested-kv-retrieval.md
canonical_concept: memgpt-nested-kv-retrieval
aliases: [嵌套键值检索, nested KV retrieval, 多跳查找]
summary: >-
  memgpt-nested-kv-retrieval（嵌套键值检索, nested KV retrieval, 多跳查找）扩展了 KV 检索任务使 value 可能也是 key 需要多跳查找；MemGPT+GPT-4 在 0-4 层嵌套中性能稳定，而 GPT-4/GPT-4 Turbo 基线在 3 层嵌套时降至 0%，证明函数链支撑多步信息汇集能力
related: [memgpt-function-chaining, memgpt-document-qa-scaling, memgpt-self-directed-memory]
---

MemGPT 论文提出嵌套键值检索（nested KV retrieval）任务，扩展了原始 KV 检索任务 [^src-1]。在原始任务中，每个键和值都是 128 位 UUID，代理需要返回给定键的关联值。在嵌套变体中，值本身可能也是键，因此需要执行多跳查找 [^src-1]。

**实验设置**：固定 140 对 UUID（约 8k tokens），嵌套层级从 0（无嵌套）到 4（需要 4 次 KV 查找），每个配置采样 30 种不同排列 [^src-2]。

**关键结果** [^src-3]：
- GPT-3.5 基线在 1 层嵌套时即降至 0%（主要失败模式：直接返回原始值）
- GPT-4 和 GPT-4 Turbo 基线在 3 层嵌套时降至 0%
- MemGPT + GPT-4 在所有嵌套层级上性能稳定不受影响
- MemGPT + GPT-4 Turbo 和 GPT-3.5 在 2 层嵌套开始下降（因未执行足够多的查找）

值得注意的是 MemGPT + GPT-4 Turbo 反而比 MemGPT + GPT-4 表现更差，表明更长的上下文窗口并不总是带来更好的代理行为 [^src-4]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/experiments.tex -- "We create a version of the KV task, nested KV retrieval, where values themselves may be keys, thus requiring the agent to perform a multi-hop lookup."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/experiments.tex -- "we fix the total number of UUIDs pairs to 140, corresponding to roughly 8k tokens...We vary the total number of nesting levels from 0...to 4"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/experiments.tex -- "MemGPT with GPT-4 on the other hand is unaffected with the number of nesting levels...GPT-4 and GPT-4 Turbo are better than GPT-3.5, but also suffer from a similar dropoff, and hit 0 percent accuracy by 3 nesting levels."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Figure 4 caption -- "While GPT-4 Turbo performs better as a baseline, MemGPT with GPT-4 Turbo performs worse than MemGPT with GPT-4."
