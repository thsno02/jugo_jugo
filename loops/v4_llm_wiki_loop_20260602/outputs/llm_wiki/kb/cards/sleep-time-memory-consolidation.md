---
id: sleep-time-memory-consolidation
title: 睡眠期离线记忆巩固机制
status: accepted
card_type: mechanism
tags: [memory-consolidation, offline-processing, sleep-time-update, inference-decoupling]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-lightmem]
justification: ../justification/sleep-time-memory-consolidation.md
canonical_concept: sleep-time-memory-consolidation
aliases: [sleep-time update, 离线记忆巩固, 睡眠期更新]
summary: >-
  sleep-time-memory-consolidation（sleep-time update, 离线记忆巩固, 睡眠期更新）将 LLM 记忆系统的长期记忆巩固过程从在线推理中解耦为离线程序，使测试时在线成本进一步大幅降低（token 减少最高 106x/117x，API 调用减少最高 159x/310x）。
related: [lightmem-three-stage-memory, memory-augmentation-overhead]
---

在 LightMem 的三阶段记忆架构中，长期记忆阶段引入了一种称为"sleep-time update"的机制：将记忆巩固（consolidation）过程作为离线程序（offline procedure）执行，从而与在线推理（online inference）完全解耦 [^src-1]。

这一设计的核心洞察是：记忆的组织和整合不必在用户查询的实时路径上完成。通过将巩固操作移至"睡眠期"（即非推理时段），系统在实际测试时的在线成本可以远低于总成本。论文报告的数据显示，纯在线测试时成本的降低幅度显著高于总体成本降低：token 使用量最高减少 106x/117x，API 调用次数最高减少 159x/310x [^src-2]，而总体（含离线部分）的降低分别为 38x/20.9x 和 30x/55.5x。

这一在线-离线解耦策略意味着系统可以在空闲时段批量处理记忆巩固任务，而在用户交互时仅需访问已整理好的长期记忆，从而实现极低的推理时延和成本。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-lightmem/text.txt` -- Abstract -- "long-term memory with sleep-time update employs an offline procedure that decouples consolidation from online inference"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-lightmem/text.txt` -- Abstract -- "purely online test-time costs are even lower, achieving up to 106x / 117x token reduction and 159x / 310x fewer API calls"
