---
id: tkpa-chunk-scoring-function
title: TKPA 文本块评分函数
status: draft
card_type: scoring-function
tags: [tkpa, chunk-scoring, pagerank, semantic-similarity, sentiment, graphrag]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graph-poisoning]
evidence_basis: experimental_paper
justification: ../justification/tkpa-chunk-scoring-function.md
canonical_concept: tkpa-chunk-scoring-function
aliases: [Chunk Selection Score, C_score, ChunkScore, 文本块选择评分]
summary: >-
  TKPA chunk scoring function C_score = w1*S_graph + w2*S_semantic + w3*S_attitude 融合三个信号
  对候选 chunk 排序。S_graph 基于 ego-subgraph 内实体 PageRank 中心性，S_semantic 为 chunk 与查询
  嵌入余弦相似度，S_attitude 量化情感极性。默认权重 (0.5, 0.3, 0.2) 优先图结构。
  消融显示 graph 结构贡献最大；k=3 chunks 即达 91.2% ASR 饱和。Chunk Selection Score PageRank cosine similarity。
related: [targeted-knowledge-poisoning-attack, tkpa-vulnerability-score]
---

在 ego-subgraph 约束的候选 chunk 中，TKPA 用加权组合评分确定重写优先级：

C_score = w1 * S_graph + w2 * S_semantic + w3 * S_attitude

- S_graph：对应实体在 ego-subgraph 内的 PageRank 中心性（结构影响力）
- S_semantic：chunk 嵌入与目标查询的余弦相似度（语境相关性）
- S_attitude：语言模型量化的情感极性（语言框架偏置潜力）

各项归一化至 [0,1] 后组合，默认权重 (0.5, 0.3, 0.2) 优先结构杠杆。[^src-1]

消融实验：等权达 89.8% ASR；单组分 graph-only 65.3%, semantic-only 58.2%, attitude-only 51.7%。修改 chunk 数 k=1→55.8%, k=2→81.3%, k=3→91.2%，k>3 饱和。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "Chunk Scoring and Selection" P367-387 -- "C_score = w_1 S_graph + w_2 S_semantic + w_3 S_attitude"
[^src-2]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "Ablation Study of TKPA's Parameters" P794-798 -- "tuning the weights to emphasize graph structure (w1=0.5,w2=0.3,w3=0.2) further boosts ASR to 91.2%"

[^card-4]: [[targeted-knowledge-poisoning-attack]] 该评分函数是 TKPA 流水线第三步
