---
id: explicit-out-of-scope-boundaries
title: 运行时显式排除边界
status: accepted
card_type: design-constraint
tags:
- out-of-scope
- design-boundary
- embeddings
- vector-search
- ocr
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- clawhub-llm-wiki-karpathy
evidence_basis: documentation
justification: ../justification/explicit-out-of-scope-boundaries.md
canonical_concept: explicit-out-of-scope-boundaries
aliases:
- still out of scope
- 排除范围
- 不实现功能
summary: explicit-out-of-scope-boundaries llm-wiki-karpathy 显式排除五项功能： embeddings/vector
  search、database-backed indexing、rename tracking、 built-in OCR/vision/PDF parsing、autonomous
  background agents。 体现运行时只管确定性结构而将智能工作交给外部 agent 的设计哲学。
related:
- karpathy-llmc-minimalism-philosophy
- llm-wiki-intentional-abstraction
- karpathy-llm-wiki-concept
---

## 运行时显式排除边界

llm-wiki-karpathy 明确声明以下功能不在 runtime 范围内 [^src-1]：

1. **Embeddings or vector search** — 不内置向量检索
2. **Database-backed indexing** — 不依赖数据库索引
3. **Rename tracking** — 不追踪重命名
4. **Built-in OCR, vision, or PDF parsing** — 不内置任何感知能力
5. **Autonomous background agents** — 不包含自主后台 agent

这些排除与 runtime philosophy 一致：runtime 专注确定性的结构管理，所有需要智能判断的工作（包括 OCR/vision/embedding）由外部 agent 负责 [^src-2]。

[^src-1]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "Still Out of Scope" P122-127 -- "This package still does not implement:"
[^src-2]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "Runtime Philosophy" P112-113 -- "The agent owns: summarization, OCR, vision, or profiling work performed outside the runtime"
[^card-2]: [[runtime-agent-responsibility-boundary]] — 排除边界是职责划分原则的具体推论
