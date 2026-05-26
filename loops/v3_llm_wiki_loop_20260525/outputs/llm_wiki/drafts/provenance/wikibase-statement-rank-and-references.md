---
schema: draft_card_provenance.v3
draft_card: ../cards/wikibase-statement-rank-and-references.md
material_id: wikibase-data-model
digest_id: digest_wikibase-data-model
source_paths:
  - data/raw/webpage/wikibase-data-model/text.txt
created_time: 2026-05-26T15:20:00+08:00
edited_time: 2026-05-26T15:20:00+08:00
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

本轮未运行。

## 备注

- 这条机制在 LLM 知识库设计里有借鉴价值——"多源声明并存 + 按 rank 筛选"比"每条声明只留一条"更适合处理矛盾。可在 comparison_provenance 与 LLM wiki 的"矛盾合成"卡片对照。
