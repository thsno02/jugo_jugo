---
id: instruction-tuning-citation-ability
title: 指令微调对 LLM 引用能力的显著提升
status: accepted
card_type: experimental-finding
tags:
- instruction-tuning
- LLaMA
- Vicuna
- citation-quality
- open-source-models
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-alce
evidence_basis: experimental_paper
justification: ../justification/instruction-tuning-citation-ability.md
canonical_concept: instruction-tuning-citation-ability
aliases:
- instruction tuning citation
- LLaMA citation gap
- 指令微调引用能力
summary: ALCE 实验 (instruction-tuning-citation-ability) 显示指令微调对 LLM 引用能力有显著影响。LLaMA-13B 原始模型 citation recall 仅 10.6%（ASQA），而 Vicuna-13B 达到 51.1%，LLaMA-2-70B-Chat 达到 62.9%。原始 LLaMA 能从上下文复制事实但难以准确标注引用来源或完全不引用。最大的指令微调模型（LLaMA-2-70B-Chat）正确性可比肩
  OpenAI 模型（41.5% vs ChatGPT 40.4%），但引用质量仍有差距。
related:
- alce-benchmark-overview
- retrieval-quality-bottleneck
---

指令微调显著提升 LLM 的引用标注能力。[^src-1]

在 ASQA 上，LLaMA-13B 原始模型的 citation recall 仅为 10.6%，而同等规模的指令微调版本 Vicuna-13B 达到 51.1%（近 5 倍提升）。LLaMA-2-70B-Chat 进一步达到 62.9%。[^src-2]

通过人工检查发现：原始 LLaMA 模型能够从上下文中复制事实信息，但在准确标注引用来源方面存在困难，甚至完全不生成引用标记。[^src-3]

正确性方面差距更小：LLaMA-2-70B-Chat 在 ASQA 上达到 41.5%（可比 ChatGPT 的 40.4%），但 citation recall（62.9%）仍落后于 ChatGPT（73.6%）。[^src-4]

更详尽的指令文本也有帮助：Full instruction 比 Short instruction 在 citation recall 上高出约 4 个百分点（73.6% vs 69.6%），暗示指令的详细程度对引用行为有直接影响。[^src-5]

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Comparison of Different LLMs" -- "instruction-tuned models (Vicuna-13B and LLaMA-2-Chat) outperform the original LLaMA models in correctness and considerably enhance the citation quality"
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "tables/asqa.tex" -- "LLaMA-13B (3-psg): Rec. 10.6...Vicuna-13B (3-psg): Rec. 51.1...Chat-70B (5-psg): Rec. 62.9"
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Comparison of Different LLMs" -- "the original LLaMA models are able to copy facts from the context, they struggle with accurately citing the sources or simply do not cite"
[^src-4]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "tables/asqa.tex" -- "Chat-70B (5-psg): EM 41.5, Rec. 62.9"; "ChatGPT Vanilla (5-psg): EM 40.4, Rec. 73.6"
[^src-5]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "tables/inst.tex" -- "Short instruction: Rec. 69.6; Full instruction: Rec. 73.6"

[^card-1]: alce-benchmark-overview
[^card-2]: retrieval-quality-bottleneck
