---
id: context-window-threshold-50k-100k
title: Context Window 50k-100k Token 阈值
status: accepted
card_type: boundary_condition
tags:
- context-window
- scalability-limit
- llm-wiki
- threshold
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- atlan-llm-wiki-vs-rag-dynamic-20260524
evidence_basis: practitioner_report
justification: ../justification/context-window-threshold-50k-100k.md
canonical_concept: context-window-threshold-50k-100k
aliases:
- 50k-100k token threshold
- context window limit
- 上下文窗口阈值
- index overflow
summary: context window threshold 50k-100k token 是 LLM wiki 方案可靠运作的上限。超过此规模 index.md 无法放入 context window，wiki 的"先读索引再拉文章"机制失效，必须引入检索层。此为 wiki 方案的硬性可扩展边界——规模不是小注脚而是整个框架。
related:
- llm-wiki-three-folder-architecture
- compile-time-vs-query-time-knowledge-assembly
- llm-wiki-enterprise-limitations
- llm-wiki-token-efficiency-95-percent
---
50,000-100,000 token 阈值是 LLM wiki 方案停止可靠运作的边界点。超过此规模，index.md 无法放入 context window，LLM context window 限制迫使引入检索层——无论存储格式如何。[^src-1]

文章强调："规模不是一个小注脚，它是整个框架。"（Scale is not a minor caveat. It is the entire frame.）[^src-2]

该阈值的实际后果：
- index 溢出导致 wiki 入口机制（先读索引→再拉文章）失效
- 被迫引入检索层，回到 query-time assembly 模式
- wiki 方案的 token 效率优势在此边界完全消失 [^card-1]

这意味着 LLM wiki 的适用范围有明确上界：约 100-200 篇文章、个人研究者规模。[^src-3]

[^src-1]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "LLM wiki vs RAG knowledge base: what's the difference?" P20 -- "The 50,000-100,000 token threshold is where the wiki approach stops working reliably: beyond that, the index cannot fit in context"
[^src-2]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "LLM wiki vs RAG knowledge base: what's the difference?" P20 -- "Scale is not a minor caveat. It is the entire frame."
[^src-3]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "LLM wiki vs RAG knowledge base: head-to-head comparison" P46 -- "Up to ~100-200 articles (index must fit in context)"
[^card-1]: 参见 [[llm-wiki-token-efficiency-95-percent]] — token 效率优势在此阈值消失
