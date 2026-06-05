---
id: attention-dilution-at-scale
title: 注意力稀释导致全上下文推理在规模化时退化
status: accepted
card_type: mechanism
tags: [llm-wiki, attention, kv-cache, scaling, degradation]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
justification: ../justification/attention-dilution-at-scale.md
canonical_concept: attention-dilution-at-scale
aliases: [注意力稀释, attention dilution, 全上下文退化, 上下文规模退化]
summary: >-
  attention-dilution-at-scale（注意力稀释 / attention dilution / 全上下文退化）是全上下文
  KV cache 推理在知识规模扩大时性能退化的机制——注意力被大量无关内容稀释，导致其在规模化场景下
  表现劣于 RAG
related: [kv-cache-vs-rag-tradeoff, compilation-gap, context-window-degradation]
---

**注意力稀释（attention dilution）** 是全上下文 KV cache 推理在知识规模扩大时性能退化的核心机制[^src-1]。

在 WiCER 论文的实验中，全上下文 KV cache 推理在策展过的（curated）小规模知识上表现优于 RAG（4.38 vs. 4.08，满分 5）[^src-2]。然而当知识规模增大时，模型的注意力机制无法在大量上下文中有效聚焦于相关信息，导致性能下降至**低于 RAG**[^src-3]。

这一发现揭示了全上下文方案的根本性限制：它不是简单地"上下文越大越好"。注意力稀释为 wiki 编译提供了动机——与其将全部原始文档塞入上下文，不如编译为更紧凑的 wiki 以减少注意力负担。但编译本身又引入了编译缺口的风险，形成一个需要平衡的张力。HN 社区的实践报告独立印证了这一机制——即使名义上下文窗口达 1M，LLM 在 200k-300k 处就开始"遗忘"[^card-context-window-degradation]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-wicer/text.txt` -- Abstract -- "degrades below RAG at scale due to attention dilution"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-wicer/text.txt` -- Abstract -- "full context KV cache inference outperforms RAG on curated knowledge (4.38 vs. 4.08 out of 5, 7.3 faster TTFT)"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-wicer/text.txt` -- Abstract -- "but degrades below RAG at scale due to attention dilution"
[^card-context-window-degradation]: [上下文窗口退化现象](context-window-degradation.md) -- HN 社区报告 LLM 在 200k-300k token 处开始遗忘，为注意力稀释机制提供了来自实践的独立佐证
