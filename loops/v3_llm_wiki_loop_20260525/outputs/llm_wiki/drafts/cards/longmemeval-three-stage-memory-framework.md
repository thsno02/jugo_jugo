---
id: longmemeval-three-stage-memory-framework
title: 把 long-term memory 系统拆成 indexing / retrieval / reading 三阶段四控制点
status: draft
card_type: concept
tags: [#memory-system, #framework, #rag]
created_time: 2026-05-26T14:25:00+08:00
edited_time: 2026-05-26T14:25:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
provenance_card: ../provenance/longmemeval-three-stage-memory-framework.md
aliases: [unified memory view, CP1-CP4, 三阶段四控制点]
related: [longmemeval-five-core-memory-abilities]
---

## 统一视角

LongMemEval 提出一个统一框架把"现有所有 memory-augmented chat assistant"都装下：把长期记忆建模成一个 key-value 数据存 $[(k_1, v_1), (k_2, v_2), ...]$，分三个执行阶段、暴露四个可调控制点（control point, CP）：

| 阶段 | 控制点 | 含义 |
|---|---|---|
| **Indexing** | CP1: Value | 把每个 session 存成什么粒度——整段 session？拆成 round？再压成 fact / summary / keyphrase？ |
| **Indexing** | CP2: Key | 用什么作为 key——直接用 value 自身？用从 value 抽出来的 fact / summary / keyphrase？还是用拼接后的 V + fact？ |
| **Retrieval** | CP3: Query | query 怎么构造——直接用问题？加上提取的时间区间？做关键词扩写？|
| **Reading** | CP4: Reading strategy | 检索到的 top-k 怎么读——直接喂给 LLM？用 Chain-of-Note 先抽证据再答？JSON 结构化？|

九个现有系统（In-context RAG、MemoryBank、LD-Agent、CoN、ChatGPT、Coze、RAPTOR、MemWalker、HippoRAG）都可视为这四个 CP 的不同实例。

## 为什么这套视角值得用

- **每条记忆系统的优化都能定位到某个 CP**。论文实验依次扫描四个 CP 找到组合："Value=round + Key=V+fact + Query=question+time + Reading=CoN(JSON)"是当时最优解。
- 把"indexing 是写入侧 vs retrieval 是读出侧 vs reading 是生成侧"分开后，三者优化彼此正交；尤其 reading 一项被很多 RAG 工作忽视，论文实验显示**即便 oracle 检索，CoN+JSON 仍能比 naive 读法多 10 个绝对分**。
- 框架是 plug-and-play 的：你可以替换某个 CP 而不动其它，对工程实现友好。

## 边界

- 框架只覆盖"在线 context 压缩"路线——把每个 session 顺序处理后存起来按需检索；它不涵盖差异化的 architecture-level memory（如 Memorizing Transformer、TRIME）或单纯的 long-context 直读路线。
- "value 可以是 round / session / fact"是离散的几种选择，并不是连续 spectrum——选项之间的取舍由实验决定，没有理论解。

## References

- 三阶段四控制点定义：`data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` 第 1418-1456 行（§4 unified view + §4.2 CP1-CP4）。
- 九系统映射表：第 1141-1153 行（表 `tab:memory-system-dimensions-comp`），最后一行是论文推荐设计：`round | K = V + fact | question + time | flat | Yes | CoN`。
- "Reading 也很重要"：第 1521 行（reading 设计在 oracle retrieval 下仍能影响 10 绝对分）。

## Footnotes

- CP 1 Value 原文："The value represents the format and granularity of each session stored in memory."（第 1447 行）
- CP 4 Reading 原文："optimizations such as extracting key information before answering (Chain-of-Note ...) and using structured format prompting ... are crucial for achieving high reading performance."（第 1456 行）
- 推荐设计行（表 `tab:memory-system-dimensions-comp`）："Our Design | round | K = V + fact | question + time | flat | Yes | CoN"（第 1153 行）
