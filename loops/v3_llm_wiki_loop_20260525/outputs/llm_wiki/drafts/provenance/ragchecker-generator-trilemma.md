---
schema: draft_card_provenance.v3
draft_card: ../cards/ragchecker-generator-trilemma.md
material_id: arxiv-ragchecker
digest_id: digest_arxiv-ragchecker
source_paths:
  - data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt
created_time: 2026-05-26T11:25:00+08:00
edited_time: 2026-05-26T11:25:00+08:00
edited_entity: llm
---

## 源证据

- faithfulness 定义（L892）：*"we first compute the proportion of $c^{(m)}_i$ that are entailed in retrieved chunks. This metric is faithfulness."*
- noise sensitivity / hallucination 分类（L898–900）：incorrect claim 的三种情形。
- context utilization 与 self-knowledge（L907–908）。
- 三难明示（L830）：*"When tuning the generator, the trilemma of context utilization, noise sensitivity, and faithfulness makes it difficult to improve all aspects simultaneously."*
- prompt 显式要求三组数字（L820–822）：92.2→93.6、59.2→63.7、35.4→38.1。
- Llama3-70B 与 GPT-4 对照（L800–805，被注释段）：Llama3 faithfulness 93.2 / 95.9；GPT-4 87.9 / 93.0；GPT-4 同时具备更高 utilization 与更低 noise sensitivity。
- 开源模型缺乏判别力（L784）：*"Open-Source Models are Worse at Distinguishing Accurate Information from Noise."*

## 卡片范围是否成立

- 三难是 RAGChecker 论文最具操作含义的发现之一，能直接指导 prompt 与模型选型，独立成卡比放在某张总指标卡里清晰。
- 三个指标的定义都来自源材料；张力关系也由 §Diagnosis 与 §Suggestions 明确给出。
- 引申主张：把"faithful 不等同于好"用 Llama3 vs GPT-4 的实例化对照解释——属于论文事实组合，不是新主张。

## 发表门控结果

本轮未运行。

## 备注

- 与同批 `ragchecker-claim-entailment-decomposition` 卡共享原语；与未来"chunk-level faithfulness"卡互补——后者解释为什么 relevant noise sensitivity 系统性大于 irrelevant 的。
