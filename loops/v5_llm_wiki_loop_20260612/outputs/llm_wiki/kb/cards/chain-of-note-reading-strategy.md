---
id: chain-of-note-reading-strategy
title: Chain-of-Note + JSON 格式读取策略
status: accepted
card_type: empirical-finding
tags:
- long-term-memory
- RAG
- Chain-of-Note
- reading-strategy
- structured-format
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-longmemeval
evidence_basis: experimental_paper
justification: ../justification/chain-of-note-reading-strategy.md
canonical_concept: chain-of-note-json-reading
aliases:
- Chain-of-Note
- CoN reading strategy
- CoN + JSON
- extract-before-read
summary: chain-of-note-json-reading 在 LongMemEval oracle 检索设定下，Chain-of-Note（CoN）加 JSON 结构化格式的读取策略相比直接自然语言读取最高提升 10 个绝对百分点（GPT-4o）。CoN 指示 LLM 先从每个记忆项中提取信息再基于笔记推理，有效将长上下文阅读分解为"复制重要细节"和"基于简洁笔记推理"两个更简单的子任务。不使用
  CoN 时 JSON 格式不一致地优于自然语言格式，但使用 CoN 后 JSON 格式一致地有益于各种能力水平的 reader LLM。
related:
- unified-memory-framework-three-stages
- value-decomposition-round-granularity
- longmemeval-error-distribution-analysis
---
在 LongMemEval 的 oracle 检索设定下（仅提供证据会话），论文评估了读取策略对 QA 性能的影响：[^src-1]

**Chain-of-Note（CoN）**：指示 LLM 先遍历文档并提取每个记忆项中的信息，然后基于这些笔记推理得出答案。这有效将长上下文阅读分解为两个更简单的子任务：
1. 复制重要细节
2. 基于更简洁的笔记进行推理

**JSON 结构化格式**：将检索项以 JSON 格式呈现，帮助模型清晰识别记忆项为待读取的数据。

关键发现：
- 即使 oracle 检索完美，次优读取策略仍导致 GPT-4o 最多 10 个绝对百分点的性能下降
- 不使用 CoN 时，JSON 格式不一致地优于自然语言格式
- 使用 CoN 后，JSON 格式一致地有益于各种能力水平的 reader LLM[^src-2]

CoN 提示模板："Answer the question step by step: first extract all the relevant information, and then reason over the information to get the answer."[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/5_experiment.tex" Section "Improving reading with chain-of-note and structured format" -- "even with perfect retrieval, a suboptimal reading strategy results in up to a 10-point absolute performance drop"
[^src-2]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/5_experiment.tex" -- "with CoN, JSON format consistently benefits reader LLMs of various capabilities"
[^src-3]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/appendix.tex" Figure "reading-prompt" -- "Answer the question step by step: first extract all the relevant information, and then reason over the information to get the answer"
