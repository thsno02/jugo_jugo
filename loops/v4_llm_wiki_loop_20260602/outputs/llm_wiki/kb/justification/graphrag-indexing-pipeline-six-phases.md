---
schema: justification_journal.v1
card: ../cards/graphrag-indexing-pipeline-six-phases.md
created_time: 2026-06-08T10:00:00+08:00
---

## creation | 2026-06-08T10:00:00+08:00

生成方式：从 repo-microsoft-graphrag material_bundle.txt 提取实现细节
来源：`data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt`
源证据：
- docs/index/default_dataflow.md — 完整六阶段 Mermaid 流程图与各阶段详细说明
- docs/index/architecture.md — 核心 workflow 状态图（LoadDocuments -> ChunkDocuments -> ExtractGraph -> DetectCommunities -> GenerateReports）
- docs/index/byog.md — workflows 可选子集配置示例
范围论证：现有 arxiv-graphrag 卡聚焦论文中的概念机制（社区层级、map-reduce、gleaning），此卡聚焦开源实现的具体管线阶段划分与数据流，是论文概念的工程落地描述，与现有卡互补而不重叠。
