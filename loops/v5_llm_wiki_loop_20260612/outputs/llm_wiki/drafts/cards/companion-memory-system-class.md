---
id: companion-memory-system-class
title: 伴侣记忆系统设计类
status: draft
card_type: design-class-definition
tags: [companion-memory, system-class, normative-governance, llm-memory]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
evidence_basis: theoretical_paper
justification: ../justification/companion-memory-system-class.md
canonical_concept: companion-memory-system-class
aliases: [companion system, companion memory, companion knowledge system, 伴侣系统, 伴侣记忆系统]
summary: >-
  companion memory system class 伴侣记忆系统设计类是一种规范定义的单用户 LLM 记忆系统类别，
  其评估目标为漂移下的纵向用户效用（longitudinal user utility under drift），而非基于对应的真值追踪。
  该类要求镜像操作连续性、补偿认知失败模式、保持架构可分离性以维持基座模型矫正通道。
  先行术语如 MemoryBank 的 companion scenario、Second Me 的单用户记忆卸载已命名此类但未规范治理。
  本框架提供缺失的规范规格：什么必须镜像、什么必须补偿、以及为何。
related: []
---

伴侣记忆系统（companion memory system）是一种规范定义的设计类，特指为单一用户长期服务的个人 LLM 知识系统。[^src-1]

该设计类的评估目标与通用知识基础不同：系统在漂移下的纵向用户效用（longitudinal user utility under drift）上被评估，而非对应真值追踪。[^src-2]

该类的三项规范义务：(1) 必须镜像操作连续性；(2) 必须补偿认知失败模式（僵化、证据压制、单一文化收敛）；(3) 必须保持架构可分离性以维持基座模型进化作为外部矫正通道。[^src-3]

先行工作已命名此类但未提供治理规范：MemoryBank 使用"long-term AI Companion scenario"，Second Me 明确为单用户构建，LongMemEval 将评估绑定到个性化辅助场景。缺失的是规范规格本身。[^src-4]

[^src-1]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "Abstract" P1 -- "Personal memory is a companion system --- its job is to serve one user over the long haul, not to track objective truth."
[^src-2]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "1.1 Three claims" P2 -- "the system is evaluated on longitudinal user utility under drift, subject to explicit anti-entrenchment and correction obligations"
[^src-3]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "11. Conclusion" P4 -- "it must mirror operational continuity, it must compensate epistemic failure, and it must preserve architectural separability"
[^src-4]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "1.1 Three claims" P2 -- "MemoryBank already uses 'long-term AI Companion scenario' as a primary capability descriptor. Second Me explicitly frames single-user memory as a 'memory offload system' serving one user."
