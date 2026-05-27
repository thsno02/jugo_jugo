---
schema: accepted_card_provenance.v3
card: ../cards/memory-as-metabolism-five-operations.md
material_id: arxiv-memory-as-metabolism
digest_id: digest_arxiv-memory-as-metabolism
source_paths:
  - data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt
draft_card: ../../drafts/cards/memory-as-metabolism-five-operations.md
draft_provenance: ../../drafts/provenance/memory-as-metabolism-five-operations.md
similarity_result: ../../drafts/similarity/memory-as-metabolism-five-operations.json
comparison_provenance: ../../drafts/comparison/memory-as-metabolism-five-operations.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:50:00+08:00
  gate_notes: 6/6 项通过；五操作总图清晰，vitality 公式与 §7.5 MUST 引用准确。
created_time: 2026-05-26T11:05:00+08:00
edited_time: 2026-05-27T14:50:00+08:00
edited_entity: llm
---

## 源证据

- 第 1037–1067 行：§5.0 角色总表（TRIAGE/DECAY/CONTEXTUALIZE/CONSOLIDATE/AUDIT/gravity/minority-retention）。
- 第 1131–1158 行：§5.1 解释为什么必须把 streaming ingestion 与 batched consolidation 拆开：
  > "Streaming coherence is self-sealing. A single entry arriving alone and scored against the dominant wiki gets quarantined immediately if it contradicts the dominant interpretation, which means the dominant interpretation never updates. Batched consolidation breaks this lock."
- 第 1184–1191 行：vitality 公式（verbatim）。
- 第 1320–1356 行：§5.5 CONSOLIDATE 四 phase。
- 第 1555–1571 行：§5.8 AUDIT 伪代码（verbatim 块）：
  > "FOR each entry in top_N_by_gravity: suspend from active wiki; run N queries that previously accessed this entry; IF query performance degrades: restore, confirm gravity; IF query performance unchanged: reduce gravity — entry is dead weight; IF query performance improves: archive — entry was actively interfering"
- 第 1898–1912 行：§7.5 conformance 的 TRIAGE MUST NOT 列表与 CONTEXTUALIZE linkout 约束。

## 卡片范围是否成立

- 把五操作合在一张 mechanism 卡而不拆五张，是因为论文自身把它们作为"single time-structured procedural rule"的实现，分散反而破坏"哪一步在哪个时间窗"的关键关系。
- 直接来自源：操作名、节奏分类、vitality 公式、AUDIT 伪代码、§7.5 的 MUST/MUST NOT。
- 引申部分：边界节里的"Valley of Amnesia"、"correlated noise amplification"是对 §5.5 末段 + §9 limitation 的浓缩。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:50:00+08:00
- 检查要点：
  - 五操作分述 + vitality 公式 + sleep-function rationale + 边界 4 节。
  - 知识密度足；非标题复述。
  - 源支撑：§5 多段 + §7.5 conformance MUST verbatim。
  - References + Footnotes 双在。
  - frontmatter 完整；related 含 7 张相关卡。

## 备注

- 与 v2 现有 `llm-knowledge-base-five-stage-workflow` 有概念上的重叠，但层级不同：v2 卡片是 Karpathy 原文的 collect/annotate/organize/revisit 流程；本卡是 governance 层的 5 个保留/治理算子。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/memory-as-metabolism-five-operations.md`
- draft provenance: `../../drafts/provenance/memory-as-metabolism-five-operations.md`
- similarity: `../../drafts/similarity/memory-as-metabolism-five-operations.json`
- comparison provenance: `../../drafts/comparison/memory-as-metabolism-five-operations.md`
