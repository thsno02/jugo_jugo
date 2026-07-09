---
id: rag-evaluation-motivation
title: RAG 系统评测的动机与现有方法不足
status: draft
card_type: problem-statement
tags: [rag-evaluation, perplexity-limitation, reference-free, closed-model, evaluation-gap]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragas]
evidence_basis: experimental_paper
justification: ../justification/rag-evaluation-motivation.md
canonical_concept: rag-evaluation-gap
aliases: [RAG evaluation gap, RAG 评测困难]
summary: >-
  RAG 系统评测面临多重困难：perplexity 无法预测下游表现且 closed-model 不提供 token probability；
  QA benchmark 通常仅考虑短 extractive answer 不代表实际使用；大多评测方法依赖 ground truth reference answer
  而实际部署时无此数据。RAGAS 论文据此提出 reference-free 自动评测需求。
related: [ragas-framework-overview]
---

RAG 系统的自动化评测面临多重困难，这构成了 RAGAS 框架的设计动机：[^src-1]

1. **Perplexity 局限**: RAG 系统常以 perplexity 评测，但这不总能预测下游任务表现。且 closed-model（如 ChatGPT、GPT-4）不提供 token probability，无法计算 perplexity。[^src-2]

2. **QA 评测局限**: 常用 QA 数据集仅考虑短 extractive answer，不代表 RAG 的实际使用场景。[^src-3]

3. **Reference answer 依赖**: 现有多数评测方法（BERTScore、MoverScore、BARTScore）需要 ground truth reference answer，而实际 RAG 部署时通常没有人工标注数据。[^card-1][^src-4]

4. **多维度评估需求**: RAG 系统表现受检索模型、语料库、LM、prompt 设计等多因素影响，需要覆盖多维度的自动评测。[^src-5]

[^src-1]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Introduction" P243 -- "Automated evaluation of retrieval-augmented systems is thus paramount"
[^src-2]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Introduction" P243 -- "evaluations are not always predictive of downstream performance... probabilities, which are not accessible for some closed models"
[^src-3]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Introduction" P243 -- "only datasets with short extractive answers are considered, which may not be representative"
[^src-4]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Evaluation Strategies" P266 -- "we usually do not have access to human-annotated datasets or reference answers"
[^src-5]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Introduction" P243 -- "the overall performance will be affected by the retrieval model, the considered corpus, the LM, or the prompt formulation"
[^card-1]: 见 [ragas-framework-overview] 框架对这些问题的回应
