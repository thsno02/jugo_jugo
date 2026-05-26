---
id: ragas-wikieval-dataset
title: WikiEval：为验证 reference-free RAG 指标而构造的 50 题 Wikipedia 数据集
status: draft
card_type: example_pattern
tags: [#ragas, #wikieval, #benchmark, #evaluation-data]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragas]
provenance_card: ../provenance/ragas-wikieval-dataset.md
aliases: [WikiEval, Ragas 验证数据集]
related: [ragas-reference-free-rag-evaluation, ragas-faithfulness-metric, ragas-answer-relevance-metric, ragas-context-relevance-metric]
---

## 数据集动机与构造

Shahul Es 等（2023）为了验证 Ragas 三个指标"和人类判断一致"，从零构造了 **WikiEval**（50 题，Hugging Face 上公开）。设计思路非常工程化：

1. 选 50 篇 **2022 年后**有更新的 Wikipedia 页面（绕开 GPT-3.5 训练截止）。
2. 用 ChatGPT 从每篇页面 introductory section 出一道**中等难度、非琐碎、不含链接、自包含**的问题；提示词显式列出 6 条出题规则。
3. 用 ChatGPT 用 introductory section 作为 context 给出"标准答案"。
4. 两名标注者沿三维度做 **pairwise** 标注：faithfulness / answer relevance / context relevance；标注者间一致率 ~95% / ~95% / ~90%；分歧讨论后解决。

## 三维度对照样本的构造手法（巧妙之处）

为了得到"高 vs 低"的 pairwise 对照样本，作者**针对每个维度都设计了一个具体生成方法**：

- **Faithfulness**：让 ChatGPT 在**无 context** 时回答同一个问题，然后请标注者比较有 context 答案 vs 无 context 答案哪个更忠实。
- **Answer Relevance**：用专门 prompt "Answer the given question in an incomplete manner." 生成低相关度 answer，让标注者与正常 answer 比较。
- **Context Relevance**：通过爬 Wikipedia 页的反链（back-links）人工"注水"context；少数页面没有反链时用 ChatGPT 补全 context。

## 与流行 QA 数据集的区别

- WikiEval 不评 short extractive answer 的"对错"——它评的是**长答案的质量维度对齐**，与 SQuAD 类基准方向正交。
- 数据规模小（50 题）但**标注精度高**，是典型的 metric validation 数据集而非 model training 数据集。
- pairwise 格式让评测可以直接用 accuracy 报告，避免在小样本上做绝对分数比较。

## 操作含义（给后续 RAG 指标研究者）

- 想引入一个新的 reference-free 指标？至少需要一个**人工标注的 pairwise 对照集**才能宣称"与人类一致"。Ragas 给了一个最小可行模板。
- 选时间窗在训练截止之后的 Wikipedia 页是规避"模型已经背过答案"的可复用 trick。
- "高 vs 低"样本最好通过**改变生成过程**（无 context / 不完整 prompt / 反链注水）来制造，而不是从已有错例里挑——前者保证维度纯净度。

## References

- 数据集构造：`data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt:200-231`。
- 三维度对照样本表：`agent_source_bundle.txt:297-352`（Tables 5/6/7）。
- HuggingFace 链接：`agent_source_bundle.txt:201` footnote。

## Footnotes

- 数据集规模与时间窗：`agent_source_bundle.txt:201` —— "we first selected 50 Wikipedia pages covering events that have happened since the start of 2022"。
- 出题规则原文：`agent_source_bundle.txt:204-211` —— "1. The question should be fully answered from the given context... 4. The question should be of moderate difficulty..."
- 标注一致率：`agent_source_bundle.txt:218` —— "For faithfulness and context relevance, the two annotators agreed in around 95% of cases. For answer relevance, they agreed in around 90% of the cases."
- 三维度低质量样本构造原文：`agent_source_bundle.txt:220-229`。
