---
id: llm-wiki-dataset-manifest-system
title: Dataset Manifest 外部数据索引
status: draft
card_type: mechanism
tags: [llm-wiki, dataset, manifest, external-data, indexing]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
evidence_basis: documentation
justification: ../justification/llm-wiki-dataset-manifest-system.md
canonical_concept: dataset-manifest-system
aliases: [dataset manifests, data indexing, 数据集清单, external data manifest]
summary: >-
  dataset-manifest-system：datasets/ 存储 manifests samples profiles 和 query recipes 索引大数据或外部数据而不复制到 raw/，manifests 可指向本地路径 URLs archives，wiki 成为界面数据留在原处
related: [llm-wiki-inventory-operational-state, llm-wiki-hub-architecture]
---

llm-wiki 的 dataset manifest 系统让 wiki 索引大型或外部数据而不将其复制进 raw/ 源语料库。datasets/ 目录存储 manifests、samples、profiles 和 query recipes。[^src-1]

Manifests 可指向本地路径、URLs、archives、samples、profiles 和查询配方。设计理念是"wiki 成为界面；数据留在原处"。[^src-2]

通过 `/wiki:dataset add "title" --location <path-or-url>` 添加，支持 `profile --dry-run` 预览轻量级 profiling。[^src-3]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Architecture" P204 -- "Dataset manifests (datasets/) let the wiki index large or external data without copying it into raw/. Manifests can point to local paths, URLs, archives, samples, profiles, and query recipes."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "How It Works" P120 -- "datasets/ stores manifests, samples, profiles, and query recipes for large data. The wiki indexes data without copying it into the source corpus."
[^src-3]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Intro" P31 -- "Index large, external, mutable, or operational data with manifests, samples, profiles, and query recipes. The wiki becomes the interface; the data stays where it belongs."
