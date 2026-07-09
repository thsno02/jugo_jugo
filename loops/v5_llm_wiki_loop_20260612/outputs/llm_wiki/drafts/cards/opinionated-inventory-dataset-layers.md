---
id: opinionated-inventory-dataset-layers
title: 有态度的 Inventory 与 Dataset 惰性层设计
status: draft
card_type: layer-design
tags: [llm-wiki, inventory, datasets, lazy-initialization, opinionated-design, tracking-layer]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-nvk-llm-wiki]
evidence_basis: code_implementation
justification: ../justification/opinionated-inventory-dataset-layers.md
canonical_concept: opinionated-inventory-dataset-layers
aliases: [inventory layer, dataset registry, lazy layers, opinionated inventory, durable tracking records]
summary: >-
  llm-wiki 的 inventory 和 datasets 是惰性可选层（lazy optional layers），仅在首次使用时创建。Inventory 用于持久跟踪记录（items/candidates/entities/corpora），有明确的适用性判断：太小用 ingest/query，太大用 datasets/collection。Datasets 层为大型外部数据提供 manifest 接口而不复制数据。两者都强调"有态度"（opinionated）——agent 必须在写入前声明适配性判断。迁移路径为显式、dry-run-first、仅追加。
related: [hub-topic-wiki-isolation, lint-as-schema-migration, topic-archive-lifecycle]
---

llm-wiki 在核心的 raw/wiki/output 三层之外，设计了两个"有态度"的可选层：

**Inventory（持久跟踪层）**[^src-1]：
- 用途：items（物理/数字资产）、ingest-candidates、entities、corpora、questions、tasks、watch
- 适配性判断（fit check）——agent 必须在写入前声明：
  - 好的适配：有状态/优先级/下一步动作的持久事项
  - 太小：一次性源（用 ingest）、事实问题（用 query）、无后续的笔记
  - 太大：数百行式数据（用 datasets 或 collection ingest）
  - 超范围：权威源文本（raw/）、综合知识（wiki/）、生成品（output/）

**Datasets（大型数据注册层）**[^src-2]：
- 用途：为太大、可变、远程、敏感的数据提供 manifest 接口
- 存储位置、schema 注释、小样本、profiles、query recipes——从不复制实际数据
- 边界判断：小且稳定 -> raw/data/；大或 query-oriented -> datasets/

**共同设计特征**：
- **惰性创建**：完全缺失的层不是 lint 错误，不会被空架手脚架预填充
- **显式迁移**：output -> inventory/dataset 迁移为 dry-run-first、仅追加、人工门控
- **有态度的 agent 行为**：大规模变更前先展示 1-3 行样本表，要求确认[^src-3]

[^src-1]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "inventory.md Fit Check" -- "Inventory is opinionated. Before creating records or proposing a migration, say why the thing does or does not belong in inventory."
[^src-2]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "datasets.md" -- "The dataset registry lets a wiki act as an interface and index for data that is too large, mutable, sensitive, or operationally awkward to store directly"
[^src-3]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "AGENTS.md Operations Inventory" -- "Be opinionated about fit... For bigger pivots, show a sample table of 1-3 proposed records"
