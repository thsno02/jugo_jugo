---
id: time-aware-query-expansion
title: 时间感知的查询扩展策略
status: accepted
card_type: mechanism
tags: [temporal-reasoning, query-expansion, memory-retrieval, time-aware-indexing, LongMemEval]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
justification: ../justification/time-aware-query-expansion.md
canonical_concept: time-aware-query-expansion
aliases: [时间感知查询扩展, time-aware query expansion, 时间过滤检索, temporal query expansion]
summary: >-
  time-aware-query-expansion（时间感知查询扩展 / temporal query expansion / 时间过滤检索）针对记忆系统中的时间推理问题，在索引阶段提取事件日期、在检索阶段用 LLM 推断查询的时间范围以过滤无关值；使用强模型（GPT-4o）时平均提升时间推理召回率 6.8%-11.3%，弱模型（8B）因时间范围幻觉反而有害
related: [fact-augmented-key-expansion, longmemeval-five-memory-abilities]
---

朴素的语义相似度检索在面对涉及时间引用的查询时表现不佳（如"你上周末推荐的餐厅是哪家？"）。LongMemEval 提出了一种时间感知的索引和查询扩展方案来解决此问题 [^src-1]：

**索引阶段**：使用 LLM 从每个值（value）中提取包含日期的事件提及，为值增加时间维度的索引 [^src-2]。

**检索阶段**：对于时间敏感的查询，使用 LLM 推断一个潜在的时间范围（起止日期），并据此过滤掉大量无关的值，缩小搜索空间 [^src-3]。

**效果**：使用轮次（round）作为值时平均提升时间推理召回率 11.3%，使用会话（session）作为值时提升 6.8%。该提升在同时应用键扩展时仍然保持一致 [^src-4]。

**关键限制——模型能力依赖**：时间范围推断高度依赖 LLM 的能力。GPT-4o 能在查询缺乏时间引用时正确拒绝生成时间范围；而 Llama 3.1 8B 即使提供了大量上下文示例，也经常在无时间引用的查询中错误地"幻觉"出一个时间范围，导致搜索空间被错误裁剪、召回率下降 [^src-5]。

Graphiti 的双时间线事实建模从存储端解决了类似问题：为每条事实维护事件时间线和事务时间线各两个时间戳，使时间信息在索引时即被结构化编码[^card-1]。LoCoMo 基准则量化了时间感知检索的必要性——时序推理是 LLM 与人类差距最大的能力维度（73%），凸显了时间过滤机制的重要性[^card-2]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/4_methodology.tex` -- Section 4.2 CP3 -- "when queries involve temporal references... naive similarity search proves insufficient. We address this with a time-aware indexing and query expansion strategy"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/5_experiment.tex` -- Section 5.4 -- "values are additionally indexed by the dates of the events they contain"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/5_experiment.tex` -- Section 5.4 -- "an LLM extracts a time range for time-sensitive queries, which is used to filter out a large number of irrelevant values"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/5_experiment.tex` -- Section 5.4 -- "this simple design improves recall by an average of 11.3% when using rounds as the value and by 6.8% when using sessions as the value"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/appendix.tex` -- Appendix temp expansion analysis -- "the model often mistakenly extracts a time range, which erroneously prunes out the search space, leading to a low memory recall. By contrast, GPT-4o is able to refuse to generate a time range when the question does not have a time reference"
[^card-1]: [双时间线事实建模](bi-temporal-fact-model.md) -- Graphiti 从存储端为每条事实维护四个时间戳（事件时间线+事务时间线），与 LongMemEval 的查询端时间过滤形成互补的时间感知方案
[^card-2]: [时序推理是 LLM 对话记忆中最困难的能力维度](temporal-reasoning-difficulty.md) -- LoCoMo 量化了时序推理与人类的 73% 差距，凸显了时间感知查询扩展等机制的必要性
