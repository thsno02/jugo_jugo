---
id: raw-wiki-schema-vault-structure
title: Raw/Wiki/Schema 三层 Vault 结构
status: draft
card_type: data-model
tags: [vault, directory-structure, obsidian, raw, wiki, schema]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [clawhub-llm-wiki-karpathy]
evidence_basis: documentation
justification: ../justification/raw-wiki-schema-vault-structure.md
canonical_concept: raw-wiki-schema-vault-structure
aliases: [default vault shape, vault 结构, raw/wiki/schema operating model]
summary: >-
  raw-wiki-schema-vault-structure 三层 Vault 结构将知识库分为 raw/（原始素材）、
  wiki/（sources/outputs/concepts/entities/syntheses/_indexes/index.md/log.md）、
  .llm-kb/（manifest.json/runs.jsonl/representations/）三层，
  体现 runtime-owned structure 与 agent-owned synthesis 的分离。
related: []
---

## Raw/Wiki/Schema 三层 Vault 结构

llm-wiki-karpathy 的默认 vault 采用三层目录模型 [^src-1]：

```
<vault>/
  raw/                          # 原始素材层
  wiki/                         # Agent 合成层
    sources/
    outputs/
    concepts/
    entities/
    syntheses/
    _indexes/
    index.md
    log.md
  .llm-kb/                      # Runtime 元数据层（schema）
    manifest.json
    runs.jsonl
    representations/
```

三层对应 "raw/wiki/schema operating model" [^src-2]：
- **raw/**: 存放未经处理的原材料（text、PDF、images、structured data）
- **wiki/**: runtime-owned structure + agent-owned synthesis 的产出
- **.llm-kb/**: runtime 独占的元数据管理层

[^src-1]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "Default Vault Shape" P42-56 -- "<vault>/ raw/ wiki/ ..."
[^src-2]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "What 0.4.4 Implements" P15 -- "a raw/wiki/schema operating model with runtime-owned structure and agent-owned synthesis"
[^card-2]: [[runtime-agent-responsibility-boundary]] — vault 结构是职责边界的物理映射
