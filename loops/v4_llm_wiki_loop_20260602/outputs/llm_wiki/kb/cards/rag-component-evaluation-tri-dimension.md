---
id: rag-component-evaluation-tri-dimension
title: RAG 组件评估三维度：上下文相关性、回答忠实性、回答相关性
status: accepted
card_type: distinction
tags: [rag, evaluation, context-relevance, answer-faithfulness, answer-relevance, component-level]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ares]
justification: ../justification/rag-component-evaluation-tri-dimension.md
canonical_concept: rag-component-evaluation-tri-dimension
aliases: [RAG三维评估, context-relevance-faithfulness-relevance, RAG组件级评估维度]
summary: >-
  rag-component-evaluation-tri-dimension（RAG三维评估, context-relevance-faithfulness-relevance）ARES 将 RAG 评估分解为上下文相关性（检索质量）、回答忠实性（生成是否基于上下文）、回答相关性（生成是否回答问题）三个正交组件级维度
related: [ares-rag-evaluation-framework, citation-quality-tri-dimension, rag-evaluation-tri-dimension, source-faithfulness-risk]
---

ARES 将 RAG 系统的评估沿三个维度展开，每个维度对应 RAG 流水线中不同组件的质量 [^src-1]：

1. **上下文相关性（context relevance）**：检索器返回的段落是否与输入查询相关。该维度直接衡量检索环节的质量。
2. **回答忠实性（answer faithfulness）**：生成的回答是否忠实于检索到的上下文，不引入上下文中不存在的信息。该维度聚焦生成器的接地（grounding）能力。
3. **回答相关性（answer relevance）**：生成的回答是否有效回答了原始查询。该维度衡量端到端的任务完成度。

这三个维度与 ALCE 的"流畅度-正确性-引用质量"三维框架形成互补：ALCE 侧重输出文本的表面质量与引用可追溯性，而 ARES 侧重 RAG 组件级的功能正确性。两者共同覆盖 RAG 系统评估的不同切面。

RAGAS 独立提出了高度平行的三维分解（检索质量、忠实性、生成质量），但两者的侧重点存在微妙差异：RAGAS 更强调检索的"聚焦性"，而 ARES 更强调回答对查询的直接相关性[^card-1]。这三个维度的自动化评估由 ARES 框架通过合成数据微调 LM 评审与 PPI 校准来实现[^card-2]。

## Footnotes

[^card-1]: [RAG 评估三维度分解](rag-evaluation-tri-dimension.md) -- RAGAS 从不同来源独立提出了平行的三维分解（检索质量、忠实性、生成质量），两个框架的维度高度重叠但侧重点有微妙差异
[^card-2]: [ARES 自动化 RAG 评估框架](ares-rag-evaluation-framework.md) -- 本卡聚焦 ARES 的三个评估维度，该卡描述支撑这些维度的自动化框架（合成数据微调+PPI 校准）

[^src-1]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- Abstract -- "evaluating RAG systems along the dimensions of context relevance, answer faithfulness, and answer relevance"
