---
id: triage-operation
title: TRIAGE 流式浅层过滤操作
status: draft
card_type: operation-specification
tags: [triage, streaming-filter, ingestion, companion-memory, conformance]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
evidence_basis: theoretical_paper
justification: ../justification/triage-operation.md
canonical_concept: triage-operation
aliases: [TRIAGE, streaming shallow filter, 分诊操作, 流式浅层过滤]
summary: >-
  TRIAGE 是伴侣记忆框架的流式摄入操作，属于 mirror 机制（中性捕获）。
  职责刻意有限：拒绝明显垃圾、对近期缓冲区去重、检查结构有效性、分配摄入时间戳和内容哈希 ID。
  一致性不变量：MUST NOT 执行语义矛盾解决、MUST NOT 读取活跃维基、MUST NOT 写入活跃维基。
  对相同输入内容幂等。保持 TRIAGE 浅层是设计承诺——一旦 TRIAGE 开始做一致性工作，
  架构坍缩回流式处理，自封闭问题回归。
related: [sleep-consolidation-architecture, mirror-vs-compensate-principle]
---

TRIAGE 在摄入时运行，职责刻意有限：拒绝明显垃圾、对近期缓冲区去重、检查结构有效性、分配摄入时间戳。仅此而已。[^src-1]

TRIAGE 不将条目分类到一致性桶中，不对活跃维基评分，不做保留决策。通过 TRIAGE 的一切进入原始缓冲区并等待下一个巩固周期。[^src-2]

一致性不变量（conformance invariants）：(1) MUST NOT 执行语义矛盾解决；(2) MUST 在写入缓冲区前分配稳定的 content-hash ID 和摄入时间戳；(3) MUST 对相同输入内容幂等；(4) MUST NOT 写入活跃维基；(5) MUST NOT 在摄入期间读取活跃维基。[^src-3]

保持 TRIAGE 浅层是设计承诺——一旦 TRIAGE 开始做一致性工作，架构坍缩回流式处理，自封闭问题回归。这是最常见的天真实现失败模式。[^src-4]

[^src-1]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.2 TRIAGE" P1 -- "TRIAGE runs at ingestion. Its job is deliberately limited: reject obvious garbage, deduplicate against the recent buffer, check structural validity, assign an ingestion timestamp. That is all."
[^src-2]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.2" P2 -- "TRIAGE does not classify entries into cohesion buckets, does not score them against the active wiki, and does not make retention decisions."
[^src-3]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "7.5 Conformance TRIAGE" -- "MUST NOT perform semantic contradiction resolution...MUST NOT read the active wiki during ingestion"
[^src-4]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.2" P3 -- "Keeping TRIAGE shallow is a design commitment. The moment TRIAGE starts doing coherence work, the architecture collapses back to streaming and the self-sealing problem returns."

[^card-1]: sleep-consolidation-architecture — TRIAGE 是睡眠巩固架构中"流式摄入写入缓冲区"的具体操作
