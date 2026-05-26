---
schema: comparison_provenance.v3
draft_card: ../cards/wikibase-timevalue-uncertain-dates.md
draft_provenance: ../provenance/wikibase-timevalue-uncertain-dates.md
similarity_result: ../similarity/wikibase-timevalue-uncertain-dates.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0714
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0667
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0588
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.08，shared_tokens 仅为「的」。draft 标题的实质 token（Wikibase / TimeValue / precision / before / after / 不确定日期）与 v2 候选（Karpathy LLM-wiki 元描述）无术语级重合。属于 jaccard 噪声。

## 2. draft 与候选在哪里不同

draft 是 mechanism 卡，来源 `wikibase-data-model`，论述 Wikibase TimeValue 的 6 字段结构（time / precision / before / after / timezone / calendarmodel）、不确定日期的 precision+before/after 表达模式（「1846-1855」用 1850 / precision=9 / before=4 / after=5）、显示存储分离设计、历史日期边界细节（18 世纪 1701-1800）、年份 0 的语义。属于「结构化时间数据建模」论点轴。

三张 v2 候选都是 Karpathy LLM-wiki 元描述。论点轴（时间数据 schema 设计 vs 个人 LLM wiki 模式）、来源（Wikibase 数据模型规范 vs Karpathy gist）、机制（precision/before/after 字段编码 vs LLM 写 markdown）完全不同。

## 3. 下一步的核心依据

shared_tokens 全是助词「的」，无语义关联。draft 引文具体到 L692-712 / L717-721 / L526，scope 自洽（已说明 disjunction 不支持、农历不在 schema 内、timezone 1972 前后语义不同等边界）。无任何 v2 卡可 merge 或 provenance_delta。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 sibling `wikibase-three-snak-types` / `wikibase-item-property-snak-statement` 同 source 互引。
