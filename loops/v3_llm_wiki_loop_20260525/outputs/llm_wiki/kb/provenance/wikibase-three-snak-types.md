---
schema: accepted_card_provenance.v3
card: ../cards/wikibase-three-snak-types.md
material_id: wikibase-data-model
digest_id: digest_wikibase-data-model
source_paths:
  - data/raw/webpage/wikibase-data-model/text.txt
draft_card: ../../drafts/cards/wikibase-three-snak-types.md
draft_provenance: ../../drafts/provenance/wikibase-three-snak-types.md
similarity_result: ../../drafts/similarity/wikibase-three-snak-types.json
comparison_provenance: ../../drafts/comparison/wikibase-three-snak-types.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；三种 Snak 语义、Circle/Mount Everest/Ambrose Bierce 例子、不滥用 NoValueSnak 警示均回到 L471–526。
created_time: 2026-05-26T15:15:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
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

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述：正文展开三种 Snak 表格 + 设计动机 + 边界。
  - 知识密度：语义对照 + 例子 + 滥用警示 + 限制（disjunction）。
  - 源支撑：source_ids 含 wikibase-data-model；L509–511 / L513 / L524 verbatim。
  - References / Footnotes 齐备。
  - frontmatter 完整且合法。
  - related 已填充：5 张 Wikibase / Karpathy 相邻卡。

## 备注

- 这套区分对"LLM 自我表达 unknown vs absent"有直接借鉴价值——可在 comparison_provenance 与 LongMemEval 的 abstention (ABS) 概念对照。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/wikibase-three-snak-types.md`
- draft provenance: `../../drafts/provenance/wikibase-three-snak-types.md`
- similarity: `../../drafts/similarity/wikibase-three-snak-types.json`
- comparison provenance: `../../drafts/comparison/wikibase-three-snak-types.md`
