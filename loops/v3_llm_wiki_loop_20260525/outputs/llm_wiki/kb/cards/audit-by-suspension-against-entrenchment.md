---
id: audit-by-suspension-against-entrenchment
title: AUDIT-by-Suspension：用反事实悬挂剥离"结构显著但功能空洞"的高引力条目
status: accepted
card_type: mechanism
tags: [#memory, #audit, #entrenchment, #kuhn]
created_time: 2026-05-26T11:20:00+08:00
edited_time: 2026-05-28T11:26:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
provenance_card: ../provenance/audit-by-suspension-against-entrenchment.md
aliases: [AUDIT operation, structural stress test, gravity-reduction path, Kuhnian discipline at entry level]
related: [memory-gravity-load-bearing-protection, memory-as-metabolism-five-operations, memory-as-metabolism-conflict-routing-matrix, memory-as-metabolism-mirror-vs-compensate, minority-pressure-promotion]
---

## AUDIT 做什么

Miteski (2026) 把 AUDIT 定义为**慢周期**（月度或更长）的结构性压力测试[^src1]。它**不是真理校正**，而是测试"高 gravity 条目是否仍然对当前 agent 操作承重"[^v3-1]。伪代码原文（§5.8）：

```
FOR each entry in top_N_by_gravity:
    suspend from active wiki
    run N queries that previously accessed this entry
    IF query performance degrades:   restore, confirm gravity
    IF query performance unchanged:  reduce gravity — entry is dead weight
    IF query performance improves:   archive — entry was actively interfering
```

关键设计点：

- **temporary suspension**，永不 hard-delete（§7.5 conformance）。
- 用历史上**真实访问过**该条目的查询子集做 stress-test，避免人造 query 偏置。
- 三分支结果直接映射到 gravity / lifecycle 决策：恢复、削 gravity、归档。

## 为什么这是 Kuhn 问题的"入条目"版本

库恩（1962）描述的"常规科学"失效模式：范式自我强化，正是因为它**组织了**新证据的解释方式，异常被归到外围当例外，直到累积到强迫范式转移。**没有 AUDIT 的 wiki 在结构上与"没有危机压力的常规科学"等价**——以"未处理异常的债务"为代价持续积累 coherence。

> "AUDIT does not resolve the Kuhnian tension; it makes the cost of unaddressed anomalies visible at the entry level rather than letting it accumulate invisibly at the wiki level."

文中引用 Wikipedia 概念网络的 Kuhnian 范式经验化（[18]）：那是**回溯**识别范式结构；AUDIT 把这个逻辑扩展为**前向、性能驱动**的入条目 stress-test，让异常债务在被迫范式转移之前可见。

## ShortGPT 类比：结构居中 ≠ 功能必要

Men 等 (ShortGPT, arXiv:2403.03853) 显示 transformer 层中 Block Influence 分数低（衡量层对输入的变换强度）的层，**即便位置居中**，删除后性能几乎无损。这是与 AUDIT 同方向的独立证据：**位置中心性不可靠地预测功能必要性**。AUDIT 在知识条目层级做同样的动作——高 gravity 是结构代理，不是功能测量，只有反事实悬挂能揭示二者之差。

## 失效模式与 §9 的诚实承认

AUDIT 灵敏度是论文承认的**最关键开放问题**：

- 若 stress-test 查询集过窄或自我确认，**有害的中心节点会逃过测试**继续受保护。
- "We do not solve this. We flag it as the specific direction where the compensate side of the framework most needs work."

这意味着 gravity 立保护、minority pressure 给反对证据通道、AUDIT 剥离失效保护——三者共同构成的"compensate 故事"是**部分而非完整**的。论文反复强调：framework **不消除**对错误信念的强化，但把这种强化**结构化、可见、可独立改进**。

## 在 §5.0 冲突路由矩阵中的角色

AUDIT 是矩阵的**决胜者**：当 mirror 与 compensate 在调度窗口内仍未解决（比如 row 6：高 gravity 条目在多个 AUDIT 周期反复与坏结果相关），AUDIT override 强制走 §5.8 的 gravity-reduction 通路——条目通过 **AUDIT 通道**失去保护，而不是通过 CONSOLIDATE 通道。这是 governance 层结构的关键：当流式 + 调度都没能纠正一个错误的承重条目，最后一道防线是 AUDIT 的强制悬挂。

## References

- 第 1555–1604 行：§5.8 AUDIT 伪代码、Kuhn 类比、ShortGPT 类比、灵敏度承认。
- 第 1113 行：§5.0 冲突路由矩阵第 6 行（high-gravity entry implicated in repeated poor outcomes → AUDIT override）。
- 第 1944–1951 行：§7.5 AUDIT MUST 列表（temporary suspension、minority branch 关闭规则）。
- 第 2168–2174 行：§9 limitations 中 AUDIT 灵敏度作为"the critical open problem"。
- 来源：`data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt`。

## Footnotes

[^1]: 伪代码原文 verbatim 出现在第 1563–1570 行（§5.8 块）。

[^2]: AUDIT 不解决 Kuhn 张力但把代价"按条目"可见化原文（第 1583–1589 行）："AUDIT does not resolve the Kuhnian tension; it makes the cost of unaddressed anomalies visible at the entry level rather than letting it accumulate invisibly at the wiki level."

[^3]: ShortGPT 类比原文（第 1611–1622 行）："Men et al.'s ShortGPT (arXiv 2403.03853) shows that transformer layers with low Block Influence scores ... can be removed with minimal performance loss, even when those layers are structurally central. The result inverts naive gravity: positional centrality in a sequential network does not reliably predict functional necessity. AUDIT makes the same move at the knowledge-entry level."
