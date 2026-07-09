---
id: wiki-curated-context-layer-over-rag
title: Wiki 作为 RAG 之上的策展 Context 层
status: draft
card_type: integration_pattern
tags: [hybrid-architecture, curated-context, rag, llm-wiki, grounding]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [atlan-llm-wiki-vs-rag-dynamic-20260524]
evidence_basis: practitioner_report
justification: ../justification/wiki-curated-context-layer-over-rag.md
canonical_concept: wiki-curated-context-layer-over-rag
aliases: [curated context layer, wiki over RAG, 策展上下文层, seed context, wiki-RAG hybrid]
summary: >-
  wiki curated context layer over RAG 是混合架构模式：wiki 的结构化摘要文章作为高质量种子 context 在 RAG 检索前传递给 LLM，提供关键概念、稳定定义、已知关系的解释框架。RAG 随后检索支撑证据。据材料报告，组合效果为更一致的回答和更少幻觉——LLM 在检索动态语料前已有经策展的知识锚定。
related: [llm-wiki-three-folder-architecture, rag-three-stage-pipeline, two-tier-knowledge-architecture]
---

在混合架构中，LLM wiki 与 RAG 管道并非互斥。Wiki 可作为策展 context 层锚定 RAG 检索——减少噪声、改善 grounding、使 LLM 回答跨查询更一致。[^src-1]

**工作方式**：Wiki 的结构化摘要文章作为高质量"种子"context，在 RAG 检索开始前传递给 LLM。LLM 不是冷启动进入原始语料，而是先获得可靠的解释框架：关键概念、稳定定义、已知关系。RAG 随后为具体查询检索支撑证据。[^src-2]

**据材料报告的组合效果**：比纯 RAG 更高的回答一致性和更少的幻觉——因为 LLM 在进入动态检索前已基于经策展的知识进行 grounding。[^src-3] [^card-1] [^card-2]

[^src-1]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "How LLM wikis and RAG knowledge bases work together" P61 -- "In hybrid architectures, the wiki provides curated, high-confidence context that anchors RAG retrieval - reducing noise, improving grounding"
[^src-2]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "Wiki as curated context layer over RAG" P63 -- "the wiki gives it a reliable interpretive frame: key concepts, stable definitions, known relationships. RAG then retrieves supporting evidence"
[^src-3]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "Wiki as curated context layer over RAG" P63 -- "higher response consistency and fewer hallucinations than RAG alone, because the LLM is grounding against curated knowledge before it reaches into dynamic retrieval"
[^card-1]: 参见 [[llm-wiki-three-folder-architecture]] — wiki 层的结构基础
[^card-2]: 参见 [[rag-three-stage-pipeline]] — RAG 层的架构基础
