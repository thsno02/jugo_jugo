---
id: cross-tool-entity-resolution
title: 跨工具实体解析
status: accepted
card_type: mechanism
tags: [enterprise-wiki, entity-resolution, knowledge-graph, linking]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [falconer-enterprise-guide]
justification: ../justification/cross-tool-entity-resolution.md
canonical_concept: cross-tool-entity-resolution
aliases: [跨工具实体解析, cross-tool semantic resolution, 跨工具语义解析]
summary: >-
  cross-tool-entity-resolution（跨工具实体解析 / cross-tool semantic resolution / 跨工具语义解析）
  是企业级知识链接从文件内双向链接升级为跨工具语义实体识别的机制；知识图谱需理解
  "payments service"在设计文档、GitHub 仓库和 Slack 频道中是同一实体
related: [data-catalog-as-enterprise-wiki, entity-resolution-hybrid-search]
  - llm-wiki-pattern
  - ingest-operation
---

个人 LLM Wiki 的链接依赖 Obsidian 的双向链接——在 vault 内部的文件之间建立 backlink，当 agent 编译新 wiki 页面时创建指向所有相关概念的反向链接，图谱逐渐变厚[^src-1]。

企业知识图谱的链接需要**跨工具**而非仅跨文件。一个在 Slack 中做出的决策需要链接到实现它的 PR、追踪它的 Linear ticket、最初讨论它的 Granola 会议记录、以及描述结果系统的 Notion 文档。这些链接默认不存在，且在工具变更时不会自动存续[^src-2]。

这要求**语义实体解析**：图谱必须理解设计文档中的 "the payments service"、GitHub 仓库中的 "payments-service" 和 Slack 频道中的 "@payments-team" 是同一实体。这更接近于知识图谱而非链接 markdown 文件的 vault[^src-3]。

Confluence 和 Notion 中的连接完全依赖人工手动创建，而人类没有时间和记忆力以公司产出内容的速率来创建这些连接[^src-4]。

Atlan 提出的"数据目录即企业 wiki"映射为跨工具实体解析提供了一种已有的实现路径：数据目录的血缘（lineage）功能本质上就是跨系统的实体关系追踪，而业务术语表则是跨工具语义对齐的载体[^card-1]。

Graphiti 的混合搜索实体消解管线[^card-2]为此类跨工具语义解析提供了一种技术基础参考，但其设计目前面向单一知识图谱，尚需扩展以处理跨系统 schema 差异。

## Footnotes

[^src-1]: `data/raw/webpage/falconer-enterprise-guide/text.txt` -- "Link: bidirectional connections need cross-tool semantics" 段 -- "When the agent compiles a new wiki page, it creates backlinks to every related concept. The graph thickens."
[^src-2]: `data/raw/webpage/falconer-enterprise-guide/text.txt` -- "Link: bidirectional connections need cross-tool semantics" 段 -- "A decision made in Slack needs to link to the PR that implemented it, the Linear ticket that tracked it, the Granola transcript where it was first discussed, and the Notion doc that documents the resulting system."
[^src-3]: `data/raw/webpage/falconer-enterprise-guide/text.txt` -- "What an enterprise LLM wiki has to do differently" 段 -- "The graph has to understand that 'the payments service' in a design doc is the same entity as 'payments-service' in a GitHub repo and '@payments-team' in a Slack channel."
[^src-4]: `data/raw/webpage/falconer-enterprise-guide/text.txt` -- "Link: bidirectional connections need cross-tool semantics" 段 -- "The connections that exist are the ones humans manually create, and humans don't have the time or memory to create them at the rate the company generates content."
[^card-1]: [数据目录作为企业级 Wiki 的结构等价物](data-catalog-as-enterprise-wiki.md) -- 数据目录的血缘功能和业务术语表是跨工具实体解析的一种已有实现路径，将反向链接从文件级升级为跨系统语义级
[^card-2]: [混合搜索实体消解流程](entity-resolution-hybrid-search.md) -- 本卡聚焦跨工具语义实体解析的架构需求，该卡提供了一种基于混合搜索的具体实体消解管线实现
