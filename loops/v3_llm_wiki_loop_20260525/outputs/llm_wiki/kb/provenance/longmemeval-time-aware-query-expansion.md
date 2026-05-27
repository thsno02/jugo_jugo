---
schema: accepted_card_provenance.v3
card: ../cards/longmemeval-time-aware-query-expansion.md
material_id: arxiv-longmemeval
digest_id: digest_arxiv-longmemeval
source_paths:
  - data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt
draft_card: ../../drafts/cards/longmemeval-time-aware-query-expansion.md
draft_provenance: ../../drafts/provenance/longmemeval-time-aware-query-expansion.md
similarity_result: ../../drafts/similarity/longmemeval-time-aware-query-expansion.json
comparison_provenance: ../../drafts/comparison/longmemeval-time-aware-query-expansion.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T11:34:00+08:00
  gate_notes: 6/6 项通过；双侧时间感知改造 + 6.8/11.3% 增益 + 强 LLM 边界 + N/A 拒答 prompt 齐备。
created_time: 2026-05-26T14:40:00+08:00
edited_time: 2026-05-27T11:34:00+08:00
edited_entity: llm
---

## 源证据

- 第 1504-1510 行（§5.3 query 章节 + 6.8% / 11.3% recall 增益数据）。
- 第 129-143 行：prompt 完整文本，包括 query 时拒答 N/A 的指令。
- 第 1757-1759 行（appendix）：详细分析 Llama 8B 失败模式。
- 第 1199-1219 行（appendix 表 `tab:query-expansion-examples`）：四个具体例子说明 false positive。
- 第 1099-1128 行（表 `tab:temp-query-results`）：完整 retrieval 数字 K=V vs K=V+fact × with/without query expansion × $\mathcal{M}_T$ 模型。

## 卡片范围是否成立

- 增益数字、强弱 LLM 对比、与 fact key expansion 正交都直接来自论文。
- "不要把时间过滤当 hard pruning"是从 false positive 例子的合理引申，不是论文原话；但论文确实强调 $\mathcal{M}_T$ 必须能拒答 N/A，与此引申一致。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T11:34:00+08:00
- 检查要点：
  - mechanism 卡双侧改造逐步描述 + 增益 + 关键边界，非标题复述。
  - 知识密度合格。
  - source_ids 含 `arxiv-longmemeval`，正文锚到第 1504-1510 / 129-143 / 1757-1759 / 1199-1219 行。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 5 张相关卡。

## 备注

- TR 这条线是 LongMemEval 唯一在 indexing 层面引入"额外结构（时间戳）"的优化；与 LoCoMo 的 event-graph 思路构成互文——两者都在用"时间锚点"对长记忆做约束。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/longmemeval-time-aware-query-expansion.md`
- draft provenance: `../../drafts/provenance/longmemeval-time-aware-query-expansion.md`
- similarity: `../../drafts/similarity/longmemeval-time-aware-query-expansion.json`
- comparison provenance: `../../drafts/comparison/longmemeval-time-aware-query-expansion.md`
