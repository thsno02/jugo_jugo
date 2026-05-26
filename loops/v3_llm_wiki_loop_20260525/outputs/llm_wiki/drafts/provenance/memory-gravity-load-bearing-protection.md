---
schema: draft_card_provenance.v3
draft_card: ../cards/memory-gravity-load-bearing-protection.md
material_id: arxiv-memory-as-metabolism
digest_id: digest_arxiv-memory-as-metabolism
source_paths:
  - data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt
created_time: 2026-05-26T11:10:00+08:00
edited_time: 2026-05-26T11:10:00+08:00
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

本轮未运行。

## 备注

- v2 卡片暂无对应 gravity 概念；本卡是 v3 的新引入，无重叠。
- 与同批次 `audit-by-suspension-against-entrenchment` 互为补充（gravity 立保护，AUDIT 剥离保护）——comparison 阶段可建立 cross-link。
