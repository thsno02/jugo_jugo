---
schema: justification_journal.v1
card: ../cards/relevant-vs-irrelevant-noise-sensitivity.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt`
源证据：
- sections/framework.tex, Generator Metrics -- 对 relevant 和 irrelevant noise sensitivity 的定义
- tables/ragchecker_results_avg.tex -- 所有 8 个 RAG 系统的 NS-I 和 NS-II 数值对比
- sections/experiments.tex -- "generators demonstrate a chunk-level faithfulness"
范围论证：该区分是 RAGChecker 独有的指标设计贡献，揭示了生成器信任机制的粒度是块级而非声明级，对 RAG 系统的知识库设计和分块策略有直接指导意义。
