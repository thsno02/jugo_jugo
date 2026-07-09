---
id: ragchecker-meta-evaluation
title: RAGChecker 元评估方法与结果
status: accepted
card_type: experimental-finding
tags:
- meta-evaluation
- human-correlation
- ragas
- trulens
- ares
- pearson
- spearman
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-ragchecker
evidence_basis: experimental_paper
justification: ../justification/ragchecker-meta-evaluation.md
canonical_concept: ragchecker-meta-evaluation
aliases:
- RAGChecker meta evaluation
- 元评估
- human correlation validation
summary: RAGChecker meta evaluation 通过 280 个 pairwise 实例验证指标与人类判断的相关性。流程：从 8 个 RAG 系统 x 10 域的输出中采样 response pair，由 10 名标注者在 correctness/completeness/overall 三维度标注偏好（5 级）。RAGChecker 在 overall assessment
  维度达到 Pearson 61.93 / Spearman 60.90，显著优于最强基线 RAGAS Answer Similarity 的 48.31/57.23。人类标注者间一致率 90.95%，annotator correlation 上界为 70.09/68.89。
related:
- ragchecker-framework-overview
- ragchecker-overall-metrics
---

RAGChecker 通过系统化的 meta evaluation 验证其指标与人类判断的对齐程度。[^src-1]

**元评估数据集构建**：从 8 个 baseline RAG 系统在 10 域 benchmark 上的输出中采样。对所有 C(8,2)=28 对系统组合，每域采样一对 response，共 280 个 pairwise 实例。每实例由 2 名标注者独立评判，在 correctness、completeness、overall assessment 三维度给出 5 级偏好。[^src-1]

**评估流程**：人类偏好标签视为分差 h_i = H(r_i^2) - H(r_i^1) ∈ {-2,-1,0,1,2}；对评估模型 E 计算归一化分差 e_i = f(E(r_i^2)-E(r_i^1)) ∈ [-2,2]；计算 h_i 与 e_i 的 Pearson/Spearman 相关。[^src-2]

**结果**（Overall Assessment 维度）：[^src-3]
- RAGChecker: Pearson **61.93**, Spearman **60.90**
- RAGAS Answer Similarity（最强基线，使用 text-embedding-ada-002）: 48.31 / 57.23
- 人类 annotator 上界: 70.09 / 68.89
- 标注者间一致率: 90.95%

RAGChecker 在三个维度均取得最强相关性，且与人类上界之间仍存在明显差距。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/experiments.tex Meta Evaluation" -- "we construct the meta evaluation dataset with sampled instances...By considering all combinations over 10 domains and 28 baseline pairs, we end up with 280 instances"
[^src-2]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/experiments.tex Meta Evaluation Process" -- "the human preference labels can be seen as the score difference...we compute a normalized score difference"
[^src-3]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "tables/human_eval_selected.tex" -- "RAGChecker...49.66 46.95 60.67 58.11 61.93 60.90...Human...63.67 59.19 71.91 68.36 70.09 68.89"

[^card-5]: 参见 [ragchecker-overall-metrics] 了解作为元评估对象的 precision/recall/F1 指标
