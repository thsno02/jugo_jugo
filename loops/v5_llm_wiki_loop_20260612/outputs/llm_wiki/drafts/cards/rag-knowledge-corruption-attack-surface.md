---
id: rag-knowledge-corruption-attack-surface
title: RAG 知识库作为新攻击面
status: draft
card_type: security-concept
tags: [rag, attack-surface, knowledge-database, poisoning]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-poisonedrag]
evidence_basis: experimental_paper
justification: ../justification/rag-knowledge-corruption-attack-surface.md
canonical_concept: rag-knowledge-corruption-attack-surface
aliases: [knowledge database attack surface, RAG 新攻击面, knowledge corruption attack]
summary: >-
  RAG 系统的知识库(knowledge database)引入了一个新的、实际可利用的攻击面(attack surface)。攻击者可向知识库注入少量恶意文本(malicious texts)，使 LLM 对特定目标问题生成攻击者指定的错误答案。攻击途径包括恶意编辑 Wikipedia 页面、发布虚假新闻或托管恶意网站、内部人员注入等。PoisonedRAG 是首个利用该攻击面的 knowledge corruption attack。
related: [poisonedrag-dual-condition-framework, poisonedrag-malicious-text-decomposition]
---

RAG 系统包含三个组件: 知识库、检索器(retriever)和 LLM。其中知识库通常从 Wikipedia、新闻文章、金融文档等外部来源收集文本，本身具有开放可写性。PoisonedRAG 论文指出该组件引入了一个新的、实际可利用的攻击面——攻击者无需修改 LLM 或 retriever 的参数/训练数据，仅需向知识库注入恶意文本即可操纵 RAG 的输出。[^src-1]

据材料所述，现实攻击途径包括: (1) 恶意编辑 Wikipedia（已有研究表明可恶意编辑 6.5% 的 Wikipedia 文档[Carlini et al. 2023]）; (2) 在互联网发布虚假信息以被知识库爬取; (3) 企业内部人员直接向私有知识库注入文本。[^src-2]

与现有的 data poisoning attack（修改 LLM/retriever 训练数据）不同，knowledge corruption attack 仅需修改部署时的知识库内容，攻击门槛更低、更实际。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Introduction" -- "we find that knowledge databases of RAG systems introduce a new and practical attack surface"
[^src-2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Introduction" -- "an attacker could inject malicious texts by maliciously editing Wikipedia pages"
[^src-3]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Background/Existing Data Poisoning Attacks" -- "our attacks do not poison the training dataset of a LLM or a retriever. Instead, our attacks exploit the new and practical attack surface introduced by knowledge databases"
