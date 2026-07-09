---
id: memgpt-nested-kv-retrieval
title: MemGPT 嵌套 KV 检索的多跳优势
status: draft
card_type: empirical-result
tags: [memgpt, nested-kv, multi-hop, uuid-lookup, function-chaining]
created_time: 2026-06-12T10:17:00+08:00
edited_time: 2026-06-12T10:17:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: peer-reviewed
justification: ../justification/experiment/memgpt-nested-kv-retrieval.md
canonical_concept: nested-kv-multi-hop-retrieval
aliases: [嵌套KV检索, nested KV retrieval, multi-hop lookup, UUID lookup]
summary: >-
  MemGPT nested-kv-multi-hop-retrieval 在嵌套 KV 任务中仅 MemGPT+GPT-4 不受嵌套层数（0-4层）影响；GPT-4/GPT-4Turbo baseline 在 3 层达 0%，GPT-3.5 在 1 层达 0%；MemGPT+GPT-4 Turbo 反而不如 GPT-4。
related: [memgpt-function-chaining, memgpt-context-window-vs-agency-tradeoff, memgpt-llm-capability-dependency]
---

Nested KV retrieval 是论文引入的新任务，基于 Liu et al. 的合成 KV 任务扩展：每个 key 和 value 是 128-bit UUID，value 可能本身也是 key，需要 multi-hop lookup。设置固定 140 UUID pairs（~8k tokens），nesting levels 从 0 到 4 变化，每层 30 个随机配置。[^src-1]

**Baseline 表现**：
- GPT-3.5：1 层嵌套即 0%（主要失败模式是直接返回第一个 value）
- GPT-4 / GPT-4 Turbo：3 层嵌套达 0%[^src-1]

**MemGPT 表现**：
- MemGPT + GPT-4：不受嵌套层数影响，通过 function chaining 反复查询直到 value 不再是 key
- MemGPT + GPT-4 Turbo / GPT-3.5：优于对应 baseline 但 2 层后开始下降（"failing to perform enough lookups"）[^src-1]

**反直觉发现**：MemGPT+GPT-4 Turbo 在此任务中不如 MemGPT+GPT-4。然而，论文仅报告现象未深入分析原因，这一反转暗示更大上下文窗口可能与 agent 主动使用函数的倾向之间存在负相关——模型"觉得"答案应该在上下文中时就不触发函数调用。[^src-2]

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Nested KV -- "MemGPT with GPT-4 on the other hand is unaffected with the number of nesting levels and is able to perform the nested lookup by accessing the key-value pairs stored in main context repeatedly via function queries."
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Nested KV -- "While GPT-4 Turbo performs better as a baseline, MemGPT with GPT-4 Turbo performs worse than MemGPT with GPT-4."
[^card-1]: -> memgpt-context-window-vs-agency-tradeoff -- 本卡报告 nested KV 实验结果，该卡分析该实验揭示的上下文大小与 agent 主动性之间的 tradeoff
[^card-2]: -> memgpt-function-chaining -- 本卡展示 function chaining 在 nested KV 中的应用效果，该卡描述 function chaining 的通用机制
