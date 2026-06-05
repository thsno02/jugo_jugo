---
schema: justification_journal.v1
card: ../cards/adaptive-benchmarking-persona-generation.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt`
源证据：
- Section 1.2 (graph_rag.tex) — "Adaptive benchmarking refers to the process of dynamically generating evaluation benchmarks tailored to specific domains or use cases"
- Algorithm 1 — 三层级人设→任务→问题的生成流程
- Section 2.3 — "our method avoids generating the questions directly from the corpus itself"
范围论证：自适应基准测试是 GraphRAG 论文的方法论贡献之一，解决了全局 sensemaking 查询缺乏标准答案的评估难题，与核心 GraphRAG 方法和评估结果卡互补但聚焦不同方面。
