---
id: contextualize-depth-fitted-compression
title: CONTEXTUALIZE 深度适配压缩
status: accepted
card_type: mechanism
tags: [companion-memory, contextualize, compression, cold-memory, linkout, selective-absorption]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
justification: ../justification/contextualize-depth-fitted-compression.md
canonical_concept: contextualize-depth-fitted-compression
aliases: [CONTEXTUALIZE 深度适配压缩, depth-fitted compression, 选择性吸收, selective absorption, 上下文深度压缩, cold memory tier]
summary: >-
  contextualize-depth-fitted-compression（CONTEXTUALIZE 深度适配 / depth-fitted compression / selective absorption）伴侣记忆框架中将外部来源压缩到用户当前工作上下文深度的操作；在梦周期而非流式摄取时运行，必须保留到原始来源的链接（linkout）；引入冷存储层作为第三存储层；代谢隐喻——细胞不吸收环境中的一切，只吸收当前代谢状态能使用的
related: [sleep-consolidation-architecture, three-layer-architecture, intentional-abstraction]
---

CONTEXTUALIZE 是伴侣记忆框架的第五个操作，处理其他操作未涉及的问题：外部来源不存在单一的规范压缩[^src-1]。

**核心问题**：同一份架构决策记录对产品负责人和开发者产生不同的有用摘要——前者需要目标、权衡和利益相关者理由，后者需要实现约束、库选择和边缘情况。两者都不是错误的，它们是同一制品的**上下文适配压缩**[^src-2]。

**三条路径的权衡**：
- 朴素完整压缩 → 膨胀 wiki + 阻碍整合操作
- 过度激进压缩 → 条目准确但操作上无用
- CONTEXTUALIZE 的第三路径 → 压缩到用户当前工作上下文深度，**同时保留到完整外部来源的链接**[^src-3]

**两个设计承诺**[^src-4]：
1. CONTEXTUALIZE 在梦周期（dream cycle）中运行，不在运行时摄取中。如果用户在摄取和整合之间上下文发生变化，下一个梦周期对新上下文压缩
2. 深度默认由系统推断（从 wiki 条目、查询模式、主题邻域），不要求用户显式指定

**冷存储层**：引入了超越原始缓冲区和活跃 wiki 的第三存储层——冷存储（cold memory）。TRIAGE 接受的完整外部来源不需要留在活跃 wiki 中，但也不能删除（因为 linkout 承诺）。三层架构：冷存储（原件）、原始缓冲区（待整合）、活跃 wiki（深度适配工作表示）[^src-5]。

**代谢隐喻**：生物细胞不吸收环境中的一切，只吸收当前代谢状态能使用的，其余通过或排泄。Wiki 摄取应将外部来源压缩到用户当前的主题参与深度[^src-6]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.4" -- "CONTEXTUALIZE is the framework's response to a problem the other operations do not handle: external sources do not have a single canonical compression."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.4" -- "The same architecture decision record yields a different useful summary for a Product Owner than for a Developer reading it the same afternoon."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.4" -- "Compress external sources to fit the user's current working-context depth on the relevant topic, and preserve a linkout to the full external source"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.4" -- "CONTEXTUALIZE runs in the dream cycle, not at runtime ingestion... the depth is inferred by default, not explicitly set by the user."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.4" -- "cold memory... high-capacity, low-access-frequency storage that holds the sources the wiki has already processed."
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 5.4" -- "Biological cells do not absorb everything in their environment; they absorb what their current metabolic state can use"
