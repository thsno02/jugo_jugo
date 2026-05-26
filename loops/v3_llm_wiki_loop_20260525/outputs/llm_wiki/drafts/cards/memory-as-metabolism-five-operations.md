---
id: memory-as-metabolism-five-operations
title: 伴侣记忆的五操作架构（TRIAGE / CONTEXTUALIZE / DECAY / CONSOLIDATE / AUDIT）
status: draft
card_type: mechanism
tags: [#memory, #architecture, #consolidation, #sleep-cycle]
created_time: 2026-05-26T11:05:00+08:00
edited_time: 2026-05-26T11:05:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
provenance_card: ../provenance/memory-as-metabolism-five-operations.md
aliases: [five-op retention policy, sleep-function architecture, TRIAGE-CONSOLIDATE-AUDIT]
related: [memory-as-metabolism-mirror-vs-compensate, memory-gravity-load-bearing-protection]
---

## 五个操作各司其职

Miteski (2026) 把 companion wiki 的保留/治理层切成 5 个操作 + 2 个支撑机制，每个都有明确的运行节奏与失败模式：

1. **TRIAGE（流式、毫秒级）**：浅过滤——拒绝明显垃圾、对最近 buffer 去重、检查结构合法性、打 ingestion 时间戳。**不做任何语义评分、不读 active wiki、不做留弃决策**。所有通过 TRIAGE 的条目进入 raw buffer 等下一个 consolidation 窗口。
2. **CONTEXTUALIZE（批量、调度内）**：把外部源压缩到"用户当前 working-context depth"的工作表示，并强制保留到原始源的 linkout。它**只在 dream cycle 里运行**，因为深度推断成本高；同一份外部源若用户上下文在两个 cycle 之间漂移，下一次按新上下文重压缩。
3. **DECAY（持续）**：在 active wiki 上跑 vitality 公式（见下）；vitality 低于阈值的条目**被压缩成 summary，不是删除**。
4. **CONSOLIDATE（批量、调度内）**：本框架的中心 compensate 机制，分四个 phase——buffer 内部互评、与 active wiki 评分、按 fuzzy coherence 分桶（直接整合 / 标记关注 / 隔离）、少数派 buffer 压力 promotion。
5. **AUDIT（慢周期、月度或更长）**：对最高 gravity 条目做"暂时悬挂 + 重跑历史查询"的反事实测试。性能未变就削 gravity；性能改善就归档。

支撑机制：**memory gravity**（承重保护）与 **minority-hypothesis retention**（buffer/quarantine 中保留方差）。

## vitality 公式（DECAY 用）

```
vitality(entry) =
    recency_weight   * (1 / days_since_access)
  + frequency_weight * access_count
  + utility_weight   * task_predictive_utility(entry)
  + gravity_weight   * memory_gravity(entry)
  - wear_penalty     * summarization_distortion(entry)
```

`task_predictive_utility` 是"按这条记忆行动后用户判定的有用性"。gravity 项是防止 vitality 退化成"满意度追逐"的关键——结构承重的条目即便很少直接产生效用也会被保留。

## sleep-function 架构的设计理由

为什么要把 streaming ingestion 与 deep integration 拆开？因为**流式 coherence 是自封闭的**：一条孤立到达的反对证据，单独与主导 wiki 比对，**总会**被立即隔离，主导解释永不更新。批量 consolidation 让 buffer 内部多条互相支持的反对证据**作为一个 cluster** 评分，单条隔离的事件变成"积累的 buffer 压力"，少数派从此有结构通道翻盘。

> "Streaming coherence is self-sealing. A single entry arriving alone and scored against the dominant wiki gets quarantined immediately if it contradicts the dominant interpretation, which means the dominant interpretation never updates. Batched consolidation breaks this lock."

## 边界与开放问题

- **CONSOLIDATE 可放大相关噪声**：多条相互支持但同样错误的条目也能积累 buffer 压力。框架明确声明"anti-entrenchment, not truth-guaranteeing"，并提出 source diversity weighting、time-spread requirements、external validation signals 等候选防御但未实现。
- **Valley of Amnesia**：promotion 阈值过早穿越会造成操作连续性的突然丢失，是 transition-stability 层面单独的开放问题。
- **TRIAGE 不能做任何 coherence 工作**：一旦 TRIAGE 开始读 active wiki 或做语义评分，架构立刻退化为流式 coherence，self-sealing 重现。这是 §7.5 conformance 章节的硬性 MUST NOT。

## References

- 第 1004–1070 行：§5.0 五操作总表与角色分配。
- 第 1131–1175 行：§5.1 raw buffer & consolidation cycle；§5.2 TRIAGE。
- 第 1176–1210 行：§5.3 DECAY 与 vitality 公式。
- 第 1320–1383 行：§5.5 CONSOLIDATE 四 phase。
- 第 1555–1604 行：§5.8 AUDIT 伪代码。
- 来源：`data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt`。

## Footnotes

[^1]: TRIAGE 的硬约束原文（第 1898–1904 行 §7.5 conformance）："MUST NOT perform semantic contradiction resolution... MUST NOT read the active wiki during ingestion — any implementation where TRIAGE queries existing wiki content is non-conforming."

[^2]: CONTEXTUALIZE 的 linkout 不可交换原文（第 1906–1912 行）："MUST preserve a linkout to the original external source — this is non-optional and cannot be traded off for storage efficiency."

[^3]: vitality 公式原文出现在第 1184–1191 行（verbatim 块）。
