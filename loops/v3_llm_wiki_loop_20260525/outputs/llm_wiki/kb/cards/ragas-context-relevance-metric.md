---
id: ragas-context-relevance-metric
title: Ragas Context Relevance：让 LLM 抽出 crucial 句子，再算占比
status: accepted
card_type: mechanism
tags: [#ragas, #context-relevance, #rag-evaluation, #retrieval-quality]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-28T16:05:00+08:00
edited_entity: llm
source_ids: [arxiv-ragas]
provenance_card: ../provenance/ragas-context-relevance-metric.md
aliases: [context relevance, CR metric, sentence extraction ratio]
related: [ragas-reference-free-rag-evaluation, ragas-faithfulness-metric, ragas-answer-relevance-metric, ragas-wikieval-dataset, alce-retriever-and-context-utilization-gap, ragchecker-retriever-claim-vs-chunk-precision]
---

## 算法

Shahul Es 等（2023）的 Context Relevance 用一个**句子级抽取 + 占比**思路[^src1]：

1. 给定 question $q$ 与 retrieved context $c(q)$，让 LLM 跑 prompt："Please extract relevant sentences from the provided context that can potentially help answer the following question. If no relevant sentences are found, or if you believe the question cannot be answered from the given context, return the phrase 'Insufficient Information'. While extracting candidate sentences you're not allowed to make any changes to sentences from given context."[^src2]
2. 得到子集 $S_{ext} \subseteq c(q)$。
3. 计算[^src3]：

$$
\text{CR} = \frac{|S_{ext}|}{|\text{total sentences in } c(q)|}
$$

CR 越高，说明 retrieved context 里"对回答这个问题真正有用"的句子占比越高，反过来即冗余越少。

## 设计要点

- **不改写抽取**：prompt 显式要求不许改原句，保证 $|S_{ext}|$ 是精确可计数的句子数。
- **Insufficient Information 出口**：当 context 整体无关时，让 LLM 返回特定字符串，作为"分母前的特判"，避免被迫挑出无关句。
- **方向**：CR 高 = retrieval 聚焦；CR 低 = retrieval 召回了一堆装饰性内容，token 浪费 + "lost in the middle" 风险（论文引用 Liu et al. 2023[^url1]）。

## 为什么这个指标重要

- token 成本：context 越长越贵，CR 直接量化 retrieval 阶段引入的"无效 token"。
- 注意力分配：长 context 中位置靠中间的关键信息容易被 LLM 忽略；CR 低意味着重要信息被冗余句子稀释。ALCE 实测 ChatGPT-16K 加更多 passage 反而不涨[^v3-3]，正是 CR 低 + lost-in-the-middle 共同造成。
- pipeline 诊断：F 低但 CR 高 → 生成阶段问题；F 低且 CR 低 → 检索阶段问题[^v3-2]。

## 边界 / 已知弱点

- WikiEval[^v3-5] 上 Ragas CR 一致率仅 **0.70**，是三个指标中最低；论文承认 "ChatGPT often struggles with the task of selecting the sentences from the context that are crucial, especially for longer contexts"[^src4]。
- CR 是**句子级**指标：如果同一信息被同义句重复 3 次，分子分母都会被推高，比例可能掩盖冗余。
- 论文公式里只用一次抽取（非多次采样）；早期草稿曾试图引入 sentence-level BERTScore 多次抽取的"sentence agreement score"，但最终发表版本去掉了。
- RAGChecker 走另一条路：把 retriever metric 拆为 *claim recall (claim-level)* 与 *context precision (chunk-level)* 的非对称组合[^v3-4]，避开"sentence-level 重复同义句"的失真；ARES 则用 fine-tuned DeBERTa 判官[^v3-6]测同一概念。横向看 Ragas CR 是"句子级 + 单次 LLM 抽取"的最简形态。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt:172-182` 算法关键 `:173` — "given a question q and its context c(q), the LLM extracts a subset of sentences, S_ext, from c(q) that are crucial to answer q"。
[^src2]: 同文件 `:175-176` — Context Relevance 的完整抽取 prompt（含 "Insufficient Information" 出口）。
[^src3]: 同文件 `:181-182` — "CR = (number of extracted sentences) / (total number of sentences in c(q))" 公式。
[^src4]: 同文件 `:271` — "We found context relevance to be the hardest quality dimension to evaluate. In particular, we observed that ChatGPT often struggles with the task of selecting the sentences from the context that are crucial, especially for longer contexts."；WikiEval 一致率 0.70 见 `:238-244`。
[^url1]: <https://arxiv.org/abs/2307.03172> — Liu et al. 2023, "Lost in the Middle: How Language Models Use Long Contexts"，原文 `:120` 引用。
[^v3-1]: [ragas-reference-free-rag-evaluation](ragas-reference-free-rag-evaluation.md) — Ragas 三维度框架，CR 是其中"检索端"的指标。
[^v3-2]: [ragas-faithfulness-metric](ragas-faithfulness-metric.md) — F 低 + CR 高 → 生成端问题；F 低 + CR 低 → 检索端问题。
[^v3-3]: [alce-retriever-and-context-utilization-gap](alce-retriever-and-context-utilization-gap.md) — ChatGPT-16K 加更多 passage 反而不涨的实测，是 CR 低 + lost-in-the-middle 联合造成的下游表现。
[^v3-4]: [ragchecker-retriever-claim-vs-chunk-precision](ragchecker-retriever-claim-vs-chunk-precision.md) — RAGChecker 把 retriever 评估拆成 claim-level recall + chunk-level precision，避开 sentence-level 同义句重复失真。
[^v3-5]: [ragas-wikieval-dataset](ragas-wikieval-dataset.md) — CR 一致率 0.70 所测的 50 题 pairwise 数据集；低 CR 样本通过"反链注水"context 构造。
[^v3-6]: [ares-three-judge-rag-evaluation](ares-three-judge-rag-evaluation.md) — ARES 的 Context Relevance 判官走 fine-tuned DeBERTa 路线测同一概念。
