---
id: llm-wiki-pattern-definition
title: LLM Wiki 模式定义与起源
status: draft
card_type: concept-definition
tags: [llm-wiki, karpathy, knowledge-management, compounding-knowledge]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [aillm-wiki-directory]
evidence_basis: documentation
justification: ../justification/llm-wiki-pattern-definition.md
canonical_concept: llm-wiki-pattern-definition
aliases: [LLM Wiki, LLM Wiki pattern, Karpathy LLM Wiki, llm wiki]
summary: >-
  LLM Wiki 模式由 Andrej Karpathy 于 2026 年 4 月提出，定义为持久的、复合的知识库（persistent, compounding knowledge base），由 LLM 维护。与 RAG 不同，模型写一个 wiki 而非每次重新检索派生答案，wiki 每次使用都变得更丰富。提出后一周内即有开源实现、YouTube 讲解和博客评论。
related: [llm-wiki-vs-rag, llm-wiki-three-step-workflow]
---

LLM Wiki 模式由 Andrej Karpathy 于 2026 年 4 月引入，核心定义为：一个持久的、复合的知识库（persistent, compounding knowledge base），由 LLM 维护。[^src-1]

其关键范式转变在于：不是通过 RAG 每次重新派生答案，而是由模型写一个 wiki，该 wiki 每次使用都变得更丰富（"gets richer every time you use it"）。[^src-2]

该模式提出后迅速传播——一周内已有开源实现、YouTube 讲解视频和多篇博客评论。[^src-3]

[^src-1]: `data/raw/webpage/aillm-wiki-directory/markdown.md` -- "Intro" P4 -- "Andrej Karpathy introduced the LLM Wiki pattern in April 2026 — a persistent, compounding knowledge base maintained by an LLM"
[^src-2]: `data/raw/webpage/aillm-wiki-directory/markdown.md` -- "Intro" P4 -- "Instead of re-deriving answers through RAG every time, your model writes a wiki that gets richer every time you use it"
[^src-3]: `data/raw/webpage/aillm-wiki-directory/markdown.md` -- "Intro" P4 -- "within a week there were already open-source implementations, YouTube explainers, and a dozen hot-take blog posts"
