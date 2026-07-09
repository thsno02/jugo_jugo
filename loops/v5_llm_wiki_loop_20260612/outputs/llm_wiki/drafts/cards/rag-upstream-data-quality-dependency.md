---
id: rag-upstream-data-quality-dependency
title: RAG 输出质量对上游数据质量的依赖
status: draft
card_type: limitation_analysis
tags: [rag, data-quality, data-governance, upstream-dependency]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [atlan-llm-wiki-vs-rag-dynamic-20260524]
evidence_basis: practitioner_report
justification: ../justification/rag-upstream-data-quality-dependency.md
canonical_concept: rag-upstream-data-quality-dependency
aliases: [RAG data quality dependency, upstream data quality, RAG 数据质量依赖, garbage in garbage out RAG]
summary: >-
  RAG upstream data quality dependency：RAG 输出质量完全取决于上游数据质量。源文档过时、矛盾或未治理时，RAG 检索并放大(amplify)这些问题。访问控制、新鲜度、血缘默认不内建于 RAG 管道。材料将此框定为数据治理问题而非检索架构问题——建在未治理数据上的 RAG 只是"将问题重新组织为新格式"。
related: [scale-decides-architecture-governance-decides-outcome, rag-three-stage-pipeline]
---

RAG 的核心局限：输出质量完全取决于上游数据质量。如果源文档过时(stale)、矛盾(contradictory)或未治理(ungoverned)，RAG 检索并放大(amplifies)这些问题。[^src-1]

**默认缺失的治理能力**：
- 访问控制(access control)
- 新鲜度保证(freshness)
- 数据血缘(lineage)

这些均不内建于标准 RAG 管道，需额外实现层。[^src-2]

**材料的框定**：这不是检索架构问题，而是数据治理问题。在未治理数据上构建 RAG pipeline（或 shadow wiki）不解决问题——只是"将问题重新组织为新格式"(reorganizes the problem into a new format)。[^src-3] [^card-1]

该观点意味着：无论选择 wiki 还是 RAG，如果源数据未治理，两种方案都将失败。[^src-4]

[^src-1]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "What is a RAG knowledge base?" P36 -- "Output quality depends entirely on upstream data quality. If the source documents are stale, contradictory, or ungoverned, RAG retrieves and amplifies those problems."
[^src-2]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "What is a RAG knowledge base?" P36 -- "Access control, freshness, and lineage are not built into RAG pipelines by default."
[^src-3]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "How Atlan approaches the enterprise knowledge base" P74 -- "Building a shadow wiki or a raw RAG pipeline on top of ungoverned data does not solve it. It reorganizes the problem into a new format."
[^src-4]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "Head-to-head comparison" P59 -- "if the source documents are stale or uncertified, both fail."
[^card-1]: 参见 [[scale-decides-architecture-governance-decides-outcome]] — 治理决定最终结果的整体论断
