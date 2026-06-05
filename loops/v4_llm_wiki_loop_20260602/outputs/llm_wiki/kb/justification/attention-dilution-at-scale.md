---
schema: justification_journal.v1
card: ../cards/attention-dilution-at-scale.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-wicer/text.txt`
源证据：
- Abstract — "full context KV cache inference outperforms RAG on curated knowledge (4.38 vs. 4.08 out of 5, 7.3 faster TTFT) but degrades below RAG at scale due to attention dilution"
范围论证：注意力稀释是论文指出的一个具体退化机制，解释了为何全上下文方案不能无限扩展。这与已有的 context-window-degradation 卡可能存在关联但视角不同——本卡聚焦于 attention 层面的机制解释，且提供了具体的性能对比数据。
