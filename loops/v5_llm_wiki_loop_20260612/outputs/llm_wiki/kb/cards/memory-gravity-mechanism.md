---
id: memory-gravity-mechanism
title: 记忆引力机制
status: accepted
card_type: mechanism-specification
tags:
- memory-gravity
- structural-centrality
- load-bearing
- graph-centrality
- companion-memory
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-memory-as-metabolism
evidence_basis: theoretical_paper
justification: ../justification/memory-gravity-mechanism.md
canonical_concept: memory-gravity
aliases:
- memory gravity
- G_i^base
- G_i^eff
- 记忆引力
- load-bearing protection
summary: memory gravity 记忆引力是伴侣记忆框架中保护负载承载条目的镜像机制。 基础引力 G_i^base = f(C(i), F(i)) 由中心性测度 C(i) 和下游碎片化成本 F(i) 决定。 必须满足四性质：中心性单调、碎片化单调、incumbency 下次线性增长（防止绝对incumbency陷阱）、有界性。 有效引力 G_i^eff(t) = G_i^base * D(t
  - t_last_access) 加入时间衰减。 引力保护底线基于 G_i^base 评估，结构中心性不因访问缺失而衰减。 引力不包含 utility 信号——三力分离：引力保护结构、utility 驱动活力衰减、AUDIT 剥夺保护。
related:
- mirror-vs-compensate-principle
- companion-memory-system-class
- audit-operation
- consolidate-operation
- minority-hypothesis-retention
- vitality-score-decay
---
记忆引力（memory gravity）保护移除后会在知识库中产生级联影响的条目。保护理由不是因为条目为真，而是因为它们对维基的连贯运行具有结构必要性。[^src-1]

将活跃维基定义为加权有向图 W = (V, E)，基础引力 G_i^base = f(C(i), F(i))，其中 C(i) 是中心性测度（捕获直接和传递引用流），F(i) 是下游碎片化成本（前瞻性测度：如果现在移除 i，维基的连贯运行会破坏多少）。[^src-2]

G^base 必须满足四项性质：(1) 中心性单调性；(2) 碎片化单调性；(3) incumbency 下次线性增长——防止绝对 incumbency 陷阱，此为安全性质而非优化；(4) 有界性。[^src-3]

有效引力加入时间衰减：G_i^eff(t) = G_i^base * D(t - t_last_access)，其中 D(0)=1，单调非增，趋近零。但引力保护底线基于 G_i^base 评估——结构中心性高的条目无论多久未被访问都保持保护。这是"安静基础"存活的机制。[^src-4]

三力架构分离：引力保护结构负载承载条目，utility 通过活力公式驱动衰减，AUDIT 通过反事实悬挂剥夺高引力但非负载承载条目的保护。将 utility 折入引力会坍缩两种不同机制。[^src-5]

已知失败模式：在被识别为错误之前已成为负载承载的虚假条目获得更多保护而非更少。AUDIT 是唯一防御。[^src-6]

[^src-1]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.6 Memory gravity" P1 -- "Memory gravity protects entries whose removal would cascade through the knowledge base. Not because those entries are true, but because they are structurally essential"
[^src-2]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.6" P2 -- "G_i^base = f(C(i), F(i)) where C(i) is a centrality measure...F(i) is downstream fragmentation cost"
[^src-3]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.6" P3-6 -- "Sub-linear growth under incumbency...prevents the Absolute Incumbency Trap"
[^src-4]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.6" P7-8 -- "G_i^eff(t) = G_i^base · D(t − t_last_access)...gravity's structural component does not decay, only the access-modulated effective component does"
[^src-5]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.6 Architectural note" P1 -- "gravity protects structurally load-bearing entries, utility drives vitality-based decay through §5.3, and AUDIT is the mechanism that strips protection"
[^src-6]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.6 A known failure mode" P1 -- "A false entry that became load-bearing before it was recognized as false is more protected, not less."

[^card-1]: companion-memory-system-class — 引力是伴侣系统镜像操作连续性的具体实现
[^card-2]: mirror-vs-compensate-principle — 引力被分类为 mirror 机制
