---
id: contradiction-as-asset
title: 矛盾即资产原则
status: draft
card_type: design-principle
tags: [llm-wiki, contradiction, knowledge-management, rohit-v2]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
evidence_basis: practitioner_report
justification: ../justification/contradiction-as-asset.md
canonical_concept: contradiction-as-asset
aliases: [contradictions are assets not errors, 矛盾是资产而非错误, contradiction protocol, 矛盾标记协议]
summary: >-
  矛盾即资产原则 contradiction-as-asset 指 LLM wiki 中发现新旧声明矛盾时不覆盖而是标记保留两版。规则是"don't overwrite, mark"——添加 contradicts: 字段，保留双方，在 lint 时浮现。作者在 pitfall #3 中违反此原则导致丢失历史推理（RAG vs LLM wiki 争论），两个月后需要旧论证时已不可恢复。Rohit v2 明确此规则而 v1 silent。
related: []
---

矛盾即资产（contradictions are assets, not errors）[^src-1]：

**规则**：当 Claude 发现新 claim 与 wiki 现有页面矛盾时，不覆盖旧页面，而是：
1. 添加 `contradicts:` 字段
2. 保留两个版本
3. 在 lint 时浮现矛盾供人审查

**反面教训**（pitfall #3）：作者曾让 Claude 用新观点（LLM wiki replaces RAG）直接覆盖旧页面（RAG is the right architecture）。两个月后需要旧推理来 argue with someone，发现已不可恢复 [^src-2]。

此原则在 Rohit v2 中明确表述；Karpathy v1 对此"silent" [^src-2]。

**适用边界**：此哲学与受监管领域（法律/医疗/金融）的合规要求冲突——合规要求单一真相源 [^src-3]。

[^card-1]: 与 [memory-lifecycle-fields] 相关——contradicts 字段是 lifecycle fields 的一部分
[^card-2]: 与 [schema-first-principle] 相关——矛盾协议在 schema.md 中定义

[^src-1]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "What I added from Rohit's v2" P40 -- "Contradiction protocol: when Claude finds a new claim that contradicts a wiki page, the rule is don't overwrite, mark."
[^src-2]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "4 Pitfalls I Hit" P60 -- "contradictions are assets, not errors. I now explicitly run contradicts: and keep both versions."
[^src-3]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "Who Should (and Shouldn't)" P80 -- "The contradictions-as-assets philosophy clashes with compliance requirements that demand single-source-of-truth."
