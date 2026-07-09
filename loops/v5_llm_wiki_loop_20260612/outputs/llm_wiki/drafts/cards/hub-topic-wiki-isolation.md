---
id: hub-topic-wiki-isolation
title: Hub-Topic 隔离架构与知识组织模型
status: draft
card_type: architecture-pattern
tags: [llm-wiki, wiki-architecture, topic-isolation, hub-structure, obsidian]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-nvk-llm-wiki]
evidence_basis: code_implementation
justification: ../justification/hub-topic-wiki-isolation.md
canonical_concept: hub-topic-wiki-isolation
aliases: [topic wiki isolation, one topic one wiki, hub registry, topic sub-wiki architecture]
summary: >-
  llm-wiki 采用 hub + topic sub-wiki 隔离架构。Hub 是纯注册中心（仅 wikis.json, _index.md, log.md, topics/），无内容目录。每个 topic wiki 拥有独立的 raw/, wiki/, output/, inbox/，支持 Obsidian vault 独立打开。设计目标是防止跨主题噪声污染查询空间。wikis.json 使用可移植相对路径以支持 iCloud 跨机器共享。
related: [llm-as-knowledge-compiler-metaphor, derived-index-concurrency-protocol, topic-archive-lifecycle]
---

llm-wiki 的知识组织遵循严格的"一主题一 wiki"原则：

**Hub 层（轻量注册中心）**：
- 仅包含 `wikis.json`（注册表）、`_index.md`、`log.md`、`topics/`
- 不存放任何内容目录（无 raw/、wiki/、output/）
- 使用可移植相对路径 `topics/<slug>` 而非绝对路径，支持 iCloud 跨 Mac 共享[^src-1]

**Topic Wiki 层（完整内容单元）**：
- 每个主题拥有独立的 `raw/`（不可变源）、`wiki/`（编译文章）、`output/`（生成制品）
- 可选惰性层：`inventory/`（持久跟踪）、`datasets/`（大型外部数据清单）
- 每个 topic wiki 可作为独立 Obsidian vault 打开（.obsidian/ 配置）[^src-2]

**设计动机**：保持查询聚焦，防止无关主题污染搜索空间。多 wiki 感知（multi-wiki peek）仅在查询时查看兄弟 wiki 的 `_index.md` 以发现重叠。[^src-3]

[^src-1]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "wiki-structure.md wikis.json Format" -- "Topic paths inside the shared hub should be relative (topics/<topic>) or use the <HUB> token."
[^src-2]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "README.md Architecture" -- "The hub is just a registry — no content directories, no .obsidian/. All content lives in topic sub-wikis with isolated indexes and articles."
[^src-3]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "AGENTS.md Core Principles" -- "One topic, one wiki. Never mix unrelated topics. The hub is just a registry."
