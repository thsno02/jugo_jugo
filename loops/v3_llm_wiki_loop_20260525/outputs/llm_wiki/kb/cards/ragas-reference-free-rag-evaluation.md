---
id: ragas-reference-free-rag-evaluation
title: Ragas 框架：无需 ground truth 也能评估 RAG 的三维度自动评测
status: accepted
card_type: concept
tags: [#rag-evaluation, #ragas, #reference-free, #llm-as-judge]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-28T16:10:00+08:00
edited_entity: llm
source_ids: [arxiv-ragas]
provenance_card: ../provenance/ragas-reference-free-rag-evaluation.md
aliases: [Retrieval Augmented Generation Assessment, RAGAS, reference-free RAG metrics]
related: [ragas-faithfulness-metric, ragas-answer-relevance-metric, ragas-context-relevance-metric, ragas-wikieval-dataset, ares-three-judge-rag-evaluation, alce-three-dimension-citation-metric, ragchecker-generator-trilemma]
---

## 框架定位

Shahul Es 等（2023, Exploding Gradients + CardiffNLP，EMNLP 2023）提出 **Ragas**（Retrieval Augmented Generation Assessment），一个**不依赖人工 ground truth 答案**的 RAG 系统自动评测框架[^src1]。其核心动机是：在 RAG 工程实践里，调一次检索器、换一个 LM、改一段 prompt 就要重测一遍，等不起人工标注；只要评测指标可以由 LLM 自动算出，迭代周期就能跨数量级压缩。

## 三个被评测的维度

Ragas 把 RAG 质量正交分解为三个 reference-free 指标[^src2]：

1. **Faithfulness（忠实度）**[^v3-1]：生成的 answer 是否能从 retrieved context 中推出？防的是 hallucination。
2. **Answer Relevance（答案相关度）**[^v3-2]：answer 是否完整、聚焦地回应了 question 本身？这里**不考虑事实性**，只考虑是否冗余 / 不完整。
3. **Context Relevance（上下文相关度）**[^v3-3]：retrieved context 是否聚焦于回答 question 所需的信息？这条决定 token 成本与"中间内容被忽略"风险。

三个指标对应 RAG pipeline 的三个独立失效点（生成端 / 答案塑形端 / 检索端），可单独诊断。

横向对照：ARES 同样把 RAG 拆成 *C.R. / A.F. / A.R.* 三个独立判官[^v3-5]，对应几乎一致——区别在于 ARES 训独立 DeBERTa 判官 + PPI 置信区间，Ragas 用 pure prompt + LLM-as-judge。ALCE 走 *fluency / correctness / citation quality* 另一条三维度路线[^v3-6]，侧重 long-form 带引用。RAGChecker 进一步在 generator 端拆出 *faithfulness × context utilization × noise sensitivity* 三难[^v3-7]——四套体系都在"用一维分数会被作弊、必须多维互相牵制"上收敛。

## 关键设计选择

- **完全用 prompt 调 LLM 做评判**：所有指标在论文实现里都用 `gpt-3.5-turbo-16k`，不需要训练任何分类器。
- **不要求 reference answer**：与 BERTScore / BARTScore / MoverScore 等基于参考答案的指标互补，适合"我们刚搭好 RAG，还没有人工标注集"的场景。
- **生态整合**：原生集成 LlamaIndex 与 LangChain，让指标可以挂到现有 RAG 评测循环里[^src4]。

## 边界 / 误用条件

- 三个指标都依赖 judge LLM 的能力上限——judge 自身的 hallucination / bias 会传染到评测结果。
- Answer Relevance 不衡量事实性；如果一个答案"完整聚焦但全错"，AR 可能仍然高，必须和 Faithfulness 联用。
- Context Relevance 在长 context 上是论文里准确率最低的维度（70% agreement）[^src3]，因为 judge 难以从长文本里挑出 crucial 句子；评估者不应把单独的 CR 数字当强信号。
- 框架不评 latency / cost / safety 等系统级指标。
- 框架的有效性靠 WikiEval[^v3-4] 50 题 pairwise 标注验证——单一小数据集，跨域泛化未在论文 scope 内。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt:87` — "we put forward a suite of metrics which can be used to evaluate these different dimensions without having to rely on ground truth human annotations."
[^src2]: 同文件 `:117-122`（关键 `:119-120`） — "Faithfulness refers to the idea that the answer should be grounded in the given context... Answer Relevance refers to the idea that the generated answer should address the actual question... Context Relevance refers to the idea that the retrieved context should be focused..."
[^src3]: 同文件 `:238-242` Table 1 — Ragas 在三指标上的 accuracy 分别为 0.95 / 0.78 / 0.70，全面优于 GPT Score / GPT Ranking baseline。
[^src4]: 同文件 `:98` — Ragas 原生集成 LlamaIndex 与 LangChain。
[^v3-1]: [ragas-faithfulness-metric](ragas-faithfulness-metric.md) — Faithfulness 指标的算法（statement decomposition + verification）与 0.95 一致率。
[^v3-2]: [ragas-answer-relevance-metric](ragas-answer-relevance-metric.md) — Answer Relevance 指标的反推 + embedding 相似度算法。
[^v3-3]: [ragas-context-relevance-metric](ragas-context-relevance-metric.md) — Context Relevance 指标的句子级抽取 + 占比算法。
[^v3-4]: [ragas-wikieval-dataset](ragas-wikieval-dataset.md) — 验证 Ragas 三指标的 50 题人工 pairwise 数据集。
[^v3-5]: [ares-three-judge-rag-evaluation](ares-three-judge-rag-evaluation.md) — ARES 的 C.R. / A.F. / A.R. 三判官对应 Ragas 三维度，差别在 fine-tuned 判官 vs pure prompt。
[^v3-6]: [alce-three-dimension-citation-metric](alce-three-dimension-citation-metric.md) — ALCE 的 fluency / correctness / citation quality 三维度路线。
[^v3-7]: [ragchecker-generator-trilemma](ragchecker-generator-trilemma.md) — RAGChecker 在 generator 端细化为 faithfulness × context utilization × noise sensitivity 三难。
