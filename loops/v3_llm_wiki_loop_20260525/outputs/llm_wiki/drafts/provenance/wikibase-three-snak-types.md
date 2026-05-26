---
schema: draft_card_provenance.v3
draft_card: ../cards/wikibase-three-snak-types.md
material_id: wikibase-data-model
digest_id: digest_wikibase-data-model
source_paths:
  - data/raw/webpage/wikibase-data-model/text.txt
created_time: 2026-05-26T15:15:00+08:00
edited_time: 2026-05-26T15:15:00+08:00
edited_entity: llm
---

## 源证据

- 第 471-475 行（Snak 总述 + BNF）。
- 第 477-498 行（PropertyValueSnak：Berlin / Georgia / Gandhi 例子）。
- 第 500-513 行（PropertyNoValueSnak：Circle / Mount Everest 例子 + 不滥用警示）。
- 第 515-526 行（PropertySomeValueSnak：Ambrose Bierce 例子 + "1347 或 1348"限制）。

## 卡片范围是否成立

- 三种 Snak 的语义、例子、警示全部直接来自原文。
- "missing vs absent vs unknown" 第四种状态作为对比是合理引申——文档第 507 行明确把 "really does not exist" 与 "not entered yet" 对立。
- "Rank 才是处理冲突的机制" 引自 statement 章节（第 572-585 行），属同文档内引用，不算跨文档综合。

## 发表门控结果

本轮未运行。

## 备注

- 这套区分对"LLM 自我表达 unknown vs absent"有直接借鉴价值——可在 comparison_provenance 与 LongMemEval 的 abstention (ABS) 概念对照。
