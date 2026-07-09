---
id: poisonedrag-vs-baselines
title: PoisonedRAG 优于五种基线攻击
status: draft
card_type: experimental-finding
tags: [poisonedrag, baseline-comparison, prompt-injection, corpus-poisoning, gcg-attack, disinformation]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-poisonedrag]
evidence_basis: experimental_paper
justification: ../justification/poisonedrag-vs-baselines.md
canonical_concept: poisonedrag-vs-baselines
aliases: [baseline comparison, PoisonedRAG vs prompt injection, 攻击基线对比]
summary: >-
  PoisonedRAG 在三个数据集上显著优于五种基线攻击: Naive Attack (ASR~0.02-0.06)、Corpus Poisoning Attack (ASR~0.01-0.03)、GCG Attack (ASR~0.01-0.02)、Prompt Injection Attack (ASR 0.62-0.93)、Disinformation Attack (ASR 0.57-1.0)。各基线失败原因: Naive/Corpus Poisoning 满足检索但不满足生成; GCG 满足生成但不满足检索; Prompt Injection 使用指令而非误导性知识。PoisonedRAG 的关键优势是同时满足双条件。
related: [poisonedrag-dual-condition-framework, poisonedrag-black-box-attack]
---

论文将 PoisonedRAG 与 5 种基线攻击进行系统对比（NQ 数据集，默认设定）:

| 攻击方法 | ASR | F1-Score | 失败原因 |
|---------|-----|----------|---------|
| Naive Attack | 0.03 | 1.0 | 满足检索但不满足生成 |
| Corpus Poisoning | 0.01 | 0.99 | 同上 |
| GCG Attack | 0.02 | 0.0 | 满足生成但不满足检索 |
| Prompt Injection | 0.62 | 0.73 | 非最优（指令式）|
| Disinformation (I alone) | 0.69 | 0.48 | 检索率不足 |
| **PoisonedRAG (BB)** | **0.97** | **0.96** | - |
| **PoisonedRAG (WB)** | **0.97** | **1.0** | - |

[^src-1]

关键洞察: 现有攻击均未被设计为同时满足检索条件与生成条件。Prompt Injection 虽部分有效（因也包含目标问题），但其本质是注入指令而非误导性知识，因此更易被检测且效果次优。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Evaluation / PoisonedRAG outperforms baselines" -- Table tab:comparision-baseline
[^src-2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Evaluation" -- "the key difference between PoisonedRAG and prompt injection attack is that PoisonedRAG relies on malicious knowledge instead of instructions"
[^card-1]: [poisonedrag-dual-condition-framework]
