---
id: mirror-vs-compensate-principle
title: 镜像-补偿设计原则
status: accepted
card_type: mechanism
tags: [companion-memory, design-principle, mirror, compensate, conflict-resolution, temporal-structure]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
justification: ../justification/mirror-vs-compensate-principle.md
canonical_concept: mirror-vs-compensate-principle
aliases: [镜像-补偿原则, mirror-vs-compensate, mirror and compensate, 镜像与补偿, 操作镜像认知补偿]
summary: >-
  mirror-vs-compensate-principle（镜像-补偿原则 / mirror-vs-compensate / 镜像与补偿）伴侣记忆系统的核心设计规则：在操作维度（词汇、结构、连续性）镜像用户，在认知失败维度（固化、证据压制）补偿用户；冲突时流式路径默认镜像、定期整合窗口执行补偿、AUDIT 作为慢周期仲裁者
related: [audit-stress-test, companion-knowledge-system, human-llm-role-division, sleep-consolidation-architecture]
---

镜像-补偿原则（mirror-vs-compensate principle）是伴侣知识系统的工具性选择规则，决定系统应继承用户的哪些属性[^src-1]。

**镜像维度**：系统在操作维度上镜像用户——当前工作上下文、承重结构、自我引用的连续性、随时间发展的词汇和框架。在这些维度上，对齐是设计目标，偏离是失败模式。一个拒绝继承用户词汇的伴侣是不可用的[^src-2]。

**补偿维度**：系统在认知失败维度上补偿用户——可证伪的高引力条目的固化、压制与已定信念矛盾的证据、重复使用下向单一文化的收敛。在这些维度上，对齐是失败模式，偏离是设计目标。一个继承用户所有确认偏差的伴侣是有害的[^src-3]。

**时间结构化的冲突解决**：当镜像与补偿指向相反方向时，框架默认在流式路径中保持操作连续性，将冲突路由到定期补偿操作[^src-4]。规则是程序性的：时间压力下默认镜像，定期整合窗口中补偿，AUDIT 作为仲裁者处理引力保护条目在多个周期中产生反复坏结果的情况[^src-5]。

框架将五个操作分为两类：TRIAGE、DECAY 和记忆引力是镜像机制；CONSOLIDATE、AUDIT 和 CONTEXTUALIZE 是补偿机制[^src-6]。镜像与补偿之间的张力不是待解决的 bug，而是设计原则本身。

然而，这一原则与 LLM Wiki 中的人机角色分工形成张力：镜像-补偿原则赋予系统主动纠偏的自主权（补偿维度），而角色分工将 LLM 定位为纯粹的执行者，战略思考完全归人类[^dist-1]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 1.2" -- "A companion system should mirror its user on some dimensions and compensate for its user on others. The selection rule is instrumental, not philosophical."
[^src-2]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 1.2" -- "A companion that refused to inherit its user's vocabulary would not be usable."
[^src-3]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 1.2" -- "A companion that inherited its user's every confirmation bias would be harmful."
[^src-4]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 1.2" -- "When mirror and compensate point in opposite directions, the framework defaults to preserving operational continuity in the streaming path and routing the conflict to scheduled compensate operations."
[^src-5]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 1.2" -- "mirror by default under time pressure, compensate during scheduled integration windows, and treat AUDIT as the tiebreaker"
[^src-6]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 1.2" -- "TRIAGE, DECAY, and memory gravity are mirror mechanisms. CONSOLIDATE, AUDIT, and CONTEXTUALIZE are compensate mechanisms"
[^dist-1]: [人机角色分工](human-llm-role-division.md) -- 本卡赋予 LLM 在认知失败维度上的纠偏自主权（补偿），该卡将 LLM 限定为执行苦差事的仆人角色，战略思考全归人类；区分点在于 LLM 是否拥有超越用户意图的纠偏权
