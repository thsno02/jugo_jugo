---
schema: accepted_card_provenance.v3
card: ../cards/audit-by-suspension-against-entrenchment.md
material_id: arxiv-memory-as-metabolism
digest_id: digest_arxiv-memory-as-metabolism
source_paths:
  - data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt
draft_card: ../../drafts/cards/audit-by-suspension-against-entrenchment.md
draft_provenance: ../../drafts/provenance/audit-by-suspension-against-entrenchment.md
similarity_result: ../../drafts/similarity/audit-by-suspension-against-entrenchment.json
comparison_provenance: ../../drafts/comparison/audit-by-suspension-against-entrenchment.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；AUDIT 伪代码 verbatim + Kuhn 类比 + ShortGPT 类比 + §9 灵敏度承认 + §5.0 决胜者全部锁到原文行号。
created_time: 2026-05-26T11:20:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
edited_entity: llm
---

## 源证据

- 第 1563–1570 行（§5.8 AUDIT 伪代码 verbatim）：
  > "FOR each entry in top_N_by_gravity: suspend from active wiki; run N queries that previously accessed this entry; IF query performance degrades: restore, confirm gravity; IF query performance unchanged: reduce gravity — entry is dead weight; IF query performance improves: archive — entry was actively interfering"
- 第 1583–1589 行（Kuhn 类比的核心收益声明）：
  > "AUDIT does not resolve the Kuhnian tension; it makes the cost of unaddressed anomalies visible at the entry level rather than letting it accumulate invisibly at the wiki level."
- 第 1591–1602 行（Wikipedia 概念网络的 Kuhn 经验化 [18] 与 AUDIT 的 forward / performance-based 扩展对比）。
- 第 1611–1622 行（ShortGPT 类比 verbatim）。
- 第 1604–1608 行（灵敏度承认）：
  > "AUDIT sensitivity is an open problem. If the query set used for stress testing is narrow or self-confirming, harmful central nodes stay protected. We do not solve this."
- 第 1113 行（§5.0 routing matrix row 6 AUDIT override）。
- 第 1944–1951 行（§7.5 AUDIT MUST 列表）。
- 第 2168–2174 行（§9 limitation："AUDIT sensitivity is the critical open problem"）。

## 卡片范围是否成立

- 卡片把 §5.8 全部内容（伪代码、Kuhn、ShortGPT、灵敏度）+ §5.0 routing matrix row 6 + §9 limitation 浓缩为单一 mechanism 卡，与论文把 AUDIT 视作"compensate 故事最后一道防线"的处理一致。
- 直接来自源：伪代码、Kuhn 类比措辞、ShortGPT 比较、灵敏度承认。
- 引申点："三者共同构成的 compensate 故事是部分而非完整的"是对论文反复强调"partial safety story"的概括，非新增主张。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 不是标题复述：伪代码 + 三分支决策映射 + Kuhn + ShortGPT 双类比 + §9 诚实承认 + §5.0 决胜者角色。
  - 知识密度足够：机制 + 类比 + 反例 + 边界（灵敏度未解决）。
  - 源支撑齐全：每条主张锁到 `agent_source_bundle.txt` 具体行号。
  - References 与 Footnotes 双章节存在。
  - frontmatter 完整合法，mechanism 类型与正文一致。
  - related 已链 memory-as-metabolism 系列。

## 备注

- 与 `memory-gravity-load-bearing-protection`、`minority-pressure-promotion` 互补——三卡是 v3 compensate 故事的完整三部分。
- v2 卡片中无对应概念，无重叠。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/audit-by-suspension-against-entrenchment.md`
- draft provenance: `../../drafts/provenance/audit-by-suspension-against-entrenchment.md`
- similarity: `../../drafts/similarity/audit-by-suspension-against-entrenchment.json`
- comparison provenance: `../../drafts/comparison/audit-by-suspension-against-entrenchment.md`
