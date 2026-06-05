---
id: memory-value-granularity-tradeoff
title: 记忆存储粒度权衡（会话/轮次/事实）
status: accepted
card_type: mechanism
tags: [memory-system, granularity, session-decomposition, value-representation, LongMemEval]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
justification: ../justification/memory-value-granularity-tradeoff.md
canonical_concept: memory-value-granularity-tradeoff
aliases: [存储粒度权衡, value granularity tradeoff, 会话分解, session decomposition, round-level decomposition]
summary: >-
  memory-value-granularity-tradeoff（存储粒度权衡 / value granularity tradeoff / 会话分解 / round-level decomposition）在对话记忆系统中，将会话分解为轮次（round）级别是比整个会话（session）更优的存储粒度；进一步压缩为事实/摘要虽降低 token 消耗但因信息丢失损害总体 QA 性能，唯一例外是跨会话推理任务因事实格式的一致性而受益
related: [chunk-size-tradeoff, lightmem-three-stage-memory, extraction-granularity-control]
---

在聊天助手的长期记忆系统中，"值"（value）的存储粒度是一个关键设计选择。LongMemEval 的实验在三个粒度级别上进行了系统比较 [^src-1]：

**轮次级别（round）优于会话级别（session）**：将会话分解为单个轮次（一条用户消息 + 一条助手回复）显著提升了以 GPT-4o 作为阅读器时的阅读性能，而使用较弱的 Llama 3.1 8B 时则与未分解的会话表现相当 [^src-2]。

**事实级别压缩的信息丢失代价**：尽管将轮次进一步压缩为摘要或用户事实在 token 使用上更高效，但由于信息丢失，这种做法对总体 QA 性能产生了负面影响 [^src-3]。唯一的例外是跨会话推理（multi-session reasoning）任务——事实分解在此场景中持续提升性能。假设原因是事实分解以更统一和简化的格式跨所有会话提取了同类信息，有助于检索和阅读 [^src-4]。

**阅读器能力决定最优 token 预算**：较弱模型（Llama 8B）在检索 token 超过 3k 后性能急剧下降，而 GPT-4o 即使在 20k 以上仍持续改善 [^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/4_methodology.tex` -- Section 4.2 CP1 -- "we compare three value representation strategies: storing entire sessions, decomposing sessions into individual rounds, and further applying summary/fact extraction"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/5_experiment.tex` -- Section 5.2 -- "decomposing sessions into rounds significantly enhances reading performance with GPT-4o as the reader"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/5_experiment.tex` -- Section 5.2 -- "replacing sessions or rounds with extracted summaries or facts negatively impacts QA performance due to information loss"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/5_experiment.tex` -- Section 5.2 -- "fact decomposition extracts the same type of information across all sessions in a more uniform and simplified format, aiding retrieval and reading"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/5_experiment.tex` -- Section 5.2 -- "Llama 3.1 8B Instruct's performance drops sharply beyond 3k retrieved tokens, GPT-4o continues to improve even with over 20k retrieved tokens"
