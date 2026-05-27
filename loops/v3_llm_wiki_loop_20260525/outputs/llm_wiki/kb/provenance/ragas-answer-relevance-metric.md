---
schema: accepted_card_provenance.v3
card: ../cards/ragas-answer-relevance-metric.md
material_id: arxiv-ragas
digest_id: digest_arxiv-ragas
source_paths:
  - data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt
draft_card: ../../drafts/cards/ragas-answer-relevance-metric.md
draft_provenance: ../../drafts/provenance/ragas-answer-relevance-metric.md
similarity_result: ../../drafts/similarity/ragas-answer-relevance-metric.json
comparison_provenance: ../../drafts/comparison/ragas-answer-relevance-metric.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；反推算法、公式、prompt 原文、WikiEval 0.78 与"不衡量事实性"的边界均回到 L150–164 / L238–242 / L271。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
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

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述：正文给出 reverse-question 算法、公式、为何用 embedding 等 substantive 论述。
  - 知识密度：算法 + 直觉 + 边界 + 与 F 联用必要性，四个层次完整。
  - 源支撑：source_ids 含 arxiv-ragas；正文与 footnote 给出 L151 / L153–156 / L160–162 verbatim。
  - References / Footnotes 齐备：L150–164 / L238–242 / L271。
  - frontmatter 完整且合法。
  - related 已填充：6 张同源指标与跨论文姊妹卡。

## 备注

- AR 与 F 的"联用必要性" 可作为后续合成页（synthesis page）的入口主题之一。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/ragas-answer-relevance-metric.md`
- draft provenance: `../../drafts/provenance/ragas-answer-relevance-metric.md`
- similarity: `../../drafts/similarity/ragas-answer-relevance-metric.json`
- comparison provenance: `../../drafts/comparison/ragas-answer-relevance-metric.md`
