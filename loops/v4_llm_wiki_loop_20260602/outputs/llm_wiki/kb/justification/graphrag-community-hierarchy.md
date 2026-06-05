---
schema: justification_journal.v1
card: ../cards/graphrag-community-hierarchy.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt`
源证据：
- Section 1.1.4 (graph_rag.tex) — "we use Leiden community detection in a hierarchical manner, recursively detecting sub-communities"
- Section 1.1.4 — "Each level of this hierarchy provides a community partition that covers the nodes of the graph in a mutually exclusive, collectively exhaustive way"
- Section 1.1.5 — leaf-level vs higher-level community summary generation procedure
范围论证：层级社区检测与自底向上摘要生成是 GraphRAG 区别于其他图+RAG 方法的核心机制，构成独立的原子知识单元。与全局 sensemaking 概念卡和 map-reduce 查询卡互补但不重叠。
