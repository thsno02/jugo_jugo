---
id: ingest-operation
title: Ingest 操作：单源摄入触发多页更新
status: draft
card_type: operation_pattern
tags: [llm-wiki, ingest, workflow, wiki-maintenance]
created_time: 2026-06-12T15:02:00+08:00
edited_time: 2026-06-12T15:02:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
evidence_basis: practitioner_report
justification: ../justification/ingest-operation.md
canonical_concept: ingest-operation
aliases: [source ingestion, 源摄入, wiki ingest workflow]
summary: >-
  ingest-operation 是 LLM Wiki 的核心操作：LLM 读取新 source 后讨论要点、写摘要页、更新 index、更新相关实体/概念页、追加 log；单次 ingest 可触及 10-15 wiki 页面
related: [three-layer-architecture, persistent-compounding-artifact]
---

Ingest 是 LLM Wiki 将新原始来源转化为结构化知识的核心操作。其流程为：LLM 读取 source → 与用户讨论 key takeaways → 在 wiki 中写摘要页 → 更新 index → 更新相关实体和概念页 → 在 log 中追加条目。[^src-1]

单次 ingest 的影响范围显著："A single source might touch 10-15 wiki pages"。这体现了 wiki 的网状特性——新知识不仅产生新页面，还通过更新现有页面融入已有知识结构。[^src-2] [^card-1]

作者个人偏好逐个摄入并保持参与（"I prefer to ingest sources one at a time and stay involved"），检查摘要和更新，引导 LLM 强调什么。但也可以在较少监督下批量摄入多个 source。具体工作流由用户决定并记录在 schema 中供后续会话使用。[^src-3] [^card-2]

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations" P2 -- "the LLM reads the source, discusses key takeaways with you, writes a summary page in the wiki, updates the index, updates relevant entity and concept pages across the wiki, and appends an entry to the log"
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations" P2 -- "A single source might touch 10-15 wiki pages."
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations" P2 -- "Personally I prefer to ingest sources one at a time and stay involved"
[^card-1]: [three-layer-architecture](three-layer-architecture.md) -- ingest 操作在三层架构中连接 Raw sources 层和 Wiki 层
[^card-2]: [persistent-compounding-artifact](persistent-compounding-artifact.md) -- ingest 是 wiki 作为复合制品不断积累的机制
