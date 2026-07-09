---
id: tkpa-experimental-results
title: TKPA 实验效果
status: accepted
card_type: experimental-finding
tags:
- tkpa
- asr
- qasd
- attack-effectiveness
- poisonedrag
- graphrag
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-graph-poisoning
evidence_basis: experimental_paper
justification: ../justification/tkpa-experimental-results.md
canonical_concept: tkpa-experimental-results
aliases:
- TKPA performance
- TKPA ASR results
- TKPA 攻击成功率
summary: TKPA experimental results 在三个数据集上达平均 ASR 91.27%、QASD 0.83。LP 93.1%/0.85， FC08 89.5%/0.81，JAPB 91.2%/0.83。远超 PoisonedRAG (70.4%/0.67) 和 Naive Swap (16.1%/0.13)。 修改量：LP 仅 48/94496 词 (0.055%)，FC08
  76/40223 词 (0.18%)，JAPB 113/44445 词 (0.254%)。 结构引导投毒以更少编辑实现更高精度。Attack Success Rate QASD semantic deviation。
related:
- targeted-knowledge-poisoning-attack
- tkpa-chunk-scoring-function
---

TKPA 在三个长文档数据集上的攻击效果：

| 数据集 | ASR (%) | QASD | 修改词数(min) | 修改比例(min) |
|--------|---------|------|-------------|-------------|
| LP (小王子) | 93.10 | 0.85 | 48/94496 | 0.055% |
| FC08 (2008金融危机) | 89.50 | 0.81 | 76/40223 | 0.18% |
| JAPB (日本泡沫) | 91.20 | 0.83 | 113/44445 | 0.254% |
| 平均 | 91.27 | 0.83 | - | - |

对比基线：PoisonedRAG 平均 ASR 70.4%/QASD 0.67；Naive Swap 仅 16.1%/0.13。[^src-1][^src-2]

TKPA 以更少修改实现更高精度操纵，验证了结构引导投毒优于朴素文本级干预。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "TKPA Performance" P604-612 -- "TKPA achieves high ASR (over 90% on average)... TKPA achieves both higher ASR and larger semantic deviation with fewer edits"
[^src-2]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- "Table 5 Words modification" P776-789 -- "TKPA LP 94496 48/155 0.055%/0.164%"

[^card-8]: [[targeted-knowledge-poisoning-attack]] 这些数据验证了 TKPA 方法的有效性
