---
schema: justification_journal.v1
card: ../cards/graph-modularity-for-summarization.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt`
源证据：
- Section 2.2 (graph_rag.tex) — "their inherent modularity and the ability to partition graphs into nested modular communities of closely related nodes"
- Section 2.2 — "GraphRAG recursively creates increasingly global summaries by using the LLM to create summaries spanning this community hierarchy"
- Section 2.2 — 列举了此前方法如何使用图但未利用模块性
范围论证：图模块性作为 GraphRAG 利用的核心图属性，是理解该方法区别于其他图+RAG 方法的关键概念。它与具体的社区层级实现卡互补，但聚焦于更抽象的结构原理层面。
