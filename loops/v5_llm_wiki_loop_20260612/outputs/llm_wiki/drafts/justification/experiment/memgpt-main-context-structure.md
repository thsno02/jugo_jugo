---
schema: justification_journal.v1
card: ../cards/experiment/memgpt-main-context-structure.md
created_time: 2026-06-12T10:00:00+08:00
---

## creation | 2026-06-12T10:00:00+08:00

生成方式：Mode A questioning loop, round 1
问题：Main context 的三段结构各自的读写权限和功能是什么？
来源：`data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`

源证据：
- Section: Main context — "The prompt tokens in MemGPT are split into three contiguous sections"

范围论证：聚焦三段结构的静态描述（权限/用途），上界不含 queue eviction 的动态行为，下界不含 working context 的具体应用场景
