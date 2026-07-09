---
id: openkb-pageindex-vectorless-retrieval
title: PageIndex 无向量推理式长文档检索
status: accepted
card_type: retrieval-technique
tags:
- pageindex
- vectorless-retrieval
- reasoning-based-retrieval
- hierarchical-tree-index
- long-document
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- repo-vectifyai-openkb
evidence_basis: code_implementation
justification: ../justification/openkb-pageindex-vectorless-retrieval.md
canonical_concept: pageindex-vectorless-retrieval
aliases:
- PageIndex
- vectorless retrieval
- reasoning-based retrieval
- document tree
- hierarchical tree index
- No Vector DB
summary: PageIndex pageindex-vectorless-retrieval 无向量推理式检索; 构建分层树索引hierarchical-tree-index LLM读树索引而非全文实现reasoning-based-retrieval; 短文档markitdown转Markdown直读全文 长PDF>=20页用PageIndex索引; 本地运行开源版无外部依赖; 可选PageIndex-Cloud提供OCR更快结构生成大文档扩展
related:
- openkb-compiled-wiki-over-rag
- openkb-two-layer-architecture
- llm-wiki-plain-file-storage
---

PageIndex 是 OpenKB 的长文档检索引擎，实现无向量（vectorless）、基于推理（reasoning-based）的文档检索。其核心机制是将长文档构建为分层树索引（hierarchical tree index），LLM 读取树索引而非全文，从而实现上下文感知的检索。[^src-1] [^card-1]

**短文档 vs 长文档处理分界**：短文档经 markitdown 转换为 Markdown 后由 LLM 直接阅读全文；长 PDF（≥20 页，阈值可配置为 `pageindex_threshold`）由 PageIndex 索引为树结构加摘要，LLM 读树而非原文。两种路径最终产出相同结果——summary + concepts。[^src-2]

PageIndex 本地运行开源版本，无外部依赖。可选 PageIndex Cloud 提供额外能力：OCR 支持（扫描 PDF，通过托管 VLM 模型）、更快结构生成、大文档可扩展索引。通过设置 `PAGEINDEX_API_KEY` 启用云端功能。[^src-3]

[^card-1]: 参见 [[openkb-compiled-wiki-over-rag]] 关于 OpenKB 不使用向量数据库的设计选择
[^src-1]: `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md` -- "PageIndex Integration" P1 -- "PageIndex solves this with vectorless, reasoning-based retrieval — building a hierarchical tree index that lets LLMs reason over the index for context-aware retrieval."
[^src-2]: `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md` -- "Short vs. Long Document Handling" P1 -- table and "Long PDFs are indexed by PageIndex into a hierarchical tree with summaries. The LLM reads the tree instead of the full text"
[^src-3]: `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md` -- "Optional: Cloud Support" P1 -- "OCR support for scanned PDFs (via hosted VLM models), Faster structure generation, Scalable indexing for large documents"
