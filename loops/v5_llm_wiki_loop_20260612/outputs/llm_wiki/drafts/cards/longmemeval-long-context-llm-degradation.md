---
id: longmemeval-long-context-llm-degradation
title: 长上下文 LLM 在 LongMemEval 上的性能退化
status: draft
card_type: empirical-finding
tags: [long-context, LLM, performance-degradation, needle-in-haystack]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
evidence_basis: experimental_paper
justification: ../justification/longmemeval-long-context-llm-degradation.md
canonical_concept: long-context-llm-memory-degradation
aliases: [long-context LLM degradation, 长上下文 LLM 性能退化]
summary: >-
  long-context-llm-memory-degradation 在 LongMemEval_S（约 115k tokens）上，GPT-4o 从 oracle 设定的 0.870 降至 0.606（降 30%），Llama 3.1 70B 从 0.744 降至 0.334（降 55%），即使应用 Chain-of-Note 也无法消除退化。据此论文认为即使最先进的长上下文 LLM 也难以在没有有效记忆机制的情况下管理不断增长的交互历史。
related: [longmemeval-benchmark-overview, longmemeval-commercial-system-memory-gap]
---

在 LongMemEval_S（约 115k tokens / 约 50 个会话）上评估四种长上下文 LLM，与 oracle 检索设定（仅提供证据会话作为上下文）相比，所有模型都出现 30%-60% 的性能下降：[^src-1]

不使用 Chain-of-Note 时：
- GPT-4o：oracle 0.870 -> 全历史 0.606（降 30.3%）
- Llama 3.1 70B Instruct：0.744 -> 0.334（降 55.1%）
- Llama 3.1 8B Instruct：0.710 -> 0.454（降 36.1%）
- Phi-3 128k 14B：0.702 -> 0.380（降 45.9%）

应用 Chain-of-Note 后退化幅度相近，GPT-4o 仍降 30.7%，Llama 3.1 70B 降 66.3%。[^src-2]

据此，论文认为即使最先进的长上下文 LLM 也难以在没有有效记忆机制的情况下管理不断增长的交互历史。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "figures/proof_of_difficulty.tex" -- "Long-context LLMs exhibit large QA performance drops on LongMemEval_S"
[^src-2]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "figures/proof_of_difficulty.tex" -- "GPT-4o ... 0.924 ... 0.640 ... 30.7%"
[^src-3]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/3_benchmark.tex" -- "even the most capable current long-context LLMs struggle to manage an ever-growing interaction history without an effective memory mechanism"
