---
id: compilation-gap
title: 编译缺口——Wiki 编译中的灾难性事实丢失
status: accepted
card_type: concept
tags: [llm-wiki, compilation, fact-loss, knowledge-distillation, wicer]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
justification: ../justification/compilation-gap.md
canonical_concept: compilation-gap
aliases: [编译缺口, compilation gap, 知识编译丢失, 灾难性事实丢失]
summary: >-
  compilation-gap（编译缺口 / compilation gap / 灾难性事实丢失）指 LLM 将原始文档蒸馏为
  wiki 时不可避免地丢弃关键事实的问题；盲编译在 17 个 RepLiQA 领域上的灾难性失败率为 53-60%，
  质量仅 2.14-2.32（满分 5），远低于 RAG 基线 3.46
related: [source-faithfulness-risk, wicer-iterative-refinement, compile-time-vs-query-time]
---

**编译缺口（compilation gap）** 是 LLM Wiki 系统在将原始文档蒸馏（distill）为结构化 wiki 时必须解决的核心挑战：编译过程会灾难性地丢弃关键事实（catastrophically discarding critical facts）[^src-1]。

与渐进性知识漂移不同，编译缺口描述的是**单次编译步骤中的急性、大规模信息丢失**。在 17 个 RepLiQA 领域、6,800 个问题的实验中，盲编译（blind compilation）的质量评分仅为 2.14 到 2.32（满分 5），而原始全上下文基线为 3.46，差距极为显著[^src-2]。更关键的是，盲编译的**灾难性失败率高达 53% 到 60%**——即超过一半的问题因关键事实被编译过程丢弃而完全无法回答[^src-3]。

编译缺口的存在意味着：仅依靠 LLM 一次性"总结"原始素材来构建 wiki 是不够的，需要迭代式的验证与修复机制来弥合这一差距。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-wicer/text.txt` -- Abstract -- "Realizing this requires solving the compilation gap: LLM compilation distilling raw documents into a wiki without catastrophically discarding critical facts."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-wicer/text.txt` -- Abstract -- "blind compilation fails entirely (2.14 to 2.32 vs. 3.46, 53 to 60% catastrophic failure rate)"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-wicer/text.txt` -- Abstract -- "53 to 60% catastrophic failure rate"
