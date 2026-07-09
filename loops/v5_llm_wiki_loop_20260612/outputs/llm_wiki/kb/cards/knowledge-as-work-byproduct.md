---
id: knowledge-as-work-byproduct
title: 知识增长作为工作副产品而非额外工作
status: accepted
card_type: design-principle
tags:
- knowledge-capture
- zero-overhead
- byproduct
- workflow-integration
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- falconer-enterprise-guide
evidence_basis: practitioner_report
justification: ../justification/knowledge-as-work-byproduct.md
canonical_concept: knowledge-as-work-byproduct
aliases:
- knowledge graph grows as a byproduct of work
- 知识作为副产品
summary: 企业 LLM wiki 的关键设计原则：知识图谱作为正常工作的副产品增长而非作为额外工作 the knowledge graph grows as a byproduct of work not as additional work；团队不改变工作方式 PR合并 Slack讨论解决 决策落地时系统自动检测受影响文档并草拟更新；这区别于此前所有失败的文档化 mandate
related:
- enterprise-llm-wiki-architecture
- maintenance-loop-as-core-innovation
---

材料提出的核心设计原则：企业 LLM wiki 中知识图谱的增长必须是正常工作的副产品（byproduct of work），而非额外工作（additional work）。[^src-1]

材料称这是将企业 LLM wiki 与"此前所有失败的文档化 mandate"区分开的关键属性。团队不需要改变工作方式——当 PR 合并、Slack 讨论解决、决策落地时，系统自动检测哪些文档受影响并草拟更新提案。文档 owner 在数秒内审批接受或拒绝。[^src-2]

这一原则暗示了企业知识管理失败的常见模式：要求人员在完成本职工作之外额外维护文档的系统，最终因维护负担而被放弃。[^card-1]

[^card-1]: 参见 [[maintenance-loop-as-core-innovation]] 中 Zettelkasten 维护杀死系统的论述
[^src-1]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Step 4: Ship normally" P57 -- "The knowledge graph grows as a byproduct of work, not as additional work."
[^src-2]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Step 4: Ship normally" P57 -- "This is the property that distinguishes an enterprise LLM wiki from every documentation mandate that's failed before it."
