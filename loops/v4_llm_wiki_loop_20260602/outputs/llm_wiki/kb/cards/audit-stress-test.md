---
id: audit-stress-test
title: AUDIT 结构性压力测试
status: accepted
card_type: mechanism
tags: [companion-memory, audit, stress-test, kuhnian, anti-entrenchment, suspension]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
justification: ../justification/audit-stress-test.md
canonical_concept: audit-stress-test
aliases: [AUDIT 压力测试, audit stress test, 结构性悬挂测试, suspension-based audit, 库恩式审计]
summary: >-
  audit-stress-test（AUDIT 压力测试 / suspension-based audit / 库恩式审计）是伴侣记忆框架中运行于慢周期（月度+）的补偿机制：临时悬挂最高引力条目，运行历史查询测试性能影响；三种结果——性能下降则恢复、不变则降低引力（死权重）、改善则归档（主动干扰）；目标是中断库恩式范式僵化
related: [memory-gravity, lint-operation, continuous-drift-detection, mirror-vs-compensate-principle]
---

AUDIT 是伴侣记忆框架中运行于慢周期（月度或更长）的结构性压力测试操作[^src-1]。它是框架对教条的主要防御——通过经验性悬挂而非语义判断来检测高引力条目是否仍然是功能性承重的。

**操作流程**[^src-2]：
```
对于 top_N_by_gravity 中的每个条目：
    从活跃 wiki 悬挂
    运行之前访问过该条目的 N 个查询
    如果查询性能下降：恢复，确认引力
    如果查询性能不变：降低引力——条目是死权重
    如果查询性能改善：归档——条目在主动干扰
```

**库恩式解读**：AUDIT 旨在中断的恰恰是库恩描述的正常科学失败模式——范式因组织了新证据的解释方式而自我强化，异常被路由到外围作为例外、测量误差或"未来工作"[^src-3]。没有 AUDIT 的 wiki 在结构上类似于没有危机压力的正常科学——以积累未解决异常的债务为代价来积累一致性。

**AUDIT 不是真理纠正机制**：它测试的是高引力条目是否仍然对代理的当前操作具有承重作用[^src-4]。曾经核心但代理已经超越的条目变成死权重；主动干扰当前查询的条目被归档。

**与 ShortGPT 的类比**：Men et al. 的 ShortGPT 表明 Block Influence 分数低的 transformer 层可以在最小性能损失下移除，即使这些层在结构上是中心的。这颠覆了朴素引力：位置中心性不能可靠预测功能必要性[^src-5]。AUDIT 在知识条目层面做了同样的事情。

**关键开放问题**：AUDIT 的灵敏度是框架最关键的未解决问题。如果用于压力测试的查询集过窄或自确认，有害的中心节点仍受保护[^src-6]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.8" -- "AUDIT runs on a slow cycle (monthly or longer). It temporarily suspends the highest-gravity entries and observes whether query performance degrades"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.8" -- "FOR each entry in top_N_by_gravity: suspend from active wiki..."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.8" -- "Kuhn's account of normal science describes exactly the failure mode that AUDIT is designed to interrupt: a paradigm becomes self-reinforcing precisely because it organizes how new evidence is interpreted"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.8" -- "AUDIT is not a truth-correction mechanism. It tests whether high-gravity entries are still load-bearing for the agent's current operation."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.8" -- "ShortGPT (arXiv 2403.03853) shows that transformer layers with low Block Influence scores... can be removed with minimal performance loss, even when those layers are structurally central."
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 9" -- "AUDIT sensitivity is the critical open problem."
