---
id: ingest-operation
title: 摄入操作
status: accepted
card_type: operational_rule
tags: [llm-wiki, operations, ingest]
created_time: 2026-06-04T22:30:00+08:00
edited_time: 2026-06-04T22:30:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/ingest-operation.md
canonical_concept: ingest-operation
aliases: [摄入操作, ingest, 资料摄入, source ingestion]
summary: >-
  ingest-operation（摄入操作 / ingest / 资料摄入 / source ingestion）是 LLM Wiki
  核心操作之一：LLM 读取新资料、更新索引和实体/概念页面，单次可触及 10-15 个 wiki 页面
related: []
---

摄入（Ingest）是 LLM Wiki 的三大操作之一，负责将新资料整合进 wiki。标准流程为：LLM 阅读资料 → 与用户讨论关键要点 → 在 wiki 中写摘要页 → 更新索引 → 更新相关的实体和概念页面 → 在日志中追加条目。单次摄入可能触及 10-15 个 wiki 页面[^src-1]。

**人类参与程度是一个谱系**：作者个人偏好逐条摄入并深度参与——阅读摘要、检查更新、引导 LLM 该强调什么。但也可以在较少监督下批量摄入多份资料[^src-2]。

工作流程不是固定的——用户需要开发适合自己风格的流程并记录在 schema 中以供后续会话使用[^src-3]。摄入是三大操作之一，另两个是巡检[^card-1]和查询。人类参与程度的深入分析见参与谱系卡[^card-2]。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations > Ingest" -- "the LLM reads the source, discusses key takeaways with you, writes a summary page in the wiki, updates the index, updates relevant entity and concept pages across the wiki, and appends an entry to the log. A single source might touch 10-15 wiki pages."
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations > Ingest" -- "I prefer to ingest sources one at a time and stay involved... But you could also batch-ingest many sources at once with less supervision."
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations > Ingest" P1 -- "It's up to you to develop the workflow that fits your style and document it in the schema for future sessions."
[^card-1]: [巡检操作](lint-operation.md) -- 摄入和巡检是 LLM Wiki 的两个互补操作：摄入添加知识，巡检维护健康
[^card-2]: [人类参与程度谱系](review-involvement-spectrum.md) -- 展开本卡提及的参与程度谱系
