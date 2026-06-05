---
id: memory-gravity
title: 记忆引力
status: accepted
card_type: mechanism
tags: [companion-memory, retention, graph-centrality, structural-protection, load-bearing]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
justification: ../justification/memory-gravity.md
canonical_concept: memory-gravity
aliases: [记忆引力, memory gravity, 结构承重保护, load-bearing protection, 引力保护]
summary: >-
  memory-gravity（记忆引力 / memory gravity / 结构承重保护）是伴侣记忆框架中保护结构承重条目免受朴素剪枝的机制；基于中心性 C(i) 和下游碎片化成本 F(i) 计算，必须满足四个属性：中心性单调、碎片化单调、亚线性增长（防止绝对在位者陷阱）、有界性；关键区别于 PageRank 在于引力是前瞻性的（移除后什么会坏）而非回顾性的
related: [companion-knowledge-system, vitality-score-formula, audit-stress-test]
---

记忆引力（memory gravity）保护那些移除后会导致知识库级联碎片化的条目[^src-1]。保护的理由不是因为这些条目是"真的"，而是因为它们对 wiki 的连贯运作具有结构必要性。

**形式定义**：将活跃 wiki 建模为加权有向图 W = (V, E)，条目 i 的基础引力定义为：G_i^base = f(C(i), F(i))，其中 C(i) 是中心性度量（wiki 引用结构中有多少流经 i），F(i) 是下游碎片化成本（此刻移除 i 会破坏多少连贯运作）[^src-2]。

**四个必备属性**[^src-3]：
1. **中心性单调**：更高中心性 → 更大保护
2. **碎片化单调**：更大移除损害 → 更大保护
3. **亚线性增长**：引力随在位度（incumbency）的增长必须是亚线性的，防止**绝对在位者陷阱**——最大引用条目积累无界保护、无论后续多少矛盾证据都无法撼动
4. **有界性**：引力值归一化到有界范围内

**时间衰减**：有效引力 G_i^eff(t) = G_i^base * D(t - t_last_access)，其中 D 是衰减函数（D(0)=1，单调不增，趋近零）。但引力保护下限基于 G_i^base 而非 G_i^eff 评估——结构中心性不因访问频率衰减[^src-4]。

**与 PageRank 的关键区别**：PageRank 和 h-index 基于回顾性引用图（历史上什么引用了节点），记忆引力在前瞻性维度上不同——F(i) 衡量的是"此刻移除会破坏什么"，而非"历史上什么引用了它"[^src-5]。

**已知失败模式**：一个在被识别为错误之前就已成为承重节点的假条目会受到更多而非更少的保护。框架不消除这一问题，而是通过 AUDIT 的悬挂测试来应对[^src-6]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.6" -- "Memory gravity protects entries whose removal would cascade through the knowledge base. Not because those entries are true, but because they are structurally essential"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.6" -- "G_i^base = f(C(i), F(i)) where C(i) is a centrality measure... F(i) is downstream fragmentation cost"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.6" -- "G^base MUST satisfy four properties: Monotonicity in centrality... Monotonicity in fragmentation... Sub-linear growth under incumbency... Boundedness"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.6" -- "gravity's structural component does not decay, only the access-modulated effective component does"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.6" -- "Memory gravity differs on a prospective dimension that bibliometrics does not address: F(i) measures what would break if the entry were removed now, not what has historically referenced it."
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.6" -- "A false entry that became load-bearing before it was recognized as false is more protected, not less. The framework does not eliminate this."
