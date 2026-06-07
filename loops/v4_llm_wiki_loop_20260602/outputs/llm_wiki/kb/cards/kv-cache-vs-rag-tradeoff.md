---
id: kv-cache-vs-rag-tradeoff
title: KV cache 推理与 RAG 的性能权衡
status: accepted
card_type: source_claim
tags: [llm-wiki, kv-cache, rag, performance, latency, tradeoff]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
justification: ../justification/kv-cache-vs-rag-tradeoff.md
canonical_concept: kv-cache-vs-rag-tradeoff
aliases: [KV cache vs RAG, KV缓存与RAG权衡, 全上下文vs检索增强]
summary: >-
  kv-cache-vs-rag-tradeoff（KV cache vs RAG / KV缓存与RAG权衡）是 WiCER 论文在 17 个
  RepLiQA 领域上的实证发现：全上下文 KV cache 推理在策展知识上优于 RAG（4.38 vs 4.08，TTFT
  快 7.3 倍），但因注意力稀释在规模化时退化至低于 RAG
related: [attention-dilution-at-scale, compilation-gap, compile-time-vs-query-time, full-context-anti-rag, memory-vs-rag-salience]
---

WiCER 论文在 17 个 RepLiQA 领域（6,800 个问题）上对全上下文 KV cache 推理与 RAG 进行了系统性基准对比，揭示了一个**规模依赖的性能交叉**[^src-1]：

**小规模策展知识（curated knowledge）下 KV cache 占优**：全上下文 KV cache 推理的质量评分为 4.38（满分 5），优于 RAG 的 4.08。同时，首字节延迟（TTFT）快 7.3 倍，实现了亚秒级的上下文访问[^src-2]。

**规模扩大时 KV cache 退化**：当知识量增大到超出策展范围时，全上下文推理因注意力稀释（attention dilution）退化至低于 RAG[^src-3]。

这一发现的实践意义在于：LLM Wiki 的全上下文方案并非在所有场景下优于 RAG。它的优势区间是知识经过策展、规模有界的场景——正好对应 wiki 编译的目标产出。这为编译操作提供了双重动机：既是为了持久化知识，也是为了将知识压缩到注意力机制能有效处理的范围内。Karpathy LLM Wiki 插件明确选择全上下文反 RAG 策略，其有效前提恰好是 WiCER 识别的优势区间——策展过的紧凑 wiki[^card-full-context-anti-rag]。Mem0 的独立实验从另一个维度印证了 RAG 的局限：提取显著事实的记忆系统在 LOCOMO 基准上一致优于所有 RAG 配置，且 token 消耗远低于 RAG 文本块[^card-1]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- Abstract -- "we observe that full context KV cache inference outperforms RAG on curated knowledge (4.38 vs. 4.08 out of 5, 7.3 faster TTFT) but degrades below RAG at scale due to attention dilution"
[^src-2]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- Abstract -- "4.38 vs. 4.08 out of 5, 7.3 faster TTFT"
[^src-3]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- Abstract -- "degrades below RAG at scale due to attention dilution"
[^card-full-context-anti-rag]: [全上下文反 RAG 架构选择](full-context-anti-rag.md) -- Karpathy LLM Wiki 拒绝 RAG 分块检索、向 LLM 提供完整 wiki 上下文的设计哲学，其有效性依赖于 wiki 保持策展紧凑——正好对应 WiCER 识别的全上下文优势区间
[^card-1]: [记忆系统 vs RAG 的显著性优势](memory-vs-rag-salience.md) -- 本卡从 WiCER 实证表明全上下文 KV cache 在策展知识上优于 RAG，该卡从 Mem0 实验表明结构化记忆在显著性提取上优于 RAG，两项独立研究从不同机制印证 RAG 替代方案的优势
