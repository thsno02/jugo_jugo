---
schema: accepted_card_provenance.v3
card: ../cards/wikibase-conceptual-not-serialization.md
material_id: wikibase-data-model
digest_id: digest_wikibase-data-model
source_paths:
  - data/raw/webpage/wikibase-data-model/text.txt
draft_card: ../../drafts/cards/wikibase-conceptual-not-serialization.md
draft_provenance: ../../drafts/provenance/wikibase-conceptual-not-serialization.md
similarity_result: ../../drafts/similarity/wikibase-conceptual-not-serialization.json
comparison_provenance: ../../drafts/comparison/wikibase-conceptual-not-serialization.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；conceptual / serialization / formal semantics 三层解耦原文 verbatim，UML + WON BNF 用途 与 §2 六个 requirements 均回到 L244–400。
created_time: 2026-05-26T15:30:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
edited_entity: llm
---

## 源证据

- 第 244-250 行（开篇 living document 段）：自定位 "conceptual model"。
- 第 248 行："Separate documents describe the serialization of the Wikibase data model in JSON and in RDF."
- 第 274-294 行（§2 Goals and requirements）：列出 coverage / simplicity / extensibility / flexibility / exchange / technical support 六个要求。
- 第 298-302 行（"not supposed to do" 列表）：明确不规定 internal data structures、export formats、formal semantics。
- 第 326-400 行（§4）：UML 用法 + Wikidata Object Notation (WON) BNF。
- 第 366 行：WON 明确"not intended to be used in implementations"。

## 卡片范围是否成立

- "conceptual / serialization / implementation 解耦"、"WON 仅用于举例"、"六个相互冲突的 requirements"——全部直接引文档原文。
- "不是 RDF/OWL，不为机器自动推理"是对 §2 中 "Formal semantics ... will be given in a separate document" 的合理归纳，没引述外部材料。
- 边界提示（"读 JSON/RDF doc 而不是本文"）忠于第 248 行的内容。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述：正文展开三层"不是什么" + 设计原因 + 边界与误用。
  - 知识密度：定位 + 设计动机 + 边界 + 操作建议。
  - 源支撑：source_ids 含 wikibase-data-model；L244 / L248 / L298–302 / L366 verbatim。
  - References / Footnotes 齐备。
  - frontmatter 完整且合法。
  - related 已填充：6 张 Wikibase / Karpathy / robin / aillm-wiki schema 相邻卡。

## 备注

- 这条"分层规范"思路与 LLM wiki "raw / wiki / agents.md 分层"、LongMemEval "indexing / retrieval / reading 三阶段"在元方法上一致——可在 comparison_provenance 阶段做"分层 spec"主题对比。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/wikibase-conceptual-not-serialization.md`
- draft provenance: `../../drafts/provenance/wikibase-conceptual-not-serialization.md`
- similarity: `../../drafts/similarity/wikibase-conceptual-not-serialization.json`
- comparison provenance: `../../drafts/comparison/wikibase-conceptual-not-serialization.md`
