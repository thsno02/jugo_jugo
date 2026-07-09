---
id: poisonedrag-threat-model
title: PoisonedRAG 威胁模型
status: draft
card_type: threat-model
tags: [poisonedrag, threat-model, attacker-capability, targeted-attack]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-poisonedrag]
evidence_basis: experimental_paper
justification: ../justification/poisonedrag-threat-model.md
canonical_concept: poisonedrag-threat-model
aliases: [PoisonedRAG threat model, knowledge corruption threat model, 知识腐蚀威胁模型]
summary: >-
  PoisonedRAG 威胁模型: 攻击者选择 M 个目标问题(target questions)和对应目标答案(target answers), 目标是使 RAG 系统对这些问题生成错误的指定答案。攻击者能力: 可向知识库注入 N 条恶意文本/目标问题; 不能访问知识库原有内容; 不能访问/查询 LLM。关于检索器分黑盒(零知识)和白盒(可访问参数)两种设定。该模型下黑盒设定被认为是极强的威胁模型假设(very strong threat model)。
related: [rag-knowledge-corruption-attack-surface, poisonedrag-black-box-attack, poisonedrag-white-box-attack]
---

PoisonedRAG 的威胁模型从三个维度定义:

**攻击者目标**:
- 选择 M 个目标问题 Q_1...Q_M 和对应目标答案 R_1...R_M
- 使 RAG 系统对 Q_i 生成 R_i（错误的攻击者指定答案）
- 应用: 传播虚假信息、商业偏见推荐、金融/健康误导[^src-1]

**攻击者能力**:
- 可向知识库注入 N 条恶意文本/每个目标问题
- **不能**: 访问知识库中已有文本、访问 LLM 参数、查询 LLM[^src-2]

**两种设定**:
- **黑盒**: 不能访问 retriever 参数，也不能查询 retriever。论文称此为 "very strong threat model"
- **白盒**: 可访问 retriever 参数（如采用公开 retriever 时成立）[^src-3]

**注入方式的现实性**: 编辑 Wikipedia (Carlini et al. 证明可编辑 6.5% 的文档)、发布假新闻、内部人员注入。PoisonedRAG 仅需注入几百 token 的文本。[^src-4]

[^src-1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Problem Formulation / Threat Model / Attacker's goals" -- "an attacker could disseminate disinformation, mislead an LLM to generate biased answers"
[^src-2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Problem Formulation / Threat Model / Attacker's background knowledge" -- "cannot access texts in a knowledge database, and cannot access the parameters nor query the LLM"
[^src-3]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Threat Model" -- "Our black-box setting is considered a very strong threat model"
[^src-4]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Threat Model" -- "maliciously edit 6.5% of Wikipedia documents... a few texts (hundreds of tokens)"
[^card-1]: [rag-knowledge-corruption-attack-surface]
