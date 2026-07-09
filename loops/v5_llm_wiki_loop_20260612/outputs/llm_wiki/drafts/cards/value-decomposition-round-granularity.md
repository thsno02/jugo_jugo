---
id: value-decomposition-round-granularity
title: Value 分解：Round 粒度优于 Session
status: draft
card_type: empirical-finding
tags: [long-term-memory, RAG, value-granularity, session-decomposition]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
evidence_basis: experimental_paper
justification: ../justification/value-decomposition-round-granularity.md
canonical_concept: round-value-granularity
aliases: [round granularity, session decomposition, value decomposition, round 粒度]
summary: >-
  round-value-granularity 在 LongMemEval_M 上，将 session 分解为 round（一个用户消息+一个助手响应）作为 value 存储粒度，显著提升 GPT-4o 作为 reader 时的 QA 性能。进一步压缩为摘要或用户事实虽然 token 效率高但由于信息损失降低整体 QA 性能，唯一例外是多会话推理问题中事实分解一致地改善了性能（据论文推测是因为事实分解以更统一简化的格式提取同类信息）。最优 token 预算因 reader 能力而异：Llama 3.1 8B 超过 3k tokens 时性能急剧下降，GPT-4o 在超过 20k tokens 时仍持续改善。
related: [unified-memory-framework-three-stages, longmemeval-benchmark-overview]
---

在 LongMemEval_M 上的实验表明，value 存储粒度的选择对 RAG 性能有显著影响：[^src-1]

1. 将 session 分解为 round（一个用户消息 + 一个助手响应）显著提升 GPT-4o 作为 reader 的 QA 性能，与使用 Llama 3.1 8B 时性能相近。

2. 进一步将 round/session 压缩为摘要或用户事实，虽然 token 效率更高，但由于信息损失而降低整体 QA 性能。

3. 唯一例外：在多会话推理问题中，事实分解一致地改善性能。论文推测这是因为事实分解以更统一简化的格式跨所有会话提取同类信息，有利于检索和阅读。[^src-2]

4. 最优 token 预算因 reader 能力而异：Llama 3.1 8B 超过 3k retrieved tokens 时性能急剧下降，GPT-4o 在超过 20k tokens 时仍持续改善。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/5_experiment.tex" Section "Value: Decomposition improves RAG performance" -- "decomposing sessions into rounds significantly enhances reading performance with GPT-4o as the reader"
[^src-2]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/5_experiment.tex" -- "fact decomposition extracts the same type of information across all sessions in a more uniform and simplified format, aiding retrieval and reading"
[^src-3]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/5_experiment.tex" -- "Llama 3.1 8B Instruct's performance drops sharply beyond 3k retrieved tokens, GPT-4o continues to improve even with over 20k retrieved tokens"
