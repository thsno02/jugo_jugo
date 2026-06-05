---
id: extract-then-read-memory-strategy
title: 先提取后阅读的记忆读取策略
status: accepted
card_type: mechanism
tags: [reading-strategy, chain-of-note, structured-format, memory-reading, LongMemEval]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
justification: ../justification/extract-then-read-memory-strategy.md
canonical_concept: extract-then-read-memory-strategy
aliases: [先提取后阅读, extract-then-read, Chain-of-Note阅读, CoN+JSON记忆阅读]
summary: >-
  extract-then-read-memory-strategy（先提取后阅读 / extract-then-read / CoN+JSON记忆阅读）在记忆系统的阅读阶段，应用 Chain-of-Note（先从每个记忆项提取相关信息再推理）结合 JSON 结构化格式呈现检索结果，将长上下文阅读分解为"复制关键细节"和"基于精简笔记推理"两步，即使在完美检索条件下也能带来高达 10 个绝对点的准确率提升
related: [fact-augmented-key-expansion, memory-extraction-update-pipeline, memory-value-granularity-tradeoff]
---

在记忆增强聊天助手的三阶段流程中，阅读（reading）阶段——即 LLM 基于检索结果生成回答——是一个容易被忽视但影响巨大的环节。LongMemEval 的实验表明，即使检索完全正确，次优的阅读策略也会导致高达 10 个绝对点的性能下降 [^src-1]。

**两项关键优化**：

1. **Chain-of-Note（CoN）**：指示 LLM 先遍历每个记忆项并提取相关信息，然后基于这些笔记进行推理。这实质上将长上下文阅读分解为两个更简单的子任务：复制关键细节和基于精简笔记推理 [^src-2]。

2. **JSON 结构化格式**：将检索到的记忆项以结构化 JSON 格式呈现，帮助模型清楚识别记忆项作为待读取的数据 [^src-3]。

**两者的组合效果**：单独使用 JSON 格式并不一致优于自然语言格式。然而，当 CoN 与 JSON 格式结合使用时，在不同能力水平的阅读器 LLM 上均持续带来改善 [^src-4]。在 oracle 检索设置下（仅提供证据会话），CoN+JSON 组合在 GPT-4o 上相比最差组合提升高达 10 个绝对点。本卡聚焦的是记忆系统的读取侧优化，与之互补的写入侧——如何从对话中提取并持久化记忆——由 Mem0 的提取-更新管线给出了一种增量式架构方案[^card-1]。

## Footnotes

[^card-1]: [记忆提取-更新双阶段管线](memory-extraction-update-pipeline.md) -- 本卡聚焦记忆的读取侧阅读策略（CoN+JSON 优化），该卡描述记忆的写入侧提取-更新管线（从对话中增量抽取并持久化事实），两者构成记忆系统完整生命周期的互补视角

[^src-1]: `data/raw/arxiv/arxiv-longmemeval/source/text/5_experiment.tex` -- Section 5.5 -- "even with perfect retrieval, a suboptimal reading strategy results in up to a 10-point absolute performance drop compared to the best approach for GPT-4o"
[^src-2]: `data/raw/arxiv/arxiv-longmemeval/source/text/5_experiment.tex` -- Section 5.5 -- "instructing the LLM to first extract information from each memory item and then reason based on these notes. This effectively decomposes long-context reading into two simpler subtasks: copying important details and reasoning with more concise notes"
[^src-3]: `data/raw/arxiv/arxiv-longmemeval/source/text/5_experiment.tex` -- Section 5.5 -- "we present retrieved items in a structured JSON format, which helps the model clearly recognize memory items as the data for reading"
[^src-4]: `data/raw/arxiv/arxiv-longmemeval/source/text/5_experiment.tex` -- Section 5.5 -- "when CoN is not applied, JSON format does not consistently outperform the natural language format. However, with CoN, JSON format consistently benefits reader LLMs of various capabilities"
