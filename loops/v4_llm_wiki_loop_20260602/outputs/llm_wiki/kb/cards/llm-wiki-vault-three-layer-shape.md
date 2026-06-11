---
id: llm-wiki-vault-three-layer-shape
title: LLM Wiki 三层目录结构
status: accepted
card_type: pattern
tags: [llm-wiki, vault-structure, directory-layout, raw-wiki-schema]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [clawhub-llm-wiki-karpathy]
justification: ../justification/llm-wiki-vault-three-layer-shape.md
canonical_concept: llm-wiki-vault-three-layer-shape
aliases: [三层目录, raw/wiki/schema, vault shape, 知识库目录结构]
summary: >-
  llm-wiki-vault-three-layer-shape（三层目录 / raw/wiki/schema）llm-wiki-karpathy 运行时采用 raw/wiki/.llm-kb 三层目录结构：raw 存放原始资料，wiki 按 sources/outputs/concepts/entities/syntheses 分区组织产出，.llm-kb 管理清单、运行日志和中间表示
related: [representation-first-ingest, runtime-agent-boundary]
---

llm-wiki-karpathy 运行时定义了一个确定性的「Default Vault Shape」，将知识库拆分为三个顶层目录[^src-1]：

**raw/**——原始资料的存放区。支持文本（`.md`、`.txt`）、PDF、图片（`.png`、`.jpg`、`.jpeg`、`.webp`、`.gif`、`.svg`）和结构化数据（`.csv`、`.tsv`、`.json`、`.html`）[^src-2]。

**wiki/**——运行时管理的 wiki 输出区，内部按笔记类型分区[^src-1]：
- `sources/`——源笔记（从 raw 编译而来）
- `outputs/`——查询驱动的输出笔记
- `concepts/`——概念笔记
- `entities/`——实体笔记
- `syntheses/`——综合笔记
- `_indexes/`——集合索引
- `index.md`——wiki 主索引
- `log.md`——运行日志

**.llm-kb/**——运行时内部状态目录[^src-1]：
- `manifest.json`——清单（schema v2，含 raw_kind、mime_type、size_bytes、asset_refs、representations）
- `runs.jsonl`——运行记录
- `representations/`——中间表示存储（OCR 文本、视觉描述等）

这一结构体现了「运行时拥有结构，代理拥有综合」的原则——目录布局和路径规范由运行时确定性管理，而笔记内容的生成和分类决策（某个产出应归入 concept 还是 synthesis）由代理负责[^src-3]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "Default Vault Shape" -- "<vault>/ raw/ wiki/ sources/ outputs/ concepts/ entities/ syntheses/ _indexes/ index.md log.md .llm-kb/ manifest.json runs.jsonl representations/"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "What 0.4.4 Implements" -- "supported raw kinds for text (.md,.txt), PDFs, images (.png,.jpg,.jpeg,.webp,.gif,.svg), and structured data (.csv,.tsv,.json,.html)"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "What 0.4.4 Implements" -- "a raw/wiki/schema operating model with runtime-owned structure and agent-owned synthesis"
