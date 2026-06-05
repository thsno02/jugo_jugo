---
id: full-context-anti-rag
title: 全上下文反 RAG 架构选择
status: accepted
card_type: distinction
tags: [llm-wiki, rag, full-context, architecture, karpathy, long-context]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
justification: ../justification/full-context-anti-rag.md
canonical_concept: full-context-anti-rag
aliases: [反 RAG, anti-RAG, 全上下文策略, full-context approach, 非分块检索]
summary: >-
  full-context-anti-rag（反 RAG / anti-RAG / 全上下文策略 / full-context approach）
  是 Karpathy LLM Wiki 的核心架构选择：拒绝 RAG 分块检索，改为向 LLM 提供完整 Wiki 上下文，
  理由是 RAG 碎片化知识并破坏跨知识图谱推理能力，因此强烈推荐 1M+ token 长上下文模型
related:
  - llm-wiki-pattern
  - three-layer-architecture
  - rag-wiki-synthesis-distinction
  - llm-wiki-rag-depth-distinction
---

Karpathy LLM Wiki 插件明确**拒绝 RAG（Retrieval-Augmented Generation）架构**，选择将完整 Wiki 上下文提供给 LLM[^src-1]。

**核心论据**：Karpathy 的原始批评认为，RAG 将知识碎片化，破坏了 LLM 跨整个知识图谱进行推理的能力[^src-2]。与 ChatGPT「知道互联网」不同，LLM Wiki「知道你教给它的内容」，每个回答都通过 [[wiki-links]] 连回知识图谱，是「一个起点而非死胡同」[^src-3]。

**架构后果**：这一立场直接导致插件**强烈推荐长上下文模型**——Wiki 越大，LLM 需要的上下文越多[^src-4]。材料推荐的模型均具备 1M+ token 上下文窗口（DeepSeek V4-Flash、Gemini-3.5-Flash、Qwen3.6-Plus 等为「性价比之选」），并指出本地模型（Ollama）的上下文通常较小（8K-128K），建议将云端用于摄入、本地用于查询[^src-5]。

**与 RAG 的关键区别**：RAG 方案通常将文档切块后存入向量数据库，查询时检索相关块；LLM Wiki 方案则将整个 Wiki（或大部分页面）作为上下文一次性提供给 LLM，依赖模型的长上下文推理而非检索管道[^src-1]。WiCER 论文的实证研究为这一哲学提供了有条件的支持：全上下文 KV cache 推理在策展过的小规模知识上确实优于 RAG（4.38 vs 4.08），但在知识规模扩大时因注意力稀释退化至低于 RAG[^card-kv-cache-vs-rag-tradeoff]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/obsidian-community-plugin/text.txt` -- "Model Selection Guide" L343-344 -- "This plugin follows Karpathy's philosophy: feed the LLM full Wiki context, not chunked RAG retrieval. Long-context models are strongly recommended"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/obsidian-community-plugin/text.txt` -- "Model Selection Guide" L347 -- "Why not RAG? Karpathy's original critique argues that RAG fragments knowledge and breaks the LLM's ability to reason across the full knowledge graph."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/obsidian-community-plugin/text.txt` -- "What is LLM-Wiki?" L114 -- "ChatGPT knows the internet. LLM-Wiki knows you — or rather, what you've taught it. Every answer carries [[wiki-links]] back into your knowledge graph. Every response is a trailhead, not a dead end."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/obsidian-community-plugin/text.txt` -- "Model Selection Guide" L343 -- "the larger your Wiki grows, the more context the LLM needs"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/obsidian-community-plugin/text.txt` -- "Model Selection Guide" L370 -- "For local models (Ollama): context windows are typically smaller (8K-128K). Consider using a cloud provider for ingestion + local model for query."
[^card-kv-cache-vs-rag-tradeoff]: [KV cache 推理与 RAG 的性能权衡](kv-cache-vs-rag-tradeoff.md) -- WiCER 实证表明全上下文在策展知识上优于 RAG 但在规模化时退化，为 Karpathy 反 RAG 立场划定了有效边界：wiki 越紧凑策展越充分，全上下文优势越大
