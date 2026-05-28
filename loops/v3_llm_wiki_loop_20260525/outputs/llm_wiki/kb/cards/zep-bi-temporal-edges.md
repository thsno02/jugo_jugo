---
id: zep-bi-temporal-edges
title: Zep 用双时间线 + 边失效让事实"会过期"而不是被覆盖
status: accepted
card_type: mechanism
tags: [#zep, #temporal-knowledge-graph, #fact-invalidation]
created_time: 2026-05-26T11:05:00+08:00
edited_time: 2026-05-28T11:32:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
provenance_card: ../provenance/zep-bi-temporal-edges.md
aliases: [bi-temporal model, Graphiti edge invalidation, t_valid/t_invalid]
related: [zep-graphiti-three-tier-graph, mem0-graph-memory-variant, lightmem-sleep-time-offline-parallel-update, longmemeval-five-core-memory-abilities, longmemeval-time-aware-query-expansion]
---

Zep/Graphiti[^v3-1] 的关键差异化能力是把"事实何时是真的"和"事实何时被系统记下来"拆成两条互不相关的时间轴，并在边上同时记录四个时间戳[^src1]：

- 事务时间轴 $T'$：$t'_\text{created}$、$t'_\text{expired}$，纯粹是数据库审计——这一条边什么时候被写入、什么时候被系统判定失效。
- 事件时间轴 $T$：$t_\text{valid}$、$t_\text{invalid}$，描述这一事实在现实世界中开始为真、停止为真的时间段。

这套 bi-temporal 模型支持两种以前 graph-RAG 体系做不好的事[^src2]：

1. **绝对/相对时间统一抽取**：每条 message 携带 $t_\text{ref}$，LLM 可以把"两周前"、"下周四"这样的相对表达解算成绝对时间；只产生事件时间戳的事实（如生日）则只填 $t_\text{valid}$。
2. **事实失效而非覆盖**：新边进入时，系统用 LLM 与"语义相关的现有边"做对比，找到时间上重叠的矛盾，把旧边的 $t_\text{invalid}$ 设置为新边的 $t_\text{valid}$。旧边并不被删除，而是被"过期掉"，依然能查到——这就保留了**关系演化的历史**。这与 Mem0g 给冲突关系打 `invalid` 标记不物理删除的思路同向[^v3-2]；与 LightMem 用时间戳偏序约束 update 也同源[^v3-3]。
3. 沿 $T'$，"新到的就是权威"是固定优先级，避免回灌旧消息导致矛盾解析摇摆。

机制含义：相比于把整个对话拍平塞进上下文或者直接 upsert 实体属性，bi-temporal 让 LongMemEval 里的 knowledge-update / temporal-reasoning 类问题[^v3-4] 变得可解——一条事实从过去某刻到现在的有效区间是显式存在的，可被检索器作为 fact 字段直接给到 LLM（context 模板里有 "Date range: from - to" 槽位）。LongMemEval 的"时间区间过滤"是另一条不依赖 bi-temporal 的实现路径[^v3-5]。

边界：失效检测依赖 LLM 比较，只针对**语义相近且实体对相同**的边触发去重和矛盾检查，跨实体的隐含矛盾不会自动解。论文也明确说，弱模型对该时间数据的理解仍有 gap[^src3]。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` — main.tex 行 120（§2.1 bi-temporal 引入）+ 行 142–144（§2.2.3 "Temporal Extraction and Edge Invalidation"）— "Zep implements a bi-temporal model, where timeline $T$ represents the chronological ordering of events, and timeline $T'$ represents the transactional order of Zep's data ingestion."
[^src2]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` — main.tex 行 144 + 行 165–191（§3 sample context template 含日期段）— "When the system identifies temporally overlapping contradictions, it invalidates the affected edges by setting their $t_\text{invalid}$ to the $t_\text{valid}$ of the invalidating edge. Following the transactional timeline $T'$, Graphiti consistently prioritizes new information when determining edge invalidation."
[^src3]: `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt` — main.tex 行 291 — "additional development may be needed to improve less capable models' understanding of Zep's temporal data."
[^v3-1]: [zep-graphiti-three-tier-graph](zep-graphiti-three-tier-graph.md) — bi-temporal edges 落在三层图的 $\mathcal{G}_s$ 边上。
[^v3-2]: [mem0-graph-memory-variant](mem0-graph-memory-variant.md) — Mem0g 给冲突关系打 `invalid` 标记的同向思路。
[^v3-3]: [lightmem-sleep-time-offline-parallel-update](lightmem-sleep-time-offline-parallel-update.md) — LightMem 用 $t_j \geq t_i$ 时间戳偏序约束 update 的同源思路。
[^v3-4]: [longmemeval-five-core-memory-abilities](longmemeval-five-core-memory-abilities.md) — KU/TR 类问题的定义。
[^v3-5]: [longmemeval-time-aware-query-expansion](longmemeval-time-aware-query-expansion.md) — 不依赖 bi-temporal 的"时间区间过滤"另一路径。
