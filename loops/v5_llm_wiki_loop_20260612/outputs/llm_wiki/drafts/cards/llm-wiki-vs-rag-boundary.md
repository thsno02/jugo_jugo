---
id: llm-wiki-vs-rag-boundary
title: LLM Wiki 与 RAG 的适用边界
status: draft
card_type: comparison
tags: [llm-wiki, rag, vector-database, scaling, multi-hop-reasoning]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [anthemcreation-fr-guide]
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-vs-rag-boundary.md
canonical_concept: llm-wiki-vs-rag-boundary
aliases: [LLM wiki vs RAG, wiki versus vector search, LLM wiki 与 RAG 对比]
summary: >-
  LLM wiki 适合个人级 10~数百文档的深度知识管理，优势在于多跳推理（multi-hop reasoning）和预合成知识；RAG 适合大规模非结构化语料库的即席检索。转折点在规模：超过数百文档需 vector database。两者非互斥，可混合部署。核心差异非速度而是推理深度。
related: [llm-wiki-compilation-analogy, llm-wiki-model-quality-risk]
---

材料将 LLM wiki 与 RAG 明确定位为互补而非互斥的方案 [^src-1]：

**LLM wiki 优势领域**：
- 个人级知识管理（10~数百文档）
- 多跳推理（raisonnement multi-hop）：关联三个不同概念回答复杂问题
- 预合成知识：矛盾已解决、链接已建立、综合已完成

**RAG 优势领域**：
- 大规模非结构化语料库
- 即席检索（requêtes ponctuelles）

**转折点**：材料据 Karpathy 指出，100 篇文章规模下 markdown 结构完全够用；超过此规模进入数千 chunk 的语义搜索需求时，vector database 才变得必要 [^src-2]。

核心区分不在速度而在推理深度——RAG 从 passage 级别生成答案，LLM wiki 从已合成的结构化知识回答 [^src-3] [^card-1]。

[^src-1]: `data/raw/webpage/anthemcreation-fr-guide/markdown.md` -- "LLM wiki vs. RAG" P44 -- "Le RAG reste pertinent pour des corpus massifs et des requêtes ponctuelles sur des bases non structurées. La LLM wiki, elle, excelle dans un registre différent : la connaissance personnelle à échelle individuelle"
[^src-2]: `data/raw/webpage/anthemcreation-fr-guide/markdown.md` -- "LLM wiki vs. RAG" P46 -- "Pour des wikis de 100 articles, le markdown structuré suffit largement. La vector database devient utile seulement au-delà d'une certaine échelle"
[^src-3]: `data/raw/webpage/anthemcreation-fr-guide/markdown.md` -- "LLM wiki vs. RAG" P45 -- "La différence fondamentale n'est pas la vitesse, c'est la profondeur du raisonnement."
[^card-1]: [[llm-wiki-compilation-analogy]] — 预编译 vs 每次重新推导的哲学基础
