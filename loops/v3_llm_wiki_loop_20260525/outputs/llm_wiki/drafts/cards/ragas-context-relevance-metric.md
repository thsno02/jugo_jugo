---
id: ragas-context-relevance-metric
title: Ragas Context Relevance：让 LLM 抽出 crucial 句子，再算占比
status: draft
card_type: mechanism
tags: [#ragas, #context-relevance, #rag-evaluation, #retrieval-quality]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragas]
provenance_card: ../provenance/ragas-context-relevance-metric.md
aliases: [context relevance, CR metric, sentence extraction ratio]
related: [ragas-reference-free-rag-evaluation, ragas-faithfulness-metric, ragas-answer-relevance-metric, ragas-wikieval-dataset, alce-retriever-and-context-utilization-gap, ragchecker-retriever-claim-vs-chunk-precision]
---

## 算法

Shahul Es 等（2023）的 Context Relevance 用一个**句子级抽取 + 占比**思路：

1. 给定 question $q$ 与 retrieved context $c(q)$，让 LLM 跑 prompt："Please extract relevant sentences from the provided context that can potentially help answer the following question. If no relevant sentences are found, or if you believe the question cannot be answered from the given context, return the phrase 'Insufficient Information'. While extracting candidate sentences you're not allowed to make any changes to sentences from given context."
2. 得到子集 $S_{ext} \subseteq c(q)$。
3. 计算：

$$
\text{CR} = \frac{|S_{ext}|}{|\text{total sentences in } c(q)|}
$$

CR 越高，说明 retrieved context 里"对回答这个问题真正有用"的句子占比越高，反过来即冗余越少。

## 设计要点

- **不改写抽取**：prompt 显式要求不许改原句，保证 $|S_{ext}|$ 是精确可计数的句子数。
- **Insufficient Information 出口**：当 context 整体无关时，让 LLM 返回特定字符串，作为"分母前的特判"，避免被迫挑出无关句。
- **方向**：CR 高 = retrieval 聚焦；CR 低 = retrieval 召回了一堆装饰性内容，token 浪费 + "lost in the middle" 风险（论文引用 Liu et al. 2023）。

## 为什么这个指标重要

- token 成本：context 越长越贵，CR 直接量化 retrieval 阶段引入的"无效 token"。
- 注意力分配：长 context 中位置靠中间的关键信息容易被 LLM 忽略；CR 低意味着重要信息被冗余句子稀释。
- pipeline 诊断：F 低但 CR 高 → 生成阶段问题；F 低且 CR 低 → 检索阶段问题。

## 边界 / 已知弱点

- WikiEval 上 Ragas CR 一致率仅 **0.70**，是三个指标中最低；论文承认 "ChatGPT often struggles with the task of selecting the sentences from the context that are crucial, especially for longer contexts"（line 271）。
- CR 是**句子级**指标：如果同一信息被同义句重复 3 次，分子分母都会被推高，比例可能掩盖冗余。
- 论文公式里只用一次抽取（非多次采样）；早期草稿曾试图引入 sentence-level BERTScore 多次抽取的"sentence agreement score"，但最终发表版本去掉了。

## References

- 算法与公式：`data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt:172-182`。
- 实证 0.70 与解释：`agent_source_bundle.txt:238-244, 271`。
- 与 "lost in the middle" 的关联：`agent_source_bundle.txt:120`（引用 Liu 2023）。

## Footnotes

- 算法原文：`agent_source_bundle.txt:173` —— "given a question q and its context c(q), the LLM extracts a subset of sentences, S_ext, from c(q) that are crucial to answer q"。
- Prompt 原文：`agent_source_bundle.txt:175-176`。
- 公式原文：`agent_source_bundle.txt:181-182` —— "CR = (number of extracted sentences) / (total number of sentences in c(q))"。
- 性能局限原文：`agent_source_bundle.txt:271` —— "We found context relevance to be the hardest quality dimension to evaluate. In particular, we observed that ChatGPT often struggles with the task of selecting the sentences from the context that are crucial, especially for longer contexts."
