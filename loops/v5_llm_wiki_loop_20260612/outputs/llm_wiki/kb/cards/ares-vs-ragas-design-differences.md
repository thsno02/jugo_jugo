---
id: ares-vs-ragas-design-differences
title: ARES 与 RAGAS 的设计差异
status: accepted
card_type: comparative-analysis
tags:
- ragas
- ares
- rag-evaluation
- llm-judge
- design-comparison
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-ares
evidence_basis: experimental_paper
justification: ../justification/ares-vs-ragas-design-differences.md
canonical_concept: ares-vs-ragas-design-differences
aliases:
- ARES vs RAGAS
- RAGAS limitations
- automated RAG evaluation comparison
summary: ARES 与 RAGAS 的核心设计差异：(1) RAGAS 依赖固定手写 prompt 评估，缺乏领域适配性；ARES 用领域自适应微调 judge。(2) RAGAS 无统计保证；ARES 通过 PPI 提供 95% 置信区间。(3) RAGAS 用 GPT-3.5 做 judge（依赖外部 API）；ARES 用可本地部署的 DeBERTa。实验证明 ARES 在准确率上比 RAGAS
  高 59.9 (C.R.) 和 14.4 (A.R.) 个百分点。
related:
- ares-ranking-accuracy-vs-baselines
- ragas-framework-overview
- ares-real-rag-system-evaluation
- rag-evaluation-motivation
---
RAGAS 是 ARES 之前最相关的开源 RAG 评估框架（v0.0.18），两者核心设计差异：[^src-1]

**评估策略**: RAGAS 依赖固定手写 prompt，对新评估场景缺乏适配性。ARES 为每个评估维度微调领域自适应 judge。[^src-2]

**统计保证**: RAGAS 无置信区间或错误估计机制。ARES 通过 PPI 提供 95% 置信区间和 rectifier function 校正。[^src-3]

**模型依赖**: RAGAS 使用 GPT-3.5 做 judge（外部 API 依赖）。ARES 用 DeBERTa-v3-Large 可在商用 GPU 本地部署。[^src-4]

**实证差距**: ARES 预测准确率比 RAGAS 高 59.9 (C.R.) 和 14.4 (A.R.) 个百分点。RAGAS 的 C.R. 准确率仅 15-36%，似乎接近随机。[^src-5]

[^card-1]: [^ref→ares-automated-rag-evaluation-system] ARES 框架定义
[^card-2]: [^ref→ares-ranking-accuracy-vs-baselines] 定量对比

[^src-1]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "related_work.tex" P787 -- "RAGAS is based on a handful of heuristic hand-written prompts"
[^src-2]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "introduction.tex" P614-615 -- "a fixed set of heuristically hand-written prompts, offering little adaptability to various evaluation contexts"
[^src-3]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "introduction.tex" P623-625 -- "unlike existing RAG evaluation systems, ARES provides confidence intervals for its scoring"
[^src-4]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "experiments.tex" P513 -- "without relying on external APIs, solely using few-shot prompts and deployable LLMs on commercial GPUs"
[^src-5]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "Tables/ARES_Ranking_vs_GPT3.5.tex" P21 -- "RAGAS Accuracy 31.4%...15.0%"
