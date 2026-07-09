---
id: volatility-freshness-scoring
title: 波动性分级与新鲜度评分机制
status: draft
card_type: scoring-mechanism
tags: [llm-wiki, volatility, freshness-score, staleness, article-maintenance, lindy-effect]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-nvk-llm-wiki]
evidence_basis: code_implementation
justification: ../justification/volatility-freshness-scoring.md
canonical_concept: volatility-freshness-scoring
aliases: [volatility tier, freshness score, staleness scoring, hot warm cold, article volatility, Lindy Effect in wiki]
summary: >-
  llm-wiki 通过 volatility 字段（hot/warm/cold）控制文章新鲜度衰减速度。新鲜度评分 0-100 由四维度各 25 分组成：源新鲜度、验证近期性、编译近期性、源链完整性。衰减曲线按 volatility 缩放——hot 衰减快（产品规格/时事），cold 衰减慢（基础概念/数学证明，Lindy Effect）。conversation-sourced 文章使用两维重基公式。无硬编码天数截止——复合评分自然标记正确时间点的正确文章。
related: [lint-as-schema-migration, multi-agent-parallel-research-pipeline, derived-index-concurrency-protocol]
---

llm-wiki 对文章的维护优先级采用波动性分级和复合新鲜度评分：

**波动性分级（volatility）**[^src-1]：
| 级别 | 衰减速率 | 适用场景 | 示例 |
|------|---------|---------|------|
| hot | 快 | 快速变化源 | NVIDIA 规格、选举结果、API changelog |
| warm | 中等 | 季度-年度节奏 | 最佳实践、框架对比、市场分析 |
| cold | 慢 | 基础概念 | TCP/IP 基础、密码学算法、Lindy Effect |

**新鲜度评分（0-100）**[^src-2]：
| 维度 | 测量内容 | 计算来源 |
|------|---------|---------|
| 源新鲜度 | raw sources 多旧 | 所有 sources 的 ingested 日期平均 |
| 验证近期性 | 人工最后确认准确性时间 | verified 日期 |
| 编译近期性 | 最后重编译时间 | updated 日期 |
| 源链完整性 | 引用源是否仍存在 | sources 条目解析比例 |

**设计特点**：
- 无硬编码天数截止——复合评分基于 volatility 和实际源状态自然标记正确文章
- Lindy Effect 应用：cold 内容存活越久越持久，非相反
- `compiled-from: conversation` 文章跳过源维度，使用两维重基公式（x2 缩放至 0-100）
- 低于阈值（默认 70）由 lint C14 标记[^src-3]

[^src-1]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "wiki-structure.md Volatility Classification" -- "hot: Fast... warm: Moderate... cold: Slow"
[^src-2]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "wiki-structure.md Freshness Score" -- "Each source-backed article's freshness is a composite of four dimensions, each contributing 0-25 points"
[^src-3]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "wiki-structure.md Freshness Score" -- "There are no hardcoded day cutoffs — the composite score naturally flags the right articles at the right time"
