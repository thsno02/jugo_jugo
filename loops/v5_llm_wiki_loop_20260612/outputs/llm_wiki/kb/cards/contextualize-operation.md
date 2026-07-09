---
id: contextualize-operation
title: CONTEXTUALIZE 深度拟合压缩操作
status: accepted
card_type: operation-specification
tags:
- contextualize
- depth-fitted-compression
- cold-memory
- linkout
- selective-absorption
- companion-memory
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-memory-as-metabolism
evidence_basis: theoretical_paper
justification: ../justification/contextualize-operation.md
canonical_concept: contextualize-operation
aliases:
- CONTEXTUALIZE
- depth-fitted compression
- selective absorption
- 语境化操作
- 深度拟合压缩
summary: CONTEXTUALIZE 是伴侣记忆框架的补偿操作，在梦周期中将外部源压缩到用户当前工作语境深度。 核心洞察：外部源无单一规范压缩——同一架构决策记录对产品经理和开发者产出不同有用摘要。 两项设计承诺：(1) 在梦周期而非流式摄入时运行（保持TRIAGE浅层+允许压缩对新语境重做）； (2) 深度默认由推断而非用户显式设置（从维基条目、查询模式、主题邻域推断）。 链出（linkout）到完整原始源是非可选承诺——压缩条目是工作表示非真值。
  引入三层存储：冷记忆（原始）、原始缓冲区（待巩固）、活跃维基（深度拟合工作表示）。 代谢类比：选择性吸收——细胞不吸收环境中的一切，只吸收当前代谢状态能使用的。
related:
- sleep-consolidation-architecture
- triage-operation
- three-tier-storage-model
---

CONTEXTUALIZE 在梦周期中将外部源压缩到用户当前工作语境深度，并保留到完整外部源的链出（linkout）。[^src-1]

核心问题：外部源无单一规范压缩。同一架构决策记录对产品经理产出目标/权衡/利益相关者理由的摘要，对开发者产出实现约束/库选择/边缘情况的摘要。两者都是语境正确的压缩。[^src-2]

两项设计承诺：
1. 在梦周期而非运行时摄入时运行——如果用户语境在摄入和巩固之间改变，下一梦周期对新语境压缩而非旧语境。缓冲区在周期间的工作包括保留重压缩的选项。
2. 深度默认由推断——从用户其他维基条目、近期查询模式、源所落入的主题邻域推断。推断有时失败，这正是链出非可选的原因。[^src-3]

一致性不变量：MUST 保留到原始外部源的链出（非可选，不可为存储效率牺牲）；MUST 在计划巩固周期中运行而非流式摄入时；MUST 在产出深度拟合表示前为每个处理的外部源创建冷记忆对象；MUST NOT 压缩后丢弃原始源。[^src-4]

代谢类比：选择性吸收——生物细胞不吸收环境中的一切，只吸收当前代谢状态能使用的，其余通过或排泄。维基是代谢活跃的；什么算营养输入取决于用户当前在消化什么。[^src-5]

[^src-1]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.4 CONTEXTUALIZE" P1 -- "Compress external sources to fit the user's current working-context depth on the relevant topic, and preserve a linkout to the full external source"
[^src-2]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.4" P1 -- "The same architecture decision record yields a different useful summary for a Product Owner than for a Developer...Neither is wrong. Both are contextually correct compressions"
[^src-3]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.4" P3-4 -- "CONTEXTUALIZE runs in the dream cycle, not at runtime ingestion...the depth is inferred by default, not explicitly set by the user"
[^src-4]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "7.5 Conformance CONTEXTUALIZE" -- "MUST preserve a linkout to the original external source...MUST run in the scheduled consolidation cycle"
[^src-5]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.4" P5 -- "Biological cells do not absorb everything in their environment; they absorb what their current metabolic state can use"

[^card-1]: sleep-consolidation-architecture — CONTEXTUALIZE 在梦周期中运行
[^card-2]: triage-operation — CONTEXTUALIZE 与 TRIAGE 在不同时间尺度处理不同内容类型
