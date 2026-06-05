---
schema: justification_journal.v1
card: ../cards/rag-generator-self-knowledge.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt`
源证据：
- sections/framework.tex, Generator Metrics -- "A correct claim not entailed by any chunk can only be based on generator's self-knowledge"
- tables/ragchecker_results_avg.tex -- GPT-4 vs Llama3-70B 的 self-knowledge 数值
- sections/experiments.tex -- "GPT-4 tends to rely on self-knowledge without explicit requirements"
范围论证：Self-knowledge 是 RAGChecker 提出的独有指标，区分了"正确但不可追溯"与"错误且不可追溯"（hallucination），对 RAG 系统的可溯源性评估有独立价值。
