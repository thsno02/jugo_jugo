---
schema: justification_journal.v1
card: ../cards/observation-based-memory-representation.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt`
源证据：
- Section 3.3 — "a single turn of the conversation h_{k_j} is transformed into an observation o_{k_j} and then stored in the long-term memory"
- Table 3 — "Observation top-5: Overall=41.4, Temporal=41.9 vs Dialog top-5: Overall=31.7, Temporal=21.3"
- Section 6.1 — "using session summaries as context does not significantly improve the performance despite high recall accuracies"
范围论证：观察式记忆表示是 LoCoMo 中独立于检索策略的记忆表示层面的发现，对 agent memory 系统的设计有直接启示。与 retrieval-snr-tradeoff 互补但关注不同层面（表示 vs. 数量）。
