---
id: llm-wiki-scale-thresholds
title: LLM Wiki 规模阈值与工具选择
status: draft
card_type: heuristic
tags: [llm-wiki, scale, grep, gbrain, hybrid-search]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-scale-thresholds.md
canonical_concept: llm-wiki-scale-thresholds
aliases: [scale thresholds, 规模阈值, 500 页分界点, grep vs hybrid search]
summary: >-
  LLM wiki 规模阈值 llm-wiki-scale-thresholds 定义了工具选择的三个区间：<30 inputs 复合效应未达临界（plain notes 足够）；35-500 页为 markdown+grep+lifecycle fields 甜区（grep <50ms）；>500 页需升级至 hybrid search（BM25+向量+图）或 GBrain 级 Postgres 基础设施。GBrain 设计面向 14,700+ 文件的 ops-grade 部署。据作者判断约 500 页（possibly 1,000）前 markdown + manual weekly lint 足够。
related: []
---

材料定义了 LLM wiki 基础设施选择的三个规模区间 [^src-1] [^src-2]：

| 区间 | 工具选择 | 依据 |
|------|---------|------|
| <30 inputs | Plain notes 足够 | 复合效应未达临界质量 |
| 35-500 页 | Markdown + grep + lifecycle fields | grep 返回 <50ms |
| >500 页（possibly 1,000） | Hybrid search / Postgres / Dream Cycle | grep 开始变慢 |

GBrain（Garry Tan）的参考规模：14,700+ 文件，夜间 cron 巩固，BM25+向量+图混合搜索 [^src-1]。

作者当前选择：在 35 页规模坚持 grep，称 GBrain 为"beautiful infrastructure with nothing to do" [^src-3]。

[^card-1]: 与 [ripple-effect-ingest] 相关——复合效应需要临界质量才显现
[^card-2]: 与 [llm-wiki-three-layer-structure] 相关——基础架构在不同规模阈值下演进

[^src-1]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "What Surprised Me" P47-54 -- comparison table showing scale recommendations
[^src-2]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "Who Should (and Shouldn't)" P78 -- "You have fewer than ~30 inputs total. The compounding only kicks in past some critical mass"
[^src-3]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "FAQ" P90 -- "I'll switch when my page count crosses ~500 and grep starts feeling slow...beautiful infrastructure with nothing to do."
