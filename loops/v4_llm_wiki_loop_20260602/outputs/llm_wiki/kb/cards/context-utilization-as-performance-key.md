---
id: context-utilization-as-performance-key
title: 上下文利用率是 RAG 性能的关键生成器指标
status: accepted
card_type: source_claim
tags: [rag, context-utilization, generator, performance, evaluation]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragchecker]
justification: ../justification/context-utilization-as-performance-key.md
canonical_concept: context-utilization-as-performance-key
aliases: [上下文利用率关键指标, context utilization as key metric, CU与F1强相关]
summary: >-
  context-utilization-as-performance-key（上下文利用率关键指标 / context utilization as key metric / CU与F1强相关）RAGChecker 实验发现在所有生成器指标中，上下文利用率（context utilization）与整体 F1 的相关性最强，且在不同检索器间相对稳定，意味着改善检索器可直接通过稳定的 CU 转化为整体 recall 提升
related: [ragchecker-three-tier-metrics, retrieval-improvement-faithfulness-noise-tradeoff]
---

RAGChecker 对 8 个 RAG 系统在 10 个领域的评估中发现：在全部 6 个生成器指标中，context utilization（上下文利用率）与整体 F1 分数的相关性最强，而其他生成器指标（faithfulness、noise sensitivity、hallucination 等）与 F1 的相关性相对较弱[^src-1]。

Context utilization 定义为：在被检索块覆盖的标准答案声明中，同时也出现在模型回答中的比例。直觉上，这衡量的是生成器"把检索到的有用信息用起来"的能力[^src-2]。

关键发现是 context utilization 在两个不同检索器（BM25 和 E5-Mistral）之间表现相对稳定。例如 GPT-4 的 CU 分别为 61.4（BM25）和 60.4（E5-Mistral），Llama3-70B 分别为 56.2 和 57.6[^src-3]。这意味着当检索器改善（claim recall 从 74.0 提升至 83.5）时，稳定的 CU 可以直接将更多的检索覆盖转化为整体 recall 的提升。

论文据此指出：生成器在 RAG 系统中的核心能力是充分利用检索到的上下文以超越其自身知识（self-knowledge），而非仅仅是忠实地复述上下文[^src-1]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/experiments.tex, Main Results" -- "Among all generator metrics, we observe that context utilization strongly correlates to the overall F1 score, while such correlation is relatively weaker for other generator metrics... the capability to fully utilize retrieved context is key"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex, Generator Metrics" -- "context utilization is computed as the ratio between |{c_i^(gt) | c_i^(gt) in chunks and c_i^(gt) in m}| and |{c_i^(gt) | c_i^(gt) in chunks}|"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "tables/ragchecker_results_avg.tex" -- "BM25_GPT-4 CU=61.4, E5-Mistral_GPT-4 CU=60.4; BM25_Llama3-70b CU=56.2, E5-Mistral_Llama3-70b CU=57.6"
