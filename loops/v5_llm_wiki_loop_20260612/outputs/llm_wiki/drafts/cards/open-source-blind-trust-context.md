---
id: open-source-blind-trust-context
title: 开源模型倾向盲目信任上下文
status: draft
card_type: experimental-finding
tags: [open-source-models, gpt-4, llama3, context-utilization, noise-sensitivity, faithfulness]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragchecker]
evidence_basis: experimental_paper
justification: ../justification/open-source-blind-trust-context.md
canonical_concept: open-source-blind-trust-context
aliases: [Open-Source Models Blind Trust, 开源模型盲信上下文]
summary: >-
  RAGChecker 实验发现开源模型（Llama3/Mixtral）在 RAG 场景中倾向盲目信任上下文。GPT-4 同时拥有更高 context utilization（60.4 vs Llama3-70B 57.6）和更低 noise sensitivity（NS(I) 28.9 vs 31.7），而开源模型虽 faithfulness 更高（Llama3-70B 95.9 vs GPT-4 92.9）但更多来自对噪声的不加区分信任。这表明开源模型在区分上下文中准确信息与噪声的推理能力方面仍有提升空间。
related: [ragchecker-generator-metrics, retrieval-noise-sensitivity-tradeoff, context-utilization-key-factor]
---

RAGChecker 实验揭示了开源模型与闭源模型在处理检索上下文时的行为差异。[^src-1]

**GPT-4 vs 开源模型对比**（E5-Mistral retriever，10 域平均）：[^src-2]
| 指标 | GPT-4 | Llama3-70B | Llama3-8B | Mixtral-8x7B |
|------|-------|-----------|-----------|--------------|
| Context Utilization | 60.4 | 57.6 | 55.0 | 55.2 |
| Noise Sensitivity (Relevant) | 28.9 | 31.7 | 33.5 | 36.5 |
| Faithfulness | 92.9 | 95.9 | 92.7 | 95.2 |
| Hallucination | 5.7 | 3.3 | 6.6 | 4.0 |

开源模型的高 faithfulness 主要源于对上下文的不加区分信任——它们较少产出 hallucination，但同时也更多地复制上下文中的噪声信息。GPT-4 则表现出更强的信息鉴别能力：能更好地区分上下文中的有用信息与噪声。[^src-1]

该发现提示开源模型需要提升在噪声上下文中的推理和鉴别能力（reasoning ability），而非简单地提升对上下文的 faithfulness。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/experiments.tex Main Results" -- "Open-Source Models are Worse at Distinguishing Accurate Information from Noise. GPT-4 has both higher context utilization and lower noise sensitivity...Open source models are faithful but tend to trust the context blindly"
[^src-2]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "tables/ragchecker_results_avg.tex" -- E5-Mistral row values

[^card-9]: 参见 [retrieval-noise-sensitivity-tradeoff] 了解 noise sensitivity trade-off 的机制
