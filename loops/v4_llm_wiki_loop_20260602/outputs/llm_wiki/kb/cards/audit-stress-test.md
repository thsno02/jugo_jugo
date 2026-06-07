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
related: [chaos-monkey-agent-stress-testing, circularity-as-thesis, companion-conformance-invariants, continuous-drift-detection, entrenchment-under-user-coupled-drift, lint-operation, memory-gravity, minority-pressure-promotion, mirror-vs-compensate-principle, spec-driven-conformance-testing]
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

AUDIT 是循环性论题的操作兑现——框架接受镜像侧的循环性，但依赖 AUDIT 等补偿机制来兑现「循环性是特征而非缺陷」的承诺[^card-1]。AUDIT 针对的核心失败模式正是用户耦合漂移下的固化：知识库退化为范式维护系统[^card-2]。作为减法机制（悬挂后观察性能），AUDIT 与少数派压力提升（加法机制：积累异质证据后挑战在位者）形成互补的反固化策略[^card-3]。

AUDIT 操作必须在合规不变量约束下运行——如禁止永久删除对象、操作于定义快照等边界条件[^card-4]。AUDIT 的内省式减法（移除后观察退化）与混沌工程的外部扰动注入（注入噪声后观察存活）代表了两种截然不同的压力测试范式[^dist-1]。规范驱动的合规测试从正确性维度提供互补保障——合规测试验证实现是否符合 RFC 2119 规范，AUDIT 验证知识条目是否仍然承重，两者分别回答"是否正确"与"是否有用"[^card-5]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.8" -- "AUDIT runs on a slow cycle (monthly or longer). It temporarily suspends the highest-gravity entries and observes whether query performance degrades"
[^src-2]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.8" -- "FOR each entry in top_N_by_gravity: suspend from active wiki..."
[^src-3]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.8" -- "Kuhn's account of normal science describes exactly the failure mode that AUDIT is designed to interrupt: a paradigm becomes self-reinforcing precisely because it organizes how new evidence is interpreted"
[^src-4]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.8" -- "AUDIT is not a truth-correction mechanism. It tests whether high-gravity entries are still load-bearing for the agent's current operation."
[^src-5]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.8" -- "ShortGPT (arXiv 2403.03853) shows that transformer layers with low Block Influence scores... can be removed with minimal performance loss, even when those layers are structurally central."
[^src-6]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 9" -- "AUDIT sensitivity is the critical open problem."
[^card-1]: [循环性作为论题](circularity-as-thesis.md) -- 本卡是补偿侧的操作机制，该卡提出接受镜像侧循环性并依赖补偿侧抵抗失败模式的哲学立场
[^card-2]: [用户耦合漂移下的固化](entrenchment-under-user-coupled-drift.md) -- 本卡通过经验性悬挂检测死权重和主动干扰，该卡描述本机制针对的核心失败模式：知识库退化为范式维护系统
[^card-3]: [少数派压力提升机制](minority-pressure-promotion.md) -- 本卡通过悬挂测试功能必要性（减法策略），该卡通过积累异质证据挑战在位者（加法策略），两者互补构成反固化双支柱
[^card-4]: [伴侣系统合规不变量](companion-conformance-invariants.md) -- 本卡描述 AUDIT 的悬挂测试机制，该卡定义 AUDIT 必须遵守的合规不变量边界（如禁止永久删除、操作于定义快照）
[^card-5]: [规范驱动的合规测试](spec-driven-conformance-testing.md) -- 本卡通过经验性悬挂验证知识条目的功能效用性（是否仍然承重），该卡通过 RFC 2119 合规测试验证实现的规范正确性（是否符合规范）；两者从效用性和正确性两个维度互补覆盖质量保障
[^dist-1]: [Chaos Monkey 式 Agent 压力测试](chaos-monkey-agent-stress-testing.md) -- 本卡通过内省式减法测试知识条目的功能必要性（悬挂后观察退化），该卡通过环境扰动测试 agent 的操作鲁棒性（注入噪声后观察存活）；区分点在于压力来源与方向——内部移除 vs 外部扰动
