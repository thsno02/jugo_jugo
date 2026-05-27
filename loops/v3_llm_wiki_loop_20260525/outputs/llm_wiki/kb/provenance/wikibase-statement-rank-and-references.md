---
schema: accepted_card_provenance.v3
card: ../cards/wikibase-statement-rank-and-references.md
material_id: wikibase-data-model
digest_id: digest_wikibase-data-model
source_paths:
  - data/raw/webpage/wikibase-data-model/text.txt
draft_card: ../../drafts/cards/wikibase-statement-rank-and-references.md
draft_provenance: ../../drafts/provenance/wikibase-statement-rank-and-references.md
similarity_result: ../../drafts/similarity/wikibase-statement-rank-and-references.json
comparison_provenance: ../../drafts/comparison/wikibase-statement-rank-and-references.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；preferred/normal/deprecated 三级、best rank、ReferenceRecord BNF、deprecated 不等于错的注解均回到 L572–592 / L313。
created_time: 2026-05-26T15:20:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
edited_entity: llm
---

## 源证据

- 第 572-585 行（§7.1 Ranks of Statements）：三级定义、多 preferred 含义、deprecated 含义、best rank 规则、"故意三级"设计意图。
- 第 588-592 行（§7.2 ReferenceRecords）：reference 是 Snak 集合 + BNF。
- 第 313 行（Overview 段）："the list of references is allowed to be empty"。

## 卡片范围是否成立

- Rank 三级、best rank、deprecated 不等于"statement 错"——全部直接引文档原文。
- ReferenceRecord 是 Snak 集合而非自由文本——是文档 BNF 明示。
- "同时多个 preferred 不是冲突未解决"是文档原话归纳，没有引申。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述：正文展开三级 rank + best rank 规则 + ReferenceRecord 结构 + 边界。
  - 知识密度：定义 + 设计意图 + 边界与误用。
  - 源支撑：source_ids 含 wikibase-data-model；L577 / L581 / L583 verbatim。
  - References / Footnotes 齐备。
  - frontmatter 完整且合法。
  - related 已填充：6 张 Wikibase / Karpathy / zep 相邻卡。

## 备注

- 这条机制在 LLM 知识库设计里有借鉴价值——"多源声明并存 + 按 rank 筛选"比"每条声明只留一条"更适合处理矛盾。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/wikibase-statement-rank-and-references.md`
- draft provenance: `../../drafts/provenance/wikibase-statement-rank-and-references.md`
- similarity: `../../drafts/similarity/wikibase-statement-rank-and-references.json`
- comparison provenance: `../../drafts/comparison/wikibase-statement-rank-and-references.md`
