---
schema: justification_journal.v1
card: ../cards/experiment/memgpt-virtual-context-management.md
created_time: 2026-06-12T10:00:00+08:00
---

## creation | 2026-06-12T10:00:00+08:00

生成方式：Mode A questioning loop, round 1
问题：MemGPT 的虚拟上下文管理具体通过什么机制实现从 main context 到 external context 的数据移动？
来源：`data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`

源证据：
- Section: Function executor — "Memory edits and retrieval are entirely self-directed"

范围论证：聚焦数据移动的具体机制流程（function call → parse → execute → feedback），上界不含具体应用场景（DMR/DocQA），下界不含 OS 类比分析
