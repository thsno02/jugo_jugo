---
id: relevant-vs-irrelevant-noise-sensitivity
title: 相关噪声与无关噪声敏感度的区分
status: accepted
card_type: distinction
tags: [rag, noise-sensitivity, generator, chunk-level-trust, evaluation]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragchecker]
justification: ../justification/relevant-vs-irrelevant-noise-sensitivity.md
canonical_concept: relevant-vs-irrelevant-noise-sensitivity
aliases: [相关噪声与无关噪声, relevant vs irrelevant noise sensitivity, 噪声敏感度区分, 块级信任模式]
summary: >-
  relevant-vs-irrelevant-noise-sensitivity（相关噪声与无关噪声 / relevant vs irrelevant noise sensitivity / 块级信任模式）RAGChecker 将生成器的噪声敏感度拆分为相关块噪声（NS-I）和无关块噪声（NS-II），实验显示 NS-I 始终远高于 NS-II，揭示生成器以块为单位信任上下文——相关块被整体信任其噪声也被采纳，而无关块仅有最小影响
related: [retrieval-snr-tradeoff, ragchecker-three-tier-metrics, chunk-size-tradeoff]
---

RAGChecker 将生成器产生的错误声明按来源分为三类，其中噪声敏感度（noise sensitivity）被进一步区分为两种[^src-1]：

- **相关噪声敏感度（NS-I）**：错误声明来自包含标准答案声明的相关块（relevant chunk）。这意味着生成器在利用一个块中的有用信息时，也同时采纳了该块中的噪声。
- **无关噪声敏感度（NS-II）**：错误声明来自不包含任何标准答案声明的无关块（irrelevant chunk）。

实验数据一致显示 NS-I 远大于 NS-II。以 10 个领域的平均数据为例：E5-Mistral_GPT-4 的 NS-I=28.9 vs NS-II=3.5；E5-Mistral_Llama3-70B 的 NS-I=31.7 vs NS-II=4.3[^src-2]。

这一差距揭示了生成器的**块级信任模式**（chunk-level faithfulness）：生成器以块为单位决定信任程度，而非以声明为单位。一个包含有用信息的相关块被作为整体信任，其中的噪声也因此被采纳；而一个完全无关的块则仅产生最小影响[^src-3]。这一发现支持了 RAG 系统中知识库质量和分块精细度的重要性——相关块中混入的噪声比无关块更危险。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex, Generator Metrics" -- "The first type includes incorrect claim that are entailed in a relevant chunk... relevant noise sensitivity. The second type includes incorrect claim that are entailed in an irrelevant chunk... irrelevant noise sensitivity"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "tables/ragchecker_results_avg.tex" -- "E5-Mistral_GPT-4: NS(I)=28.9, NS(II)=3.5; E5-Mistral_Llama3-70b: NS(I)=31.7, NS(II)=4.3"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/experiments.tex, Main Results" -- "it further enhance the point that generators demonstrate a chunk-level faithfulness. It means a relevant chunk is trusted as a whole, while an irrelevant one only has minimal impact"
