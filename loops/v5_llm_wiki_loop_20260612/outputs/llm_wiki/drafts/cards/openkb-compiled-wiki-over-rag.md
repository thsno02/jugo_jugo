---
id: openkb-compiled-wiki-over-rag
title: OpenKB 编译式 Wiki 取代传统 RAG 的设计哲学
status: draft
card_type: design-philosophy
tags: [openkb, compiled-wiki, anti-rag, knowledge-accumulation, karpathy]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-vectifyai-openkb]
evidence_basis: code_implementation
justification: ../justification/openkb-compiled-wiki-over-rag.md
canonical_concept: openkb-compiled-wiki-over-rag
aliases: [OpenKB, Open Knowledge Base, compiled wiki, persistent wiki, knowledge compilation, No Vector DB]
summary: >-
  OpenKB openkb-compiled-wiki-over-rag 编译式wiki取代传统RAG;
  传统RAG每次查询从零重新发现知识无积累; OpenKB编译一次为持久wiki交叉引用已存在矛盾被标记;
  基于Karpathy概念LLM生成summaries/concept-pages/cross-references自动维护;
  知识随时间复利而非每次查询重新推导; No-Vector-DB由PageIndex提供vectorless-retrieval
related: [openkb-two-layer-architecture, openkb-pageindex-vectorless-retrieval]
---

OpenKB（Open Knowledge Base）是一个开源 CLI 系统，将原始文档编译为结构化、互链的 wiki 式知识库，其核心设计哲学是"编译式 wiki 取代传统 RAG"。[^src-1]

**与传统 RAG 的本质区别**：传统 RAG 每次查询从零重新发现知识，无积累——"Traditional RAG rediscovers knowledge from scratch on every query. Nothing accumulates." OpenKB 编译一次为持久 wiki，交叉引用已存在，矛盾被标记，综合反映所有已消化内容。[^src-2]

**设计灵感**：基于 Andrej Karpathy 描述的概念——LLM 生成摘要（summaries）、概念页（concept pages）和交叉引用（cross-references），全部自动维护。知识随时间复利（compounds over time）而非每次查询重新推导。[^src-3]

**No Vector DB** 承诺：不使用向量数据库，由 PageIndex 提供无向量的推理式检索替代嵌入检索。[^src-4]

[^src-1]: `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md` -- "What is OpenKB" P1 -- "OpenKB (Open Knowledge Base) is an open-source system (in CLI) that compiles raw documents into a structured, interlinked wiki-style knowledge base using LLMs"
[^src-2]: `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md` -- "Why not traditional RAG?" P1 -- "Traditional RAG rediscovers knowledge from scratch on every query. Nothing accumulates. OpenKB compiles knowledge once into a persistent wiki, then keeps it current."
[^src-3]: `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md` -- "What is OpenKB" P2 -- "The idea is based on a concept described by Andrej Karpathy: LLMs generate summaries, concept pages, and cross-references, all maintained automatically. Knowledge compounds over time instead of being re-derived on every query."
[^src-4]: `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md` -- "Header" P1 -- "No Vector DB"
