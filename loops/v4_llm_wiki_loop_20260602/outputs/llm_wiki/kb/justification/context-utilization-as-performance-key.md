---
schema: justification_journal.v1
card: ../cards/context-utilization-as-performance-key.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt`
源证据：
- sections/experiments.tex -- "context utilization strongly correlates to the overall F1 score"
- sections/experiments.tex -- "generators' context utilization are relatively stable between the two retrievers"
- tables/ragchecker_results_avg.tex -- CU 数值在 BM25 和 E5-Mistral 之间的稳定性数据
范围论证：此发现是 RAGChecker 实验的核心 insight 之一，对 RAG 系统优化策略有直接指导意义：优先改善检索器比调优生成器更有效，因为稳定的 CU 会自动放大检索改善。
