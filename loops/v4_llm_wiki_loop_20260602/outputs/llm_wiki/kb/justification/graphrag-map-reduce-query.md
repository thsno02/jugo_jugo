---
schema: justification_journal.v1
card: ../cards/graphrag-map-reduce-query.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt`
源证据：
- Section 1.1.6 (graph_rag.tex) — "Prepare community summaries...randomly shuffled and divided into chunks"
- Section 1.1.6 — "Intermediate answers are generated in parallel...score between 0-100"
- Section 1.1.6 — "sorted in descending order of helpfulness score and iteratively added into a new context window"
范围论证：Map-reduce 查询流程是 GraphRAG 在查询时的核心操作模式，与索引时的社区层级构建分离，构成独立的操作性知识单元。
