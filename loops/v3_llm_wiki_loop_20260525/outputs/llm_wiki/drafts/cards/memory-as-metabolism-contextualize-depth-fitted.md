---
id: memory-as-metabolism-contextualize-depth-fitted
title: CONTEXTUALIZE：把外部源按用户当前 working-context depth 压缩，强制保留 linkout
status: draft
card_type: mechanism
tags: [#memory, #companion-system, #contextualize, #selective-absorption, #dream-cycle]
created_time: 2026-05-26T15:10:00+08:00
edited_time: 2026-05-26T15:10:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
provenance_card: ../provenance/memory-as-metabolism-contextualize-depth-fitted.md
aliases: [CONTEXTUALIZE operation, depth-fitted compression, selective absorption, cold memory tier]
related: [memory-as-metabolism-five-operations, memory-as-metabolism-mirror-vs-compensate]
---

## 解决的问题：外部源没有"唯一正确压缩"

Miteski (2026) 把 CONTEXTUALIZE 作为五操作之一**独立**地从 TRIAGE 拆出来，理由是同一份外部文档（如架构决策记录）对 Product Owner 和 Developer 来说应该有**不同的有用摘要**——前者要目标 / 权衡 / 利益相关方理由，后者要实现约束 / 库选型 / edge cases。**两者都不是错的，只是当前工作深度不同**——论文称之为 "contextually correct compressions"。

> "A naive ingestion pipeline that compresses external sources to some imagined complete representation pays a double cost. It bloats the wiki with content the user does not need, and it makes the wiki harder to consolidate against because the entries are too long to participate cleanly in coherence operations."[^1]

## 三条不可让渡的设计承诺

1. **强制 linkout 到原始源（§7.5 conformance MUST）**：原文必须可恢复——当用户 context shift 时（例如从 PO 变 EM），下一个 dream cycle 用**新** context 重压缩原文。「MUST preserve a linkout to the original external source — this is non-optional and cannot be traded off for storage efficiency.」[^2]
2. **在 dream cycle 里跑，不在 streaming ingestion**：深度推断成本高，必须批量 + sleep 调度。raw buffer 把外部源原样留到下一个 cycle，**也是安全属性**——若用户 context 在 ingestion 与 consolidation 之间漂移，consolidation 时用的是**新** context。
3. **depth 由推断而非用户显式声明**：让用户对每条 ingested source 都标 working depth 是"operationally absurd"。系统从用户其它 wiki 条目、最近查询模式、主题邻域推断——与 memory gravity 同源的推断动作。**推断会错**——这正是为何 linkout 不可让渡。

## 三层存储模型（CONTEXTUALIZE 引入的第三层）

CONTEXTUALIZE 直接催生一个新存储层：**cold memory**。

- **raw buffer**：TRIAGE 通过的待 consolidate 条目；
- **active wiki**：depth-fitted 后的工作表示；
- **cold memory**：CONTEXTUALIZE 处理过的**原始外部源**，高容量 / 低访问频率；正常操作不检索，只有"working representation 需要按新 context 重压缩"时才召回。

这三层把 linkout 承诺**结构化**为存储义务，而不是"靠实现纪律保证不删除"。

## 与 D-Mem 的差别（论文唯一的最近邻 prior art）

D-Mem (You, Yuan, Cai, arXiv 2603.18631) 有 dual-process：快速检索路径 + Full Deliberation 回退到原始 dialogue，由 learned Quality Gating 决定何时切换。CONTEXTUALIZE 与之不同在两点：
- **压缩深度在 integration 之前就决定**，不是检索时反应式切换；
- **深度从 wiki topology + query 行为推断**，不仅仅从单次 retrieval query 推断。

> "The coordination bundle—depth inference from user context, compression fitted to that depth, originals preserved as a structural non-optional commitment, deferred to the dream cycle rather than run at streaming ingestion—is what prior work does not assemble together."[^3]

## metabolic 比喻

生物细胞**不**吸收环境里所有东西，只吸收当前代谢状态能