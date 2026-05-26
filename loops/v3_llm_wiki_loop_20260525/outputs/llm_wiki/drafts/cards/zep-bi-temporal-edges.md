---
id: zep-bi-temporal-edges
title: Zep 用双时间线 + 边失效让事实"会过期"而不是被覆盖
status: draft
card_type: mechanism
tags: [#zep, #temporal-knowledge-graph, #fact-invalidation]
created_time: 2026-05-26T11:05:00+08:00
edited_time: 2026-05-26T11:05:00+08:00
edited_entity: llm
source_ids: [arxiv-zep]
provenance_card: ../provenance/zep-bi-temporal-edges.md
aliases: [bi-temporal model, Graphiti edge invalidation, t_valid/t_invalid]
related: [zep-graphiti-three-tier-graph]
---

Zep/Graphiti 的关键差异化能力是把"事实何时是真的"和"事实何时被系统记下来"拆成两条互不相关的时间轴，并在边上同时记录四个时间戳：

- 事务时间轴 $T'$：$t'_\text{created}$、$t'_\text{expired}$，纯粹是数据库审计——这一条边什么时候被写入、什么时候被系统判定失效。
- 事件时间轴 $T$：$t_\text{valid}$、$t_\text{invalid}$，描述这一事实在现实世界中开始为真、停止为真的时间段。

这套 bi-temporal 模型支持两种以前 graph-RAG 体系做不好的事：

1. **绝对/相对时间统一抽取**：每条 message 携带 $t_\text{ref}$，LLM 可以把"两周前"、"下周四"这样的相对表达解算成绝对时间；只产生事件时间戳的事实（如生日）则只填 $t_\text{valid}$。
2. **事实失效而非覆盖**：新边进入时，系统用 LLM 与"语义相关的现有边"做对比，找到时间上重叠的矛盾，把旧边的 $t_\text{invalid}$ 设置为新边的 $t_\text{valid}$。旧边并不被删除，而是被"过期掉"，依然能查到——这就保留了**关系演化的历史**。
3. 沿 $T'$，"新到的就是权威"是固定优先级，避免回灌旧消息导致矛盾解析摇摆。

机制含义：相比于把整个对话拍平塞进上下文或者直接 upsert 实体属性，bi-temporal 让 LongMemEval 里的 knowledge-update / temporal-reasoning 类问题变得可解——一条事实从过去某刻到现在的有效区间是显式存在的，可被检索器作为 fact 字段直接给到 LLM（context 模板里有 "Date range: from - to" 槽位）。

边界：失效检测依赖 LLM 比较，只针对**语义相近且实体对相同**的边触发去重和矛盾检查，跨实体的隐含矛盾不会自动解。论文也明确说，弱模型对该时间数据的理解仍有 gap（"additional development may be needed to improve less capable models' understanding of Zep's temporal data"）。

## References

Zep 论文 §2.2.3 "Temporal Extraction and Edge Invalidation" 与 §2.1 描述 bi-temporal 模型；§3 sample context template 显示事实时间区间会被注入到 prompt。

- 源路径：`data/raw/arxiv/arxiv-zep/agent_source_bundle.txt`（main.tex 行 120 双时间线引入；行 142–144 四时间戳与失效流程；行 165–191 prompt 模板含日期段；行 291 弱模型理解时间数据的局限）。

## Footnotes

- 双时间线原文（行 120）："Zep implements a bi-temporal model, where timeline $T$ represents the chronological ordering of events, and timeline $T'$ represents the transactional order of Zep's data ingestion."
- 失效机制原文（行 144）："When the system identifies temporally overlapping contradictions, it invalidates the affected edges by setting their $t_\text{invalid}$ to the $t_\text{valid}$ of the invalidating edge. Following the transactional timeline $T'$, Graphiti consistently prioritizes new information when determining edge invalidation."
- 弱模型局限（行 291）："additional development may be needed to improve less capable models' understanding of Zep's temporal data."
