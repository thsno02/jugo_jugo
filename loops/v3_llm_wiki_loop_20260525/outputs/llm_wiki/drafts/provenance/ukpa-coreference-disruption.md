---
schema: draft_card_provenance.v3
draft_card: ../cards/ukpa-coreference-disruption.md
material_id: arxiv-graph-poisoning
digest_id: digest_arxiv-graph-poisoning
source_paths:
  - data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt
created_time: 2026-05-26T11:10:00+08:00
edited_time: 2026-05-26T11:10:00+08:00
edited_entity: llm
---

## 源证据

- 攻击动机（L478–489）：*"GraphRAG relies heavily on linguistic coherence cues, particularly coreference chains and referring expressions, to decide when multiple mentions across chunks should be merged into a single entity node."*
- 攻击者无法看图（L486–488）：*"the attacker never observes the final structure, yet edits that look benign can still propagate through the construction process and cause large-scale structural distortions."*
- 流水线四步：分别在 L506–512 (Chunk Iteration)、L515–525 (Perturbation Candidate Generation)、L527–541 (Structural Impact Scoring)、L544–550 (Selection and Corpus Update)。
- 代理评分（L531–537）：$\mathcal{I}_\mathrm{score} = \alpha S_\mathrm{entity} + \beta S_\mathrm{relation} + \gamma (1 - S_\mathrm{vec})$；默认权重 $(0.25,0.25,0.5)$ 见 L576–577。
- 拓扑表（L641–662）：节点保留 0.5648/0.5769（MS GraphRAG），0.4335/0.3926（LightRAG）；边保留更低；Jaccard 最低 0.0789。
- QA 表（L667–687）：MS GraphRAG 95→50，LightRAG 90→45，TP 基线 85。
- 修改词量（L769–789）：LP 32/94496（0.033%），RUW 60/134072（0.045%）。

## 卡片范围是否成立

- UKPA 与 TKPA 设计哲学完全不同（语言学 vs 图论；广泛降级 vs 单点劫持），独立成卡比合并写更清晰。
- 卡片范围严格限定在 UKPA 流水线 + 代理评分 + 杀伤力数字；不涉及防御对照（另卡处理）。
- 引申极少：把 UKPA 与 TextFooler 的根本差别放在边界处，论文 §Baselines 已暗示。

## 发表门控结果

本轮未运行。

## 备注

- v2 无相关卡。
- 后续 comparison 可与未来出现的"共指消解 / coreference resolution 综述"卡对照——本卡只关注攻击侧。
