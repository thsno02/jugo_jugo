---
id: llm-wiki-scale-limitations
title: LLM Wiki 规模局限性
status: draft
card_type: limitation
tags: [llm-wiki, scalability, limitations, vector-database]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [anthemcreation-en-guide]
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-scale-limitations.md
canonical_concept: llm-wiki-scale-limitations
aliases: [wiki scale limitations, scalability limits, personal scale]
summary: >-
  LLM wiki 规模局限性 scale-limitations：适用于个人规模 10~几百篇文档。超出后 interlink 管理 token 成本高昂，vector search 更合适。Karpathy 本人管理超 100 篇文章的 wiki 未用 vector database。Vector database 仅在需要对数千 chunks 语义搜索时才必要。
related: [llm-wiki-vs-rag-reasoning-depth, llm-wiki-model-quality-risk]
---

LLM wiki 明确定位为个人规模知识管理工具，适用于 10~几百篇文档 [^src-1]。

**规模上限的原因**：超出该范围后，管理页面间 interlinks 的 token 成本变得高昂，此时 vector search 成为更合适的方案。

**实证参考**：Karpathy 本人管理超过 100 篇文章、40 万字的 wiki，未使用任何 vector database 或重型索引 [^src-2]。

据材料判断，vector database 仅在需要对数千 chunks 进行语义搜索时才变得必要 [^card-1]。在此阈值以下，结构化 markdown 完全足够。

[^src-1]: `data/raw/webpage/anthemcreation-en-guide/markdown.md` -- "LLM wiki vs. RAG" -- "personal knowledge at an individual scale, from 10 to a few hundred documents"
[^src-2]: `data/raw/webpage/anthemcreation-en-guide/markdown.md` -- "Key takeaways" -- "Karpathy personally manages wikis of over 100 articles without any vector database or heavy indexing."
[^card-1]: 参见 [[llm-wiki-vs-rag-reasoning-depth]] 关于 RAG 在大规模语料上的适用性
