---
id: llm-multi-document-synthesis-limitation
title: LLM 多文档综合能力不足
status: accepted
card_type: experimental-finding
tags:
- multi-document-synthesis
- long-context
- irrelevant-distraction
- context-window
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-alce
evidence_basis: experimental_paper
justification: ../justification/llm-multi-document-synthesis-limitation.md
canonical_concept: llm-multi-document-synthesis-limitation
aliases:
- multi-document synthesis challenge
- LLM distraction by irrelevant context
- 多文档综合能力局限
summary: ALCE 实验 (llm-multi-document-synthesis-limitation) 揭示当前 LLM 在综合多文档时的系统性不足。具体表现：(1) 增加上下文段落数对 ChatGPT 无帮助（correctness 在 top-1 后 plateau）；(2) ChatGPT-16K 放入 20 篇段落反而性能下降（ASQA EM 36.1% vs 5-psg 时 40.4%）；(3)
  LLM 易被无关段落干扰，ClosedBook 正确性反超 Vanilla；(4) GPT-4 比 ChatGPT 更擅长长上下文综合（20-psg 时 44.4% vs 36.1%），但提升仍非线性比例于检索覆盖率。
related:
- retrieval-quality-bottleneck
- closedbook-posthoc-citation-gap
---

当前 LLM 在综合多上下文文档方面存在系统性能力不足。[^src-1]

增加段落数对 ChatGPT 帮助极为有限：ASQA 上从 3-psg 到 5-psg 正确性仅从 39.6% 微增至 40.4%，而 ChatGPT-16K 放入 20 篇段落后反而降至 36.1%。[^src-2]

LLM 易被上下文中的无关段落干扰，导致 ClosedBook（不使用任何检索）的正确性在 ELI5 上反超 Vanilla（18.6% vs 12.0%）。这一现象与 Shi et al.(2023) "large language models can be easily distracted by irrelevant context" 的发现一致。[^src-3]

GPT-4 展现出明显更强的长上下文综合能力：从 5-psg 到 20-psg，ASQA 正确性从 41.3% 提升至 44.4%，citation recall 从 68.5% 提升至 73.0%。相比之下 ChatGPT-16K 同样区间几乎无提升甚至下降。[^src-4]

这些发现表明：(1) 长上下文窗口本身不足以解决问题，模型需要能力去综合利用多源信息；(2) 更好的指令微调能带来显著改善。[^src-5]

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Conclusion" -- "advancing LLMs' ability to synthesize multiple sources"
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "tables/asqa_different_llms.tex" -- "ChatGPT (3-psg) 39.6...ChatGPT (5-psg) 40.4"; "ChatGPT-16K (20-psg) 36.1"
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Experiments" -- "open-book models are easily distracted by irrelevant passages and generate responses with lower correctness, a phenomenon also observed by Shi et al."
[^src-4]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Experiments" -- "GPT-4 brings limited improvement but is better at using long context...including more passages with ChatGPT-16K does not improve the results"
[^src-5]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Experiments" -- "processing more passages is non-trivial and GPT-4 is better at synthesizing information from its long context than ChatGPT"

[^card-1]: retrieval-quality-bottleneck
[^card-2]: closedbook-posthoc-citation-gap
