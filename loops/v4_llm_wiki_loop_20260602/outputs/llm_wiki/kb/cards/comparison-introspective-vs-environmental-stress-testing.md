---
id: comparison-introspective-vs-environmental-stress-testing
title: 内省减法 vs 环境扰动：两种 Agent 压力测试范式
status: accepted
card_type: distinction
tags: [stress-testing, comparison, agent-robustness, chaos-engineering, audit, testing-paradigm]
created_time: 2026-06-05T12:00:00+08:00
edited_time: 2026-06-05T12:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism, arxiv-etamp-memory-poisoning]
justification: ../justification/comparison-introspective-vs-environmental-stress-testing.md
canonical_concept: introspective-vs-environmental-stress-testing
aliases: [内省减法vs环境扰动, introspective vs environmental stress testing, subtraction vs perturbation testing]
summary: >-
  两篇独立论文在 agent 压力测试上的范式分歧：伴侣记忆框架的 AUDIT 通过内省式减法（悬挂知识条目后观察查询退化）测试内部知识的功能必要性；eTAMP 的 Chaos Monkey 通过环境扰动注入（点击丢弃、滚动反转、输入变换）测试 agent 的操作鲁棒性。压力来源（内部移除 vs 外部噪声）、测试目标（知识相关性 vs 操作韧性）、时间尺度（月度慢周期 vs 任务执行期间）均不同
related: [audit-stress-test, chaos-monkey-agent-stress-testing]
---

「压力测试」在两篇独立的 agent 研究中被赋予了截然不同的含义，揭示了该概念在 agent 系统中的两种正交范式。

**内省式减法（AUDIT）**[^card-1]：伴侣记忆框架的 AUDIT 操作运行于慢周期（月度+），临时悬挂最高引力的知识条目，然后运行历史查询观察性能是否退化。压力来自内部移除——如果系统在缺少某条目时性能不变甚至改善，说明该条目是死权重或主动干扰。其理论基础是库恩范式理论：高引力条目可能因自我强化而僵化，需要经验性悬挂来打破。

**环境扰动注入（Chaos Monkey）**[^card-2]：eTAMP 论文借鉴 Netflix 混沌工程原理，在 agent 执行任务期间注入概率性扰动（点击丢弃、滚动反转、输入 Caesar 密码变换）。压力来自外部噪声——测试 agent 在环境不可靠时能否仍然完成任务并保持安全特性。

**核心区分维度**：

| 维度 | AUDIT 内省减法 | Chaos Monkey 环境扰动 |
|------|--------------|---------------------|
| 压力来源 | 内部移除（悬挂知识条目） | 外部注入（环境噪声） |
| 测试目标 | 知识功能必要性 | 操作鲁棒性与安全性 |
| 时间尺度 | 慢周期（月度+） | 任务执行期间（实时） |
| 操作方式 | 减法（移除后观察） | 加法（注入后观察） |
| 判断标准 | 性能退化/不变/改善三态 | 任务成功率与步数变化 |
| 理论根基 | 库恩范式理论 | Netflix 混沌工程 |

**互补性**：两种范式并非对立而是互补。一个完善的 agent 测试体系既需要内省减法来防止知识僵化，也需要环境扰动来验证操作韧性。前者回答「系统内部是否有冗余或干扰」，后者回答「系统能否在不可靠环境中存活」。

## Footnotes

[^card-1]: [AUDIT 结构性压力测试](audit-stress-test.md) -- 内省式减法范式的代表：通过悬挂高引力条目测试知识功能必要性
[^card-2]: [Chaos Monkey 式 Agent 压力测试](chaos-monkey-agent-stress-testing.md) -- 环境扰动范式的代表：通过注入操作噪声测试 agent 鲁棒性
