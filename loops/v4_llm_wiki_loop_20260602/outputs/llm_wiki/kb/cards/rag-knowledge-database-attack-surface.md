---
id: rag-knowledge-database-attack-surface
title: RAG 知识库作为新攻击面
status: accepted
card_type: concept
tags: [rag, security, attack-surface, knowledge-database, poisoning]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-poisonedrag]
justification: ../justification/rag-knowledge-database-attack-surface.md
canonical_concept: rag-knowledge-database-attack-surface
aliases: [RAG知识库攻击面, knowledge database attack surface, RAG外部知识攻击向量]
summary: >-
  rag-knowledge-database-attack-surface（RAG知识库攻击面 / knowledge database attack surface）RAG 系统的知识库引入了一个新的、实用的攻击面：攻击者可通过向知识库注入少量恶意文本来操纵 LLM 生成攻击者指定的错误答案。
related: []
  - rag-retrieval-generation-dual-condition
  - rag-knowledge-corruption-attack
---

RAG 系统由知识库、检索器和 LLM 三个组件构成。其中知识库从 Wikipedia、新闻文章、金融文档等多种来源收集文本 [^src-1]。PoisonedRAG 论文发现，这些知识库引入了一个**新的、实用的攻击面**（new and practical attack surface）：攻击者可以通过向知识库注入恶意文本来诱使 LLM 生成攻击者选择的目标答案 [^src-2]。

具体的注入途径包括：恶意编辑 Wikipedia 页面（已有研究表明可编辑 6.5% 的 Wikipedia 文档）、发布虚假新闻或托管恶意网站、以内部人员身份向企业私有知识库注入文本 [^src-3]。这一攻击面的关键特性在于：攻击者不需要访问知识库中的已有文本，不需要访问或查询 LLM 的参数，甚至在黑盒设定下也不需要访问检索器的参数 [^src-4]。

这与传统的数据投毒攻击不同。传统攻击通过篡改 LLM 或检索器的训练数据来改变模型行为，这在 RAG 系统采用大型科技公司（如 Meta、Google）发布的 LLM 或检索器时难以实现。而知识库攻击面允许攻击者直接操作外部数据源，绕过了模型层面的安全保障 [^src-5]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "background.tex" -- "The database contains a set of texts collected from various sources such as Wikipedia, news articles, and financial documents."
[^src-2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "introduction.tex" -- "we find that knowledge databases of RAG systems introduce a new and practical attack surface"
[^src-3]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "introduction.tex" -- "an attacker could inject malicious texts by maliciously editing Wikipedia pages; an attacker could also post fake news or host malicious websites to inject malicious texts when the knowledge databases are collected from the Internet; an insider can inject malicious texts into an enterprise private knowledge database."
[^src-4]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "preliminary.tex" -- "We consider that an attacker cannot access texts in a knowledge database, and cannot access the parameters nor query the LLM."
[^src-5]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "background.tex" -- "our attacks do not poison the training dataset of a LLM or a retriever. Instead, our attacks exploit the new and practical attack surface introduced by knowledge databases of RAG systems."
