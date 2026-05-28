---
id: memory-gravity-load-bearing-protection
title: Memory Gravity：用结构承重保护知识基础，对抗"绝对在位陷阱"
status: accepted
card_type: mechanism
tags: [#memory, #graph-centrality, #retention, #safety]
created_time: 2026-05-26T11:10:00+08:00
edited_time: 2026-05-28T11:24:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
provenance_card: ../provenance/memory-gravity-load-bearing-protection.md
aliases: [memory gravity, structural load-bearing protection, prospective fragmentation cost]
related: [memory-as-metabolism-five-operations, audit-by-suspension-against-entrenchment, memory-as-metabolism-mirror-vs-compensate, minority-pressure-promotion, zep-graphiti-three-tier-graph]
---

## 是什么

Miteski (2026) 把 active wiki 视作有向加权图 W = (V, E)，节点是 wiki 条目，边是依赖引用[^src1]。每个条目 i 的 base gravity 定义为：

```
G_i^base = f(C(i), F(i))
```

- **C(i)**：中心性度量（eigenvector centrality / PageRank / 域适配变体，框架不锁定，但要求文档化）。
- **F(i)**：**前瞻性碎片化成本**——若现在删除 i，wiki 当前的连贯运转会"破"多少。

它的角色是 mirror 机制中"保护操作连续性"的一半：与 vitality 公式中的 utility 项分立，确保**安静的基础条目**（quiet foundations）即便很少直接产生效用也不被 DECAY 压缩。

## 四条 MUST 性质

1. **中心性单调**：C(i)>C(j) ∧ F(i)=F(j) ⇒ G_i^base > G_j^base。
2. **碎片化单调**：F(i)>F(j) ∧ C(i)=C(j) ⇒ G_i^base > G_j^base。
3. **在位次线性增长（sub-linear under incumbency）**：当 C(i) 无界增长时，G^base 必须次线性增长。这是为了防御 **Absolute Incumbency Trap**——某条目被引用次数极高导致其保护无限增长、结构上无法被推翻——的安全属性，不是优化。
4. **有界归一**：G^base 归一到有界范围，跨条目可比。

## 时间衰减但结构不衰减

```
G_i^eff(t) = G_i^base · D(t − t_last_access)
```

D(Δt) 是单调非增的衰减函数（指数 / 幂律 / 分段都可，需文档化），且 D(0)=1。**关键设计**：

- gravity-protection floor 在 §7.5 中是**对 G_i^base 评估**，不是对 G_i^eff——所以一个长期未访问但仍结构承重的条目，受**结构性下限**保护，不会因为冷却而被 DECAY 压缩。
- vitality 公式（§5.3）中引用的 gravity 是 G_i^eff，这样 vitality 继承访问驱动的衰减；但 decay-eligibility 由 G_i^base 决定。这是 quiet foundations 的具体保障路径。

## 三力分离

base gravity 是**纯结构属性**；effective gravity 是其访问调制形式；**utility 信号绝不进入 gravity**。这保留了框架的三力架构：

- **gravity** 保护结构承重；
- **utility** 通过 §5.3 vitality 驱动 access-modulated decay；
- **AUDIT** 通过反事实悬挂剥离"结构显著但功能空洞"的高 gravity 条目。

把 utility 折进 effective gravity 会**坍缩两个独立机制**，破坏 compensate 故事——这是论文的一个显式架构承诺。

## 与 PageRank / h-index 的区别

Memory gravity 借用了软件系统中的"architectural gravity"和文献计量学的 PageRank/h-index，但有一个关键的前瞻维度：F(i) 测的是"若现在删除会破多少"，**不是**过去被引用多少。这意味着一个刚集成进来、引用还不多但已是当前工作上下文承重的条目，也会被保护——纯回溯度量会低估这一点。

## 已知失效模式与 AUDIT 兜底

**一个在被识别为错误之前已经成为承重的错误条目，会受到更多保护而非更少。** 论文不掩饰这一点：唯一防御是 AUDIT 的反事实悬挂——若高 gravity 条目在多轮 AUDIT 中持续与坏结果相关，走 §5.8 的 gravity-reduction 通路剥离保护（**不是改 gravity 公式本身**）。这只在 AUDIT 灵敏度足够时奏效，AUDIT 灵敏度是 §9 的开放问题。

## References

- 第 1385–1525 行：§5.6 Memory gravity 全章——base/eff、四性质、三力分离、PageRank/h-index 比较、已知失效模式。
- 第 1928–1942 行：§7.5 DECAY MUST NOT 与 gravity-protection floor 的 G^base 条款。
- 来源：`data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt`。

## Footnotes

[^1]: Absolute Incumbency Trap 的安全属性原文（第 1432–1444 行）："Sub-linear growth is a safety property, not an optimization. It complements property 4 by constraining the *shape* of gravity's response to increasing incumbency, not merely the range of gravity values."

[^2]: 三力分立的硬承诺原文（第 1478–1491 行）："Folding utility into effective gravity would collapse two distinct mechanisms into one and would change the framework's compensate story; the three forces remain distinct."

[^3]: F(i) 前瞻性原文（第 1519–1527 行）："Memory gravity differs on a prospective dimension that bibliometrics does not address: F(i) measures what would break if the entry were removed now, not what has historically referenced it."
