---
id: memgpt-nested-kv-retrieval
title: MemGPT 嵌套键值检索任务
status: draft
card_type: experimental-result
tags: [benchmark, multi-hop-retrieval, document-analysis, function-chaining]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: experimental_paper
justification: ../justification/memgpt-nested-kv-retrieval.md
canonical_concept: memgpt-nested-kv-retrieval
aliases: [nested KV retrieval, nested key-value retrieval, 嵌套键值检索, multi-hop KV lookup]
summary: >-
  MemGPT memgpt-nested-kv-retrieval 嵌套键值检索 是基于Liu et al.(2023)的KV检索任务扩展,
  将值本身设为键从而要求多跳查找。固定140对UUID(约8k tokens), 嵌套层数0-4。
  GPT-3.5在嵌套1层即降至0%准确率, GPT-4在3层降至0%,
  而MemGPT+GPT-4不受嵌套层数影响保持性能。该任务验证了函数链(function chaining)
  使MemGPT能通过反复查询主上下文中的KV对执行多跳查找。
related: [memgpt-function-chaining, memgpt-deep-memory-retrieval]
---

嵌套键值检索 (nested KV retrieval) 是 MemGPT 论文提出的新任务，扩展自 Liu et al. (2023) 的合成 KV 检索任务，旨在展示 MemGPT 从多个数据源聚合信息的能力。[^src-1]

**任务设计**: 原始 KV 任务中每个键值均为 128-bit UUID。嵌套版本中，值本身可能也是键，因此要求 agent 执行多跳查找（multi-hop lookup）。实验固定 140 对 UUID（约 8k tokens，即 GPT-4 基线的上下文长度），嵌套层数从 0 到 4 变化，每层采样 30 种不同排列。[^src-1]

**实验结果** (Figure 5): [^src-2]
- GPT-3.5: 无法完成嵌套任务，1 层嵌套即降至 0% 准确率（主要失败模式：直接返回原始值而不做嵌套查找）
- GPT-4 / GPT-4 Turbo: 优于 GPT-3.5 但仍快速衰减，3 层嵌套时降至 0%
- **MemGPT + GPT-4**: 不受嵌套层数影响，通过反复函数查询主上下文中的 KV 对执行嵌套查找
- MemGPT + GPT-4 Turbo / GPT-3.5: 优于对应基线但在 2 层嵌套后仍开始衰减（因未执行足够多的查找）

值得注意的是，MemGPT with GPT-4 Turbo 的表现反而不如 MemGPT with GPT-4。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/experiments.tex" -- "We introduce a new task based on the synthetic Key-Value retrieval proposed in prior work...nested KV retrieval, where values themselves may be keys, thus requiring the agent to perform a multi-hop lookup"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/experiments.tex" -- "MemGPT with GPT-4 on the other hand is unaffected with the number of nesting levels and is able to perform the nested lookup by accessing the key-value pairs stored in main context repeatedly via function queries"
[^card-1]: [memgpt-function-chaining] 嵌套 KV 检索的成功直接依赖 function chaining 机制的多步执行能力
