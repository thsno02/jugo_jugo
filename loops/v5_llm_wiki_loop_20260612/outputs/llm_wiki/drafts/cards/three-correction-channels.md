---
id: three-correction-channels
title: 三矫正通道安全故事
status: draft
card_type: safety-architecture
tags: [correction-channels, safety, consolidation, federation, base-model-evolution, companion-memory]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
evidence_basis: theoretical_paper
justification: ../justification/three-correction-channels.md
canonical_concept: three-correction-channels
aliases: [three correction channels, safety story, 三矫正通道, 安全故事, partial safety story]
summary: >-
  three correction channels 三矫正通道是伴侣记忆框架的安全故事，在三个不同时间尺度上提供结构防御：
  (1) 代理内巩固周期（小时到天）——少数压力晋升使累积矛盾证据有信念修正的结构路径；
  (2) 跨代理联邦（周到年）——跨命名单元类型（家庭/团队/部门/社区维基）分享匿名化引力和少数信号；
  (3) 外部基座模型进化（月到年）——由架构可分离性保留。
  安全故事明确部分性：不解决坏信念强化问题，不声称解决。
  残余失败模式：完全新颖的坏信念既未在基座模型中表示也未被后续经验矛盾，无通道捕获。
related: [architectural-separability, consolidate-operation, minority-hypothesis-retention]
---

框架的安全故事由三个在不同时间尺度上运行的矫正通道组成。没有单一通道足够，组合使安全故事非平凡。[^src-1]

通道 1：代理内巩固周期（小时到天）——最快通道。少数压力晋升给累积矛盾证据一个在巩固窗口中转移主导解释的结构路径。[^src-2]

通道 2：跨代理联邦（周到年）——跨命名单元类型分享匿名化引力和少数信号。四种结构不同的组织形式：家庭维基（代际更替）、团队维基（招聘/离职节奏）、部门维基（角色交接）、社区维基（自选成员，最复杂漂移动态）。联邦是独立研究方向，非单代理问题的救援。[^src-3]

通道 3：外部基座模型进化（月到年）——最慢通道。不由框架实现，由框架的架构可分离性承诺保留。研究方向：伴侣系统应如何响应基座模型交换？巩固周期是否应在更新后重跑？[^src-4]

安全故事明确部分性：不解决坏信念强化问题，不声称解决。残余失败模式——完全新颖的坏信念既未在基座模型中表示也未被后续经验矛盾——无通道捕获。[^src-5]

[^src-1]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "10. Research Agenda" P1 -- "We name three correction channels operating on different timescales. Each opens a distinct research direction."
[^src-2]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "10.1" P1 -- "The single-agent consolidation mechanism described in Section 5.5 is the fastest correction channel"
[^src-3]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "10.2" P1-5 -- "Family wikis have the longest time horizons...Team and company wikis...Department wikis...Community wikis"
[^src-4]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "10.3" P1 -- "The slowest correction channel operates on the timescale of base model generations...It is not implemented by the framework; it is preserved by the framework's architectural commitment to separability."
[^src-5]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "9. Limitations" P8 -- "If a user arrives at a bad belief not represented anywhere in the base model and not contradicted by subsequent experience, none of the four layers in Section 8.3 catches it."

[^card-1]: architectural-separability — 通道3由可分离性承诺保留
[^card-2]: consolidate-operation — 通道1由 CONSOLIDATE 操作实现
[^card-3]: minority-hypothesis-retention — 通道1的少数压力晋升依赖此机制
