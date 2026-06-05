---
id: fact-augmented-key-expansion
title: 事实增强的索引键扩展
status: accepted
card_type: mechanism
tags: [memory-indexing, key-expansion, document-expansion, retrieval-optimization, LongMemEval]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
justification: ../justification/fact-augmented-key-expansion.md
canonical_concept: fact-augmented-key-expansion
aliases: [事实增强键扩展, fact-augmented key, 多路径检索, multi-key indexing, key expansion]
summary: >-
  fact-augmented-key-expansion（事实增强键扩展 / multi-key indexing / key expansion）将从记忆值中提取的用户事实拼接到原始值上作为索引键，实现多路径检索；相比仅用值本身作键，平均提升 recall@k 9.4%、下游 QA 准确率 5.4%；单独使用压缩形式作键反而不如原始值
related: [memory-value-granularity-tradeoff, memory-extraction-update-pipeline]
---

在长期记忆系统的索引阶段，键（key）的设计决定了检索的有效性。LongMemEval 提出了一种基于文档扩展（document expansion）的键扩展方法 [^src-1]：

**核心方法**：从值（value，即会话轮次或会话）中提取摘要、关键词或用户事实，然后将这些压缩信息**拼接到原始值上**形成索引键。这种方法同时保留了压缩信息的聚焦语义和原始值的完整性 [^src-2]。

**直觉上的反常发现**：尽管摘要、关键词和用户事实具有更聚焦的语义，单独使用这些压缩形式作为键并不能提升记忆召回性能。假设原因是检索器已经能有效处理长文本语义 [^src-3]。

**用户事实扩展效果最佳**：在所有扩展策略中，使用用户事实进行键扩展带来了最大的性能提升——平均提升 recall@k 9.4% 和最终准确率 5.4% [^src-4]。

**索引阶段合并优于检索阶段合并**：作者还比较了在检索阶段通过排名合并实现多路径检索（rank merging）的替代方案，但发现其性能远低于索引阶段的键合并。原因之一是排名合并将索引大小扩大了 m+1 倍 [^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/5_experiment.tex` -- Section 5.3 -- "we applied a simple document expansion technique, where the compressed information is concatenated with the original value to form the key during indexing"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/4_methodology.tex` -- Section 4.2 CP2 -- "summaries, keyphrases, user facts, and timestamped events are extracted from the values to augment the index. This optimization highlights the key information and enables effective retrieval with multiple pathways"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/5_experiment.tex` -- Section 5.3 -- "despite their more focused semantics, using these condensed forms alone does not enhance the memory recall performance. We hypothesize that this is due to the retriever's ability to already effectively handle long-text semantics"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/5_experiment.tex` -- Section 5.3 -- "This approach, particularly when using user facts, yielded an average improvement of 9.4% in recall@k and 5.4% in final accuracy across all models"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-longmemeval/source/text/appendix.tex` -- Section Appendix rank merging -- "rank merging has much lower performance than key merging. One potential reason is that rank merging increases the index size by m+1 times"
