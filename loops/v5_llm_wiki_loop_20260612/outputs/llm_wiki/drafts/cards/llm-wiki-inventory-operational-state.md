---
id: llm-wiki-inventory-operational-state
title: Inventory 操作状态与证据分离
status: draft
card_type: design-principle
tags: [llm-wiki, inventory, operational-state, evidence-separation]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
evidence_basis: documentation
justification: ../justification/llm-wiki-inventory-operational-state.md
canonical_concept: inventory-operational-state
aliases: [inventory, tracking records, operational state, 库存追踪, durable state]
summary: >-
  inventory-operational-state 设计：inventory/ 存持久操作状态（物品 items、源候选 source candidates、语料库 corpora、实体 entities、开放问题 open questions、任务 tasks、监视项 watch items、下一步行动 next actions），有意不作为事实声明证据与 wiki 证据层分离
related: [llm-wiki-hub-architecture, llm-wiki-dataset-manifest-system]
---

llm-wiki 的 inventory 系统存储持久操作状态，包含七种记录类型：物品（items）、源候选（source candidates）、语料库（corpora）、实体（entities）、开放问题（open questions）、任务（tasks）、监视项（watch items）和下一步行动（next actions）。[^src-1]

核心设计意图：inventory 有意不作为事实声明的证据。它与 wiki 证据层明确分离——可以被列出和回顾，但不会成为知识声明的论据来源。[^src-2]

Chat 视图默认以紧凑表格显示。支持通过 scan-outputs --dry-run 预览旧格式迁移。[^src-3]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Architecture" P203 -- "Inventory (inventory/) is for durable operational state: actual items, source candidates, corpora, entities, open questions, tasks, watch items, and next actions."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Architecture" P203 -- "It is intentionally not evidence for factual claims."
[^src-3]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "How It Works" P119 -- "Parts, source queues, corpora, watch items, and next actions live under inventory/ so they can be listed and revisited without becoming evidence."
