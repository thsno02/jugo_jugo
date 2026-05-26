---
schema: comparison_provenance.v3
draft_card: ../cards/wikibase-three-snak-types.md
draft_provenance: ../provenance/wikibase-three-snak-types.md
similarity_result: ../similarity/wikibase-three-snak-types.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0
  - card_id: idea-file-share-the-idea
    card_path: llm_wiki/kb/cards/idea-file-share-the-idea.md
    score: 0.0
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0
decision: new_card
audit_required: false
created_time: 2026-05-26T16:17:00+08:00
edited_time: 2026-05-26T16:17:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "三种 Snak——区分"未填"、"无值"、"未知值"" **token 共享为空，score 全部 0.000**。三个候选都来自 Karpathy "llm wiki" launch 推文，是 v2 仅 15 张卡时算法的兜底排序。

## 2. draft 与候选在哪里不同

- draft 主题：Wikibase 数据模型中 PropertyValueSnak / PropertyNoValueSnak / PropertySomeValueSnak 三种 Snak 与"信息缺失"四种状态的语义区分；Rank 才是处理冲突的机制。论据轴是 knowledge representation + missing-data 建模。
- 候选 1 / 2：Karpathy 推文 idea file 抽象性 / 分享逻辑。
- 候选 3：LLM 对 wiki 跑 health checks。

虽然候选 3 和 draft 都含"wiki"字面，但语义完全不同：候选 3 谈"LLM 对 wiki 跑健康检查找不一致数据"，是数据维护行为；draft 谈"Wikibase 用三类 Snak 显式编码 missing-vs-absent-vs-unknown"，是知识表示模型——一个是运维操作，一个是 schema 语义。jieba 算出 0 score 与 body 判断一致。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies（含 `llm-wiki-health-checks`）与 Wikibase Snak / data model 主题毫无关联 → `new_card`。draft 自带 三类 Snak 语义差表、不要滥用 NoValueSnak 的原文 quote、Rank vs Snak 的关系说明、SomeValueSnak 不支持 disjunction 的限制，证据完整 → 不是 `revise_before_gate`。v2 无 Wikibase / knowledge representation 邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；与 `wikibase-item-property-snak-statement` 等同 family related。

## 5. 备注

Wikibase / knowledge representation 主题在 v2 KB 完全缺席。
