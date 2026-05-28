---
id: ragas-answer-relevance-metric
title: Ragas Answer Relevance：让 LLM 从 answer 反推 question，再用 embedding 算相似度
status: accepted
card_type: mechanism
tags: [#ragas, #answer-relevance, #embedding, #rag-evaluation]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-28T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragas]
provenance_card: ../provenance/ragas-answer-relevance-metric.md
aliases: [answer relevance, AR metric, 反推问句相似度]
related: [ragas-reference-free-rag-evaluation, ragas-faithfulness-metric, ragas-wikieval-dataset, ares-three-judge-rag-evaluation]
---

## 算法（反推 + 相似度）

Shahul Es 等（2023）的 Answer Relevance 用一个**反向**思路：

1. 用 LLM 在仅看 `a_s(q)`（不看原始 question）的条件下，生成 $n$ 条 "如果让我猜，这个答案是在回答什么问题" 的潜在问句 $q_i$，prompt 为 "Generate a question for the given answer."[^src2]。
2. 用 `text-embedding-ada-002` 计算每个 $q_i$ 与原始 question $q$ 的余弦相似度 $\text{sim}(q, q_i)$。
3. 取平均[^src3]：

$$
\text{AR} = \frac{1}{n} \sum_{i=1}^{n} \text{sim}(q, q_i)
$$

## 直觉

- 一个**对题**的 answer，其反推出来的问题应该和原 question 高度相似。
- 一个**跑题或冗余**的 answer，反推出来的问题会偏离原 question——因为反推时 LLM 会把答案里多余的内容也当成"被回答的东西"。
- 这个指标**不衡量事实性**：只要答案在结构上 / 主题上对题，AR 可以高[^src1]。

## 为什么用 embedding 相似度而非 LLM judge

- 反推出的 $q_i$ 通常是自然语句，embedding 相似度可以稳定地比较与 $q$ 的语义距离。
- 用 LLM 再 judge "$q$ 与 $q_i$ 是不是同一个问题"会引入第二层 prompt 敏感性；embedding 的 cosine 更具确定性。
- 多次采样 $n$ 条 $q_i$ 取均值，是对 LLM 反推随机性的方差抑制。

## 实证表现 & 边界

- WikiEval[^v3-3] 上 Ragas AR 一致率 **0.78**，仍优于 GPT Score（0.52）和 GPT Ranking（0.40），但比 Faithfulness 的 0.95 低[^src4]。论文解释："the agreement is lower, but this is largely due to the fact that the differences between the two candidate answers are often very subtle"（line 271）。
- **必须与 Faithfulness 联用**[^v3-2]：AR 高 + F 低 = "答得很对题但内容不实"；只看 AR 会误导决策。
- 反推 prompt 把"answer 完全跑题"和"answer 包含冗余主题"两类失败混在一起判，无法细分。
- embedding 选型（ada-002）会影响绝对分数；跨论文比较 AR 必须固定 embedding 模型。
- ARES 的 *Answer Relevance* 判官[^v3-4]测的是同一概念但走 fine-tuned DeBERTa 判官路线，不依赖 embedding；二者在 NQ 上 τ ≈ 1.0 可以对照看。Ragas 三指标的总框架在 [ragas-reference-free-rag-evaluation](ragas-reference-free-rag-evaluation.md)[^v3-1]。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt:151` — "our assessment of answer relevance does not take into account factuality, but penalises cases where the answer is incomplete or where it contains redundant information."
[^src2]: 同文件 `:150-164`（关键 `:153-156`） — "Generate a question for the given answer. answer: [answer]" 反推 prompt。
[^src3]: 同文件 `:160-162` — "AR = (1/n) Σ sim(q, q_i)" 公式。
[^src4]: 同文件 `:238-242` — WikiEval Table 1，Ragas AR vs GPT Score / GPT Ranking（0.78 / 0.52 / 0.40）。
[^v3-1]: [ragas-reference-free-rag-evaluation](ragas-reference-free-rag-evaluation.md) — Ragas 三维度框架，AR 是其中"答案塑形端"的指标。
[^v3-2]: [ragas-faithfulness-metric](ragas-faithfulness-metric.md) — Faithfulness 与 AR 必须联用：F 测内容真假、AR 测主题对题。
[^v3-3]: [ragas-wikieval-dataset](ragas-wikieval-dataset.md) — AR 一致率 0.78 所测的 50 题 pairwise 数据集；构造低 AR 样本的具体手法是 "Answer the given question in an incomplete manner." prompt。
[^v3-4]: [ares-three-judge-rag-evaluation](ares-three-judge-rag-evaluation.md) — ARES 的 A.R. 判官测同一概念但走 fine-tuned DeBERTa 路线。
