---
id: triage-shallow-filter
title: TRIAGE 浅层过滤器
status: accepted
card_type: operational_rule
tags: [companion-memory, triage, ingestion, conformance, anti-self-sealing]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
justification: ../justification/triage-shallow-filter.md
canonical_concept: triage-shallow-filter
aliases: [TRIAGE 浅层过滤, triage shallow filter, 浅层摄取过滤, streaming shallow filter]
summary: >-
  triage-shallow-filter（TRIAGE 浅层过滤 / streaming shallow filter）是伴侣记忆框架中摄取操作的合规级别约束：TRIAGE 只做垃圾拒绝、去重、结构验证、时间戳分配，禁止读取活跃 wiki 或执行语义矛盾解决；一旦 TRIAGE 开始做一致性工作，架构就退回流式模式、自密封问题回归
related: [sleep-consolidation-architecture, ingest-operation, companion-knowledge-system]
---

TRIAGE 是伴侣记忆框架中在摄取阶段运行的浅层过滤操作，其职责被刻意限制[^src-1]：

**允许的操作**：拒绝明显垃圾、对近期缓冲区去重、检查结构有效性、分配摄取时间戳。仅此而已。

**禁止的操作**：TRIAGE 不分类条目到一致性桶中，不对活跃 wiki 评分，不做保留决策[^src-2]。通过 TRIAGE 的一切进入原始缓冲区，等待下一个整合周期。

**这是设计承诺而非优化**：TRIAGE 开始做一致性工作的那一刻，架构就退回流式模式，自密封问题回归[^src-3]。

**合规不变量**（Section 7.5）[^src-4]：
- 禁止执行语义矛盾解决
- 必须在写入缓冲区前分配稳定的内容哈希 ID 和摄取时间戳
- 必须对相同输入内容幂等：相同内容哈希不产生重复缓冲区条目
- 禁止直接写入活跃 wiki
- 禁止在摄取期间读取活跃 wiki

**实现判别标准**：如果一个实现的 TRIAGE 操作曾经读取活跃 wiki 或对现有 wiki 内容评分条目，则该实现不合规——无论其特定测试用例的结果看起来是否正确[^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.2" -- "TRIAGE runs at ingestion. Its job is deliberately limited: reject obvious garbage, deduplicate against the recent buffer, check structural validity, assign an ingestion timestamp. That is all."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.2" -- "TRIAGE does not classify entries into cohesion buckets, does not score them against the active wiki, and does not make retention decisions."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.2" -- "Keeping TRIAGE shallow is a design commitment. The moment TRIAGE starts doing coherence work, the architecture collapses back to streaming and the self-sealing problem returns."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 7.5" -- "TRIAGE - MUST NOT perform semantic contradiction resolution... MUST NOT read the active wiki during ingestion"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Trace 2" -- "If an implementation's TRIAGE operation ever reads the active wiki or scores entries against existing wiki content, it is non-conforming --- regardless of whether its outcomes look correct in a given test case."
