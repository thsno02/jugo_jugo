---
id: two-tier-knowledge-architecture
title: 两层知识架构分层逻辑
status: accepted
card_type: architecture_pattern
tags:
- hybrid-architecture
- two-tier
- knowledge-curation
- knowledge-retrieval
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- atlan-llm-wiki-vs-rag-dynamic-20260524
evidence_basis: practitioner_report
justification: ../justification/two-tier-knowledge-architecture.md
canonical_concept: two-tier-knowledge-architecture
aliases:
- two-tier architecture
- 两层架构
- knowledge curation vs retrieval
- wiki for curation RAG for retrieval
summary: two-tier knowledge architecture 将知识系统分为两层：第一层（wiki/catalog）处理"我们确定知道的"——已认证概念、稳定定义、变化缓慢的内部框架（knowledge curation）；第二层（RAG）处理"语料库中现在有什么"——实时文档搜索、证据检索、大规模动态数据集广覆盖（knowledge retrieval）。分层目的：避免策展知识层被广检索的噪声和方差污染。
related:
- wiki-curated-context-layer-over-rag
- data-catalog-as-enterprise-wiki
---

两层知识架构让每层做各自最擅长的事：[^src-1]

**第一层——知识策展(wiki/catalog)**：处理"我们确定知道的"(what we know for sure)——已认证概念、稳定定义、变化缓慢的内部框架。

**第二层——知识检索(RAG)**：处理"语料库中现在有什么"(what's in the corpus right now)——实时文档搜索、证据检索、跨大规模动态数据集的广覆盖。[^src-2]

**分层的核心目的**：避免策展知识层被广检索的噪声和方差污染。将稳定、经验证的知识与动态、未筛选的检索结果隔离。[^src-3]

该架构在企业场景中演化为：当"wiki 层"不再是 markdown 文件夹而是经治理的数据目录时，产生最强大的混合效果。[^src-4] [^card-1]

[^src-1]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "Wiki for knowledge curation, RAG for knowledge retrieval" P65 -- "A two-tier architecture lets each layer do what it does best."
[^src-2]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "Wiki for knowledge curation, RAG for knowledge retrieval" P65 -- "The LLM wiki handles the 'what we know for sure' layer...RAG handles the 'what's in the corpus right now' layer"
[^src-3]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "Wiki for knowledge curation, RAG for knowledge retrieval" P65 -- "This separation avoids contaminating the curated knowledge layer with the noise and variance of broad retrieval."
[^src-4]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "When the wiki layer is the governed metadata layer" P67 -- "The most powerful hybrid arises when the 'wiki' is not a markdown folder but a governed data catalog"
[^card-1]: 参见 [[data-catalog-as-enterprise-wiki]] — 两层架构的企业实现形态
