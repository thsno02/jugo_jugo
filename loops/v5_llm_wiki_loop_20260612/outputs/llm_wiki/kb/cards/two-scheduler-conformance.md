---
id: two-scheduler-conformance
title: 双调度器架构一致性要求
status: accepted
card_type: implementation-commitment
tags:
- two-scheduler
- hot-path
- sleep-cycle
- latency
- conformance
- companion-memory
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-memory-as-metabolism
evidence_basis: theoretical_paper
justification: ../justification/two-scheduler-conformance.md
canonical_concept: two-scheduler-conformance
aliases:
- two-scheduler architecture
- hot-path scheduler
- sleep-cycle scheduler
- 双调度器架构
- homeostasis-driven scheduling
summary: two-scheduler conformance 双调度器架构是伴侣记忆框架的一致性级实现承诺。 运行时分为两个具有不同延迟要求的调度器：热路径调度器门控 TRIAGE 和检索读取（在对话延迟预算内完成）； 睡眠周期调度器将 DECAY、CONSOLIDATE、AUDIT 作为后台作业排队。 将两者混为一个调度器是最常见的天真实现失败：睡眠操作窃取热路径延迟，或热路径要求使睡眠操作永久推迟。
  在 CONSOLIDATE 或 AUDIT 运行期间阻塞对话的实现是不一致的（无论正确性如何）。 睡眠调度由稳态层（homeostasis layer）驱动而非 cron：读取交互近期性、热状态、电池轨迹、存储压力等状态向量。
related:
- sleep-consolidation-architecture
- triage-operation
- consolidate-operation
---

双调度器架构是一致性级实现承诺——违反它即破坏治理合约。[^src-1]

运行时分为两个调度器：
- **热路径调度器**：门控 TRIAGE 和检索读取，必须在用户对话延迟预算内完成
- **睡眠周期调度器**：将 DECAY、CONSOLIDATE、AUDIT 作为后台作业排队 [^src-2]

将两者混为单一调度器是最常见的天真实现失败：睡眠周期操作窃取热路径延迟，或热路径延迟要求导致睡眠周期操作永久推迟。[^src-3]

一致性边界：在 CONSOLIDATE 或 AUDIT 运行期间阻塞对话的实现是不一致的，无论其正确性如何。活跃维基 MUST 在任何 CONSOLIDATE 或 AUDIT 运行期间保持可读——读路径上无阻塞锁。[^src-4]

睡眠调度由稳态层（homeostasis layer）驱动而非 cron：读取状态向量（交互近期性、热状态、电池轨迹、存储压力、用户下一活跃会话窗口的可用信号）。如果系统可推断用户 8 AM 离开且巩固需 30 分钟，4:45 AM 是计算窗口而非固定夜间定时器。这是反应式调度与预期式稳态之间的区别。[^src-5]

[^src-1]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "6.1 Implementation commitments" P1 -- "The first two --- two-scheduler architecture and homeostasis-driven sleep scheduling --- are conformance-level: an implementation that violates them breaks the governance contract."
[^src-2]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "6.1" P2 -- "The hot-path scheduler gates TRIAGE and retrieval reads...The sleep-cycle scheduler queues DECAY, CONSOLIDATE, and AUDIT as background jobs."
[^src-3]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "6.1" P2 -- "Conflating these into a single scheduler is the most common naive implementation failure"
[^src-4]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "6.1" P2 -- "an implementation that blocks conversation during CONSOLIDATE is non-conforming regardless of correctness"
[^src-5]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "6.1" P3 -- "Sleep-cycle operations are scheduled by a homeostasis layer reading a state vector...This is the difference between reactive scheduling and anticipatory homeostasis"

[^card-1]: sleep-consolidation-architecture — 双调度器是睡眠巩固架构的实现要求
[^card-2]: triage-operation — TRIAGE 在热路径调度器中运行
[^card-3]: consolidate-operation — CONSOLIDATE 在睡眠周期调度器中运行
