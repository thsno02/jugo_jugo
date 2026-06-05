---
id: contradiction-as-asset
title: 矛盾作为知识资产
status: accepted
card_type: operational_rule
tags: [llm-wiki, contradiction, knowledge-management, preservation]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
justification: ../justification/contradiction-as-asset.md
canonical_concept: contradiction-as-asset
aliases: [矛盾即资产, contradictions are assets, 矛盾保留协议, contradiction protocol, 矛盾标记]
summary: >-
  contradiction-as-asset（矛盾即资产 / contradictions are assets / 矛盾保留协议 / contradiction
  protocol / 矛盾标记）指 LLM Wiki 中发现矛盾时不覆盖旧主张而是标记 contradicts: 字段保留双方，
  因为旧推理在未来可能有用；覆盖导致不可逆的知识损失
related: [contradiction-state-machine, edge-invalidation-mechanism, lint-operation, memory-lifecycle-metadata, minority-pressure-promotion, source-faithfulness-risk]
---

当 LLM 在摄入新资料时发现与已有 wiki 页面的主张矛盾，操作规则是**不覆盖，而是标记**：添加 `contradicts:` 字段，保留新旧双方，在巡检（lint）时集中处理[^src-1]。

这一规则的核心原则是：**矛盾是资产，不是错误**（contradictions are assets, not errors）[^src-2]。

作者通过一次痛苦的实践教训验证了这一原则。他在第 4 个月让 Claude 用新观点（LLM wiki 取代 RAG）直接覆盖了旧页面（RAG 是个人知识库的正确架构）。两个月后，他需要旧推理来与他人讨论，却发现原始论证已不可恢复[^src-3]。

该规则来自 Rohit v2 的矛盾处理协议。Karpathy v1 对矛盾处理是「沉默的」（silent），未给出明确指导[^src-4]。这与 lint 操作形成互补：lint 操作检测矛盾的存在，而本规则规定了发现矛盾时的处理方式。

Obsidian 社区插件将此原则工程化为一套矛盾状态机，通过明确的状态转换路径（detected → resolved / pending_fix）系统化管理被保留的矛盾[^card-1]。伴侣记忆框架则更进一步：少数派假设不仅被保留，还通过跨周期缓冲区压力积累机制获得挑战主导解释的能力[^card-2]。与此形成张力的是，Graphiti 的边失效机制选择了相反策略——始终优先采纳新信息，将旧边标记为失效[^dist-1]。

## Footnotes

[^src-1]: `data/raw/webpage/openaitoolshub-six-months/text.txt` -- L58 -- "when Claude finds a new claim that contradicts a wiki page, the rule is don't overwrite, mark. Add contradicts: field, keep both, surface during lint."
[^src-2]: `data/raw/webpage/openaitoolshub-six-months/text.txt` -- L96 -- "contradictions are assets, not errors. I now explicitly run contradicts: and keep both versions."
[^src-3]: `data/raw/webpage/openaitoolshub-six-months/text.txt` -- L96 -- "I had an old wiki page claiming 'RAG is the right architecture for personal knowledge bases.' A new article I ingested said the opposite (LLM wiki replaces RAG). I let Claude rewrite the old page to match. Wrong move. Two months later I needed the old reasoning to argue with someone, and it was gone."
[^src-4]: `data/raw/webpage/openaitoolshub-six-months/text.txt` -- L96 -- "Rohit v2 is right about this and v1 is silent."
[^card-1]: [矛盾状态机](contradiction-state-machine.md) -- 本卡提出矛盾保留的原则，该卡实现了系统化跟踪矛盾的状态机机制
[^card-2]: [少数派压力提升机制](minority-pressure-promotion.md) -- 本卡主张保留矛盾双方，该卡进一步提出少数派假设可通过多周期压力积累挑战主导解释
[^dist-1]: [边失效与动态知识更新机制](edge-invalidation-mechanism.md) -- 本卡主张矛盾双方对等保留，该卡主张新信息优先、旧边失效，区分点在于对矛盾的价值判断：资产 vs. 待解决的不一致
