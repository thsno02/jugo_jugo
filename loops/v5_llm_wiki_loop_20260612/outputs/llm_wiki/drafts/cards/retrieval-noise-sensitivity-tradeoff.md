---
id: retrieval-noise-sensitivity-tradeoff
title: 检索召回与生成器噪声敏感度的权衡
status: draft
card_type: experimental-finding
tags: [noise-sensitivity, claim-recall, tradeoff, faithfulness, relevant-chunk]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragchecker]
evidence_basis: experimental_paper
justification: ../justification/retrieval-noise-sensitivity-tradeoff.md
canonical_concept: retrieval-noise-sensitivity-tradeoff
aliases: [Retriever Recall Trades-off with Generator Noise Sensitivity, 检索-噪声权衡]
summary: >-
  RAGChecker 实验揭示检索器 claim recall 与生成器 noise sensitivity 之间存在 trade-off。当 retriever 从 BM25 升级为 E5-Mistral（claim recall 74.0→83.5），所有 generator 的 relevant noise sensitivity 均上升（如 GPT-4 26.2→28.9，Llama3-70B 30.4→31.7）。原因是固定大小分块策略下，relevant chunks 不可避免地携带噪声信息，而 generator 对 relevant chunks 表现出 chunk-level 的信任（relevant NS 显著高于 irrelevant NS）。
related: [ragchecker-generator-metrics, retriever-quality-consistent-impact, open-source-blind-trust-context]
---

RAGChecker 实验发现 retriever claim recall 的提升伴随着 generator noise sensitivity 的增加，形成固有的 trade-off。[^src-1]

**定量证据**（BM25 → E5-Mistral，10 域平均）：[^src-2]
- GPT-4: Relevant NS 26.2 → 28.9, Irrelevant NS 4.1 → 3.5
- Llama3-70B: Relevant NS 30.4 → 31.7, Irrelevant NS 5.3 → 4.3
- Llama3-8B: Relevant NS 31.3 → 33.5, Irrelevant NS 6.1 → 5.5

**机制解释**：由于固定大小分块策略，retrieved relevant chunks 不可避免地同时携带有用信息和噪声。当 claim recall 提升时，更多 relevant chunks 进入上下文，噪声随之增加。Generator 对 relevant chunk 的 faithfulness 不具备足够的鉴别力，将 chunk 整体作为可信来源。[^src-1]

**Relevant vs Irrelevant NS 差距**：对所有 baseline RAG 系统，relevant noise sensitivity 显著高于 irrelevant noise sensitivity（如 GPT-4: 28.9 vs 3.5）。这表明 generator 呈现 chunk-level 的信任模式——relevant chunk 被整体信任，而 irrelevant chunk 仅有最小影响。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/experiments.tex Main Results" -- "Retriever Recall Trades-off with Generator Noise Sensitivity...retrieved relevant chunks may inevitably also carry over noise...generators' capability to precisely leverage relevant context is still a challenge"
[^src-2]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "tables/ragchecker_results_avg.tex" -- metric values for NS(I) and NS(II)
[^src-3]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/experiments.tex Main Results" -- "Relevant Noise Sensitivity is More Challenging...a relevant chunk is trusted as a whole, while an irrelevant one only has minimal impact"

[^card-8]: 参见 [ragchecker-generator-metrics] 了解 relevant/irrelevant noise sensitivity 的定义
