---
id: locomo-observation-rag-beats-summary-rag
title: RAG 检索单元用"observation"比 session 摘要更适合长对话 QA
status: draft
card_type: operational_rule
tags: [#rag, #long-term-memory, #retrieval-granularity]
created_time: 2026-05-26T14:15:00+08:00
edited_time: 2026-05-26T14:15:00+08:00
edited_entity: llm
source_ids: [arxiv-locomo]
provenance_card: ../provenance/locomo-observation-rag-beats-summary-rag.md
aliases: [observation 检索, RAG 单元粒度]
related: [locomo-three-task-evaluation-framework, longmemeval-key-expansion-with-facts, locomo-long-context-adversarial-collapse, longmemeval-three-stage-memory-framework]
---

## 规则

在 LoCoMo 上对比三种 RAG 检索单元（在 `gpt-3.5-turbo-16k` 作 reader 时）：

| 检索单元 | top-k | F1 overall | 关键观察 |
|---|---|---|---|
| Dialog（原始对话片段） | 25 | 35.8 | recall 高（79.9），但需要大 k |
| **Observation**（个人陈述 / assertion） | 5 | **41.4** | 用 5 条就拿到最高 F1，且 adversarial 升到 44.7 |
| Summary（session 摘要） | 5 | 32.5 | recall 高（75-90），但 F1 始终落后 |

因此实操结论：

1. **小 k 用 observation**。当只能塞少量上下文进 reader 时，把对话先抽成"关于说话人的 assertion"再检索，是当时最优解（GPT-3.5-turbo 提升 ~5% over baseline）。
2. **observation 不是"k 越大越好"**。observation 数从 5 涨到 50，F1 反而从 41.4 掉到 37.8——多出来的 observation 充当噪声，提高 SNR 比扩大召回更重要。
3. **session 摘要在 QA 里几乎没用**。recall 看着很高（top-10 召回 90.7），但 reader 实际答题分数最差——把对话压缩成摘要时损失的细节正是 QA 答案所在。
4. **dialog 单元只有在大 k 才追得上 observation**。dialog top-50 才达到 F1 34.8，仍低于 observation top-5 的 41.4。

## 为什么这样

- Observation 是"关于一个说话人的单一断言"，本身就把对话语义抽到了"问题-答案"可对齐的颗粒度，因此 reader 拿 5 条就能回答；session summary 把这种断言糅合成段，丢的是细节。
- "more retrieval ≠ better RAG"在长对话场景被放大：reader 反而更怕被无关 observation 干扰。

## 边界

- 这条规则建立在 `gpt-3.5-turbo-16k` 作 reader 的实验上；更强 reader（如 GPT-4o）的曲线可能不同，论文未在 LoCoMo 上覆盖。
- Observation 抽取依赖一次额外 LLM 调用 + 必须把答案 turn-id 带进 observation 以做证据追溯——这增加 indexing 成本。

## References

- 三粒度对比表：`data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` 第 407-423 行（表 2 完整数据）。
- 解读："There is a noticeable 5\% improvement with $\texttt{gpt-3.5-turbo}$ when the input is top 5 relevant observations instead of pure conversation logs. This improvement falters with an increase in the number of retrieved observations, suggesting that it is important to reduce the signal-to-noise (SNR) ratio in retrieved contexts."（第 445 行）

## Footnotes

- Summary 检索失败的原因："Conversely, using session summaries as context does not significantly improve the performance despite high recall accuracies, likely due to loss of information during the conversion of dialogs to summaries."（第 445 行）
- Observation 定义："a database of \textit{observations} (assertions about each speaker; see \Sref{ssec:llm-agent})"（第 346 行）。
