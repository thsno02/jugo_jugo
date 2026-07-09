---
id: poisonedrag-nontarget-question-impact
title: 恶意文本对非目标问题的影响极小
status: draft
card_type: experimental-finding
tags: [poisonedrag, non-target-questions, collateral-impact, stealthiness]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-poisonedrag]
evidence_basis: experimental_paper
justification: ../justification/poisonedrag-nontarget-question-impact.md
canonical_concept: poisonedrag-nontarget-question-impact
aliases: [non-target question impact, collateral damage, 非目标问题影响]
summary: >-
  PoisonedRAG 注入的恶意文本对非目标问题(non-target questions)影响极小。在 NQ 数据集上, 仅 0.3% (黑盒) / 0.9% (白盒) 的非目标问题检索到恶意文本, 且仅 0% / 0.4% 的非目标问题答案被影响。这意味着攻击具有高度针对性(targeted), 不会引起系统整体性能的可观测下降, 增强了隐蔽性。偶尔被检索的原因是恶意文本与非目标问题共享关键词(如均与 Star Wars 相关)。
related: [poisonedrag-black-box-attack, poisonedrag-attack-success-scaling]
---

PoisonedRAG 的一个重要隐蔽性指标是对非目标问题的附带影响:

**实验设定**: NQ 数据集默认设定，随机选 100 个非目标问题×重复 10 次 = 1000 个非目标问题

**结果**:
- 恶意文本被非目标问题检索到的比例: 黑盒 0.3%, 白盒 0.9%
- 非目标问题答案被恶意文本影响的比例: 黑盒 0%, 白盒 0.4% [^src-1]

**附带检索原因**: 某些非目标问题与恶意文本在语义上有交集。例如: 非目标问题 "How many seasons are in Star Wars The Clone Wars?" 检索到了为 "How many death stars are there in Star Wars?" 构造的恶意文本。[^src-2]

**意义**: 攻击高度精准(targeted)，不引起系统整体性能下降，增强了攻击的隐蔽性和实际威胁性。

[^src-1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Discussion / Impact of malicious texts on non-target questions" -- "0.3% and 0.9% ... 0% and 0.4%"
[^src-2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "appendix / Examples of Non-target Questions" -- "How many seasons are in Star Wars The Clone Wars?"
[^card-1]: [poisonedrag-attack-success-scaling]
