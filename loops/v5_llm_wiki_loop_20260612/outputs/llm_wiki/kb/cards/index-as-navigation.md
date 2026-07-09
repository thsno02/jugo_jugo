---
id: index-as-navigation
title: Index 文件替代 RAG 检索的适用规模
status: accepted
card_type: implementation_pattern
tags:
- llm-wiki
- index
- navigation
- scale-boundary
- rag-alternative
created_time: 2026-06-12 15:06:00+08:00
edited_time: 2026-06-12 15:06:00+08:00
edited_entity: llm
source_ids:
- karpathy-gist-llm-wiki
evidence_basis: practitioner_report
justification: ../justification/index-as-navigation.md
canonical_concept: index-as-navigation
aliases:
- index.md navigation
- index-based retrieval
- 索引文件导航
- wiki index
summary: index-as-navigation 描述 LLM Wiki 使用 index.md（按类别组织的页面目录）替代 embedding-based RAG 的检索策略；在约 100 sources / 数百页规模下"surprisingly well"有效；更大规模需要专用搜索工具如 qmd
related:
- three-layer-architecture
- persistent-compounding-artifact
---

LLM Wiki 使用一个简单的 index.md 文件作为内容导航机制：按类别（entities, concepts, sources 等）组织的页面目录，每个条目包含链接、一行摘要和可选元数据。[^src-1]

查询时，LLM 先读 index 定位相关页面，再深入阅读具体页面。这种方法在中等规模下出乎意料地有效——"works surprisingly well at moderate scale (~100 sources, ~hundreds of pages) and avoids the need for embedding-based RAG infrastructure"。[^src-2]

这隐含了一个规模边界：作者的实践验证范围约为 100 sources / 数百页。超出此规模，材料建议使用专用搜索工具如 qmd（local markdown search engine with hybrid BM25/vector search and LLM re-ranking）。[^src-3] [^card-1]

注意："surprisingly well" 暗示作者本人也预期这种简单方法不应在此规模下工作良好——这是一个经验性发现而非理论推导。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Indexing and logging" P2 -- "It's a catalog of everything in the wiki — each page listed with a link, a one-line summary, and optionally metadata like date or source count. Organized by category"
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Indexing and logging" P2 -- "This works surprisingly well at moderate scale (~100 sources, ~hundreds of pages) and avoids the need for embedding-based RAG infrastructure."
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Optional: CLI tools" P1 -- "at small scale the index file is enough, but as the wiki grows you want proper search. qmd is a good option"
[^card-1]: [persistent-compounding-artifact](persistent-compounding-artifact.md) -- index 是 wiki 作为可查询复合制品的核心导航机制
