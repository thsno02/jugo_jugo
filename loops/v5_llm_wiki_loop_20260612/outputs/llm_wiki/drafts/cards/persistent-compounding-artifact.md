---
id: persistent-compounding-artifact
title: LLM Wiki 作为持久性复合制品
status: draft
card_type: core_concept
tags: [llm-wiki, knowledge-management, rag-alternative, compounding]
created_time: 2026-06-12T15:00:00+08:00
edited_time: 2026-06-12T15:00:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
evidence_basis: practitioner_report
justification: ../justification/persistent-compounding-artifact.md
canonical_concept: persistent-compounding-artifact
aliases: [persistent wiki, compounding knowledge base, 持久性复合知识库]
summary: >-
  persistent-compounding-artifact 是 LLM Wiki 的核心设计理念：知识编译一次后保持更新（compiled once, kept current），区别于 RAG 每次查询从头推导；wiki 随每个 source 和每次提问累积变得更丰富
related: []
---

LLM Wiki 的核心理念是将知识库构建为一个 **持久性复合制品** (persistent compounding artifact)。与 RAG 系统在每次查询时"从头重新发现知识"不同，LLM Wiki 由 LLM 增量构建并维护一个持久化 wiki——结构化、互链的 markdown 文件集合。[^src-1]

关键差异在于知识的生命周期：RAG 模式下"nothing is built up"，每次需要合成多文档的微妙问题时都必须重新查找拼凑；而 LLM Wiki 中"the knowledge is compiled once and then kept current, not re-derived on every query"。[^src-2]

这种设计使得 wiki 中的交叉引用已经就位、矛盾已经被标记、综合已经反映了所有已读内容。每添加一个 source 或提出一个问题，wiki 都变得更丰富。[^src-3]

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P1 -- "Instead of just retrieving from raw documents at query time, the LLM incrementally builds and maintains a persistent wiki"
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P2 -- "The knowledge is compiled once and then kept current, not re-derived on every query."
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P3 -- "the wiki is a persistent, compounding artifact. The cross-references are already there. The contradictions have already been flagged."
