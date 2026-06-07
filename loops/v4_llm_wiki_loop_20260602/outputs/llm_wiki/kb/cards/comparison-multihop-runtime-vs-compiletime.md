---
id: comparison-multihop-runtime-vs-compiletime
title: 多跳推理的两条路径：运行时函数链 vs 编译时预综合
status: accepted
card_type: distinction
tags: [multi-hop, architecture, memgpt, llm-wiki, compile-time, runtime]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt, anthemcreation-fr-guide]
justification: ../justification/comparison-multihop-runtime-vs-compiletime.md
canonical_concept: comparison-multihop-runtime-vs-compiletime
aliases: [运行时 vs 编译时多跳, runtime vs compile-time multi-hop]
summary: >-
  comparison-multihop-runtime-vs-compiletime（运行时 vs 编译时多跳）区分多跳推理的两条架构路径：
  MemGPT 在查询时通过代理函数链逐步解析依赖，LLM Wiki 在摄入时预建跨链接使多跳查询退化为直接查找；
  前者灵活但受模型能力约束，后者稳健但依赖摄入质量
related: [llm-wiki-rag-depth-distinction, memgpt-function-chaining, memgpt-nested-kv-retrieval]
---

多跳推理（multi-hop reasoning）要求系统将多个信息片段串联起来回答一个问题。两种架构在根本不同的阶段解决这一问题：

**运行时函数链（MemGPT 路径）**：代理在查询时动态发出多次函数调用，每次调用的结果作为下一次调用的输入。MemGPT 的嵌套键值检索实验展示了这一能力——GPT-4 基线在 3 层嵌套时准确率降至 0%，而 MemGPT + GPT-4 在所有层级上性能稳定[^card-1][^src-1]。优势在于灵活性：无需预先知道哪些信息会被串联。劣势在于受底层模型代理能力约束（GPT-4 Turbo 反而比 GPT-4 表现更差）。

**编译时预综合（LLM Wiki 路径）**：在知识摄入阶段，LLM 已经建立概念间的跨链接、解决来源间的矛盾、构建综合叙述。查询时的多跳推理退化为沿已有链接的直接遍历[^card-2]。优势在于查询时稳健且不依赖模型的多步代理能力。劣势在于摄入质量决定上限——如果某条链接在摄入时未被建立，查询时无法动态补偿。

**核心区分**在于多跳依赖的解析时机：查询时（runtime）还是摄入时（compile-time）。这一区分映射到更广泛的系统设计权衡——即时灵活性 vs 预计算稳健性。GraphRAG 的 map-reduce 流程代表了[编者注]第三条中间路径[^card-3]：在摄入时预建社区摘要（编译时），但在查询时通过 map-reduce 聚合这些摘要（运行时），兼具两者的部分特征。

## Footnotes

[^card-1]: [MemGPT 嵌套键值检索与多跳能力](memgpt-nested-kv-retrieval.md) -- 本卡的运行时路径实例，展示代理函数链在多层嵌套键值查找中的稳定性与局限
[^card-2]: [LLM Wiki 与 RAG 的核心差异在于推理深度](llm-wiki-rag-depth-distinction.md) -- 本卡的编译时路径实例，论证预综合跨链接使多跳推理自然可行
[^card-3]: [GraphRAG Map-Reduce 查询](graphrag-map-reduce-query.md) -- GraphRAG 的 map-reduce 社区摘要聚合机制
[^src-1]: arxiv-memgpt (Packer et al. 2023) -- "GPT-4 and GPT-4 Turbo are better than GPT-3.5, but also suffer from a similar dropoff, and hit 0 percent accuracy by 3 nesting levels. MemGPT with GPT-4 on the other hand is unaffected with the number of nesting levels and is able to perform the nested lookup by accessing the key-value pairs stored in main context repeatedly via function queries."
