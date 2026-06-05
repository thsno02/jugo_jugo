---
schema: justification_journal.v1
card: ../cards/locomo-reflect-respond-architecture.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt`
源证据：
- Section 3.3 — "reflect and respond... short-term and long-term memory"
- Section 3.3 — "summary w_k conditioned on h_k and w_{k-1}; observation o_{k_j} stored in long-term memory"
- Section 3.3 — "agent generates a response by basing it on the latest summary, reflections, observations, persona"
范围论证：反思-回应架构是 LoCoMo 数据生成管线的核心代理机制，其短期摘要+长期 observation 的双层设计是后续 RAG 实验的基础。与 observation-based-memory-representation 互补但关注架构整体而非单一表示层。
