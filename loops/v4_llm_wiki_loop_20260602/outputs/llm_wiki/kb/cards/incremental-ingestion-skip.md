---
id: incremental-ingestion-skip
title: 增量摄入与批量跳过
status: accepted
card_type: mechanism
tags: [llm-wiki, ingestion, incremental, idempotent, cost-control]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
justification: ../justification/incremental-ingestion-skip.md
canonical_concept: incremental-ingestion-skip
aliases: [增量摄入, Smart Batch Skip, 批量跳过, incremental ingestion, 已处理文件跳过]
summary: >-
  incremental-ingestion-skip（增量摄入 / Smart Batch Skip / 批量跳过）
  是 LLM Wiki 插件的增量处理机制：文件夹批量摄入时自动检测已处理文件并跳过，
  重复摄入同一源文件时执行增量更新（合并新信息）而非全量重写，
  节省 API 成本并保持幂等性
related: [extraction-granularity-control, obsidian-karpathy-wiki-plugin, query-to-wiki-feedback]
---

Karpathy LLM Wiki 插件实现了**两层增量摄入**机制，确保批量操作的幂等性和成本效率。

**第一层：文件级跳过（Smart Batch Skip）**

文件夹批量摄入时，插件**自动检测已处理文件并跳过**[^src-1]。批量报告中会显示跳过文件的数量。这意味着用户可以安全地对同一文件夹反复执行 "Ingest from folder" 命令——新增文件被处理，已处理文件被跳过，无额外 API 成本[^src-2]。

**第二层：页面级增量更新**

当用户对同一源文件再次执行单文件摄入时，系统不会全量重写已存在的实体/概念页面，而是**执行增量更新——新信息被合并进已有页面**[^src-3]。摘要页（summary pages）则会被重新生成[^src-3]。设置了 `reviewed: true` 的页面受到保护，不会被覆盖[^src-4]。

**成本控制价值**：该机制与提取粒度控制[^card-1]构成互补的成本优化维度——粒度控制解决「每次提取多深」，增量跳过解决「哪些文件需要处理」。材料明确将 Smart Batch Skip 列为 API 成本控制策略之一[^src-2]。

**工程设计特征**：
- 文件级检测是确定性的（基于已处理标记），不依赖 LLM 判断
- 页面级合并是语义的（依赖 LLM 理解新旧内容），属于智能知识融合[^src-4]
- 两层设计使得系统在文件未变时完全跳过（零成本），文件已变时精确更新（最小成本）

该机制与查询反馈回路[^card-2]共同体现了系统对知识重复写入的零容忍设计——无论知识来源是源文档还是查询对话，写入前都有去重/跳过机制防止冗余。

## Footnotes

[^src-1]: `data/raw/webpage/obsidian-community-plugin/markdown.md` L58 -- "Smart Batch Skip: When ingesting a folder, the plugin automatically detects already-processed files and skips them to save time and API costs. The batch report shows skipped count."
[^src-2]: `data/raw/webpage/obsidian-community-plugin/markdown.md` L210 -- "Smart Batch Skip automatically skips already-ingested files"
[^src-3]: `data/raw/webpage/obsidian-community-plugin/markdown.md` L57 -- "Re-ingesting the same source does incremental updates on entity/concept pages (new info merged in). Summary pages are regenerated."
[^src-4]: `data/raw/webpage/obsidian-community-plugin/markdown.md` L85 -- "Smart Knowledge Fusion — Multi-source updates merge new info without redundancy, contradictions preserved with attribution, reviewed: true pages protected from overwrite"
[^card-1]: [提取粒度控制](extraction-granularity-control.md) -- 本卡解决「哪些文件需要处理」的成本优化，该卡解决「每次提取多深」的成本优化，两者正交互补
[^card-2]: [查询到 Wiki 的反馈回路](query-to-wiki-feedback.md) -- 本卡对源文档摄入执行增量跳过，该卡对查询对话保存执行语义去重，两者共同体现写入前去重的设计一致性
