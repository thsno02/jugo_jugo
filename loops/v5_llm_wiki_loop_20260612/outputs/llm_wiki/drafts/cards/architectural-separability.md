---
id: architectural-separability
title: 架构可分离性作为安全承诺
status: draft
card_type: design-commitment
tags: [separability, base-model-evolution, correction-channel, safety, companion-memory]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
evidence_basis: theoretical_paper
justification: ../justification/architectural-separability.md
canonical_concept: architectural-separability
aliases: [architectural separability, separability from base-model weights, external correction channel, 架构可分离性, 基座模型进化通道]
summary: >-
  architectural separability 架构可分离性是伴侣记忆框架的安全设计承诺，
  要求维基保持在基座模型权重之外。这保留基座模型进化作为外部矫正通道：
  用户运行伴侣系统五年后受益于模型改进的事实先验和对齐训练，因为更换基座模型是配置变更非维基操作。
  将维基折入权重则此通道永久关闭。Lewis et al. 2020 和 Atlas 已建立外部化教条（更新无需重训），
  本框架补充的是伴侣特定安全理由：可分离性对抗用户耦合认知僵化是结构必要的而非仅操作方便。
  三个诚实限制：维基仍锚定解释、基座更新并非总是修正、用户不控制更新时机。
related: [companion-memory-system-class, three-correction-channels]
---

架构可分离性要求维基保持在基座模型权重之外。这是设计承诺而非实现细节。[^src-1]

保留的外部矫正通道：用户运行伴侣系统五年后受益于模型改进的事实先验和对齐训练，因为更换基座模型是配置变更非维基操作。将维基折入权重则此通道永久关闭。[^src-2]

先行外部化教条：Lewis et al. 2020 基于操作理由（无需重训即可修订扩展）；Atlas 扩展（测试时更新或交换索引）；harness engineering review 推荐跨模型转移测试。本框架补充的伴侣特定安全理由：可分离性不仅操作方便，而是对抗用户耦合认知僵化结构上必要的。[^src-3]

三个诚实限制：(1) 维基仍锚定解释，高引力虚假条目仍偏置输出；(2) 基座模型更新并非总是修正——实验室因多种原因更新；(3) 用户不控制更新时机。框架受益于此通道但不能依赖它。[^src-4]

冲突路由矩阵第7行：基座模型更新引入与高引力维基条目矛盾的事实先验时，维基条目被标记为在更新后下一个 CONSOLIDATE 周期中审查。此行结构上依赖架构可分离性——无可分离性则此行不可能存在。[^src-5]

[^src-1]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "8.3" Layer 4 -- "The separation of external memory from model weights is an established architectural doctrine...separability is not merely operationally convenient but structurally necessary"
[^src-2]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "Abstract" P5 -- "swapping the model is a configuration change, not a wiki operation. Fold the wiki into weights and you lose this channel."
[^src-3]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "8.3" Layer 4 P2 -- "Lewis et al. (2020) already justifies it on operational grounds...the harness engineering review goes further"
[^src-4]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "8.3" Layer 4 P3 -- "Three honest limits: the wiki still anchors interpretation...base model updates are not always corrections...the user does not control when updates happen"
[^src-5]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.0 Conflict routing matrix" Row 7 -- "This row depends structurally on architectural separability: the external correction channel exists only because the wiki is not folded into base model weights."

[^card-1]: companion-memory-system-class — 可分离性是伴侣系统三项规范义务之一
