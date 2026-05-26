---
id: minority-pressure-promotion
title: 少数派 buffer 压力 promotion：让多周期累积的反对证据有结构性翻盘通道
status: draft
card_type: mechanism
tags: [#memory, #consolidation, #belief-revision, #variance]
created_time: 2026-05-26T11:15:00+08:00
edited_time: 2026-05-26T11:15:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
provenance_card: ../provenance/minority-pressure-promotion.md
aliases: [minority-hypothesis retention, multi-cycle buffer pressure, prediction 4]
related: [memory-as-metabolism-five-operations, memory-gravity-load-bearing-protection, memory-as-metabolism-mirror-vs-compensate, memory-as-metabolism-conflict-routing-matrix, audit-by-suspension-against-entrenchment, longmemeval-five-core-memory-abilities]
---

## 解决的问题：流式 coherence 的自封闭

单条与高 gravity 主导条目矛盾的证据，孤立到达时**总会**被立即隔离——这意味着主导解释**永远不更新**。即便系统"存了"反对意见，也只是 museum storage。Miteski (2026) 把这个失败模式作为 §1.3 中"circularity is the thesis"的反面：mirror 那一侧的自封闭必须被 compensate 一侧的**结构机制**打破，而不是靠"希望被检索"。

## 机制：buffer-internal scoring + multi-cycle accumulation

CONSOLIDATE 的四 phase 中：

1. **Buffer-internal scoring（不可选阶段）**：buffer 内每条新条目先互相评分（mutual support / contradiction），**独立于 active wiki**。这是少数派压力**可见**的关键——三条互相支持的反对证据在 buffer 内形成 cluster，单看每条都达不到主导，但作为 cluster 形成可识别压力。
2. **Wiki scoring**：每条 buffer 条目再与 active wiki 评分（语义一致性、任务对齐、与高 gravity 节点的矛盾代价）。
3. **Fuzzy 分桶**（trapezoid 隶属函数）：高 cohesion 直接整合，中等标记关注，低 cohesion 隔离待评估。
4. **Minority-pressure promotion**：与 active wiki **个别矛盾**但 buffer **内部互相支持**的条目，被标记为对主导解释的**候选更新**，而不是隔离。本周期要么更新 wiki，要么保留到下一周期继续累积。

**单条 = 噪声，累积 = 信号**——这是 promotion 阈值的设计逻辑。

支撑机制是 **minority-hypothesis retention**：dormant 替代假说以低成本留在 buffer/quarantine，不是为存而存，而是让下一个 consolidation cycle "有东西可评"。没有它，buffer 每个周期都从零开始，少数派必须在单周期窗口内累积完整支持——通常不可能。

## 一个未在任何现有 benchmark 测过的失效模式（Prediction 4）

论文最锐利、最愿意被证伪的预测：

> 少数派假说**不是被存**，**不是被检索**，**而是可测地改变下游输出**。

度量：**resurfacing-to-influence 率**——promotion 后系统对相关查询的回答与"未 promotion 的对照组"之间的差异。

与 LongMemEval 的"knowledge updates"类别（Shi et al. arXiv:2410.10813）**结构上不同**：后者评估用户显式说"我的城市变了"后系统是否记住；Prediction 4 测的是**没有显式输入**情况下，多周期 buffer 压力对受 centrality 保护的现任条目的结构性翻盘。

与 THEANINE 的 TeaFarm 反事实评估也不同：TeaFarm 问"memory 是否改变输出"，Prediction 4 问"个别被隔离的反对 cluster 通过多周期 buffer 压力积累后是否实现整合，并可测地改变输出"。一个系统可以通过 TeaFarm（memory 确实影响输出）但仍存在 Prediction 4 的失效模式——本应触发信念修正的 cluster 被一条一条隔离，因为没有单条跨过阈值。

## 边界

- **可能放大相关噪声**：多条互相支持但同样错误的条目也能积累 buffer 压力。框架明确为"anti-entrenchment, not truth-guaranteeing"，给出的候选缓解（source diversity weighting、time-spread requirements、external validation signals）尚未实现。
- **Valley of Amnesia**：promotion 阈值过早穿越，会在新解释获得结构稳定之前突然丢失操作连续性。这是 transition-stability 单独的开放问题。
- **不能彻底解决 echo chamber**：单 agent 内 consolidation 只是三个 compensate 通道之一，另两个是 cross-agent federation 与底模更新（§8.3）。

## References

- 第 1320–1383 行：§5.5 CONSOLIDATE 四 phase + 噪声放大与 Valley of Amnesia 的承认。
- 第 1528–1554 行：§5.7 minority-hypothesis retention。
- 第 1796–1887 行：§7 Predictions 1–4 与 Prediction 4 的 benchmark 区分论证。
- 第 1913–1926 行：§7.5 CONSOLIDATE MUST 要求"score buffer entries against each other before scoring against the active wiki"。
- 来源：`data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt`。

## Footnotes

[^1]: Buffer-internal scoring 的不可选地位原文（第 1913–1917 行）："CONSOLIDATE MUST score buffer entries against each other before scoring against the active wiki — buffer-internal scoring is a non-optional phase, not an optimization; skipping it reintroduces the self-sealing failure mode the buffer architecture was designed to prevent."

[^2]: Prediction 4 措辞原文（第 1828–1832 行）："The claim is not that minority hypotheses are *stored*, nor that they are *surfaced*, but that they measurably *change downstream outputs* at a non-trivial rate."

[^3]: Retention alone is not variance（第 1884–1886 行）："Retention alone is not variance. Surfacing alone is not variance. Only *influence on a downstream output* is effective variance, and that is what Prediction 4 is willing to be measured on."
