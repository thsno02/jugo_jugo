---
id: extraction-granularity-levels
title: 提取粒度五级设置
status: draft
card_type: configuration
tags: [llm-wiki, extraction, granularity, cost-optimization]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
evidence_basis: documentation
justification: ../justification/extraction-granularity-levels.md
canonical_concept: extraction-granularity-levels
aliases: [extraction granularity, 提取粒度, entity extraction levels]
summary: >-
  五级提取粒度控制 LLM 从源文档提取实体/概念的深度：Fine 约 100 项（深度分析）、
  Standard 约 50 项（日常默认）、Coarse 约 10 项（快速概览）、Minimal 约 5 项
  （批量处理）、Custom 1-300 项（自定义）。v1.6.2 引入，v1.10.0 扩展。
related: [three-layer-wiki-architecture, parallel-page-generation]
---

提取粒度（Extraction Granularity）控制 LLM 从源文档提取实体/概念的深度，v1.6.2 引入，v1.10.0 扩展为五级：[^src-1]

| 粒度 | 约提取项数 | 适用场景 |
|------|-----------|---------|
| Fine | ~100 | 深度分析，边缘提及也纳入，高 token 成本，适合关键文档 |
| Standard | ~50 | 平衡提取，日常笔记的默认选择 |
| Coarse | ~10 | 快速概览，仅核心实体，低成本快速 ingest |
| Minimal | ~5 | 仅必要项，适合批量处理 100+ 文件或测试 |
| Custom | 1-300 | 用户自定义实体/概念限制 |

材料建议：大文件夹用 Minimal/Coarse 节省时间和 API 成本，关键文档选择性用 Fine。[^src-2] [^card-1]

[^src-1]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Extraction Granularity" P1 -- "Five options control how deeply the LLM extracts entities from sources"
[^src-2]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Extraction Granularity" P1 -- "Use Minimal or Coarse for large folders to save time and API costs. Use Fine selectively on key documents"
[^card-1]: 参见 [[three-layer-wiki-architecture]] 了解 sources → wiki 的 ingest 流程
