---
id: memory-overwrite-vs-omission-failure
title: 记忆覆写与遗漏两种失败模式
status: accepted
card_type: distinction
tags: [memory-failure, commercial-system, ChatGPT, Coze, information-loss, compression-tradeoff]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
justification: ../justification/memory-overwrite-vs-omission-failure.md
canonical_concept: memory-overwrite-vs-omission-failure
aliases: [记忆覆写与遗漏, overwrite vs omission, 压缩覆写, 间接信息遗漏]
summary: >-
  memory-overwrite-vs-omission-failure（记忆覆写与遗漏 / overwrite vs omission / 压缩覆写 / 间接信息遗漏）商业记忆系统呈现两种互补的失败模式：ChatGPT 在压缩历史时覆写关键信息（先记后丢），Coze 则经常未能记录间接提供的用户信息（从未记下），揭示了可靠个性化与效率之间的潜在权衡
related: [memory-value-granularity-tradeoff, long-term-memory-accuracy-gap]
---

LongMemEval 对两个商业记忆增强聊天系统（ChatGPT 和 Coze）的人工评估揭示了两种截然不同但互补的记忆失败模式 [^src-1]：

**ChatGPT：压缩覆写（先记后丢）**——ChatGPT 通常在证据会话呈现后立即正确记录证据陈述。然而，随着交互继续，当系统压缩历史时，经常会修改这些信息，导致信息丢失 [^src-2]。这种"先记后丢"的模式揭示了一个根本性权衡：记忆压缩策略在追求效率的同时可能损害已记录信息的可靠性。

**Coze：间接信息遗漏（从未记下）**——与 ChatGPT 相反，Coze 的大多数错误源于一开始就未能从某些会话中记录信息。系统特别容易遗漏以间接方式提供的用户信息——例如用户在讨论汽车保险时附带提及的购车事实 [^src-3]。

**能力差异的影响**：在单会话信息提取（IE）任务上，两个系统都表现尚可。但在需要跨多个会话聚合的其他任务类型上（MR、KU、TR），两者均出现显著性能下降。Coze 的跨会话推理准确率低至 11.8%（GPT-3.5-turbo），ChatGPT 在时间推理上也仅达 43.5%（GPT-4o）[^src-4]。Mem0 的提取-更新管线通过结构化的增量处理范式直接应对这两种失败模式——提取阶段避免遗漏，语义比对的更新阶段避免覆写[^card-1]。

## Footnotes

[^card-1]: [记忆提取-更新双阶段管线](memory-extraction-update-pipeline.md) -- LongMemEval 诊断了覆写和遗漏两种失败模式，Mem0 的提取-更新管线在架构层面回应了这些问题：提取阶段结合对话摘要和近期消息防止遗漏，更新阶段通过语义比对和 CRUD 操作防止覆写

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/3_benchmark.tex` -- Section 3.3 -- "We found ChatGPT tended to overwrite crucial information as the chat continues, while Coze often failed to record indirectly provided user information"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/appendix.tex` -- Section Appendix manual analysis -- "ChatGPT generally records the evidence statements immediately after it has been presented in the evidence session. However, as the interaction proceeds, ChatGPT often modify this information when it compresses the history, resulting in information loss"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/appendix.tex` -- Section Appendix manual analysis -- "most of Coze's errors are due to failing to record information from some session"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/appendix.tex` -- Table commercial-system-detailed -- "ChatGPT GPT-4o: IE 0.688, MR 0.441, KU 0.833, TR 0.435; Coze GPT-3.5-turbo: IE 0.625, MR 0.118, KU 0.375, TR 0.043"
