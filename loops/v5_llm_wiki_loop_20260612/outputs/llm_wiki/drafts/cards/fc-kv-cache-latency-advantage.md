---
id: fc-kv-cache-latency-advantage
title: Full-context KV Cache 的延迟优势
status: draft
card_type: 实验发现
tags: [kv-cache, latency, ttft, inference-performance, rag-comparison]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
evidence_basis: experimental_paper
justification: ../justification/fc-kv-cache-latency-advantage.md
canonical_concept: fc-kv-cache-latency-advantage
aliases: [KV cache latency advantage, full-context TTFT, FC vs RAG latency, 全上下文延迟优势]
summary: >-
  Full-context KV cache 推理在热缓存后实现亚秒 TTFT: Policygenius 67K tokens 中位 0.86s(RAG 6.28s, 7.3x 更快), RepLiQA 55-95K tokens 中位 1.04s(RAG 4.83s, 4.6x 更快)。机制为热查询仅处理约 20-30 新 tokens 对比缓存的 67K 前缀。RAG 吞吐量更高(30.7 vs 12.0 tok/s)因注意力跨度短。编译后 wiki 进一步降低至 sub-400ms TTFT(wiki-moderate 0.21s, 12.7x 快于 RAG)。RTX 4090 预计热 TTFT ~0.2s, 几乎消除 RAG 延迟优势。
related: []
---

Full-context KV cache 推理在热缓存条件下实现显著的 TTFT（Time-to-First-Token）优势。[^src-1]

**Policygenius（30 文档, 67K tokens）**：
- FC 热 TTFT 中位数：0.857s（P5/P95: 0.534/1.053s）
- RAG TTFT 中位数：6.277s（P5/P95: 4.483/7.697s）
- FC/RAG TTFT 比率：7.3x 更快
- 机制：热查询仅处理约 20 新 tokens 对比已缓存的 67K 前缀

**RepLiQA（80 文档/主题, 55-95K tokens）**：
- FC Q8 TTFT 中位数：1.040s
- RAG TTFT 中位数：4.825s
- FC/RAG 比率：约 4.6x（比率降低因 RepLiQA 更大语料使 FC TTFT 比例增加更多）[^src-2]

**吞吐量权衡**：RAG 因注意力跨度更短实现 2.6x 更高生成吞吐量（30.74 vs 12.01 tok/s），使总响应时间接近（7.93s vs 6.39s）。

**编译 wiki 的进一步延迟优势**：
- Wiki-light (约 24K 词): 0.380s, 2.8x 快于 FC raw
- Wiki-moderate (约 8K 词): 0.211s, 5.0x 快于 FC raw, 12.7x 快于 RAG
- Wiki-aggressive (约 6K 词): 0.195s, 5.6x 快于 FC raw[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "Full-Context KV Cache / Timing" P586-614 -- Table 2 timing comparison
[^src-2]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "The Scalability Gap / RAG timing" P640-646 -- "full-context TTFT advantage of ~4.6x on average"
[^src-3]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "Wiki Compilation Timing" P1312-1344 -- Table wiki_timing

[^card-12]: [[llm-wiki-pattern]] 的核心延迟优势，即使编译质量有损仍保持
[^card-13]: 与 [[attention-dilution-crossover]] 的互补：延迟优势持续但质量优势逆转
