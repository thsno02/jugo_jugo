---
id: collection-ingestion-adapter-system
title: 集合 Ingest 适配器系统——结构化上游批量导入
status: draft
card_type: subsystem-design
tags: [llm-wiki, collection-ingestion, adapter-pattern, git-adapter, mediawiki, wayback-cdx, csv-messages]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-nvk-llm-wiki]
evidence_basis: code_implementation
justification: ../justification/collection-ingestion-adapter-system.md
canonical_concept: collection-ingestion-adapter-system
aliases: [ingest-collection, collection adapter, bulk ingest, git adapter, mediawiki-dump adapter, wayback-cdx adapter, csv-messages adapter]
summary: >-
  llm-wiki 的 /wiki:ingest-collection 实现 5 种适配器用于结构化上游批量导入：git（浅克隆 spec 仓库如 BIPs）、mediawiki-dump（流式 XML 解析）、mediawiki-api（分页 API 抓取）、csv-messages（每行/对象一条消息源）、wayback-cdx（CDX 作为清单，id_ replay 获取存档快照）。从不递归爬取 HTML。产出一个 manifest（raw/repos/）加每个上游页面一个不可变 child source。去重键为 collection + upstream_id + revision/sha。编译采用选择性聚类而非逐页一文章。
related: [llm-as-knowledge-compiler-metaphor, opinionated-inventory-dataset-layers, hub-topic-wiki-isolation]
---

llm-wiki 的集合 ingest 子系统实现了一种"适配器模式"处理有界上游语料库的批量导入：

**5 种适配器**[^src-1]：
| 适配器 | 用途 | 主要访问路径 |
|--------|------|-------------|
| git | GitHub/GitLab 规范仓库 | shallow clone, ls-tree, 文件读取 |
| mediawiki-dump | 完整 MediaWiki 导入 | 官方 .xml/.xml.bz2/.xml.gz dump |
| mediawiki-api | 目标性 MediaWiki 导入 | api.php allpages + revisions |
| csv-messages | 邮件列表/消息归档 | Python stdlib csv/json 解析 |
| wayback-cdx | Internet Archive 存档快照 | CDX API 清单 + id_ replay |

**核心原则**：从不递归爬取 HTML。使用结构化上游接口。[^src-2]

**产出结构**：
- 1 个 manifest source（`raw/repos/`，标签 `collection-manifest`）
- N 个 child sources（通常 `raw/articles/`，csv-messages 用 `raw/notes/`）
- 去重键：`collection` + `upstream_id` + `revision`/`sha`
- 上游内容变更时写入新 raw source，不覆盖旧的

**编译指南**：
- 优先综合聚类（概念、标准族、时间线、词汇表）而非逐上游页面一文章
- BIP 发布于仓库意味着满足流程标准，不代表采纳或共识
- 社区 wiki 默认 confidence: medium，除非有权威规范佐证[^src-3]

[^src-1]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "ingest-collection.md" -- "Supported: git, mediawiki-dump, mediawiki-api, csv-messages, wayback-cdx"
[^src-2]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "AGENTS.md Collection Ingestion" -- "Never recursively crawl HTML; use structured upstream interfaces."
[^src-3]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "ingestion.md Collection Compilation" -- "Prefer synthesized clusters over one compiled article per page."
