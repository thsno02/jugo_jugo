---
schema: accepted_card_provenance.v3
card: ../cards/memory-as-metabolism-conflict-routing-matrix.md
material_id: arxiv-memory-as-metabolism
digest_id: digest_arxiv-memory-as-metabolism
source_paths:
  - data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt
draft_card: ../../drafts/cards/memory-as-metabolism-conflict-routing-matrix.md
draft_provenance: ../../drafts/provenance/memory-as-metabolism-conflict-routing-matrix.md
similarity_result: ../../drafts/similarity/memory-as-metabolism-conflict-routing-matrix.json
comparison_provenance: ../../drafts/comparison/memory-as-metabolism-conflict-routing-matrix.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:46:00+08:00
  gate_notes: 6/6 项通过；7 行矩阵逐行展开且与 §5.0 verbatim 对应。
created_time: 2026-05-26T15:10:00+08:00
edited_time: 2026-05-27T14:46:00+08:00
edited_entity: llm
---

## 源证据

### §5.0 矩阵 legend（第 1085–1093 行）

> "Mirror = apply user-aligned behavior in the interaction/working representation without mutating canonical entries. Compensate = route through CONSOLIDATE with elevated friction relative to the default. Buffer = store in minority branch without immediate integration. AUDIT override = route to AUDIT with priority and apply the §5.8 gravity-reduction path if failure persists. External correction = flag for post-update CONSOLIDATE review due to base-model prior change."

### 矩阵 7 行（第 1100–1115 行附近，按论文表序）

行 1（vocabulary 偏离、无效用退化）→ Mirror in interaction, preserve divergence marker, do not silently overwrite canonical wiki.
行 2（同上 + 效用退化）→ Compensate; utility degradation triggers domain reclassification; higher friction in CONSOLIDATE.
行 3（sycophancy 模式）→ Compensate regardless of utility signal; AUDIT priority queue; highest friction; flag high-gravity reinforcing entries.
行 4（单源单周期反对证据）→ Default Buffer; exception clause for high-trust sources.
行 5（多源多周期累积反对证据）→ Compensate (consolidate candidate); §5.5 promotion 评估.
行 6（高 gravity 多周期 AUDIT 反复差）→ AUDIT override; §5.8 gravity-reduction.
行 7（底模更新带新先验）→ External correction channel; depends structurally on §8.3 separability.

### §5.0 Limitation 段（第 1120–1129 行）

> "Row 7 names the base-model correction channel, but the structural residual—fully novel bad beliefs not represented in the base model and not contradicted by subsequent experience—is not captured by any row in this matrix ... The matrix specifies how the framework behaves when the relevant conflict signal exists; it does not manufacture signal that external sources do not provide. The matrix does not define calibration parameters (e.g., cycle counts, source diversity thresholds), which are explicitly left to implementation and empirical validation."

### §1.2 程序冲突规则原则化（第 318–328 行）

> "What neither the vocabulary nor the individual mechanisms provide is a time-structured procedural conflict rule for resolving the mirror-vs-compensate tension in a personal companion-memory substrate—specifically, a decision procedure governing what gets buffered versus quarantined versus audited, across which timescale, and with what decision consequences at each stage. The contribution is the TRIAGE → CONSOLIDATE → AUDIT execution model as a binding."

### §11 conclusion 把矩阵列为 framing contribution 之一（第 2423–2431 行）

> "The mirror-vs-compensate principle as a time-structured procedural conflict rule—not just the observation that mirroring and compensating are in tension (prior work including 'To Mask or to Mirror,' arXiv 2510.01924, names that tension and uses the vocabulary explicitly), but a specific resolution procedure operationalized across concrete architectural timescales: mirror by default in the streaming path, compensate during scheduled consolidation windows, AUDIT as the slow-cycle tiebreaker, and instantiated case-by-case in the conflict routing matrix (§5.0). The specificity is the contribution."

## 卡片范围是否成立

本卡聚焦 §5.0 conflict routing matrix。现有 `memory-as-metabolism-mirror-vs-compensate` 卡片只在"时间结构化的程序冲突规则"一段提到这个矩阵存在，**未列出 7 行**、未拆 Row 3 / Row 4 exception / Row 7 与 separability 的强依赖。

所有 7 行内容、legend、limitation 段都直接来自 §5.0 原文。Row 3 的"sycophancy 显式拦截"、Row 4 的 exception clause、Row 7 的 separability 强依赖是论文显式陈述。"residual failure mode"在 §5.0 末尾 + §9 都有显式承认。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:46:00+08:00
- 检查要点：
  - 主张-legend-7 行-边界-操作含义结构完整。
  - 知识密度极高：legend、7 行 + 行级 nuance、两条边界。
  - 源支撑：§5.0 legend / 7 行 / Limitation + §1.2 + §11 五段 verbatim。
  - References + Footnotes 双在；Footnotes 3 条 verbatim。
  - frontmatter 完整；related 含 6 张相关卡。

## 备注

- 与 `memory-as-metabolism-mirror-vs-compensate` 关系：那张卡讲原则与三时间尺度概要，本卡讲矩阵的**具体 7 行**——前者是 why，本卡是 how。
- 与 `memory-as-metabolism-architectural-separability` 强耦合（Row 7）；与 `audit-by-suspension-against-entrenchment` 强耦合（Row 6）。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/memory-as-metabolism-conflict-routing-matrix.md`
- draft provenance: `../../drafts/provenance/memory-as-metabolism-conflict-routing-matrix.md`
- similarity: `../../drafts/similarity/memory-as-metabolism-conflict-routing-matrix.json`
- comparison provenance: `../../drafts/comparison/memory-as-metabolism-conflict-routing-matrix.md`
