---
id: mem0-zep-comparison
title: Mem0 与 Zep 的 Token 效率对比
status: accepted
card_type: empirical-finding
tags:
- zep
- token-overhead
- graph-construction
- memory-redundancy
- operational-bottleneck
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-mem0
evidence_basis: experimental_paper
justification: ../justification/mem0-zep-comparison.md
canonical_concept: mem0-vs-zep-efficiency
aliases:
- Mem0 vs Zep
- Zep token overhead
- Zep 延迟问题
- memory graph redundancy
summary: Zep 记忆图消耗超 600k tokens（原始对话 26k 的 20 倍以上），因其在每个节点缓存完整抽象摘要并在边上存储事实，导致大量知识片段重复。Mem0
  仅 7k tokens、Mem0^g 14k tokens。Zep 还存在严重操作瓶颈：添加记忆后立即检索常失败，需数小时延迟后才能正确搜索，暗示异步 LLM
  调用和大量后台处理。Mem0 图构建即使最坏情况下也在一分钟内完成。
related:
- mem0-latency-token-efficiency
- zep-longmemeval-results
- mem0-performance-results
---

Mem0 论文详细对比了与 Zep（一个商业 AI agent 记忆管理平台）的 token 效率差异：[^src-1]

**Token 占用对比**：
- Mem0：每对话平均 **7k** tokens
- Mem0^g：每对话平均 **14k** tokens（因引入图记忆的节点和关系而翻倍）
- Zep：超过 **600k** tokens
- 原始对话全文：约 26k tokens

Zep 的膨胀源于其设计选择：在每个节点缓存完整抽象摘要，同时在连接边上存储事实，导致相同知识片段在图中大量重复。原始对话全文 26k tokens 仅为 Zep 图的约 1/20。[^src-2]

**操作瓶颈**：实验还揭示 Zep 存在显著操作延迟——添加记忆后立即尝试检索常无法正确回答查询，而数小时后重新执行相同搜索则产生明显更好的结果。这暗示 Zep 的图构建涉及多次异步 LLM 调用和大量后台处理，使其不适合实时应用。[^src-3]

相比之下，Mem0 的图构建即使在最坏情况下也在一分钟内完成，用户可立即利用新添加的记忆进行查询响应。[^src-4]

[^card-1]: [[mem0-latency-token-efficiency]] 提供了 Mem0 自身的延迟数据
[^card-2]: [[mem0-graph-memory-architecture]] 描述了 Mem0^g 更高效的图构建设计

[^src-1]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/result.tex" P1315 -- "Mem0 encodes complete dialogue turns in a natural language representation and therefore occupies only 7k tokens per conversation on an average"
[^src-2]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/result.tex" P1315 -- "The inflation arises from Zep's design choice to cache a full abstractive summary at every node while also storing facts on the connecting edges, leading to extensive redundancy across the graph"
[^src-3]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/result.tex" P1316 -- "After adding memories to Zep's system, we observed that immediate memory retrieval attempts often failed to answer our queries correctly. Interestingly, re-running identical searches after a delay of several hours yielded considerably better results"
[^src-4]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/result.tex" P1316 -- "Mem0 graph construction completes in under a minute even in worst-case scenarios"
