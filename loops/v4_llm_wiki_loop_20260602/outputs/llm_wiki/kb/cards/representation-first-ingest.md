---
id: representation-first-ingest
title: 表示先行摄入模型
status: accepted
card_type: mechanism
tags: [llm-wiki, ingest, multimodal, representation, compile-readiness]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [clawhub-llm-wiki-karpathy]
justification: ../justification/representation-first-ingest.md
canonical_concept: representation-first-ingest
aliases: [表示先行, representation-first, 多模态摄入, multimodal ingest, 两路径摄入]
summary: >-
  representation-first-ingest（表示先行 / 多模态摄入 / 两路径摄入）llm-wiki-karpathy 运行时的双路径摄入机制：文本/结构化数据直接编译，PDF/图片须先存储中间表示（OCR、视觉描述等）至 .llm-kb/representations/ 后方可编译，运行时自身不执行 OCR/视觉处理
related: [ingest-operation, runtime-agent-boundary]
---

llm-wiki-karpathy 运行时（v0.4.4）实现了双路径摄入模型，被称为「representation-first」[^src-1]：

**路径一：文本与结构化数据**——`.md`、`.txt`、`.csv`、`.tsv`、`.json`、`.html` 等可直接从 `raw/` 目录通过 `kb_prepare_source` 和 `kb_read_raw` 编译为 wiki 源笔记[^src-2]。

**路径二：PDF 与图片**——`.pdf`、`.png`、`.jpg` 等非文本资产需经过四步流程[^src-3]：
1. 通过 `kb_get_raw_asset` 检查资产元数据
2. 通过 `kb_prepare_source_bundle` 检查编译就绪状态
3. 将中间产物（OCR 文本、视觉描述、页面笔记、元数据、档案）存储到 `.llm-kb/representations/` 目录下
4. 仅当表示链（representation trail）完整后才编译最终源笔记

关键设计决策：运行时**有意不执行** OCR 或视觉处理本身。它为代理（agent）提供中间产物的规范存储位置，然后验证最终 wiki 页面是否基于这些中间产物[^src-4]。

编译就绪状态有三种：`ready`、`partial`、`needs_representation`[^src-5]。`kb_prepare_source_bundle` 作为运行时与代理之间的桥梁，返回原始元数据、已审查的资产引用、已存储的表示和就绪状态[^src-6]。本卡描述的双路径机制是 Karpathy LLM Wiki 摄入操作的具体实现之一[^card-1]。

## Footnotes

[^card-1]: [摄入操作](ingest-operation.md) -- 本卡描述双路径摄入的具体实现机制（文本直编译 vs. 多模态先存表示），该卡定义摄入操作的通用流程与人类参与谱系

[^src-1]: `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` -- "What 0.4.4 Implements" -- "This release makes the runtime representation-first and explicitly multimodal"
[^src-2]: `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` -- "Multimodal Ingest Model" -- "Text and structured data can still compile directly from raw/ with kb_prepare_source and kb_read_raw."
[^src-3]: `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` -- "Multimodal Ingest Model" -- "PDFs and images use a representation-first path: inspect the asset with kb_get_raw_asset ... compile the final source note only after the representation trail is present"
[^src-4]: `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` -- "Multimodal Ingest Model" -- "The runtime intentionally does not perform OCR or vision itself. Instead, it gives agents a canonical place to store those intermediate artifacts and then validates that the final wiki pages stay grounded in them."
[^src-5]: `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` -- "What 0.4.4 Implements" -- "compile-readiness tracking with ready, partial, and needs_representation"
[^src-6]: `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` -- "Runtime Philosophy" -- "kb_prepare_source_bundle is the bridge between those layers for non-text assets: it returns the exact raw metadata, reviewed asset refs, stored representations, and readiness state the agent needs before compiling a source note."
