---
id: mem0-performance-results
title: Mem0 性能实验结果
status: draft
card_type: empirical-finding
tags: [benchmark-results, single-hop, multi-hop, temporal, open-domain, state-of-the-art]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0]
evidence_basis: experimental_paper
justification: ../justification/mem0-performance-results.md
canonical_concept: mem0-performance-results
aliases: [Mem0 LOCOMO results, Mem0 benchmark scores, Mem0 实验结果]
summary: >-
  Mem0 在 LOCOMO 上的实验结果：single-hop Judge=67.13 F1=38.72（SOTA），multi-hop Judge=51.15 F1=28.64（SOTA），temporal Judge 方面 Mem0^g=58.13 F1=51.55（SOTA），open-domain Zep Judge=76.60 略优于 Mem0^g=75.71。Mem0 相对 OpenAI memory 在 Judge 上有 26% 相对改进。Mem0 base 擅长 single-hop/multi-hop，Mem0^g 擅长 temporal/open-domain。
related: []
---

Mem0 和 Mem0^g 在 LOCOMO 四类问题上的性能表现：[^src-1]

**Single-Hop**：Mem0 达到最强结果——F1=38.72, BLEU-1=27.13, Judge=67.13。图记忆（Mem0^g）边际下降，表明关系结构对单轮检索任务效用有限。

**Multi-Hop**：Mem0 明确领先——F1=28.64, Judge=51.15，体现其高效检索和整合跨会话分散信息的能力。Mem0^g 在此未提供增益（Judge=47.19），据材料推测图结构在多步推理中可能引入开销或冗余。

**Temporal**：Mem0^g 取得最高 F1=51.55, Judge=58.13，验证结构化关系图在捕获时间序列和事件排序方面的优势。Mem0 base 也表现不俗（Judge=55.51）。

**Open-Domain**：Zep 以 Judge=76.60 略优于 Mem0^g 的 75.71（差距仅 0.89 个百分点），Mem0 为 72.93。[^src-2]

总体而言，Mem0 相对 OpenAI memory 在 Judge 指标上实现 26% 相对改进。Mem0 base 的稠密自然语言记忆对简单检索高效，Mem0^g 的显式关系建模在需要时间和上下文整合的任务中至关重要。[^src-3]

[^card-1]: [[mem0-locomo-benchmark-evaluation]] 描述了评估设置
[^card-2]: [[mem0-memory-architecture-overview]] 和 [[mem0-graph-memory-architecture]] 描述了被评估的两种架构

[^src-1]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/result.tex" P1074-1081 -- Table results showing Mem0 F1=38.72 Judge=67.13 for single-hop, F1=28.64 Judge=51.15 for multi-hop
[^src-2]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/result.tex" P1207 -- "Zep achieves the highest F1 (49.56) and Judge (76.60) scores, edging out our methods by a narrow margin"
[^src-3]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/abs.tex" P689 -- "Mem0 achieves 26% relative improvements in the LLM-as-a-Judge metric over OpenAI"
