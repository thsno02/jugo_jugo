---
id: ragchecker-three-tier-metrics
title: RAGChecker 三层诊断指标体系
status: accepted
card_type: mechanism
tags: [rag, evaluation, metrics, diagnostic, ragchecker]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragchecker]
justification: ../justification/ragchecker-three-tier-metrics.md
canonical_concept: ragchecker-three-tier-metrics
aliases: [RAGChecker三层指标, RAGChecker metric taxonomy, RAG三层诊断指标]
summary: >-
  ragchecker-three-tier-metrics（RAGChecker三层指标 / RAGChecker metric taxonomy / RAG三层诊断指标）RAGChecker 面向用户和开发者两类角色设计三层指标：整体层（precision/recall/F1）、检索器层（claim recall / context precision）、生成器层（faithfulness / noise sensitivity / hallucination / self-knowledge / context utilization），共 11 个基于声明蕴含的指标
related: [claim-level-entailment-evaluation]
---

RAGChecker 的设计原则基于对 RAG 评估框架两类使用者的观察[^src-1]：

1. **用户角色**——关心 RAG 系统的整体性能，需要单一数值指标进行排名和比较。
2. **开发者角色**——需要定位错误来源和改进空间，需要模块级的诊断指标。

由此形成三层指标体系：

**整体层**（Overall Metrics）：在声明级别计算模型回答与标准答案之间的 precision（回答中正确声明的比例）、recall（标准答案中被覆盖声明的比例）和 F1[^src-2]。

**检索器层**（Retriever Metrics）：（1）claim recall——标准答案声明中被检索块覆盖的比例，衡量检索完整性；（2）context precision——包含至少一条标准答案声明的检索块占全部检索块的比例，在块级别而非声明级别定义精度[^src-3]。块级精度的设计考虑是：由于固定大小分块策略，一个块可能同时包含相关和无关信息，因此最优检索器的声明级精度也无法达到 100%。

**生成器层**（Generator Metrics）：共 6 个指标——faithfulness（回答声明被检索块蕴含的比例）、relevant noise sensitivity（来自相关块的错误声明）、irrelevant noise sensitivity（来自无关块的错误声明）、hallucination（不来自任何检索块的错误声明）、self-knowledge（不来自检索块的正确声明）、context utilization（被检索覆盖的标准答案声明中被生成器使用的比例）[^src-4]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex, Design Principle" -- "we observe there are two major personae using a RAG evaluation framework. The first persona is a user that cares about the overall performance... The second persona is a developer that focuses on improving a RAG system"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex, Overall Metrics" -- "precision is the proportion of correct claims in all response claims, and recall is the proportion of correct claims in all ground-truth answer claims"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex, Retriever Metrics" -- "we define the retriever precision at chunk-level instead of claim-level... it is likely that a chunk may contain relevant claims and irrelevant or misleading information at the same time"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex, Generator Metrics" -- "we provide in total six metrics characterizing different aspects of its performance"
