---
schema: accepted_card_provenance.v3
card: ../cards/wikibase-item-property-snak-statement.md
material_id: wikibase-data-model
digest_id: digest_wikibase-data-model
source_paths:
  - data/raw/webpage/wikibase-data-model/text.txt
draft_card: ../../drafts/cards/wikibase-item-property-snak-statement.md
draft_provenance: ../../drafts/provenance/wikibase-item-property-snak-statement.md
similarity_result: ../../drafts/similarity/wikibase-item-property-snak-statement.json
comparison_provenance: ../../drafts/comparison/wikibase-item-property-snak-statement.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；四结构 + Statement BNF + Snak "small but more than a byte" + Datatype 非强类型说明均回到 L311–545。
created_time: 2026-05-26T15:10:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
edited_entity: llm
---

## 源证据

- 第 309-321 行（Overview）：Item / Statement / Property / Snak 的关系叙述。
- 第 423-432 行（Items）：IRI 形式 `Q1234567890`、稳定 ID、"Berlin 是 Item" 例子。
- 第 439-447 行（Properties）：IRI 形式 `P123456789`、与 Item 用不同 ID 命名、Datatype 仅"建议"。
- 第 467-475 行（Snaks 总述 + 三种 Snak BNF）。
- 第 528-545 行（Statements）：subject / mainSnak / qualifierSnaks / referenceRecords / rank + 完整 BNF + Obama 实例。
- 第 480 行：Datatype 非强类型的官方说明。

## 卡片范围是否成立

- 四结构、IRI 形式、BNF、Datatype 非强类型——全部直接引文档原文。
- "为什么不是简单三元组"是合理归纳——文档第 547 行起明确给出三个 Obama / Harry Potter / Austria 例子展示 qualifier 怎么把"主-谓-宾"扩成"声明 + 限定"。
- Rank 与 ReferenceRecord 信息出自第 572-592 行。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述：正文展开四结构 + BNF + 为什么不是三元组 + 边界。
  - 知识密度：抽象层级 + 例子 + 设计动机 + 误用警示。
  - 源支撑：source_ids 含 wikibase-data-model；L319 / L480 / L545 verbatim。
  - References / Footnotes 齐备。
  - frontmatter 完整且合法。
  - related 已填充：7 张 Wikibase / mem0 / graphrag / zep / Karpathy 相邻卡。

## 备注

- 这套抽象（Item / Property / Snak / Statement）在做"LLM 知识图谱 / Wikidata RAG"时反复出现。
- 与 wikibase-three-snak-types 卡互补——本卡讲整体结构，那张卡专门讲三种 Snak。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/wikibase-item-property-snak-statement.md`
- draft provenance: `../../drafts/provenance/wikibase-item-property-snak-statement.md`
- similarity: `../../drafts/similarity/wikibase-item-property-snak-statement.json`
- comparison provenance: `../../drafts/comparison/wikibase-item-property-snak-statement.md`
