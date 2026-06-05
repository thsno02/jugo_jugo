---
id: open-source-vs-proprietary-context-discrimination
title: 开源模型与闭源模型在上下文辨别力上的差距
status: accepted
card_type: source_claim
tags: [rag, open-source, gpt-4, llama, context-utilization, noise-sensitivity]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragchecker]
justification: ../justification/open-source-vs-proprietary-context-discrimination.md
canonical_concept: open-source-vs-proprietary-context-discrimination
aliases: [开源闭源上下文辨别差距, open vs proprietary context discrimination, 盲信上下文, blind context trust]
summary: >-
  open-source-vs-proprietary-context-discrimination（开源闭源上下文辨别差距 / blind context trust）RAGChecker 实验发现开源模型（Llama3/Mixtral）具有更高的 faithfulness 但这主要源于更高的 noise sensitivity——盲目信任上下文；GPT-4 的 context utilization 更高而 noise sensitivity 更低，能更好地区分上下文中的有效信息与噪声
related: [relevant-vs-irrelevant-noise-sensitivity, context-utilization-as-performance-key, rag-generator-self-knowledge]
---

RAGChecker 对 8 个 RAG 系统的评估揭示了开源模型和闭源模型在处理检索上下文时的本质差异[^src-1]。

Llama3-70B 展现了最高的 faithfulness（BM25 配对时 93.2，E5-Mistral 配对时 95.9），而 GPT-4 的 faithfulness 明显较低（分别为 87.9 和 92.9）。然而更高的 faithfulness 并不等同于更好的性能——Llama3-70B 的高忠实度主要由更高的 noise sensitivity 驱动[^src-2]。

具体而言，GPT-4 相比开源模型同时具有：
- **更高的 context utilization**（GPT-4: 61.4/60.4 vs Llama3-70B: 56.2/57.6）
- **更低的 noise sensitivity**（GPT-4 NS-I: 26.2/28.9 vs Llama3-70B NS-I: 30.4/31.7）

这意味着 GPT-4 能够在检索上下文中更精准地识别有效信息并忽略噪声，而开源模型倾向于"盲目信任"上下文——当检索质量提升时，它们更加忠实但也更易受噪声影响[^src-3]。

论文指出这一差距凸显了提升开源模型推理能力的需求——使其能够在噪声上下文中辨别和优先利用有价值的信息[^src-1]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/experiments.tex, Main Results" -- "Open-Source Models are Worse at Distinguishing Accurate Information from Noise. GPT-4 has both higher context utilization and lower noise sensitivity than the other three open source models. Open source models are faithful but tend to trust the context blindly"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/experiments.tex, Main Results" -- "Llama3-70b demonstrates the highest faithfulness scores... However, the superior faithfulness scores of Llama3-70b are primarily due to its higher noise sensitivity"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "tables/ragchecker_results_avg.tex" -- "GPT-4 CU=61.4/60.4, NS-I=26.2/28.9; Llama3-70b CU=56.2/57.6, NS-I=30.4/31.7"
