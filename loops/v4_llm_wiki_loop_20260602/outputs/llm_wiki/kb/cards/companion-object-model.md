---
id: companion-object-model
title: 伴侣系统对象模型
status: accepted
card_type: concept
tags: [companion-memory, object-model, entities, lifecycle, state-transitions]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
justification: ../justification/companion-object-model.md
canonical_concept: companion-object-model
aliases: [伴侣系统对象模型, companion object model, 伴侣实体模型, companion entity model, 系统模型]
summary: >-
  companion-object-model（伴侣系统对象模型 / companion entity model）伴侣记忆框架定义的五种核心实体及其生命周期状态：原始缓冲区条目（pending→consolidated/rejected/expired）、活跃 wiki 条目（active→decaying→archived，带 gravity-protected/quarantined 正交标志）、冷存储对象、审计记录、少数派分支；所有操作读写这些实体，合规测试依赖这些对象边界
related: [companion-knowledge-system, companion-conformance-invariants, memory-lifecycle-metadata]
---

伴侣记忆框架在 Section 4 定义了操作所作用的对象模型——所有操作读取和写入这些实体，合规测试依赖这些对象边界[^src-1]。

**五种核心实体**[^src-2]：

1. **原始缓冲区条目**（Raw buffer entry）
   - 生命周期：pending → consolidated / rejected / expired
   - 必需字段：稳定 ID（内容哈希）、摄取时间戳、来源指针（Git blob 哈希）、来源通道、初始优先级
   - 由 TRIAGE 创建，由 CONSOLIDATE 消费

2. **活跃 wiki 条目**（Active wiki entry）
   - 生命周期：active → decaying → archived
   - 正交状态标志：gravity-protected（由 DECAY/AUDIT 设置）、quarantined（由 CONSOLIDATE 设置）
   - 由 CONSOLIDATE 创建，由 DECAY 和 AUDIT 修改
   - **永不删除**——archived 是终态，完整内容移至冷存储

3. **冷存储对象**（Cold memory object）
   - 生命周期：stored → recalled → re-compressed
   - 必须维护到原始来源的有效链接（非可选承诺）

4. **审计记录**（Audit record）
   - 生命周期：created → closed
   - 必须仅追加——创建后不可修改

5. **少数派分支**（Minority branch）
   - 生命周期：open → promoted → closed
   - 关闭仅通过两条显式路径：通过 CONSOLIDATE 提升（集群跨过提升阈值），或 AUDIT 触发的归档

**关键状态规则**：gravity-protected 和 quarantined 是状态标志而非生命周期阶段——条目可以同时是 active 和 gravity-protected，也可以同时是 decaying 和 quarantined[^src-3]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 4" -- "Before specifying operations, the framework names the objects those operations act on... Naming them explicitly is what allows conformance to be tested"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 4" -- Core entities table
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 4" -- "gravity-protected and quarantined are status flags, not lifecycle stages. An entry can be active and gravity-protected simultaneously."
