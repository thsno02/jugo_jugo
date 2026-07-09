---
id: mirror-vs-compensate-principle
title: 镜像与补偿原则
status: draft
card_type: design-principle
tags: [mirror-compensate, companion-memory, design-principle, temporal-procedure]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
evidence_basis: theoretical_paper
justification: ../justification/mirror-vs-compensate-principle.md
canonical_concept: mirror-vs-compensate-principle
aliases: [mirror-vs-compensate, mirror where mirroring serves utility compensate where mirroring damages it, 镜像补偿原则]
summary: >-
  mirror-vs-compensate principle 镜像与补偿原则是伴侣记忆系统的核心设计规则，
  系统在操作维度（工作语境、负载承载结构、自引用连续性、词汇）上镜像用户，
  在认知失败维度（僵化、证据压制、单一文化收敛）上补偿用户。
  该原则为时间结构化程序冲突规则：流式路径默认镜像，计划整合窗口补偿，AUDIT 为慢周期仲裁者。
  先行文献 "To Mask or to Mirror" (Qian et al.) 已命名此张力，本框架贡献的是跨时间尺度的具体解决程序。
related: [companion-memory-system-class]
---

镜像与补偿原则（mirror-vs-compensate principle）规定：伴侣系统在操作维度上镜像用户，在认知失败维度上补偿用户。选择规则是工具性的，非哲学性的。[^src-1]

镜像的操作维度包括：用户当前推理的工作语境、用户依赖的负载承载结构、允许用户接续之前工作的自引用连续性、用户长期发展的词汇和框架。[^src-2]

补偿的认知失败维度包括：可证伪的高引力条目的僵化、对矛盾已定信念的证据压制、重复使用下向单一文化的收敛。[^src-3]

该原则的时间结构化程序冲突规则：流式路径下时间压力中默认镜像；计划整合窗口中补偿；当引力保护条目跨多周期牵涉不良结果时 AUDIT 作为仲裁者。[^src-4]

类比表述：拐杖镜像用户步态但补偿跛行；眼镜镜像视野并补偿畸变。[^src-5]

[^src-1]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "1.2 Mirror where mirroring serves utility" P1 -- "A companion system should mirror its user on some dimensions and compensate for its user on others. The selection rule is instrumental, not philosophical."
[^src-2]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "1.2" P2 -- "the working context the user is currently reasoning within, the load-bearing structure the user depends on for coherent thought, the continuity of self-reference"
[^src-3]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "1.2" P3 -- "entrenchment of demonstrably false high-gravity entries, suppression of evidence contradicting settled beliefs, convergence toward monoculture under repeated use"
[^src-4]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "1.2" P6 -- "mirror by default under time pressure, compensate during scheduled integration windows, and treat AUDIT as the tiebreaker"
[^src-5]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "1.2" P5 -- "A cane mirrors the user's gait --- it does not try to walk differently. A cane does not mirror a limp --- it compensates for it."

[^card-1]: companion-memory-system-class — 镜像与补偿原则是伴侣记忆设计类的核心规范义务之实施规则
