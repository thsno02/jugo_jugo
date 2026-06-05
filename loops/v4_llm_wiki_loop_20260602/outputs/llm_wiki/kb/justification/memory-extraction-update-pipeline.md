---
schema: justification_journal.v1
card: ../cards/memory-extraction-update-pipeline.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt`
源证据：
- sections/proposed_work.tex — "Our architecture follows an incremental processing paradigm, enabling it to operate seamlessly within ongoing conversations. As illustrated in Figure 2, the complete pipeline architecture consists of two phases: extraction and update."
- sections/proposed_work.tex — "Rather than using a separate classifier, we leverage the LLM's reasoning capabilities to directly select the appropriate operation"
范围论证：该卡片聚焦于 Mem0 的核心双阶段架构设计，是理解整个系统的基础机制。提取和更新两个阶段构成一个完整的增量式记忆管理流程，与 wiki 系统的 ingest 操作有直接类比关系。
