---
id: longmemeval-time-aware-query-expansion
title: 时间感知的索引与 query 扩展能把 temporal 召回提 6.8-11.3%
status: accepted
card_type: mechanism
tags: [#temporal-reasoning, #query-expansion, #rag]
created_time: 2026-05-26T14:40:00+08:00
edited_time: 2026-05-28T10:42:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
provenance_card: ../provenance/longmemeval-time-aware-query-expansion.md
aliases: [time-aware indexing, temporal query expansion]
related: [longmemeval-five-core-memory-abilities, longmemeval-key-expansion-with-facts, longmemeval-three-stage-memory-framework, zep-bi-temporal-edges, mem0-graph-memory-variant]
---

## 机制

针对 LongMemEval 五能力[^v3-1]里的 temporal reasoning（TR），普通 dense retrieval 通常崩——因为 query "上个月推荐的餐厅"对应的 evidence session 在向量空间里和"普通餐厅推荐"几乎重叠。LongMemEval §5.3 给出 **时间感知的双侧改造**[^src1]，对应 LongMemEval 三阶段框架中 CP3 Query 的最优落点[^v3-2]：

1. **Indexing 侧**：除了普通 key（V 或 V+fact），额外让一个 LLM $\mathcal{M}_T$ 从每条 value 抽取"带时间戳的事件" $\{(date_i, event_i)\}$，写入一条平行 index。
2. **Retrieval 侧**：对于带时间引用的 query，$\mathcal{M}_T$ 再从 query 推断一个时间区间 `{start, end}`（如"哪家航空在 3、4 月飞最多"→ `2023/03/01~2023/04/30`）[^src2]。该区间用来**过滤** value 池，剩下的再做向量相似度排序。

效果：

- Value=round 时 recall 平均 +11.3%；Value=session 时 +6.8%[^src3]。
- key 用 V+fact 拼接时，时间过滤的收益仍稳定（不会与 key expansion 冲突）[^v3-3]。

## 关键边界——必须用强 LLM 抽时间

论文比较 GPT-4o vs Llama 3.1 8B Instruct 作 $\mathcal{M}_T$[^src4]：

- GPT-4o 能在 query 不含时间引用时**拒绝输出区间**（输出 N/A），避免无谓压缩搜索空间[^src5]。
- Llama 3.1 8B 即使给了 10 个 in-context examples，仍会对"How long had I been taking guitar lessons when I bought the new guitar amp?"等 query 错误地猜出一个区间（false positive）[^src6]，从而把 recall 拉低。
- 因此该机制依赖 reasoning 较强的 LLM 来"知道什么时候不抽时间"。

## 误用

- 不要把时间过滤当 hard pruning 用——若 query 的时间引用本身错（如用户说"上周"实际指上个月），过滤会直接漏掉证据。论文做法是**只在 query 含明确时间引用时**才启用过滤。
- 时间区间过滤只解决"知道在哪段时间找"，不解决"时间区间内仍有多条候选"——所以它与 fact-augmented key expansion[^v3-3] 是正交、可叠加的优化。
- 与 Zep 的 bi-temporal edges 思路相比，这里只用"时间区间过滤"，不显式刻画事件 valid_at 与 ingested_at 的二维时间[^v3-4]。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 第 1504-1510 行（§5.3 query 章节）— 时间感知双侧改造机制描述。
[^src2]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 第 129-143 行（`fig:temporal-query-prompt` 完整 prompt 文本）— 时间抽取 prompt。
[^src3]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 第 1510 行 — "this simple design improves recall by an average of 11.3\% when using rounds as the value and by 6.8\% when using sessions as the value."
[^src4]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 第 1757-1759 行 + 第 1199-1219 行（query-expansion 例子表）— 强弱 LLM 对比。
[^src5]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 第 139 行（prompt 原文）— "If the question does not have any temporal referencea, do not attempt to guess a time range. Instead, just say N/A."
[^src6]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` — 第 1198-1201 行 — "How long had I been taking guitar lessons when I bought the new guitar amp? ... Predicted time range (Llama 3.1 8B Instruct): 2023/05/01$\sim$2023/05/28 [false positive]"。
[^v3-1]: [longmemeval-five-core-memory-abilities](longmemeval-five-core-memory-abilities.md) — TR 在五能力中的定义。
[^v3-2]: [longmemeval-three-stage-memory-framework](longmemeval-three-stage-memory-framework.md) — 该机制是 CP3 Query 的最优落点。
[^v3-3]: [longmemeval-key-expansion-with-facts](longmemeval-key-expansion-with-facts.md) — fact-augmented key expansion 是正交、可叠加的优化。
[^v3-4]: [zep-bi-temporal-edges](zep-bi-temporal-edges.md) — Zep 用 bi-temporal edges 更显式地刻画时间维度。
