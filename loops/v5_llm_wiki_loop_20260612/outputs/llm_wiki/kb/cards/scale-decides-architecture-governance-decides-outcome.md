---
id: scale-decides-architecture-governance-decides-outcome
title: 规模决定架构选择，治理决定最终结果
status: accepted
card_type: thesis_statement
tags:
- data-governance
- architecture-selection
- scale
- enterprise-knowledge
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- atlan-llm-wiki-vs-rag-dynamic-20260524
evidence_basis: practitioner_report
justification: ../justification/scale-decides-architecture-governance-decides-outcome.md
canonical_concept: scale-decides-architecture-governance-decides-outcome
aliases:
- scale decides architecture governance decides outcome
- 规模决定架构治理决定结果
summary: scale decides architecture governance decides outcome 是材料的核心论断：规模决定选择 LLM wiki 还是 RAG（小规模 wiki 胜，大规模 RAG 胜），但无论哪种架构选择，最终结果取决于底层数据治理水平。未治理数据使两种方案都会失败。企业真正需要的不是更好的检索架构，而是有治理的知识底层(substrate)。
related:
- rag-upstream-data-quality-dependency
- llm-wiki-enterprise-limitations
- data-catalog-as-enterprise-wiki
---

"规模决定架构，治理决定结果"(Scale decides the architecture, governance decides the outcome)是文章的总结论断。[^src-1]

**规模维度的判断**：
- 小规模（个人研究者、稳定有界语料）→ LLM wiki 在简洁性、token 效率和零基础设施方面胜出
- 企业规模 → wiki 在访问控制、并发和索引溢出方面崩溃，RAG 是必要路径 [^src-2]

**治理维度的判断**：
- 无论选择何种架构，如果上游数据质量和治理水平不足，两种方案都将失败
- 企业真正需要的不是更好的检索架构，而是有治理的知识底层
- "在底层(substrate)层面解决治理问题的组织将优于那些将其视为检索架构问题的组织" [^src-3]

该论断将 LLM wiki vs RAG 的争论重新框定为规模问题而非优劣问题，同时将企业关注点从架构选择转向治理投资。[^card-1] [^card-2]

[^src-1]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "The bottom line" P83 -- "The LLM wiki vs RAG debate is a question of scale, not superiority."
[^src-2]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "The bottom line" P84 -- "At that scale, it outperforms RAG on simplicity, token efficiency, and zero infrastructure. At enterprise scale, it breaks on access control, concurrency, and index overflow"
[^src-3]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "The bottom line" P85 -- "Organizations that solve it at the substrate level will outperform those treating it as a retrieval architecture question."
[^card-1]: 参见 [[rag-upstream-data-quality-dependency]] — 治理缺失导致 RAG 失败的具体机制
[^card-2]: 参见 [[llm-wiki-enterprise-limitations]] — 规模导致 wiki 失败的具体机制
