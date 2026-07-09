---
id: cross-tool-entity-resolution
title: 跨工具实体解析
status: accepted
card_type: mechanism
tags:
- entity-resolution
- knowledge-graph
- cross-tool
- semantic-linking
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- falconer-enterprise-guide
evidence_basis: practitioner_report
justification: ../justification/cross-tool-entity-resolution.md
canonical_concept: cross-tool-entity-resolution
aliases:
- cross-tool semantic resolution
- 跨工具语义解析
- entity resolution
summary: 企业 LLM wiki 的链接机制需从 Obsidian 文件内反向链接升级为跨工具实体解析；需理解 payments service 设计文档 = payments-service GitHub repo = @payments-team Slack channel 为同一实体；本质上更接近知识图谱而非链接 Markdown 文件 vault
related:
- personal-to-enterprise-scaling-barriers
- karpathy-llm-wiki-pattern
- graphiti-entity-fact-extraction
- enterprise-llm-wiki-architecture
---
企业 LLM wiki 中的链接机制需要从 Obsidian 式文件内反向链接升级为跨工具语义实体解析（cross-tool semantic resolution）。[^card-1]

材料给出的具体示例：系统必须理解设计文档中的 "the payments service"、GitHub repo 中的 "payments-service"、Slack channel 中的 "@payments-team" 是同一实体。这种解析接近知识图谱（knowledge graph）而非链接 Markdown 文件的 vault。[^src-1]

此外，一个决策的完整链接链需要跨越：Slack 中的讨论→实施它的 PR→追踪它的 Linear ticket→首次讨论它的 Granola 转录→记录其结果的 Notion 文档。这些链接默认不存在，且当任何一个工具变更时不会存活。[^src-2]

[^card-1]: 参见 [[personal-to-enterprise-scaling-barriers]] Link 维度的障碍分析
[^src-1]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "What an enterprise LLM wiki has to do differently" P38 -- "The graph has to understand that 'the payments service' in a design doc is the same entity as 'payments-service' in a GitHub repo and '@payments-team' in a Slack channel."
[^src-2]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Link: bidirectional connections need cross-tool semantics" P27 -- "A decision made in Slack needs to link to the PR that implemented it, the Linear ticket that tracked it, the Granola transcript where it was first discussed"
