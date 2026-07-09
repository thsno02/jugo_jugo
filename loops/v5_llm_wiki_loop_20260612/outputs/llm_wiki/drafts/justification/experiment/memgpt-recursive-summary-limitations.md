---
schema: justification_journal.v1
card: ../cards/experiment/memgpt-recursive-summary-limitations.md
created_time: 2026-06-12T10:00:00+08:00
---

## creation | 2026-06-12T10:00:00+08:00

生成方式：Mode A questioning loop, round 5
问题：Recursive summary 机制有什么潜在信息损失？
来源：`data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`

源证据：
- Section: Queue Manager — "generates a new recursive summary using the existing recursive summary and evicted messages"

范围论证：聚焦 recursive summary 的信息损失分析，上界不含 eviction policy 的触发条件，下界不含 summary 生成的具体 prompt 实现
