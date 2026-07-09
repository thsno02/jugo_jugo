---
id: poisonedrag-dual-condition-framework
title: PoisonedRAG 双条件框架
status: draft
card_type: attack-methodology
tags: [poisonedrag, retrieval-condition, generation-condition, optimization]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-poisonedrag]
evidence_basis: experimental_paper
justification: ../justification/poisonedrag-dual-condition-framework.md
canonical_concept: poisonedrag-dual-condition-framework
aliases: [retrieval condition and generation condition, 检索条件与生成条件, two necessary conditions]
summary: >-
  PoisonedRAG 将有效的知识腐蚀攻击分解为两个必要条件(necessary conditions): (1) retrieval condition——恶意文本 P 必须被检索器为目标问题检索出; (2) generation condition——当 P 作为上下文时 LLM 必须生成攻击者指定的目标答案。两个条件分别从优化问题的约束(Eq.1)和目标函数(Eq.0)推导而来。PoisonedRAG 的核心设计围绕同时满足这两个条件展开。
related: [rag-knowledge-corruption-attack-surface, poisonedrag-malicious-text-decomposition]
---

PoisonedRAG 将知识腐蚀攻击形式化为一个受约束优化问题: 最大化攻击成功率(ASR)，约束条件为检索过程从被污染的知识库中选取 top-k 文本。[^src-1]

从该优化问题中推导出两个必要条件:

1. **Retrieval condition (检索条件)**: 恶意文本 P 必须出现在目标问题 Q 的 top-k 检索结果中。即 P 的 embedding 向量需与 Q 具有高相似度。[^src-2]

2. **Generation condition (生成条件)**: 当 P 单独作为上下文时，LLM 应当生成攻击者指定的目标答案 R。这样当 P 与其他文本（恶意或干净的）共同作为上下文时，LLM 更可能生成 R。[^src-3]

两个条件可能存在冲突——极度满足检索条件（如令 P=Q）可能无法满足生成条件。PoisonedRAG 的核心技术贡献即为解决该冲突。[^card-1]

[^src-1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Problem Formulation / Knowledge Corruption Attack to RAG" -- "we formulate knowledge corruption attacks to RAG as a constrained optimization problem"
[^src-2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Design of PoisonedRAG / Deriving Two Necessary Conditions" -- "the embedding vectors produced by a retriever for the malicious text P and the target question Q should be similar"
[^src-3]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Design of PoisonedRAG / Deriving Two Necessary Conditions" -- "the LLM should generate the target answer R when P alone is used as the context for the target question Q"
[^card-1]: [rag-knowledge-corruption-attack-surface]
