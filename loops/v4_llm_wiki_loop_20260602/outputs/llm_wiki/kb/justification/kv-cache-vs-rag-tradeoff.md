---
schema: justification_journal.v1
card: ../cards/kv-cache-vs-rag-tradeoff.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-wicer/text.txt`
源证据：
- Abstract — "full context KV cache inference outperforms RAG on curated knowledge (4.38 vs. 4.08 out of 5, 7.3 faster TTFT) but degrades below RAG at scale due to attention dilution"
范围论证：KV cache 与 RAG 的性能权衡是论文最核心的实证发现之一，提供了具体的量化对比数据。与已有的 compile-time-vs-query-time 卡互补——后者讨论架构区分，本卡提供具体的性能数据和规模依赖的交叉点。
