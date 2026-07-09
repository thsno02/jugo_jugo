---
schema: justification_journal.v1
card: ../cards/experiment/memgpt-archival-vs-recall-storage.md
created_time: 2026-06-12T10:00:00+08:00
---

## creation | 2026-06-12T10:00:00+08:00

生成方式：Mode A questioning loop, round 2
问题：Archival storage 和 recall storage 在功能和存储内容上有什么区别？
来源：`data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`

源证据：
- Section: Queue Manager + Document QA — recall storage 自动存消息，archival storage 显式读写任意文本

范围论证：聚焦两种 external storage 的区别，上界不含 main context 内部结构，下界不含具体数据库实现选型原因
