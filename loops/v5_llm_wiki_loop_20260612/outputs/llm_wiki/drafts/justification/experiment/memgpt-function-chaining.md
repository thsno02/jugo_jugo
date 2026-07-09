---
schema: justification_journal.v1
card: ../cards/experiment/memgpt-function-chaining.md
created_time: 2026-06-12T10:00:00+08:00
---

## creation | 2026-06-12T10:00:00+08:00

生成方式：Mode A questioning loop, round 1
问题：Function chaining 如何工作？heartbeat flag 的作用是什么？
来源：`data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`

源证据：
- Section: Control flow — "Function chaining allows MemGPT to execute multiple function calls sequentially"

范围论证：聚焦 heartbeat/yield 二态机制，上界不含具体任务中的应用效果（nested KV），下界不含 event 类型枚举
