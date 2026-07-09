---
id: semantic-tiered-duplicate-detection
title: 语义两层去重检测
status: accepted
card_type: mechanism
tags:
- llm-wiki
- deduplication
- semantic-matching
- alias
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- obsidian-community-plugin
evidence_basis: documentation
justification: ../justification/semantic-tiered-duplicate-detection.md
canonical_concept: semantic-tiered-duplicate-detection
aliases:
- semantic tiering
- 语义分层去重
- two-tier duplicate detection
- alias-aware dedup
summary: 语义两层去重：Tier 1 始终经 LLM 验证，捕获直接名称匹配（跨语言翻译、缩写、高相似度标题）； Tier 2 在剩余 token 预算内填充中等相似度候选（共享链接、中等相似度）。别名（aliases）对 Tier 1 至关重要。v1.7.10 引入此机制。
related:
- wiki-page-aliases
- smart-fix-all-causality-order
---

自 v1.7.10 起，该插件实现语义两层去重检测机制：[^src-1]

**Tier 1**（始终经 LLM 验证）：捕获直接名称匹配——跨语言翻译（如 "CoT" 与 "思维链"）、缩写、高相似度标题。[^src-1]

**Tier 2**：在剩余 token 预算内填充间接信号候选——共享链接、中等相似度标题。[^src-1]

别名（aliases）对 Tier 1 检测至关重要。v1.7.11 之前生成的页面缺少别名，需运行 "Complete Aliases" 补全后去重才能有效工作。[^src-2] [^card-1]

[^src-1]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "How does duplicate detection work?" P1 -- "Tier 1 (always LLM-verified) catches cross-language matches, abbreviations, high-similarity titles. Tier 2 fills remaining token budget with moderate-similarity candidates"
[^src-2]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Semantic-Tier Duplicate Detection" P1 -- "Tier 1 (direct name matches: cross-language, abbreviations, high-similarity titles) always verified; Tier 2 (indirect signals: shared links, moderate similarity) fills token budget"
[^card-1]: 参见 [[wiki-page-aliases]] 了解别名机制
