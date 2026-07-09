---
id: llm-wiki-hub-architecture
title: llm-wiki Hub 架构与目录分层
status: accepted
card_type: system-architecture
tags:
- llm-wiki
- directory-structure
- knowledge-management
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- llm-wiki-net
evidence_basis: documentation
justification: ../justification/llm-wiki-hub-architecture.md
canonical_concept: llm-wiki-hub-architecture
aliases:
- hub architecture
- wiki hub
- llm-wiki directory structure
summary: llm-wiki hub architecture 目录分层设计：hub（~/wiki/）为轻量注册中心仅含 wikis.json 和 _index.md，topic
  wikis（~/wiki/topics/<name>/）为隔离研究区域含 raw/ wiki/ output/ inventory/ datasets/ 等子目录，各层职责明确分离
related:
- llm-wiki-immutable-raw-sources
- llm-wiki-index-derived-cache
- llm-wiki-dataset-manifest-system
- llm-wiki-five-install-modes
- llm-wiki-icloud-shared-hub
- llm-wiki-inventory-operational-state
- llm-wiki-zero-runtime-dependencies
- hub-topic-wiki-isolation
---
llm-wiki 采用分层目录架构。Hub（~/wiki/）是轻量注册中心，不存储内容，仅含 wikis.json（所有 topic wiki 的注册表）、_index.md（带统计的列表）和 log.md（全局活动日志）。[^src-1]

所有实际内容存储在 topic wikis（~/wiki/topics/<name>/）中，每个 topic wiki 是隔离的研究区域，包含以下子目录：
- .obsidian/（Obsidian vault 配置）
- inbox/（投放区）
- inventory/（持久追踪记录）
- datasets/（大数据 manifests）
- raw/（不可变原始源）
- wiki/（编译文章，下分 concepts/、topics/、references/）
- output/（生成制品）[^src-2]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Directory Structure" P96-116 -- "~/wiki/ # Hub — lightweight, no content ├── wikis.json # Registry of all topic wikis"
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Architecture" P195-196 -- "The hub (~/wiki/) is just a registry. No content — only wikis.json, _index.md, and log.md. All content lives in topic sub-wikis."
