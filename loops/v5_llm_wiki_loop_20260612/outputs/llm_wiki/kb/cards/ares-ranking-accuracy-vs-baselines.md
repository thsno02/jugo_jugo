---
id: ares-ranking-accuracy-vs-baselines
title: ARES 排名准确度优于 RAGAS 和 GPT-3.5
status: accepted
card_type: experimental-finding
tags:
- kendall-tau
- ragas
- gpt-3.5
- ranking-accuracy
- rag-evaluation
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-ares
evidence_basis: experimental_paper
justification: ../justification/ares-ranking-accuracy-vs-baselines.md
canonical_concept: ares-ranking-accuracy-vs-baselines
aliases:
- ARES vs RAGAS
- ARES ranking performance
- Kendall's tau comparison
summary: 在 KILT + SuperGLUE 六个数据集的 mock RAG 系统排名实验中，ARES Kendall's tau 比 RAGAS 平均高
  0.065 (context relevance) 和 0.132 (answer relevance)；比 few-shot GPT-3.5 judge 平均高
  0.06。预测准确率方面 ARES 比 RAGAS 高 59.9 (C.R.) 和 14.4 (A.R.) 个百分点。ARES 比 1350 个 sampled
  annotations 的 tau 高 0.08，同时少用 78% 标注。
related:
- ares-mock-rag-system-construction
- ares-vs-ragas-design-differences
- prediction-powered-inference-for-rag-ranking
---

在 NQ、HotpotQA、WoW、FEVER、MultiRC、ReCoRD 六个数据集上，ARES 使用 DeBERTa-v3-Large judge + 300 个人工标注的 PPI，与 RAGAS v0.0.18 和 few-shot GPT-3.5 judge 对比。[^src-1]

ARES Kendall's tau 比 RAGAS 平均高 0.065 (C.R.) 和 0.132 (A.R.)。[^src-2]

在预测准确率上，ARES C.R. 比 RAGAS 高 59.9 个百分点，A.R. 高 14.4 个百分点。[^src-3]

与 sampled annotations（每个 mock 系统 150 个标注，共 1350 个）相比，ARES tau 平均高 0.08，同时仅用 300 个标注（少 78%）。[^src-4]

PPI 在所有数据集上均提升了 LLM judge 的排名准确度。[^src-5]

[^card-1]: [^ref→ares-automated-rag-evaluation-system] 整体框架
[^card-2]: [^ref→prediction-powered-inference-for-rag-ranking] PPI 贡献

[^src-1]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P809-811 -- "We compare against RAGAS (version 0.0.18) and a baseline few-shot prompted GPT-3.5 judge"
[^src-2]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P814 -- "ARES averages a Kendall's tau 0.065 higher for context relevance and 0.132 higher for answer relevance than RAGAS"
[^src-3]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P816-817 -- "59.9 percentage points higher than RAGAS...14.4 percentage points higher than RAGAS"
[^src-4]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P821-822 -- "Kendall's tau for ARES is 0.08 higher on average...despite using 78% less annotations"
[^src-5]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P819 -- "for all datasets tested, PPI improved the ranking prediction accuracy"
