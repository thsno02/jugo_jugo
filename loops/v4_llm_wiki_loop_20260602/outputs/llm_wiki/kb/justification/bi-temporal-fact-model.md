---
schema: justification_journal.v1
card: ../cards/bi-temporal-fact-model.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-zep/agent_source_bundle.txt`
源证据：
- Section 2.1 — "Zep implements a bi-temporal model, where timeline T represents the chronological ordering of events, and timeline T' represents the transactional order of Zep's data ingestion."
- Section 2.2.3 — "the system tracks four timestamps: t'_created and t'_expired in T'... t_valid and t_invalid in T"
范围论证：双时间线模型是 Graphiti 区别于其他知识图谱引擎的核心创新之一，论文明确将其称为"novel advancement"。它独立于三层架构本身，是一个可分离的时间建模机制，值得独立成卡。
