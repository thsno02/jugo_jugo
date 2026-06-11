---
id: llm-wiki-explicit-non-scope
title: LLM Wiki 显式非范围声明
status: accepted
card_type: design-decision
tags: [llm-wiki, scope, architecture, design-boundary, simplicity]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [clawhub-llm-wiki-karpathy]
justification: ../justification/llm-wiki-explicit-non-scope.md
canonical_concept: llm-wiki-explicit-non-scope
aliases: [out of scope, 显式非范围, still out of scope, 不实现清单]
summary: >-
  llm-wiki-explicit-non-scope（显式非范围 / out of scope / 不实现清单）llm-wiki-karpathy 运行时显式声明五项不实现：无向量搜索/嵌入、无数据库索引、无重命名追踪、无内置 OCR/视觉/PDF 解析、无自主后台代理
related: [runtime-agent-boundary, representation-first-ingest]
---

llm-wiki-karpathy 运行时在文档中显式维护一份「Still Out of Scope」清单，声明五项有意不实现的能力[^src-1]：

1. **无嵌入或向量搜索（embeddings or vector search）**——知识检索依赖确定性的全文搜索（`kb_search`）和结构化索引，不引入嵌入模型
2. **无数据库索引（database-backed indexing）**——所有状态存储在文件系统中的 JSON/JSONL/Markdown 文件，不依赖外部数据库
3. **无重命名追踪（rename tracking）**——文件重命名后通过 `kb_repair_source_ids` 显式修复引用，不自动追踪
4. **无内置 OCR、视觉或 PDF 解析（built-in OCR, vision, or PDF parsing）**——运行时提供存储位置和验证，实际处理由外部代理完成
5. **无包内自主后台代理（autonomous background agents）**——运行时是被动工具，不包含自主运行的代理进程

这一显式非范围声明体现了两个架构价值观：

**文件系统优先**——拒绝数据库和嵌入意味着整个知识库可以用 `git`、`grep`、`find` 等标准 Unix 工具操作，对人类和 LLM 代理同样可审计[^src-1]。

**运行时-代理分离的一致性**——不内置 OCR/视觉/自主代理，保持了运行时作为确定性工具的定位，所有需要智能的操作一律外推给调用方代理[^src-2]。

## Footnotes

[^src-1]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "Still Out of Scope" -- "This package still does not implement: embeddings or vector search, database-backed indexing, rename tracking, built-in OCR, vision, or PDF parsing inside the runtime itself, autonomous background agents inside the package"
[^src-2]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "Runtime Philosophy" -- "The runtime intentionally does not perform OCR or vision itself."
