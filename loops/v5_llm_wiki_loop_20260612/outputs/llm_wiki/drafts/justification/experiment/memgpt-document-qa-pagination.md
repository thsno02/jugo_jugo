---
schema: justification_journal.v1
card: ../cards/experiment/memgpt-document-qa-pagination.md
created_time: 2026-06-12T10:00:00+08:00
---

## creation | 2026-06-12T10:00:00+08:00

生成方式：Mode A questioning loop, round 2
问题：Document QA 任务中 MemGPT 与 fixed-context baseline 的关键区别是什么？
来源：`data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`

源证据：
- Section: Multi-document QA — "MemGPT is effectively able to make multiple calls to the retriever"

范围论证：聚焦迭代检索的结构性优势，上界不含 nested KV 任务，下界不含 embedding 索引实现细节
