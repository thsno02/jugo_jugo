---
id: consolidate-operation
title: CONSOLIDATE 批量深度整合操作
status: draft
card_type: operation-specification
tags: [consolidate, batch-integration, coherence, minority-pressure, companion-memory]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
evidence_basis: theoretical_paper
justification: ../justification/consolidate-operation.md
canonical_concept: consolidate-operation
aliases: [CONSOLIDATE, batched deep integration, 巩固操作, 批量整合]
summary: >-
  CONSOLIDATE 是伴侣记忆框架的核心补偿机制，在计划周期中对原始缓冲区和活跃维基一同运行。
  四阶段：(1) 缓冲区内部评分（使少数压力可见）；(2) 维基评分（语义一致性、任务对齐、矛盾成本）；
  (3) 分类路由（梯形隶属函数的模糊一致性梯度）；(4) 少数压力晋升。
  一致性不变量：MUST 在对维基评分之前先做缓冲区内部评分、操作于定义快照、每次运行最多一个 Git commit、
  MUST NOT 永久丢弃少数假说、所有边更新原子写入。
  已知局限：批量巩固也可能放大相关噪声而非真正修正——互相支持但错误的条目可挑战正确的主导解释。
related: [sleep-consolidation-architecture, minority-hypothesis-retention, memory-gravity-mechanism]
---

CONSOLIDATE 是框架的核心补偿机制，在计划周期中对原始缓冲区和活跃维基一同运行。[^src-1]

四阶段：
1. 缓冲区内部评分——每个缓冲区条目对其他缓冲区条目评分（相互支持与矛盾），独立于活跃维基。这是累积少数压力变得可见之处。
2. 维基评分——每个缓冲区条目对活跃维基评分（语义一致性、任务对齐、与高引力节点的矛盾成本）。
3. 分类路由——使用梯形隶属函数将条目放置在模糊一致性梯度上：高一致性直接整合，中一致性标记关注，低一致性隔离。
4. 少数压力晋升——个别矛盾维基但在缓冲区中相互支持的条目被标记为主导解释更新候选，而非隔离。[^src-2]

一致性不变量：MUST 在对维基评分之前先做缓冲区内部评分（跳过此步重引入自封闭失败模式）；操作于定义快照（特定 Git commit hash + 元数据索引高水位）；在固定模型版本下可复现；每次运行最多产出一个 Git commit；MUST NOT 永久丢弃少数假说；所有边更新原子写入。[^src-3]

已知局限：批量巩固也可能放大相关噪声——多个相互支持但错误的条目可能积累足够缓冲区压力挑战正确的主导解释。CONSOLIDATE 是反僵化的，非保真的。[^src-4]

[^src-1]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.5 CONSOLIDATE" P1 -- "CONSOLIDATE is the framework's central compensate mechanism. It runs on a schedule against the raw buffer and the active wiki together."
[^src-2]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.5" P2-5 -- "Buffer-internal scoring...Wiki scoring...Classification and routing...Minority-pressure promotion"
[^src-3]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "7.5 Conformance CONSOLIDATE" -- "MUST score buffer entries against each other before scoring against the active wiki...MUST produce at most one Git commit per run"
[^src-4]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.5" P6 -- "Batched consolidation can also amplify correlated noise rather than genuine correction...CONSOLIDATE is therefore anti-entrenchment, not truth-guaranteeing."

[^card-1]: sleep-consolidation-architecture — CONSOLIDATE 是睡眠巩固架构中"深度整合工作"的具体操作
[^card-2]: minority-hypothesis-retention — 少数压力晋升是 CONSOLIDATE 第四阶段的核心功能
