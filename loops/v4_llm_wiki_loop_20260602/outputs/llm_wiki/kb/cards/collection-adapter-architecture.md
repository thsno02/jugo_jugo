---
id: collection-adapter-architecture
title: 集合摄入适配器架构
status: accepted
card_type: mechanism
tags: [llm-wiki, collection, adapter, bulk-ingest, mediawiki, wayback, git]
created_time: 2026-06-08T10:00:00+08:00
edited_time: 2026-06-08T10:00:00+08:00
edited_entity: llm
source_ids: [repo-nvk-llm-wiki]
justification: ../justification/collection-adapter-architecture.md
canonical_concept: collection-adapter-architecture
aliases: [集合适配器, collection adapters, 批量摄入架构, ingest-collection adapters]
summary: >-
  collection-adapter-architecture（集合适配器 / collection adapters / 批量摄入架构 / ingest-collection adapters）
  是 llm-wiki 处理大规模上游语料的可插拔适配器系统：git/mediawiki-dump/mediawiki-api/csv-messages/wayback-cdx
  五种适配器共享「清单+子源」的二层写入模式和去重不变量
related: [parallel-multi-agent-research, hub-resolution-algorithm, llm-wiki-pattern]
---

`/wiki:ingest-collection` 命令处理**有界上游语料库（bounded upstream corpus）**的批量摄入——区别于单篇文章的 `/wiki:ingest`。其核心设计是可插拔的适配器架构[^src-1]。

**五种适配器**[^src-2]：

| 适配器 | 输入源 | 子源目标 | 特殊处理 |
|--------|--------|----------|----------|
| `git` | GitHub/GitLab 仓库 | `raw/articles/` | shallow clone、blob SHA 去重、BIP 头解析 |
| `mediawiki-dump` | XML dump（.xml/.xml.bz2/.xml.gz） | `raw/articles/` | 流式 iterparse 避免全量加载、跳过重定向 |
| `mediawiki-api` | api.php 端点 | `raw/articles/` | continuation token 分页、速率限制尊重 |
| `csv-messages` | CSV/TSV/JSON/JSONL | `raw/notes/` | 字段推断（id/date/author/subject/body） |
| `wayback-cdx` | Wayback CDX API | `raw/articles/` | `id_` 重放 URL、readability 转 markdown |

**共享的二层写入模式**[^src-3]：
1. 写入一个**清单源（manifest）**到 `raw/repos/`，标签 `[collection, collection-manifest, <adapter>]`
2. 为每个上游页面/文件/消息写入一个**不可变子源（child source）**

**去重不变量**：按 `collection + upstream_id + revision/sha` 三元组去重。如果上游内容变更，写入新的不可变来源文件而非覆盖旧文件[^src-4]。

**适配器自动检测**[^src-5]：
1. `.xml`/`.xml.bz2`/`.xml.gz` → `mediawiki-dump`
2. `github.com/`、`.git` 或含 `.git/` 的本地目录 → `git`
3. `.csv`/`.tsv`/`.json`/`.jsonl` + 消息类字段 → `csv-messages`
4. `web.archive.org/cdx` 或 "Wayback" → `wayback-cdx`
5. URL 含 `/wiki/`/`/w/` 或可达 `api.php` → `mediawiki-api`

**编译指导**：集合摄入后不为每个上游页面创建一篇编译文章。正确做法是按概念、标准族、时间线、术语表等进行聚类综合编译[^src-6]。对于 BIP 仓库，「发表」代表满足仓库流程标准，不等于获得采纳共识[^src-7]。对于社区 wiki，默认置信度为 medium 除非有更强来源佐证[^src-8]。

**安全阀**：超过 500 个子源且用户未显式提供 `--limit` 时，显示数量并请求确认后再写入[^src-9]。

该架构体现了 llm-wiki「一主题一 wiki」设计中处理外部大规模语料的策略：不是将语料直接变成 wiki 文章，而是先作为不可变来源保存，再通过编译通道选择性综合[^card-1]。

## Footnotes

[^card-1]: [LLM Wiki 模式](llm-wiki-pattern.md) -- 集合适配器是 LLM Wiki 模式中「raw 不可变 → compile 综合」原则在大规模语料场景的落地

[^src-1]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: AGENTS.md -- "Bulk-ingest bounded upstream corpora without turning them directly into compiled wiki articles. Use this for Git document repositories, BIP-style proposal sets, MediaWiki XML dumps/API sites, CSV/JSON message archives, and Wayback CDX snapshot sets."
[^src-2]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/ingest-collection.md -- "Adapters: git, mediawiki-dump, mediawiki-api, csv-messages, wayback-cdx"
[^src-3]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/ingest-collection.md -- "Write one manifest source to raw/repos/... Write child sources to raw/articles/"
[^src-4]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/ingest-collection.md -- "Deduplicate by collection + upstream_id + revision/sha... if upstream content changes, write a new raw source instead of overwriting the old one."
[^src-5]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/ingest-collection.md -- "Source ending in .xml... -> mediawiki-dump... Source contains github.com/... -> git..."
[^src-6]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: AGENTS.md -- "Compile collections selectively: synthesize concepts, topics, timelines, glossaries, standards families, and reference indexes. Do not create one compiled wiki article per upstream page by default."
[^src-7]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/ingest-collection.md -- "For BIPs, publication is provenance for proposal text, not proof of adoption or consensus."
[^src-8]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/ingest-collection.md -- "For community wikis, default confidence to medium unless corroborated by stronger sources."
[^src-9]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/ingest-collection.md -- "If more than 500 child sources would be written and the user did not explicitly provide --limit, show the count and ask for confirmation"
