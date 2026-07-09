---
id: llm-wiki-scale-ceiling
title: LLM Wiki 的规模上限与去重脆弱性
status: accepted
card_type: limitation-analysis
tags:
- scale-ceiling
- deduplication
- context-window
- llm-wiki
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- robin-cartier-llm-knowledge-bases
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-scale-ceiling.md
canonical_concept: llm-wiki-scale-ceiling
aliases:
- scale ceiling
- 200 pages limit
- deduplication fragility
- wiki scale limit
summary: LLM wiki pattern 存在规模上限：约 200 页 / ~100K tokens（index + content），超出后 LLM 无法在上下文中容纳
  index，需要 sub-wikis 或 retrieval layer。去重（deduplication）依赖 LLM 判断，规模增大后脆弱——无确定性防护时
  wiki 积累近重复页面。时序信号弱（仅 last_updated），单用户默认（无访问控制、无 merge conflicts 处理、无审计追踪）。
related:
- llm-knowledge-base-pattern
- llm-wiki-scale-thresholds
---

LLM wiki pattern 据源材料存在明确的规模上限和结构性局限：[^src-1] [^card-1]

**规模上限**：约 200 页 / ~100K tokens（index + content）。超出该阈值后，LLM 无法在上下文窗口中容纳完整 index，需要引入 sub-wikis 或 retrieval layer 才能继续运作。

**去重脆弱性**：去重（deduplication）完全依赖 LLM 判断，在规模增大后变得脆弱。缺乏确定性防护机制时，wiki 会随时间积累近重复页面。

**其他局限**：
- 时序信号弱：仅有单一"last updated"字段，缺失关系型存储能提供的趋势追踪能力（first_seen / last_seen）
- 单用户默认：无访问控制、无 merge conflict 处理机制、审计追踪仅限于 log 文件

**适用场景判断**：当用途为个人第二大脑/研究/学习时适合该 pattern；当需要运营自动化/趋势追踪/流水线驱动知识时应选用结构化知识库（关系型）；企业规模/百万文档时应选 RAG 或混合方案。[^src-1]

[^src-1]: `data/raw/webpage/robin-cartier-llm-knowledge-bases/markdown.md` -- "Strengths and limits" P1 -- "Scale ceiling around ~200 pages / ~100K tokens of index + content. Beyond that, the LLM can't hold the index in context and you need sub-wikis or a retrieval layer."
[^card-1]: 参见 [[llm-knowledge-base-pattern]] 了解该 pattern 的基本架构
