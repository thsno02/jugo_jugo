---
id: locomo-evaluation-framework
title: LoCoMo 三任务评估框架
status: draft
card_type: framework
tags: [evaluation-benchmark, question-answering, event-summarization, multimodal-dialogue-generation, long-term-memory]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-locomo]
evidence_basis: experimental_paper
justification: ../justification/locomo-evaluation-framework.md
canonical_concept: locomo-evaluation-framework
aliases: [LoCoMo evaluation benchmark, LoCoMo benchmark, 三任务评估框架]
summary: >-
  locomo-evaluation-framework LoCoMo 三任务评估框架，系统度量 LLM 长期对话记忆：(1) QA 任务含5类推理（single-hop 36%/multi-hop 14.6%/temporal 20.6%/open-domain 3.9%/adversarial 24.9%，共7512题），评估记忆召回；(2) event summarization 任务评估因果时间理解，用 FactScore 度量 precision/recall；(3) multimodal dialogue generation 任务评估连贯叙事维持，用 MMRelevance 度量。
related: [locomo-dataset, temporal-event-graph-dialogue, locomo-human-llm-performance-gap, locomo-event-summarization-degradation, locomo-summarization-error-taxonomy, locomo-temporal-reasoning-difficulty]
---

LoCoMo 提出三任务评估框架，分别从不同维度度量模型对长期对话的理解能力。[^src-1]

**任务一：Question Answering（记忆召回）**
涵盖五类推理：single-hop（36%）、multi-hop（14.6%）、temporal reasoning（20.6%）、open-domain knowledge（3.9%）、adversarial（24.9%），合计 7,512 问题。答案尽量直接取自对话原文以简化精确匹配评估，使用 F1 score。[^src-2]

**任务二：Event Summarization（因果时间理解）**
模型需总结指定时间范围内的事件，与 temporal event graph G 对比。采用 FactScore 将参考和生成分解为 atomic facts，计算 precision/recall/F1。事件图中事件密集且含时间/因果互引，难度高于一般摘要任务。[^src-3]

**任务三：Multimodal Dialogue Generation（连贯叙事）**
评估模型是否能基于 persona 和事件持续生成一致的多模态对话。使用 MMRelevance 度量生成对话与 ground truth 的多模态对齐程度。[^src-4] [^card-1]

[^src-1]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "LoCoMo Evaluation Benchmark" -- "we introduce an evaluation benchmark composed of three tasks to assess the accuracy of long-term memory"
[^src-2]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Question Answering Task" -- "we introduce a question-answering task divided into five distinct reasoning categories"
[^src-3]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Event Summarization Task" -- "we employ FactScore, a method that evaluates the factuality of generated text by decomposing both the reference and hypothesis into atomic facts"
[^src-4]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Multi-Modal Dialogue Generation Task" -- "we assess such consistency by measuring how closely the predicted multi-modal dialogues align with the ground truth... quantifying this alignment through MMRelevance"

[^card-1]: 与 [locomo-dataset] 关联——框架建立在该数据集之上
