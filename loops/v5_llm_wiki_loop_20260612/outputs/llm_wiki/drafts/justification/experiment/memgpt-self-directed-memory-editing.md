---
schema: justification_journal.v1
card: ../cards/experiment/memgpt-self-directed-memory-editing.md
created_time: 2026-06-12T10:00:00+08:00
---

## creation | 2026-06-12T10:00:00+08:00

生成方式：Mode A questioning loop, round 2
问题：MemGPT 系统如何处理 LLM 生成输出的错误情况？
来源：`data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`

源证据：
- Section: Function executor — "runtime errors... are then fed back to the processor by MemGPT"

范围论证：聚焦 parse→execute→feedback 闭环机制，上界不含具体应用性能数据，下界不含 prompt engineering 的引导策略
