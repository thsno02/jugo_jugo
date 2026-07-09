---
id: llm-wiki-three-folder-architecture
title: LLM Wiki 三文件夹架构
status: accepted
card_type: architecture_pattern
tags:
- llm-wiki
- karpathy
- markdown
- personal-knowledge-base
- three-folder
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- atlan-llm-wiki-vs-rag-dynamic-20260524
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-three-folder-architecture.md
canonical_concept: llm-wiki-three-folder-architecture
aliases:
- three-folder architecture
- Karpathy LLM wiki
- 三文件夹架构
- LLM wiki
- markdown wiki
summary: LLM wiki three-folder architecture 由 Karpathy 于 2026 年 4 月通过 GitHub Gist 提出。三组件：raw/ 存储非结构化源材料(PDF/notes/web clips)，wiki/ 存放 LLM 编译的摘要文章(一概念一文章)，index.md 为全文章主地图（适配单个 context window）。数据流：源材料→raw/→LLM
  编译→wiki/→index.md。查询时 LLM 先读 index.md 识别相关文章再加载对应 wiki/ 条目。无 embedding、无向量搜索、零基础设施。LLM 角色为"compiler"而非仅 retriever。Backlinks 充当轻量级知识图谱边。
related:
- compile-time-vs-query-time-knowledge-assembly
- llm-wiki-health-check-prompts
- context-window-threshold-50k-100k
- karpathy-llm-wiki-concept
- karpathy-llm-wiki-pattern
- karpathy-llm-wiki-three-layer-architecture
- llm-knowledge-base-pattern
- llm-wiki-definition-and-core-value
- llm-wiki-knowledge-system
- llm-wiki-pattern
- llm-wiki-pattern-definition
- llm-wiki-pattern-overview
- llmwiki-compile-first-architecture
- olw-llm-as-compiler
- data-catalog-as-enterprise-wiki
- knowledge-management-as-dominant-ai-cost-center
- llm-wiki-enterprise-limitations
- llm-wiki-token-efficiency-95-percent
- wiki-curated-context-layer-over-rag
---
LLM wiki 是一种结构化的、基于 markdown 的个人知识库，设计为直接加载进 LLM context。由 Andrej Karpathy 于 2026 年 4 月通过 GitHub Gist 提出。[^src-1]

**三文件夹架构**：

1. **raw/**：非结构化源材料——PDF、笔记、web clips、原始研究输入
2. **wiki/**：LLM 编译的摘要文章——一概念/主题一文章
3. **index.md**：全部文章的主地图(master map)——尺寸适配模型 context window，LLM 的入口点 [^src-2]

**数据流**：源材料 → raw/ → LLM 编译合成 → wiki/ 结构化文章 → index.md 索引引用

**查询时工作方式**：LLM 先读 index.md → 识别哪些文章相关 → 仅加载那些文章——无 embedding step、无向量搜索、无检索管道。[^src-3]

**规模参数**：约 100 篇文章、约 400,000 词源材料时，index 可轻松放入现代 context window。[^src-4]

**LLM 的角色**：不只是检索文本，而是将原始知识合成(synthesize)为结构化文章——DAIR.AI Academy 称之为"compiler"角色。这使 wiki 成为主动维护的知识库而非静态文档。[^src-5]

**Backlinks**：文章间的交叉引用充当轻量级知识图谱边(knowledge graph edges)，增加可导航性而无需图数据库。[^src-6]

[^src-1]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "What is an LLM wiki?" P22 -- "An LLM wiki is a structured, markdown-based personal knowledge base designed to be loaded directly into LLM context. Karpathy introduced the approach in April 2026 via GitHub Gist."
[^src-2]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "Core components of an LLM wiki" P27-31 -- "raw/: Unstructured source material...wiki/: LLM-compiled summary articles...index.md: Master map of all articles"
[^src-3]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "What is an LLM wiki?" P23 -- "At query time, the LLM reads index.md first, identifies which articles are relevant, and loads only those - no embedding, no vector search."
[^src-4]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "What is an LLM wiki?" P24 -- "At roughly 100 articles and ~400,000 words of source material, the index fits easily in a modern context window."
[^src-5]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "What is an LLM wiki?" P25 -- "The DAIR.AI Academy articulates the LLM's role as 'compiler': not just retrieving text but synthesizing raw knowledge into structured articles."
[^src-6]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "What is an LLM wiki?" P25 -- "Backlinks between articles function as lightweight knowledge graph edges, adding navigability without a graph database."
