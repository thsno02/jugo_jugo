---
id: full-context-accuracy-ceiling
title: 全上下文方法的准确率天花板效应
status: accepted
card_type: source_claim
tags: [full_context, accuracy_ceiling, latency_tradeoff, benchmark, Mem0]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0]
justification: ../justification/full-context-accuracy-ceiling.md
canonical_concept: full-context-accuracy-ceiling
aliases: [全上下文准确率天花板, full-context accuracy ceiling, 全上下文最高准确率]
summary: >-
  full-context-accuracy-ceiling（全上下文准确率天花板 / full-context accuracy ceiling）Mem0 LOCOMO 实验中全上下文方法（~26K token）达到最高 Judge=72.90%，但 p95 延迟 17.1 秒，而 Mem0（1764 token）以 Judge=66.88% 实现 p95=1.44 秒（91% 延迟降低），揭示记忆压缩带来的准确率-效率权衡
related: [context-extension-insufficiency, memory-vs-rag-salience, full-context-anti-rag]
---

在 LOCOMO 基准测试中，将整个对话历史（约 26K token）直接传入 LLM 的全上下文方法达到了所有方法中最高的整体 Judge 分数（72.90%），但同时产生了最高的计算开销 [^src-1]。

这一结果揭示了记忆系统设计中的核心权衡：

**准确率差距**：全上下文（72.90%）vs Mem0^g（68.44%）vs Mem0（66.88%）。记忆压缩过程中不可避免地丢失了部分信息，导致约 4-6 个百分点的准确率下降 [^src-2]。

**效率收益**：Mem0 的 p95 总延迟仅 1.440 秒（92% 降低），Mem0^g 为 2.590 秒（85% 降低），相对于全上下文的 17.117 秒。Mem0 使用的 token 上下文仅为 1764 个，仅为全上下文的 6.8% [^src-3]。

**扩展性差异**：论文强调随着对话长度增加，全上下文方法的计算开销呈指数增长，而记忆系统保持一致性能，"使其在效率和响应性至关重要的生产规模部署中更加可行" [^src-4]。

该发现意味着全上下文方法设定了一个准确率天花板，记忆系统的价值在于以可接受的准确率损失换取数量级的效率提升——这在实际部署中通常是合理的权衡。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/result.tex -- "a full-context method that ingests a chunk of roughly 26,000 tokens still achieves the highest Judge score (approximately 73%)"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/result.tex -- Table 2: Full-context Judge=72.90%, Mem0=66.88%, Mem0^g=68.44%
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/result.tex -- "Mem0 and Mem0^g significantly reduce token usage and thus achieve lower p95 latencies of around 1.44 seconds (a 92% reduction) and 2.6 seconds (a 85% reduction)"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/result.tex -- "memory-focused approaches like Mem0 and Mem0^g maintain consistent performance regardless of conversation length, making them substantially more viable for production-scale deployments"
