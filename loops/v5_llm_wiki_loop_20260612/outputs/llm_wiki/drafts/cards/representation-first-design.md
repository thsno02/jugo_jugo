---
id: representation-first-design
title: Representation-First 多模态设计
status: draft
card_type: design-principle
tags: [representation-first, multimodal, ingest, pdf, image, ocr]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [clawhub-llm-wiki-karpathy]
evidence_basis: documentation
justification: ../justification/representation-first-design.md
canonical_concept: representation-first-design
aliases: [representation-first, 表示优先, multimodal ingest model, 多模态摄入模型]
summary: >-
  representation-first-design 表示优先多模态设计要求非文本资产（PDF/images）
  必须先经过中间表示（OCR text/vision/metadata）存入 .llm-kb/representations/，
  才可编译为最终 source note。运行时不自行执行 OCR/vision，而是为 agent 提供
  canonical 存储位置并在 lint 时验证 review trail。文本/结构化数据仍可直接编译。
related: []
---

## Representation-First 多模态设计

llm-wiki-karpathy v0.4.4 的核心设计理念是 "representation-first"，显式支持多模态摄入 [^src-1]。

### 两条摄入路径

| 资产类型 | 路径 | 关键命令 |
|----------|------|----------|
| 文本/结构化数据 (.md,.txt,.csv,.json 等) | 直接编译 | `kb_prepare_source` + `kb_read_raw` |
| PDF/图片 (.pdf,.png,.jpg 等) | Representation-first | inspect -> store representations -> compile |

### Representation-First 路径步骤

1. 使用 `kb_get_raw_asset` 检视资产元数据与安全路径
2. 使用 `kb_prepare_source_bundle` 检查 compile readiness
3. 将中间制品（OCR、vision、page notes、metadata、profiles）存入 `.llm-kb/representations/`
4. 在 representation trail 就位后编译最终 source note

### 关键设计决策

运行时本身不执行 OCR 或 vision [^src-2]。它只提供：
- 为 agent 存储中间制品的 canonical 位置
- 验证最终 wiki 页面确实基于这些制品（通过 lint 检查 representation trail）

[^src-1]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "What 0.4.4 Implements" P14 -- "This release makes the runtime representation-first and explicitly multimodal"
[^src-2]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "Multimodal Ingest Model" P40 -- "The runtime intentionally does not perform OCR or vision itself"
