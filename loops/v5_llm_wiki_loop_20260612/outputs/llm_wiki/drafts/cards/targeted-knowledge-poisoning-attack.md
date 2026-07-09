---
id: targeted-knowledge-poisoning-attack
title: 定向知识投毒攻击 TKPA
status: draft
card_type: attack-method
tags: [graphrag, tkpa, targeted-attack, graph-theory, knowledge-poisoning]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graph-poisoning]
evidence_basis: experimental_paper
justification: ../justification/targeted-knowledge-poisoning-attack.md
canonical_concept: targeted-knowledge-poisoning-attack
aliases: [TKPA, Targeted Knowledge Poisoning Attack, Targeted KPA, 定向知识投毒]
summary: >-
  Targeted Knowledge Poisoning Attack TKPA 利用图论分析（中心性、社区结构、ego-subgraph）定位知识图谱中
  结构上最脆弱的区域，选择性重写少量文本 chunk，实现对特定 QA 输出的精确操纵。四步流水线：
  Vulnerable Community Localization -> Ego-subgraph Extraction -> Chunk Scoring and Selection -> LLM-driven Manipulation。
  平均 ASR 91.27%，修改量 <0.06% 语料。定向知识投毒攻击 TKPA graph-theoretic。
related: [graphrag-knowledge-poisoning-attack-surface, tkpa-vulnerability-score, tkpa-chunk-scoring-function]
---

TKPA 将投毒视为知识图谱上的网络干预问题。给定用户查询，攻击者先通过 LLM 提取目标实体，再利用图论原理——中心性定位结构影响力节点、社区结构限制影响区域、ego-subgraph 实现编辑局部化——逐步缩小攻击范围。[^src-1]

四步流水线：(1) 脆弱社区定位 VCL；(2) Ego-subgraph 提取；(3) Chunk 评分与选择；(4) LLM 驱动的文本重写。仅修改 top-k 个高分 chunk（通常 k=3 即达饱和），即可通过图结构传播实现对选定查询的精准语义操纵。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "Targeted Knowledge Poisoning Attack" P322-328 -- "the key insight behind TKPA is to treat poisoning as a network intervention problem on the knowledge graph rather than a random text-editing task"
[^src-2]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "Targeted Knowledge Poisoning Attack" P328-329 -- "This structure-guided view leads to a four-module pipeline that progressively narrows the attack scope"

[^card-2]: [[graphrag-knowledge-poisoning-attack-surface]] TKPA 是该攻击面的定向实例化
