---
id: ragas-faithfulness-metric
title: Ragas Faithfulness：先把 answer 拆成 statements，再逐条对 context 做 LLM 验证
status: accepted
card_type: mechanism
tags: [#ragas, #faithfulness, #hallucination-detection, #rag-evaluation]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
edited_entity: llm
source_ids: [arxiv-ragas]
provenance_card: ../provenance/ragas-faithfulness-metric.md
aliases: [F = |V| / |S|, statement decomposition, 忠实度指标]
related: [ragas-reference-free-rag-evaluation, ragas-answer-relevance-metric, ragas-context-relevance-metric, ragas-wikieval-dataset, alce-citation-recall-precision-nli, ragchecker-claim-entailment-decomposition, ragchecker-generator-trilemma]
---

## 算法两步走

Shahul Es 等（2023）把 Faithfulness 计算分成两个互不混淆的 prompt 步骤：

1. **Statement Decomposition（语句拆解）**：用 LLM 对 `(question, answer)` 跑 prompt "Given a question and answer, create one or more statements from each sentence in the given answer."，得到 statements 集 $S(a_s(q)) = \{s_1, s_2, ..., s_n\}$。目的是把长句拆成可独立验证的、原子化的断言。
2. **Statement Verification（逐条验证）**：对每个 $s_i$，让 LLM 在给定 $c(q)$ 的条件下判定 "supported by the information present in the context" 是 Yes 还是 No，给出简短解释和 verdict。

最终分数：

$$
F = \frac{|V|}{|S|}
$$

其中 $|V|$ 是被 LLM 判定为 "supported" 的 statement 数，$|S|$ 是 statement 总数。

## 为什么先拆再验证

- 直接问 "this answer is faithful: Yes/No" 把多个独立事实揉成一个判定，失败模式无法定位。
- 拆解后每个 statement 是**原子级断言**，verification 步可以逐条返回 verdict，错误可归因到具体语句；这也让指标对"半对半错"的答案能给出 0.5 之类的中间分数，而非二元。
- 把 generation（拆解）和 NLI（验证）分到两个 prompt 里，遵循"每个 prompt 只问一件事"的工程惯例。

## 实证表现

在 WikiEval 上，Ragas Faithfulness 与人类标注的 pairwise 偏好一致率达 **0.95**，显著优于 GPT Score（0.72）和 GPT Ranking（0.54）。论文称 "the Ragas prediction are in general highly accurate" 对此维度（line 271）。

## 边界 / 误用条件

- "Statement 不被 context 支持"在 verifier 看来等价于"不忠实"，但这其中混合了两种情况：(a) answer 编造了 context 没有的事实（true hallucination）；(b) context 本身就是错的，answer 只是忠实地复述了错事实。Faithfulness 只能检测前者意义下的"对 context 忠实"。
- 拆解步是有损操作：复杂句子里的 anaphora / 上下文依赖在拆解后可能丢失。
- prompt 里包含一个 demonstration（in-context example），未在论文 prompt listing 中展示；不同 demo 会影响拆解粒度。

## References

- 两步算法：`data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt:131-147`。
- 分数公式：`agent_source_bundle.txt:147`。
- 实证结果 0.95：`agent_source_bundle.txt:238-242`。

## Footnotes

- 算法关键句：`agent_source_bundle.txt:133` —— "To estimate faithfulness, we first use an LLM to extract a set of statements, S(as(q)). The aim of this step is to decompose longer sentences into shorter and more focused assertions."
- 验证 prompt 原文：`agent_source_bundle.txt:141` —— "Consider the given context and following statements, then determine whether they are supported by the information present in the context. Provide a brief explanation for each statement before arriving at the verdict (Yes/No)."
- 分数公式原文：`agent_source_bundle.txt:147` —— "The final faithfulness score, F, is then computed as F = |V| / |S|."
