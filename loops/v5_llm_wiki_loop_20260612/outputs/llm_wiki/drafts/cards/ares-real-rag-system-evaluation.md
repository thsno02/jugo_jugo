---
id: ares-real-rag-system-evaluation
title: ARES 真实 RAG 系统评估表现
status: draft
card_type: experimental-finding
tags: [real-rag, colbertv2, gpt-4, bm25, rag-evaluation, kendall-tau]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ares]
evidence_basis: experimental_paper
justification: ../justification/ares-real-rag-system-evaluation.md
canonical_concept: ares-real-rag-system-evaluation
aliases: [ARES on real RAG systems, ARES real-world evaluation]
summary: >-
  在 NQ/WoW/FEVER 上评估真实 RAG 系统（BM25、Ada embeddings、ColBERTv2 检索器 + MPT-7b、GPT-3.5、GPT-4 生成器 + Facebook RAG），ARES 平均 Kendall's tau 为 0.91 (C.R.) 和 0.97 (A.R.)，比 RAGAS 高 0.16 (C.R.) 和 0.15 (A.R.)。PPI 置信区间平均宽 7.4 点 (C.R.) 和 6.1 点 (A.R.)，ground truth 捕获率超 95%。最佳检索器 ColBERTv2，最佳生成器 GPT-4。
related: []
---

ARES 在真实 RAG 系统（非 mock 系统）上的评估验证了框架的实际应用价值。[^src-1]

RAG 配置空间：三种检索器（BM25、OpenAI Ada cosine、ColBERTv2）+ 三种生成器（MPT-7b-Instruct、GPT-3.5-Turbo、GPT-4）+ Facebook RAG（DPR + BART）。每次检索只取一个段落。[^src-2]

ARES 平均 Kendall's tau：C.R. 0.91、A.R. 0.97。比 RAGAS 分别高 0.16 和 0.15。[^src-3]

PPI 产出准确置信区间：平均宽度 C.R. 7.4 点、A.R. 6.1 点；ground truth 捕获率超 95%。[^src-4]

实验发现最佳检索器为 ColBERTv2，最佳生成器为 GPT-4。[^src-5]

[^card-1]: [^ref→ares-ranking-accuracy-vs-baselines] mock 系统对比实验
[^card-2]: [^ref→prediction-powered-inference-for-rag-ranking] PPI 置信区间

[^src-1]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P862-863 -- "we also wanted to evaluate whether ARES can score and rank existing RAG systems"
[^src-2]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P867-871 -- "three different retrievers (BM25, OpenAI Ada embeddings...ColBERTv2) and three different generative LLMs (MPT-7b-Instruct, GPT-3.5-Turbo, and GPT-4)"
[^src-3]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P873-874 -- "averaging a Kendall's tau of 0.91 for context relevance and 0.97 for answer relevance"
[^src-4]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P875 -- "the PPI confidence intervals were 7.4 points wide for context relevance and 6.1 points wide for answer relevance"
[^src-5]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P876-877 -- "the best performing retriever was ColBERTv2 while the best performing generative LLM was GPT-4"
