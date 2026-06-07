---
id: comparison-posthoc-vs-builtin-provenance
title: 事后审计追踪与内建溯源索引的区分
status: accepted
card_type: distinction
tags: [provenance, architecture, audit, bidirectional-index, traceability]
created_time: 2026-06-05T18:00:00+08:00
edited_time: 2026-06-05T18:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net, arxiv-zep]
justification: ../justification/comparison-posthoc-vs-builtin-provenance.md
canonical_concept: posthoc-vs-builtin-provenance
aliases: [事后追踪与内建溯源, post-hoc vs built-in provenance]
summary: >-
  comparison-posthoc-vs-builtin-provenance（事后追踪与内建溯源）区分两种知识溯源架构策略：
  LLM Wiki 的审计机制在需要验证时事后沿制品图遍历（output->wiki->raw），
  Graphiti 的 episode 子图在数据写入时即建立双向索引实现内建溯源
related: [audit-provenance-tracing, non-lossy-episodic-store]
---

知识系统中「如何追溯到来源」这一核心问题存在两种截然不同的架构策略。

**事后遍历（post-hoc traversal）**：LLM Wiki 的审计机制在需要验证时沿制品图回溯——从 output 经 wiki 到 raw sources，检测漂移、验证可信度[^card-1][^src-1]。溯源能力依赖于层间的引用关系在制品生成时被正确维护，审计本身不创建新的溯源索引，而是沿已有的制品图路径行走。这种策略的优势在于不增加写入时的开销，但依赖制品图的完整性。

**内建双向索引（built-in bidirectional indexing）**：Graphiti 的 episode 子图在数据写入时即建立 episode 与语义边之间的双向索引[^card-2][^src-2]。正向可从 episode 检索派生实体，反向可从语义制品追溯到源 episode 用于引用。溯源是数据模型的一部分而非事后验证。这种策略的优势在于溯源始终可用、不依赖事后遍历的完整性，但增加了写入时的复杂度。

**区分的核心**在于溯源能力的建立时机：事后策略将溯源视为验证行为（按需触发），内建策略将溯源视为数据结构的固有属性（始终存在）。两者都保留原始数据不丢失——LLM Wiki 通过 raw sources 的不可变性，Graphiti 通过 episode 的无损存储——但它们在「何时建立来源与制品之间的可遍历链接」上做出了不同的架构选择。

## Footnotes

[^card-1]: [审计与溯源追踪](audit-provenance-tracing.md) -- 事后遍历策略的代表：沿 output->wiki->raw 制品图回溯验证可信度
[^card-2]: [无损 Episode 数据存储与双向溯源](non-lossy-episodic-store.md) -- 内建溯源策略的代表：写入时建立 episode 与语义边的双向索引
[^src-1]: llm-wiki-net -- "Audit walks that full artifact graph. It can trace an output back through the wiki state and raw sources it depended on, then escalate into fresh research when the stored evidence is stale or incomplete."
[^src-2]: arxiv-zep (Rasmussen et al. 2025) -- "Episodes and their derived semantic edges maintain bidirectional indices that track the relationships between edges and their source episodes. This design reinforces the non-lossy nature of Graphiti's episodic subgraph by enabling both forward and backward traversal: semantic artifacts can be traced to their sources for citation or quotation."
