---
schema: draft_card_provenance.v3
draft_card: ../cards/ragas-answer-relevance-metric.md
material_id: arxiv-ragas
digest_id: digest_arxiv-ragas
source_paths:
  - data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
edited_entity: llm
---

## 源证据

1. `agent_source_bundle.txt:150-164` —— Answer Relevance 段完整描述。
2. `agent_source_bundle.txt:151` —— 明确"不考虑事实性，只惩罚不完整 / 冗余"。
3. `agent_source_bundle.txt:153-156` —— Reverse generation prompt。
4. `agent_source_bundle.txt:158-162` —— 公式 AR = (1/n) Σ sim(q, q_i)。
5. `agent_source_bundle.txt:238-242` —— Ragas AR accuracy = 0.78（vs GPT Score 0.52）。
6. `agent_source_bundle.txt:271` —— AR 差距小的解释。

## 卡片范围是否成立

- 卡片范围清晰对应 AR 这一单一指标，与 framework / 其他指标卡职责分离。
- "必须与 Faithfulness 联用" 是基于指标定义（不衡量事实性）的合理操作建议。
- "embedding 选型影响 AR 跨论文比较" 是基于 embedding 实践的合理工程引申。

## 发表门控结果

本轮未运行。

## 备注

- AR 与 F 的"联用必要性" 可作为后续合成页（synthesis page）的入口主题之一。
