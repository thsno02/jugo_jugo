---
schema: justification_journal.v1
card: ../cards/fact-augmented-key-expansion.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-longmemeval/source/text/5_experiment.tex`
源证据：
- Section 5.3 — "we applied a simple document expansion technique, where the compressed information is concatenated with the original value to form the key during indexing"
- Section 5.3 — "yielded an average improvement of 9.4% in recall@k and 5.4% in final accuracy"
- Appendix — "rank merging has much lower performance than key merging"
范围论证：事实增强键扩展是独立于值粒度权衡的索引策略，提供了具体的实验证据，适合作为独立的 mechanism 卡片。
