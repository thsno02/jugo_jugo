---
schema: accepted_card_provenance.v3
card: ../cards/memory-gravity-load-bearing-protection.md
material_id: arxiv-memory-as-metabolism
digest_id: digest_arxiv-memory-as-metabolism
source_paths:
  - data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt
draft_card: ../../drafts/cards/memory-gravity-load-bearing-protection.md
draft_provenance: ../../drafts/provenance/memory-gravity-load-bearing-protection.md
similarity_result: ../../drafts/similarity/memory-gravity-load-bearing-protection.json
comparison_provenance: ../../drafts/comparison/memory-gravity-load-bearing-protection.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:54:00+08:00
  gate_notes: 6/6 项通过；§5.6 全章覆盖且公式 verbatim 引用。
created_time: 2026-05-26T11:10:00+08:00
edited_time: 2026-05-27T14:54:00+08:00
edited_entity: llm
---

## 源证据

- 第 1395–1399 行（G^base 定义 verbatim）：
  > "G_i^base = f(C(i), F(i))"
- 第 1432–1444 行（次线性增长安全性）：
  > "Sub-linear growth is a safety property, not an optimization."
- 第 1453–1461 行（time-decay verbatim）：
  > "G_i^eff(t) = G_i^base · D(t − t_last_access)"
- 第 1478–1491 行（三力分离的硬承诺）：
  > "Folding utility into effective gravity would collapse two distinct mechanisms into one and would change the framework's compensate story; the three forces remain distinct."
- 第 1494–1503 行（已知失效模式 + AUDIT 兜底）：
  > "A false entry that became load-bearing before it was recognized as false is *more* protected, not less. The framework does not eliminate this. AUDIT is the defense..."
- 第 1519–1527 行（与 PageRank/h-index 区别）：
  > "Memory gravity differs on a prospective dimension that bibliometrics does not address: F(i) measures what would break if the entry were removed now, not what has historically referenced it."

## 卡片范围是否成立

- 卡片以单一 mechanism 为中心，覆盖 §5.6 的全部定义、四性质、time-decay、三力分立、与 PageRank/h-index 的区别、已知失效模式，与论文本身把 memory gravity 作为独立支撑机制的处理一致。
- 直接来自源：四性质、G^base/G^eff 关系、三力分立、PageRank/h-index 比较、AUDIT 兜底。
- 未引入超出论文的主张；"quiet foundations 保护路径"是对 §5.3 + §7.5 的综合复述。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:54:00+08:00
- 检查要点：
  - 定义-四性质-时间衰减-三力分离-与 PageRank 对比-失效模式 6 节。
  - 知识密度高；非标题复述。
  - 源支撑：§5.6 多段 + §7.5 verbatim 引用。
  - References + Footnotes 双在；Footnotes 3 条 verbatim。
  - frontmatter 完整；related 含 5 张相关卡。

## 备注

- v2 卡片暂无对应 gravity 概念；本卡是 v3 的新引入，无重叠。
- 与同批次 `audit-by-suspension-against-entrenchment` 互为补充（gravity 立保护，AUDIT 剥离保护）。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/memory-gravity-load-bearing-protection.md`
- draft provenance: `../../drafts/provenance/memory-gravity-load-bearing-protection.md`
- similarity: `../../drafts/similarity/memory-gravity-load-bearing-protection.json`
- comparison provenance: `../../drafts/comparison/memory-gravity-load-bearing-protection.md`
