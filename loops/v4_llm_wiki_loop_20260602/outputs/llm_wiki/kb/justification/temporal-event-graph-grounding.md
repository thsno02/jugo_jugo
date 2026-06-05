---
schema: justification_journal.v1
card: ../cards/temporal-event-graph-grounding.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt`
源证据：
- Section 3.2 — "we construct a temporal event graph, labeled as G, for each agent"
- Section 3.2 — "G includes causal connections l = (e_i, e_j) that illustrate the causal relationships among events"
- Section 3.3 — "conditioning the agent's response on the subset of events in G that occur between the last and current session"
范围论证：时序事件图是 LoCoMo 管线的核心机制之一，独立于观察记忆和人设系统，值得单独成卡。它提供了一种将因果-时序结构注入长期对话的具体方法。
