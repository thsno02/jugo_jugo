---
id: cache-augmented-generation
title: 缓存增强生成（CAG）
status: draft
card_type: 相关概念
tags: [cag, kv-cache, knowledge-serving, rag-alternative]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
evidence_basis: experimental_paper
justification: ../justification/cache-augmented-generation.md
canonical_concept: cache-augmented-generation
aliases: [CAG, Cache-Augmented Generation, 缓存增强生成, cache-augmented generation]
summary: >-
  Cache-Augmented Generation (CAG, Chan et al. 2025) 形式化了将所有相关知识预加载至 LLM 上下文并缓存 KV 状态以零检索开销服务查询的方法。CAG 完全消除检索失败但继承 lost-in-the-middle 问题。WiCER 论文认为 full-context KV cache 推理是 LLM Wiki pattern 和 CAG 的实际可部署实现。该论文据称提供了这些思想的首个大规模实证测试(17 域 6800 问题)。
related: []
---

缓存增强生成（Cache-Augmented Generation, CAG）由 Chan et al. (2025, WWW) 形式化，提出将所有相关知识预加载至 LLM 上下文并缓存 KV 状态，以零检索开销服务查询。[^src-1]

**核心思想**：
- 预加载全部相关知识到 LLM 上下文
- 缓存产生的 KV 状态
- 后续查询直接复用缓存，无需检索步骤

**与 RAG 的关系**：CAG 完全消除检索失败（retrieval failure），但继承了 lost-in-the-middle 问题——当文档数增长时质量退化。

**WiCER 论文的定位**：该论文将 full-context KV cache 推理视为 LLM Wiki pattern 和 CAG 的"实际可部署实现"（practical, deployable implementation），并据称提供了这些思想的首个大规模实证测试，量化了编译后单上下文何时崩溃。[^src-2]

**局限**：CAG（和 full-context 推理）受限于上下文窗口大小。当文档集超出窗口（如 RepLiQA 中 Regional Cuisine 和 Regional Folklore 超出 96K），方法不可用。

[^src-1]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "Related Work / Knowledge Compilation and CAG" P433-446 -- "Chan et al. formalize this as Cache-Augmented Generation (CAG): preload all relevant knowledge...cache the KV states"
[^src-2]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "Introduction" P331-337 -- "full-context KV cache inference is a practical, deployable implementation of the LLM Wiki pattern"

[^card-14]: [[llm-wiki-pattern]] 的同族概念
[^card-15]: [[attention-dilution-crossover]] 展示了 CAG 继承的 lost-in-the-middle 问题
