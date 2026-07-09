---
id: obsidian-wiki-delta-tracking-manifest
title: obsidian-wiki 增量追踪与 manifest 机制
status: draft
card_type: implementation-mechanism
tags: [delta-tracking, manifest-json, incremental-ingest, deduplication]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-ar9av-obsidian-wiki]
evidence_basis: code_implementation
justification: ../justification/obsidian-wiki-delta-tracking-manifest.md
canonical_concept: manifest-based-delta-tracking
aliases: [delta tracking, .manifest.json, incremental ingest, manifest]
summary: >-
  obsidian-wiki 通过 .manifest.json 实现增量追踪（manifest-based-delta-tracking）：
  记录每个已摄入源的路径、时间戳、产出了哪些 wiki 页。下次 ingest 计算 delta 只处理
  新增或变化内容。跨项目使用时 wiki-update 通过 last_commit_synced 字段配合 git log
  只处理增量 commit。避免每次重新摄入整个文档库。
related: [obsidian-wiki-four-stage-pipeline]
---

obsidian-wiki 通过 `.manifest.json` 文件实现增量（delta）追踪[^src-1]，避免每次重新摄入整个文档库。

**Manifest 记录内容**：每个已摄入源的路径、时间戳、以及该源产出了哪些 wiki 页面[^src-2]。

**Delta 计算**：下次 ingest 时，代理读取 manifest 计算差异，只处理新增或已变更的源材料[^src-3]。

**跨项目增量**：当从其他项目使用 `wiki-update` 时，manifest 中的 `last_commit_synced` 字段配合 `git log <last_commit>..HEAD` 实现只处理新增 commit 的增量同步[^src-4]。

[^card-1]: [obsidian-wiki-four-stage-pipeline] — delta tracking 服务于四阶段流水线的 Ingest 阶段，决定哪些源需要进入流水线

[^src-1]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "How it works" P6 -- "A .manifest.json tracks every source that's been ingested — path, timestamps, which wiki pages it produced."
[^src-2]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "What we added on top of Karpathy's pattern" P1 -- "A manifest tracks every source file that's been ingested: path, timestamps, which wiki pages it produced."
[^src-3]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "How it works" P6 -- "On the next ingest, the agent computes the delta and only processes what's new or changed."
[^src-4]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "Using from other projects" P3 -- "On repeat runs, it checks last_commit_synced in .manifest.json and only processes the delta via git log <last_commit>..HEAD."
