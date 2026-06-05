---
schema: justification_journal.v1
card: ../cards/wiki-rag-hybrid-pattern.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt`
源证据：
- L363 — "In hybrid architectures, the wiki provides curated, high-confidence context that anchors RAG retrieval"
- L367-368 — "higher response consistency and fewer hallucinations than RAG alone"
- L373 — "This separation avoids contaminating the curated knowledge layer with the noise and variance of broad retrieval."
- L378 — "An LLM agent that knows the shape, certification status, and lineage of a dataset before it queries it is a fundamentally more reliable agent"
范围论证：现有 KB 无任何卡涉及 wiki 与 RAG 的组合使用。本卡从 Atlan 文章的"How LLM wikis and RAG knowledge bases work together"章节提取三种混合模式，每种模式都是 wiki 层为 RAG 提供策展锚点的变体。三种模式作为一个机制卡提取，因为它们共享同一核心原理（策展层锚定检索层）。
