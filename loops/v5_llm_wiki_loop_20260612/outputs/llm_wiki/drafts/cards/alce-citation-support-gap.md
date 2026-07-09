---
id: alce-citation-support-gap
title: 当前最强模型仍有约 50% 生成缺乏完整引用支持
status: draft
card_type: empirical-result
tags: [citation-gap, ChatGPT, GPT-4, ELI5, unsupported-generation]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
evidence_basis: experimental_paper
justification: ../justification/alce-citation-support-gap.md
canonical_concept: alce-citation-support-gap
aliases: [50% citation gap, LLM citation coverage deficit, 引用覆盖缺口]
summary: >-
  ALCE 基准实验 (alce-citation-support-gap) 的核心发现：在 ELI5 数据集上，即使是最强系统（ChatGPT Rerank: citation recall 69.3%, GPT-4 20-psg: 48.5%）仍有约 30-50% 的生成语句缺乏完整引用支持。Vanilla ChatGPT 的 ELI5 citation recall 仅 51.1%，意味着近一半语句无法被所引段落完全蕴含。ASQA 上情况稍好（ChatGPT Rerank 达 84.8%），但 QAMPARI 的引用质量普遍低于 30%。这量化了 LLM 带引用生成离可信部署的距离。
related: [alce-benchmark-overview, nli-based-citation-quality-metrics]
---

ALCE 的实验量化了 LLM 带引用生成的可信度缺口。[^src-1]

在 ELI5 数据集上（最具挑战性），ChatGPT Vanilla 的 citation recall 仅为 51.1%，意味着近一半生成语句无法被引用段落完全蕴含。即使使用 Rerank 策略（最优），也仅提升至 69.3%。[^src-2]

GPT-4 在 ELI5 上表现更差：5-psg 的 citation recall 仅 44.0%，20-psg 为 48.5%。这似乎是因为 GPT-4 倾向生成更丰富的内容，超出引用段落的支持范围。[^src-3]

ASQA 上情况相对好：ChatGPT Rerank 达到 84.8% citation recall（最优），Vanilla 为 73.6%。但开源模型普遍低于 65%。[^src-4]

QAMPARI 的引用质量最低：所有模型的 citation recall 均低于 28%，反映了列表型问答中逐条匹配引用的难度。[^src-5]

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Abstract" -- "current systems have considerable room for improvement---For example, on the ELI5 dataset, even the best models lack complete citation support 50% of the time"
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "tables/eli5.tex" -- "Vanilla (5-psg): Rec. 51.1; w/ Rerank: Rec. 69.3"
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "tables/eli5.tex" -- "GPT-4 (5-psg): Rec. 44.0; GPT-4 (20-psg): Rec. 48.5"
[^src-4]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "tables/asqa.tex" -- "ChatGPT Vanilla (5-psg): Rec. 73.6; w/ Rerank: Rec. 84.8"
[^src-5]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "tables/qampari.tex" -- all citation recall values below 28%

[^card-1]: alce-benchmark-overview
[^card-2]: nli-based-citation-quality-metrics
