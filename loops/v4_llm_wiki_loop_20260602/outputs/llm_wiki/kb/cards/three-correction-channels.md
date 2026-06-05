---
id: three-correction-channels
title: 三纠正通道
status: accepted
card_type: concept
tags: [companion-memory, safety, correction, timescale, federation, base-model]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
justification: ../justification/three-correction-channels.md
canonical_concept: three-correction-channels
aliases: [三纠正通道, three correction channels, 三时间尺度安全, three-timescale safety, 三层安全故事]
summary: >-
  three-correction-channels（三纠正通道 / three-timescale safety）伴侣记忆框架的安全故事：三个不同时间尺度的纠正通道——代理内整合周期（小时到天）、跨代理联邦（周到年）、基模型演进（月到年）；没有单一通道充分，组合构成非平凡但明确部分的安全叙事
related: [companion-knowledge-system, sleep-consolidation-architecture, architectural-separability-as-safety]
---

伴侣记忆框架的安全故事由三个在不同时间尺度上运作的纠正通道组成[^src-1]。

**通道 1：代理内整合周期**（小时到天）[^src-2]
最快的纠正通道。通过 CONSOLIDATE 的缓冲区内评分和少数派压力提升，积累的矛盾证据可以在整合窗口期间获得挑战主导解释的结构路径。开放问题包括评分函数如何权衡缓冲区内一致性与 wiki 一致性、少数派压力阈值如何调优。

**通道 2：跨代理联邦**（周到年）[^src-3]
联邦是独立的研究层而非单代理问题的救赎。四个命名的组织单元各有不同的更新动态：
- **家庭 wiki**：最长时间跨度，真正的代际更换
- **团队/公司 wiki**：按招聘和离职节奏更新
- **部门 wiki**：介于团队和组织规模之间
- **社区 wiki**：自选成员、最复杂的漂移动态

**通道 3：外部基模型演进**（月到年）[^src-4]
最慢的纠正通道。不是由框架实现，而是通过架构可分离性承诺来保留。研究方向包括：基模型更新后是否应重新运行整合周期、引力评分如何调整、wiki 与不同基模型之间的版本兼容性。

**组合安全叙事**：三个通道在不同时间尺度上运作、针对不同失败模式、可组合而不冲突。没有单一通道充分。框架的安全故事是组合[^src-5]。

**诚实限制**：框架在单代理层面不自我纠正认知基础。它提供三个时间尺度的结构性防御，但不解决坏信念强化问题，也不声称解决[^src-6]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 10" -- "We name three correction channels operating on different timescales."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 10.1" -- "The single-agent consolidation mechanism described in Section 5.5 is the fastest correction channel --- it runs on a schedule measured in hours or days."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 10.2" -- "The relevant units are not 'multiple companion systems' in the abstract. They are specific, structurally different organizational forms, each with its own update dynamics."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 10.3" -- "The slowest correction channel operates on the timescale of base model generations --- months to years. It is not implemented by the framework; it is preserved by the framework's architectural commitment to separability."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 10" -- "These three channels operate on different timescales... address different failure modes, and compose without conflicting. No single channel is sufficient."
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 11" -- "The framework does not self-correct on epistemic grounds at the single-agent level."
