---
schema: justification_journal.v1
card: ../cards/retrieval-snr-tradeoff.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt`
源证据：
- Section 6.1 — "it is important to reduce the signal-to-noise (SNR) ratio in retrieved contexts"
- Table 3 — "Observation: top-5=41.4, top-50=37.8; Dialog: top-5=31.7, top-50=34.8"
范围论证：检索量-性能反转是 RAG 系统设计中的通用原理，虽然在 LoCoMo 中被具体量化，但对 agent memory 系统的检索策略有广泛参考价值。与 observation-based-memory-representation 关注不同层面（数量 vs. 表示）。
