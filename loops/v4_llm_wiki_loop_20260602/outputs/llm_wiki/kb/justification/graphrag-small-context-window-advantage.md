---
schema: justification_journal.v1
card: ../cards/graphrag-small-context-window-advantage.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt`
源证据：
- Appendix C (appendix.tex) — "Surprisingly, the smallest context window size tested (8k) was universally better for all comparisons on comprehensiveness (average win rate of 58.1%)"
- Appendix C — "Given the potential for information to be 'lost in the middle' of longer contexts"
- Section 2.1.3 — "We used a fixed context window size of 8k tokens"
范围论证：小上下文窗口反而更优是论文的一个反直觉发现，与已有的 context-window-degradation 卡互补但来自不同来源的具体实验证据，构成独立的原子知识。
