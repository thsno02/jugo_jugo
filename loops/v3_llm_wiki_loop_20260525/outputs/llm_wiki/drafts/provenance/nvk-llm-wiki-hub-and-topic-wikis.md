---
schema: draft_card_provenance.v3
draft_card: ../cards/nvk-llm-wiki-hub-and-topic-wikis.md
material_id: llm-wiki-net
digest_id: digest_llm-wiki-net
source_paths:
  - data/raw/webpage/llm-wiki-net/text.txt
created_time: 2026-05-26T11:25:00+08:00
edited_time: 2026-05-26T11:25:00+08:00
edited_entity: llm
---

## 源证据

- 目录树（行 140）一句长行原文：
  > "~/wiki/ # Hub — lightweight, no content ├── wikis.json # Registry of all topic wikis ├── _index.md # Lists topic wikis with stats ├── log.md # Global activity log └── topics/ # Each topic is an isolated wiki ├── nutrition/ ..."
- "One topic, one wiki"（行 142–144）：
  > "Each research area is isolated. No cross-topic noise. Queries stay focused. A multi-wiki peek finds overlap when relevant."
- "Raw is immutable"（行 150–152）：
  > "Once a source is ingested it is never modified. Articles synthesize on top. Retraction removes both cleanly."
- "Inventory is state"（行 154–156）：
  > "Parts, source queues, corpora, watch items, and next actions live under inventory/ so they can be listed and revisited without becoming evidence."
- "Datasets stay external"（行 158–160）：
  > "datasets/ stores manifests, samples, profiles, and query recipes for large data. The wiki indexes data without copying it into the source corpus."
- "Archive is quiet"（行 162–164）。
- Wiki articles 三类目录（行 306–312）："Concepts / Topics / References"。
- `_index.md` 为"derived caches"（行 322）：
  > "Indexes (_index.md) exist in every directory. They're derived caches — rebuilt automatically from file frontmatter. The agent reads indexes first and never scans blindly."
- iCloud / portable path 劝告（行 332–334）。

## 卡片范围是否成立

卡片把页面里"Architecture / How the wiki works"两段中关于目录布局、五个不变量、isolation、portable path 的内容综合成一张概念卡。所有引文与目录结构都直接来自页面。"操作含义"段是从"One topic, one wiki / Raw is immutable / Inventory is state" 的合理推广（特别是关于"topic 是研究域维度，project 用 output/projects 子目录"）——这两个事实在源材料中分别出现（行 142、行 395），但卡片把它们合在一起作为操作建议。

## 发表门控结果

本轮未运行。

## 备注

- 与 `beyond-the-token-bottleneck-llm-wiki-case-study` 形成"工具 vs 案例"对比；与 `llm-knowledge-base-five-stage-workflow` 形成"工具 vs 模式"对比。
