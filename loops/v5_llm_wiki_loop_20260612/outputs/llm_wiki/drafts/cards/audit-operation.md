---
id: audit-operation
title: AUDIT 结构压力测试操作
status: draft
card_type: operation-specification
tags: [audit, stress-test, suspension, kuhn-problem, companion-memory, conformance]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
evidence_basis: theoretical_paper
justification: ../justification/audit-operation.md
canonical_concept: audit-operation
aliases: [AUDIT, structural stress test, 审计操作, 结构压力测试]
summary: >-
  AUDIT 是伴侣记忆框架的慢周期补偿操作，通过临时悬挂最高引力条目并观察查询性能来压力测试。
  三种结果：性能退化则恢复并确认引力；性能不变则减少引力（死重）；性能改善则归档（主动干扰）。
  AUDIT 不是真值修正机制，它测试高引力条目是否仍为代理当前运行的负载承载。
  作为框架对 Kuhn 问题的主要防御——使累积异常债务在条目级别可见而非在维基级别隐性积累。
  AUDIT 敏感度是关键开放问题——如果压力测试查询集狭窄或自确认，僵化存活。
related: [memory-gravity-mechanism, consolidate-operation, minority-hypothesis-retention]
---

AUDIT 在慢周期（月度或更长）运行。它临时悬挂最高引力条目并观察查询性能是否退化。[^src-1]

三种结果路径：
- 查询性能退化 → 恢复，确认引力
- 查询性能不变 → 减少引力——条目为死重
- 查询性能改善 → 归档——条目在主动干扰 [^src-2]

AUDIT 不是真值修正机制。它测试高引力条目是否仍为代理当前运行的负载承载。曾经中心但代理已超越的条目变为死重。[^src-3]

AUDIT 操作化了 Kuhnian 学科：Kuhn 的正常科学描述了 AUDIT 设计所要中断的失败模式——范式变得自我强化，异常被路由到外围。无 AUDIT 的维基结构上类似于无危机压力的正常科学。AUDIT 使未解决异常的成本在条目级别可见，而非在维基级别隐性积累。[^src-4]

一致性不变量：MUST 通过临时悬挂而非永久删除操作；MUST 恢复悬挂后证明性能退化的条目；MUST NOT 关闭少数分支除非满足晋升或明确归档条件；MUST 在执行任何状态转换前将所有结果写入审计记录。[^src-5]

AUDIT 敏感度是框架的关键开放问题——如果压力测试查询集狭窄或自确认，有害中心节点保持保护。[^src-6]

[^src-1]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.8 AUDIT" P1 -- "AUDIT runs on a slow cycle (monthly or longer). It temporarily suspends the highest-gravity entries and observes whether query performance degrades"
[^src-2]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.8" P1 -- "IF query performance degrades: restore, confirm gravity / IF query performance unchanged: reduce gravity / IF query performance improves: archive"
[^src-3]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.8" P2 -- "AUDIT is not a truth-correction mechanism. It tests whether high-gravity entries are still load-bearing for the agent's current operation."
[^src-4]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.8" P3 -- "Kuhn's account of normal science describes exactly the failure mode that AUDIT is designed to interrupt"
[^src-5]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "7.5 Conformance AUDIT" -- "MUST operate by temporary suspension, not permanent deletion...MUST restore entries whose suspension demonstrably degrades query performance"
[^src-6]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.8" P5 -- "AUDIT sensitivity is an open problem. If the query set used for stress testing is narrow or self-confirming, harmful central nodes stay protected."

[^card-1]: memory-gravity-mechanism — AUDIT 是唯一能剥夺高引力条目保护的机制
[^card-2]: consolidate-operation — AUDIT 与 CONSOLIDATE 在关闭少数分支时协作
