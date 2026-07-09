---
id: llm-wiki-model-recommendations
title: LLM Wiki 模型推荐策略
status: draft
card_type: guidance
tags: [llm-wiki, model-selection, cost-optimization, long-context]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
evidence_basis: documentation
justification: ../justification/llm-wiki-model-recommendations.md
canonical_concept: llm-wiki-model-recommendations
aliases: [model recommendations, 模型推荐, value-first strategy, 性价比策略]
summary: >-
  Value-First 策略：不需要旗舰模型。推荐 DeepSeek V4-Flash（1M，最低成本 $0.14/M）、
  Gemini-3.5-Flash（1M，4 倍速）、Qwen3.6-Plus（1M）、Grok-4（2M）等性价比选项。
  旗舰模型（Opus 4.7/GPT-5.5）仅选择性使用。本地模型上下文较小，建议云端 ingest + 本地 query。
related: [full-context-vs-rag, extraction-granularity-levels]
---

该插件采用 Value-First 策略——不需要旗舰模型即可获得优秀结果：[^src-1]

| 层级 | 模型 | 上下文 | 定位 |
|------|------|--------|------|
| 性价比首选 | DeepSeek V4-Flash | 1M | 最低成本 $0.14/M，适合批量 ingest |
| 性价比首选 | Gemini-3.5-Flash | 1M | 4 倍输出速度 |
| 性价比首选 | Qwen3.6-Plus | 1M | 强编码与 agent 能力 |
| 性价比首选 | Grok-4 | 2M | 超大 Wiki |
| 平衡 | Claude Sonnet 4.6 | 1M | 质量/成本平衡 |
| 轻量 | Claude Haiku 4.5 | 200K | 小型 Wiki |
| 旗舰 | Claude Opus 4.7 / GPT-5.5 | 1M | 极致质量，选择性使用 |

本地模型（Ollama）上下文通常较小（8K-128K），建议云端提供商做 ingest + 本地模型做 query。[^src-2] [^card-1]

[^src-1]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Model Recommendations" P1 -- "Value-First Strategy: You don't need flagship models. The following cost-effective alternatives deliver excellent results at lower prices"
[^src-2]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Model Recommendations" P1 -- "For local models (Ollama): context windows are typically smaller (8K–128K). Consider using a cloud provider for ingestion + local model for query"
[^card-1]: 参见 [[full-context-vs-rag]] 了解为何长上下文至关重要
