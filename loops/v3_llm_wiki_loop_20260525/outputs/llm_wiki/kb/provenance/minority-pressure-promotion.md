---
schema: accepted_card_provenance.v3
card: ../cards/minority-pressure-promotion.md
material_id: arxiv-memory-as-metabolism
digest_id: digest_arxiv-memory-as-metabolism
source_paths:
  - data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt
draft_card: ../../drafts/cards/minority-pressure-promotion.md
draft_provenance: ../../drafts/provenance/minority-pressure-promotion.md
similarity_result: ../../drafts/similarity/minority-pressure-promotion.json
comparison_provenance: ../../drafts/comparison/minority-pressure-promotion.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T15:00:00+08:00
  gate_notes: 6/6 项通过；机制 + Prediction 4 + 与现有 benchmark 区分均有 verbatim 源。
created_time: 2026-05-26T11:15:00+08:00
edited_time: 2026-05-27T15:00:00+08:00
edited_entity: llm
---

## 源证据

- 第 1346–1356 行（CONSOLIDATE phase 4）：
  > "Minority-pressure promotion. Entries that contradict the active wiki *individually* but mutually support each other *in the buffer* are flagged as candidate updates to the dominant interpretation rather than quarantined ... Single contradictions are treated as noise; accumulated contradictions are treated as signal."
- 第 1528–1543 行（§5.7 minority retention 角色）：
  > "Dormant alternatives are kept in the buffer and in quarantine at low storage cost. They are not stored for their own sake; they are stored so that the next consolidation cycle has something to score against incoming entries."
- 第 1828–1832 行（Prediction 4 verbatim）：
  > "The claim is not that minority hypotheses are *stored*, nor that they are *surfaced*, but that they measurably *change downstream outputs* at a non-trivial rate."
- 第 1839–1858 行（与 LongMemEval/TeaFarm 的区分）。
- 第 1913–1917 行（CONSOLIDATE MUST buffer-internal scoring）。

## 卡片范围是否成立

- 本卡聚焦 "minority pressure 如何 procedurally 翻盘"——把 CONSOLIDATE phase 4、§5.7 retention、Prediction 4 的可测目标缝合，形成完整的"机制 + 度量"叙述。
- 直接来自源：buffer-internal scoring、cluster 累积、Prediction 4 措辞、与 LongMemEval/TeaFarm 的区分。
- 边界节直接来自 §5.5 末段与 §8.3。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T15:00:00+08:00
- 检查要点：
  - 问题-机制-Prediction 4-边界 4 节，substantive。
  - 知识密度高；非标题复述。
  - 源支撑：CONSOLIDATE phase 4 / §5.7 / Prediction 4 verbatim。
  - References + Footnotes 双在；Footnotes 3 条 verbatim。
  - frontmatter 完整；related 含 6 张相关卡。

## 备注

- 与 `memory-gravity-load-bearing-protection`、`audit-by-suspension-against-entrenchment` 互为系统补充。
- v2 卡片中暂无相似概念，无重叠。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/minority-pressure-promotion.md`
- draft provenance: `../../drafts/provenance/minority-pressure-promotion.md`
- similarity: `../../drafts/similarity/minority-pressure-promotion.json`
- comparison provenance: `../../drafts/comparison/minority-pressure-promotion.md`
