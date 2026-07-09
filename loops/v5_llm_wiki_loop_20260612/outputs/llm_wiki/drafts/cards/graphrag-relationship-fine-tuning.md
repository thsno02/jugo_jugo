---
id: graphrag-relationship-fine-tuning
title: GraphRAG 关系抽取微调方法
status: draft
card_type: technique
tags: [graphrag, fine-tuning, relationship-extraction, synthetic-data, gpt-4o, azure-ml]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
evidence_basis: experimental_paper
justification: ../justification/graphrag-relationship-fine-tuning.md
canonical_concept: graphrag-relationship-fine-tuning
aliases: [relationship fine-tuning, GraphRAG fine-tuning, 关系抽取微调, synthetic data for KG extraction]
summary: >-
  GraphRAG graphrag-relationship-fine-tuning 关系抽取微调使用 GPT-4o 合成训练数据的三步流程：随机采样新闻主题生成 mock 新闻→用 GraphRAG prompt 抽取实体关系→基于抽取结果重新生成文章确保所有实体关系均被提及。第二次生成的文章作为微调输入，抽取的关系作为标签。共产出 29059 篇文章及对应标签。使用 Azure ML Studio 进行微调训练。
related: [graphrag-entity-extraction-self-reflection, graphrag-pipeline-architecture]
---

GraphRAG 论文描述了一种为关系抽取模型生成合成训练数据的微调方法。

**三步合成数据生成流程**:
1. 给定随机采样的新闻主题，使用 GPT-4o 生成 mock 新闻故事
2. 使用 GraphRAG 的标准 prompt 从生成的文章中抽取实体和关系
3. 基于抽取出的实体和关系，让 LLM 重新生成一篇新闻故事

**关键设计**: 第二次生成确保文章中明确提及了所有已抽取的实体和关系，消除了标签与输入之间的不对齐。

**训练配置**:
- 输入：第二次生成的文章
- 标签：抽取出的关系
- 数据量：29,059 篇新闻文章 + 对应关系标签
- 训练平台：Azure ML Studio

[^src-1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Relationship fine-tuning procedure" (fine_tuning.tex) -- "The second generation of the mock news article helps ensure the all the entities and relationships are mentioned in the article"
[^card-1]: [graphrag-entity-extraction-self-reflection] 微调是提升抽取质量的另一路径
[^card-2]: [graphrag-pipeline-architecture] 微调应用于流水线第二步的关系抽取
