---
id: three-tier-storage-model
title: 三层存储架构
status: draft
card_type: architectural-pattern
tags: [cold-memory, raw-buffer, active-wiki, storage-tiers, companion-memory]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
evidence_basis: theoretical_paper
justification: ../justification/three-tier-storage-model.md
canonical_concept: three-tier-storage-model
aliases: [three-tier architecture, cold memory raw buffer active wiki, 三层存储, 冷记忆, 原始缓冲区, 活跃维基]
summary: >-
  three-tier storage model 三层存储架构由冷记忆（原始外部源，高容量低访问频率）、
  原始缓冲区（待巩固条目，短期）、活跃维基（深度拟合工作表示，长期）组成。
  冷记忆由 CONTEXTUALIZE 在产出深度拟合工作表示时创建，保存已处理源的原始内容。
  冷记忆条目仅在用户或 CONSOLIDATE 周期判定工作表示需对新语境重压缩时被检索。
  此架构使存储义务显式化而非让它们作为链出保留的隐含后果。
related: [contextualize-operation, sleep-consolidation-architecture]
---

三层存储架构使框架的存储义务显式化：[^src-1]

1. **冷记忆**（cold memory）：已被维基处理的外部源原始内容的高容量、低访问频率存储。条目仅在用户或 CONSOLIDATE 周期判定工作表示需对新语境重压缩时被检索。
2. **原始缓冲区**（raw buffer）：短期存储，保存通过 TRIAGE 但待巩固的条目。
3. **活跃维基**（active wiki）：长期存储，保存深度拟合的工作表示。

冷记忆对象由 CONTEXTUALIZE 创建——当它产出深度拟合工作表示时，原始外部源移入冷记忆。原始是不可变的。重压缩创建新的冷记忆对象并更新活跃维基条目的 commit hash——先前冷记忆对象被保留而非覆盖。[^src-2]

不变量：每个冷记忆对象 MUST 维护到其原始源的有效链出——这是 CONTEXTUALIZE 在计划巩固中处理外部源时做出的非可选承诺。任何操作 MUST NOT 永久删除任何对象——终端状态为 archived 或 expired，从不硬删除。[^src-3]

[^src-1]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.4 CONTEXTUALIZE" P6 -- "The three-tier architecture --- cold memory (originals), raw buffer (pending consolidation), active wiki (depth-fitted working representations) --- makes the storage obligations explicit"
[^src-2]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "4. System Model" -- "Cold memory objects are created by CONTEXTUALIZE...Re-compression creates a new cold memory object and updates the active wiki entry's commit hash --- the prior cold memory object is retained, not overwritten."
[^src-3]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "4. Required invariants" -- "Every cold memory object MUST maintain a valid linkout to its original source...No operation MUST permanently delete any object"

[^card-1]: contextualize-operation — 三层存储由 CONTEXTUALIZE 引入以支持深度拟合压缩
