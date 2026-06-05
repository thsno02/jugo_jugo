---
id: lossy-compression-citation-tradeoff
title: 有损压缩的引用权衡：摘要/片段提升正确性但损害引用质量
status: accepted
card_type: mechanism
tags: [summarization, snippet, lossy-compression, context-window, citation-tradeoff]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
justification: ../justification/lossy-compression-citation-tradeoff.md
canonical_concept: lossy-compression-citation-tradeoff
aliases: [有损压缩引用权衡, Summ/Snippet tradeoff, 摘要压缩与引用质量的矛盾]
summary: >-
  lossy-compression-citation-tradeoff（有损压缩引用权衡, Summ/Snippet tradeoff）将检索段落压缩为摘要或片段可平均缩短6倍，放入更多段落（5→10），提升正确性（ASQA EM 40.4→43.3），但因压缩丢失信息导致引用质量下降（citation recall 73.6→68.9），交互式全文检查（Interact）未能弥补
related: [retrieval-as-citation-bottleneck, citation-support-gap]
---

ALCE 论文提出并验证了一种利用有损压缩突破上下文窗口限制的策略，同时揭示了其内在权衡 [^src-1]。

**动机**：在 4K 上下文窗口下，最多只能安全放入 5 个检索段落。而在 ASQA 上，top-5 段落仅覆盖 56.8% 的答案 [^src-2]。为放入更多段落，可以先将段落压缩为摘要（Summ，抽象式）或片段（Snippet，抽取式），平均将段落长度缩减 6 倍，从而在相同上下文窗口中放入 10 个段落 [^src-3]。

**正确性提升**：在 ASQA 上，Summ（10-psg）的 EM recall 为 43.3%，高于 Vanilla（5-psg）的 40.4%；Snippet 为 41.4%。在 QAMPARI 上提升更明显（Summ 23.6% vs Vanilla 20.8%）[^src-4]。

**引用质量下降**：但在 ASQA 和 ELI5 上，这种正确性提升伴随着引用质量的代价。ASQA 上 Summ 的 citation recall 从 73.6% 降至 68.9%，citation precision 从 72.5% 降至 61.8% [^src-5]。原因在于摘要/片段是有损压缩，丢失了原始段落中供引用验证的细节。

**Interact 未能弥补**：作者提出 Interact 策略——在摘要/片段基础上允许模型交互式检查原文全文——但未带来改善。作者推测当前 LLM 不擅长交互式使用，且检查全文的收益有限 [^src-6]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/model.tex -- "we propose to provide summaries or snippets of passages instead of the full text"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/model.tex -- "top-5 retrieved passages can only cover 56.8% percent of the answers in ASQA"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/model.tex -- "for ASQA, they reduce passage length by 6x on average"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- tables/asqa.tex -- "Summ (10-psg): EM 43.3; Vanilla (5-psg): EM 40.4"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/results.tex -- "such an improvement comes at a cost of citation quality due to the lossy compression"
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/results.tex -- "Combining Interact with Summ/Snippet does not bring improvement, and we hypothesize that checking the full passages offers limited benefit and current LLMs are not proficient in an interactive usage."
