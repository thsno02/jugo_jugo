---
id: ukpa-graph-fragmentation-results
title: UKPA 图碎片化实验结果
status: accepted
card_type: experimental-finding
tags:
- ukpa
- graph-fragmentation
- node-retention
- edge-jaccard
- qa-accuracy
- graphrag
- lightrag
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-graph-poisoning
evidence_basis: experimental_paper
justification: ../justification/ukpa-graph-fragmentation-results.md
canonical_concept: ukpa-graph-fragmentation-results
aliases:
- UKPA structural degradation
- UKPA graph damage
- UKPA QA accuracy drop
- UKPA 图结构退化
summary: 'UKPA graph fragmentation results 显示攻击导致严重图拓扑重写而非简单信息删除。MS-GraphRAG RUW: Node Ret 0.5648, Edge Ret 0.2770, Edge Jaccard 0.1581; LightRAG RUW: Node Ret 0.4335, Edge Jaccard 0.0789。QA 准确率：MS-GraphRAG
  95%->50%, LightRAG 90%->45%。 对比 TextFooler 基线仅降至 85%。修改量 RUW 60/134072 词 (0.045%), LP 32/94496 词 (0.033%)。 Node retention Edge Jaccard similarity structural degradation。'
related:
- universal-knowledge-poisoning-attack
- ukpa-structural-impact-score
---

UKPA 对图结构的破坏（不是简单删除节点/边而是拓扑近乎完全重写）：

MS-GraphRAG (RUW): Node Ret Rate 0.5648, Edge Ret Rate 0.2770, Node Jaccard 0.4100, Edge Jaccard 0.1581
LightRAG (RUW): Node Ret Rate 0.4335, Edge Ret Rate 0.1443, Node Jaccard 0.2899, Edge Jaccard 0.0789

Edge Jaccard 低至 0.0789 表明边集几乎被完全替换。[^src-1]

下游 QA 影响：
- MS-GraphRAG: 无攻击 95% -> UKPA 50% (TextFooler 仅降至 85%)
- LightRAG: 无攻击 90% -> UKPA 45% (TextFooler 仅降至 85%)[^src-2]

修改量极小：RUW 60/134072 词 (0.045%), LP 32/94496 词 (0.033%)。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "Table 2 Structural degradation" P652-661 -- "Node Ret. Rate 0.5648... Edge Jaccard 0.0789"
[^src-2]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "Table 3 UKPA QA accuracy" P670-687 -- "No Attack 95%... UKPA 50%"
[^src-3]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "Table 5" P782-784 -- "UKPA LP 94496 32 0.033%... RUW 134072 60 0.045%"

[^card-9]: [[universal-knowledge-poisoning-attack]] 这些数据量化了 UKPA 的破坏效果
