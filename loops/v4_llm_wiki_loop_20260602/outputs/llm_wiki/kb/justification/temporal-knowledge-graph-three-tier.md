---
schema: justification_journal.v1
card: ../cards/temporal-knowledge-graph-three-tier.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt`
源证据：
- Section 2 (Knowledge Graph Construction) — "This graph comprises three hierarchical tiers of subgraphs: an episode subgraph, a semantic entity subgraph, and a community subgraph."
- Section 2 — "The resulting hierarchical organization—from episodes to facts to entities to communities—extends existing hierarchical RAG strategies"
范围论证：三层子图架构是 Zep/Graphiti 的核心设计决策，将原始数据保留、语义提取、高层聚类分层处理，是理解整个系统的基础。该架构区别于扁平的 RAG 向量存储，值得独立成卡。
