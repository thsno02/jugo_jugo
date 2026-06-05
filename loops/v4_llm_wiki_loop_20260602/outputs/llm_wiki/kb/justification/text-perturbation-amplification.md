---
schema: justification_journal.v1
card: ../cards/text-perturbation-amplification.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graph-poisoning/text.txt`
源证据：
- Abstract — "modifying only a few words in the source text can significantly change the constructed graph, poison the GraphRAG, and severely mislead downstream reasoning"
- Abstract — "With fewer than 0.05% of full text modified, the QA accuracy collapses from 95% to 50%"
范围论证：微扰放大效应是贯穿两种攻击的底层机制，独立于具体攻击类型存在。它揭示的是 LLM 驱动图谱构建管道的内在脆弱性质，而非某种特定攻击手段，因此值得独立建卡。
