---
id: poisonedrag-wikipedia-chatbot-attack
title: 大规模 Wikipedia 知识库攻击验证
status: draft
card_type: experimental-finding
tags: [poisonedrag, wikipedia, chatbot, real-world, large-scale]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-poisonedrag]
evidence_basis: experimental_paper
justification: ../justification/poisonedrag-wikipedia-chatbot-attack.md
canonical_concept: poisonedrag-wikipedia-chatbot-attack
aliases: [Wikipedia chatbot attack, 21M text knowledge base attack, Wikipedia 知识库攻击]
summary: >-
  PoisonedRAG 在包含 21,015,324 条文本的英文 Wikipedia dump (2018.12.20) 上验证有效。以此构建的 ChatBot 在注入 5 条恶意文本/目标问题后, 黑盒 ASR 达 0.94-1.0, 白盒 0.91-0.97。该实验展示攻击在真实规模知识库上的可扩展性——恶意文本占比低于百万分之一但仍能被精准检索。
related: [poisonedrag-attack-success-scaling, poisonedrag-black-box-attack, rag-knowledge-corruption-attack-surface]
---

论文使用 2018 年 12 月 20 日的英文 Wikipedia dump 构建了一个含 21,015,324 条文本的知识库（每篇文章按 100 词分割），并基于此构建 ChatBot。

**攻击结果** (注入 5 条/目标问题):
- NQ 目标问题: BB 0.95 / WB 0.97
- HotpotQA 目标问题: BB 1.0 / WB 0.94
- MS-MARCO 目标问题: BB 0.94 / WB 0.91 [^src-1]

**意义**:
- 知识库规模是之前实验的 2-8 倍 (NQ 2.68M → 21M)
- 恶意文本占比极低 (5/21M ≈ 0.000024%)
- 证明攻击可扩展至真实 Wikipedia 规模的 RAG 应用[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Wikipedia-based ChatBot" -- Table tab:real-world case study
[^src-2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Wikipedia-based ChatBot" -- "the total number of texts in the knowledge database is 21,015,324"
[^card-1]: [poisonedrag-attack-success-scaling]
