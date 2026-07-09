---
id: wiki-page-aliases
title: Wiki 页面强制别名机制
status: draft
card_type: mechanism
tags: [llm-wiki, alias, i18n, deduplication]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
evidence_basis: documentation
justification: ../justification/wiki-page-aliases.md
canonical_concept: wiki-page-aliases
aliases: [mandatory page aliases, 强制别名, alias completion, 别名补全]
summary: >-
  每个生成页面强制包含至少 1 个别名（翻译、缩写、替代名称），实现跨语言去重检测。
  Lint 检测缺失别名并支持一键并行批量生成。别名用于索引中的别名感知搜索。
related: [semantic-tiered-duplicate-detection, smart-fix-all-causality-order]
---

该插件要求每个生成的 Wiki 页面包含至少 1 个别名（alias），可以是翻译、缩写或替代名称。这一强制机制支撑跨语言去重检测。[^src-1]

Lint 扫描可检测缺失别名的页面，支持一键并行批量生成（"Complete Aliases"）。别名一旦存在，索引即支持别名感知搜索——例如搜索 "DSA" 可找到 "DeepSeek-Sparse-Attention"。[^src-2] [^card-1]

[^src-1]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Features" P1 -- "Mandatory Page Aliases — Every generated page includes at least 1 alias (translation, acronym, alternate name), enabling cross-language duplicate detection"
[^src-2]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Rebuild your index" P1 -- "alias entries for every page, enabling alias-aware search (e.g., searching 'DSA' finds 'DeepSeek-Sparse-Attention')"
[^card-1]: 参见 [[semantic-tiered-duplicate-detection]] 了解别名在去重中的作用
