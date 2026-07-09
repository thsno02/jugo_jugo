---
id: mem0-graph-temporal-advantage
title: 图记忆在时间推理中的优势
status: draft
card_type: empirical-finding
tags: [temporal-reasoning, graph-memory, event-sequencing, timestamp]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0]
evidence_basis: experimental_paper
justification: ../justification/mem0-graph-temporal-advantage.md
canonical_concept: graph-memory-temporal-advantage
aliases: [graph memory temporal reasoning, 图记忆时间推理, temporal question advantage]
summary: >-
  Mem0^g 在 temporal 推理任务上显著优于其他方法（F1=51.55 Judge=58.13），验证结构化关系图在捕获时间序列、事件排序和持续时间方面的优势。显式关系上下文增强时间连贯性。OpenAI memory 在 temporal 上严重欠表现（Judge<15%），主因生成的 memories 多数缺失 timestamps。Mem0 base 也达到 Judge=55.51，表明自然语言记忆本身可辅助时间判断。
related: []
---

时间推理任务依赖于对事件序列、相对排序和持续时间的准确建模。在 LOCOMO temporal 类别中：[^src-1]

- **Mem0^g**：F1=51.55, Judge=58.13——所有方法中最高
- **Mem0 base**：F1=48.93, BLEU-1=40.51, Judge=55.51
- **OpenAI memory**：Judge 低于 15%，严重欠表现

Mem0^g 的优势源于其结构化关系表示为时间锚定提供显式上下文，使得事件排序和因果推理更加可靠。关系图中的时间戳元数据和三元组结构天然支持"何时"类型的查询。[^src-2]

OpenAI memory 的失败提供了反面证据：尽管实验中明确提示 ChatGPT 提取带时间戳的记忆，生成的大多数 memories 仍缺失时间戳信息，导致时间相关查询几乎无法回答。这表明记忆系统中时间信息的保留对此类任务至关重要。[^src-3]

值得注意的是，Mem0 base（纯自然语言记忆，无图结构）也达到 Judge=55.51，据材料推测自然语言记忆中保留的时间表述（如日期、相对时间引用）本身可部分支持时间推理。[^src-4]

[^card-1]: [[mem0-graph-memory-architecture]] 描述了图记忆的时间戳元数据设计
[^card-2]: [[mem0-performance-results]] 提供了跨类别性能比较

[^src-1]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/result.tex" P1210 -- "Temporal reasoning tasks hinge on accurate modeling of event sequences, their relative ordering, and durations"
[^src-2]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/result.tex" P1267 -- "In temporal reasoning, Mem0^g substantially outperforms other methods, validating that structured relational graphs excel in capturing chronological relationships and event sequences"
[^src-3]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/result.tex" P1212 -- "OpenAI notably underperforms, with scores below 15%, primarily due to missing timestamps in most generated memories despite explicit prompting"
[^src-4]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/result.tex" P1211 -- "the base variant, Mem0, also provide a decent Judge score (55.51), suggesting that natural language alone can aid in temporally grounded judgments"
