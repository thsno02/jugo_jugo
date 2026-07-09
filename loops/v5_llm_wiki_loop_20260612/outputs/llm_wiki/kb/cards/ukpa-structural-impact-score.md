---
id: ukpa-structural-impact-score
title: UKPA 结构影响评分
status: accepted
card_type: scoring-function
tags:
- ukpa
- structural-impact-score
- entity-fragmentation
- semantic-closeness
- graphrag
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-graph-poisoning
evidence_basis: experimental_paper
justification: ../justification/ukpa-structural-impact-score.md
canonical_concept: ukpa-structural-impact-score
aliases:
- Structural Impact Score
- I_score
- UKPA scoring function
- 结构影响评分
summary: UKPA structural impact score I_score = alpha*S_entity + beta*S_relation + gamma*(1-S_vec) 作为代理评分 在无法访问最终图的条件下估计候选改写的结构破坏力。S_entity 为原始/修改 chunk 实体集对称差， S_relation 为关系集对称差，S_vec 为嵌入余弦相似度。默认 (0.25,0.25,0.5)
  优先语义接近性保证隐蔽。 消融：等权 QA acc 0.55 vs 默认 0.50；单组分仅 0.70-0.75。编辑距离<=3 已达最大攻击效果。
related:
- universal-knowledge-poisoning-attack
- ukpa-graph-fragmentation-results
---
UKPA 在无法观察最终图结构的约束下，用代理评分函数估计每个候选改写的局部结构变化：

I_score = alpha * S_entity + beta * S_relation + gamma * (1 - S_vec)

- S_entity：原始与修改 chunk 提取实体集的对称差（实体碎片化程度）
- S_relation：关系集的对称差（关系扭曲程度）
- S_vec：原始与修改 chunk 嵌入的余弦相似度（1-S_vec 惩罚语义偏离）

默认权重 (alpha,beta,gamma) = (0.25, 0.25, 0.5) 优先保证语义接近以维持隐蔽性。[^src-1]

消融：等权 QA acc 0.55；默认设置 0.50（更低=攻击更强）。单组分仅降至 0.70-0.75。编辑距离 d_edit<=3 已实现最大 QA 降低，d>3 增加困惑度无额外收益。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "Structural Impact Scoring" P531-541 -- "I_score = alpha S_entity + beta S_relation + gamma (1 - S_vec)"
[^src-2]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "Ablation Study of UKPA's Parameters" P813-820 -- "tuning the weights to prioritize semantic preservation (alpha=0.25,beta=0.25,gamma=0.5) further reduces it to 0.50"

[^card-6]: [[universal-knowledge-poisoning-attack]] 该评分函数是 UKPA 第三步的核心
