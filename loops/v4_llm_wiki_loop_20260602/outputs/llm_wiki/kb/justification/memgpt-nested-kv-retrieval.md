---
schema: justification_journal.v1
card: ../cards/memgpt-nested-kv-retrieval.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`
源证据：
- sections/experiments.tex — "We create a version of the KV task, nested KV retrieval, where values themselves may be keys"
- sections/experiments.tex — "MemGPT with GPT-4 on the other hand is unaffected with the number of nesting levels"
范围论证：嵌套 KV 检索是 MemGPT 论文独创的评估任务，直接证明函数链支撑的多跳信息汇集能力，与 document QA 实验互补但聚焦于多跳逻辑推理，作为独立实验结果卡。
