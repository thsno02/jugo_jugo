---
schema: justification_journal.v1
card: ../cards/experiment/memgpt-queue-eviction-policy.md
created_time: 2026-06-12T10:00:00+08:00
---

## creation | 2026-06-12T10:00:00+08:00

生成方式：Mode A questioning loop, round 1
问题：Queue Manager 的 eviction policy 具体包含哪些阶段和触发条件？
来源：`data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`

源证据：
- Section: Queue Manager — "When the prompt tokens exceed the 'warning token count'"

范围论证：聚焦两阶段 eviction 流程（warning → flush），上界不含 recursive summary 质量分析，下界不含具体 token 阈值的实现细节
