---
id: citation-support-gap
title: LLM 引用支持缺口：最佳模型仍有约 50% 陈述缺乏完整引用
status: accepted
card_type: source_claim
tags: [citation, hallucination, LLM-limitation, ELI5, empirical-finding]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
justification: ../justification/citation-support-gap.md
canonical_concept: citation-support-gap
aliases: [引用支持缺口, citation support deficit, 50%引用缺失]
summary: >-
  citation-support-gap（引用支持缺口, 50%引用缺失）在 ALCE 基准上，即使最佳模型（ChatGPT/GPT-4）在 ELI5 数据集上仍有约 50% 的陈述缺乏被引段落的完整支持，反映当前 LLM 引用生成能力的根本不足
related: [alce-citation-benchmark, retrieval-as-citation-bottleneck]
---

在 ALCE 基准的实验中，当前最先进的 LLM 在引用生成任务上存在显著的引用支持缺口。具体而言，在 ELI5 数据集上，ChatGPT 的 citation recall 仅为 51.1%，即约一半的生成陈述没有被其引用的段落完全支持 [^src-1]。

这一缺口在不同数据集和模型间普遍存在：
- **ELI5**：ChatGPT Vanilla citation recall 51.1%，GPT-4（5-psg）为 44.0%；即使使用 Rerank 策略提升至 69.3%，仍有约 30% 的陈述缺乏完整引用支持 [^src-2]
- **ASQA**：ChatGPT Vanilla citation recall 73.6%，表现较好但仍有超过 1/4 的陈述未被充分支持 [^src-3]
- **QAMPARI**：整体 citation recall 更低，ChatGPT Vanilla 仅 20.5% [^src-4]

开源模型的表现更为薄弱：原始 LLaMA-13B 在 ASQA 上 citation recall 仅 10.6%，在 ELI5 上仅 3.1% [^src-5]。经过指令微调的 Vicuna-13B 有所改善（ASQA 51.1%），但仍远低于 ChatGPT。

这些结果表明，生成带引用的可验证文本仍是 LLM 面临的一项根本性挑战，不仅涉及引用标注能力，还涉及检索质量、上下文利用能力和多源信息综合能力的协同提升 [^src-6]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- abstract -- "on the ELI5 dataset, even the best models lack complete citation support 50% of the time."
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- tables/eli5.tex -- "Vanilla (5-psg): 51.1 citation recall; w/ Rerank: 69.3; GPT-4 (5-psg): 44.0"
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- tables/asqa.tex -- "Vanilla (5-psg): 73.6 citation recall"
[^src-4]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- tables/qampari.tex -- "Vanilla (5-psg): 20.5 citation recall"
[^src-5]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- tables/asqa.tex -- "LLaMA-13B (3-psg): citation Rec. 10.6"
[^src-6]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/conclusion.tex -- "current systems have considerable room for improvement on ALCE"
