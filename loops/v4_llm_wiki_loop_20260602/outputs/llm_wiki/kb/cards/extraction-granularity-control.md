---
id: extraction-granularity-control
title: 提取粒度控制
status: accepted
card_type: mechanism
tags: [llm-wiki, extraction, granularity, cost-control, configuration]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
justification: ../justification/extraction-granularity-control.md
canonical_concept: extraction-granularity-control
aliases: [提取粒度, extraction granularity, 实体提取深度, entity extraction depth]
summary: >-
  extraction-granularity-control（提取粒度 / extraction granularity / 实体提取深度）
  是 LLM Wiki 插件的可配置提取深度机制：五个预设级别（Minimal 5 / Coarse 10 / Standard 50 / Fine 100 / Custom 1-300），
  在分析深度与 API 成本之间取得平衡
related: [ingest-operation, source-granularity-effect]
  - ingest-operation
---

Karpathy LLM Wiki 插件提供**五级可配置的提取粒度**（Extraction Granularity），控制 LLM 从源文档中提取实体和概念的深度[^src-1]：

| 级别 | 预计项目数 | 适用场景 |
|------|-----------|---------|
| Fine | ~100 | 深度分析，含边缘提及；token 成本高，适合关键资料 |
| Standard | ~50 | 均衡提取，日常笔记的良好默认值 |
| Coarse | ~10 | 快速概览，仅核心实体；成本低、速度快 |
| Minimal | ~5 | 仅必要项目；适合批量处理 100+ 文件或测试新资料 |
| Custom | 1-300 | 用户自定义实体/概念数量上限，用于专业工作流 |

该设计的核心洞察是：**提取深度与 API 成本之间存在直接权衡**。材料建议对大文件夹使用 Minimal 或 Coarse 以节省时间和 API 费用，仅对需要深度分析的关键文档选择性使用 Fine[^src-2]。这意味着同一 Wiki 中不同来源可以有不同的提取粒度——关键文献深挖、背景资料浅扫[^src-3]。

提取粒度设置影响实体提取和概念提取两个维度，LLM 对源文档的分析深度和产出页面数量都随之变化[^src-4]。提取粒度是摄入操作中的关键参数之一[^card-1]。值得注意的是，提取深度（产出多少实体）与源文件的切分粒度（输入多大）构成 wiki 编译质量的两个正交维度——即使提取深度设为 Fine，若整本书作为单文件输入仍可能产出"slop"[^card-2]。

## Footnotes

[^card-1]: [摄入操作](ingest-operation.md) -- 本卡聚焦提取深度的五级配置机制，该卡定义提取所依附的摄入操作整体流程（阅读资料 → 写摘要 → 更新索引）

[^src-1]: `data/raw/webpage/obsidian-community-plugin/text.txt` -- "Extraction Granularity" L240-249 -- "Five options control how deeply the LLM extracts entities from sources: Fine (~100 items)... Standard (~50 items)... Coarse (~10 items)... Minimal (~5 items)... Custom (1-300 items)"
[^src-2]: `data/raw/webpage/obsidian-community-plugin/text.txt` -- "Extraction Granularity" L250 -- "Recommendation: Use Minimal or Coarse for large folders to save time and API costs. Use Fine selectively on key documents that warrant deep analysis."
[^src-3]: `data/raw/webpage/obsidian-community-plugin/text.txt` -- "Performance & Cost FAQ" L420-421 -- "Choose 'Minimal', 'Coarse', or 'Standard' Extraction Granularity to reduce page count and save API costs."
[^card-2]: [源文件粒度效应](source-granularity-effect.md) -- 本卡控制从源文档提取实体的深度（产出多少），该卡控制源文档本身的切分粒度（输入多大），两者共同构成 wiki 编译质量的双维度调参空间

[^src-4]: `data/raw/webpage/obsidian-community-plugin/text.txt` -- "Knowledge Quality" L260 -- "Entity/Concept Extraction — LLM extracts entities (people, orgs, products, events) and concepts (theories, methods, terms) from your notes with flexible extraction granularity"
