---
schema: justification_journal.v1
card: ../cards/ragchecker-three-tier-metrics.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt`
源证据：
- sections/framework.tex, Design Principle -- "we observe there are two major personae using a RAG evaluation framework"
- sections/framework.tex, Overall/Retriever/Generator Metrics -- 11 个指标的完整定义
- sections/appendix_formulation.tex -- 所有指标的数学公式
范围论证：三层指标体系是 RAGChecker 的框架级贡献，定义了 RAG 评估的结构化诊断方法。11 个指标覆盖了从用户视角到开发者调优的完整需求。
