---
id: instruction-tuning-citation-effect
title: 指令微调对 LLM 引用能力的显著提升效应
status: accepted
card_type: source_claim
tags: [instruction-tuning, citation, LLaMA, Vicuna, open-source-model]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
justification: ../justification/instruction-tuning-citation-effect.md
canonical_concept: instruction-tuning-citation-effect
aliases: [指令微调引用效应, instruction tuning for citation, 指令对齐与引用质量]
summary: >-
  instruction-tuning-citation-effect（指令微调引用效应）指令微调显著提升 LLM 引用能力：ASQA 上 LLaMA-13B 的 citation recall 仅 10.6%，Vicuna-13B 达 51.1%（+40.5pp）；原始 LLaMA 能从上下文复制事实但无法准确标注引用源；更详细的引用指令也进一步提升引用质量
related: [citation-support-gap, alce-citation-benchmark]
---

ALCE 的 LLM 对比实验揭示了指令微调（instruction tuning）对引用能力的显著影响 [^src-1]。

**基础模型 vs 指令微调模型**：原始 LLaMA-13B 在 ASQA 上 citation recall 仅 10.6%，而经过指令微调的 Vicuna-13B 达到 51.1%（提升 40.5 个百分点）[^src-2]。在 ELI5 上差距同样显著：LLaMA-13B 仅 3.1%，Vicuna-13B 为 15.6% [^src-3]。

**行为差异分析**：原始 LLaMA 模型能够从上下文中复制事实信息，但在准确标注引用来源方面表现挣扎，或干脆不提供引用 [^src-4]。指令微调使模型学会遵循引用格式要求。

**模型规模与指令微调的交互**：LLaMA-2-70B-Chat 在 ASQA 上达到了与 ChatGPT 可比的正确性（EM 41.5% vs 40.4%），但在引用质量上仍有差距（citation recall 62.9% vs 73.6%）[^src-5]。

**指令详细程度的影响**：在 ChatGPT 上，使用完整版引用指令相比简短版指令，citation recall 从 69.6% 提升至 73.6%，而正确性也从 39.5% 提升至 40.4% [^src-6]。至少包含一个示范（demonstration）也是保证高 citation recall 的重要因素 [^src-7]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/results.tex -- "instruction-tuned models (Vicuna-13B and LLaMA-2-Chat) outperform the original LLaMA models in correctness and considerably enhance the citation quality."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- tables/asqa.tex -- "LLaMA-13B (3-psg): citation Rec. 10.6; Vicuna-13B (3-psg): citation Rec. 51.1"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- tables/eli5.tex -- "LLaMA-13B (3-psg): citation Rec. 3.1; Vicuna-13B (3-psg): citation Rec. 15.6"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/results.tex -- "while the original LLaMA models are able to copy facts from the context, they struggle with accurately citing the sources or simply do not cite."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/results.tex -- "the best open-source model, LLaMA-2-70B-Chat, achieves comparable correctness score as the OpenAI models, but still lags behind in citation quality."
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- tables/inst.tex -- "Short instruction: Rec. 69.6; Full instruction: Rec. 73.6"
[^src-7]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/results.tex -- "using comprehensive instructions enhances the citation quality...including at least one demonstration improves the performance"
