---
id: topic-archive-lifecycle
title: Topic 归档生命周期——静默保留而非删除
status: accepted
card_type: lifecycle-mechanism
tags:
- llm-wiki
- archive
- topic-lifecycle
- quiet-preservation
- context-filter
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- repo-nvk-llm-wiki
evidence_basis: code_implementation
justification: ../justification/topic-archive-lifecycle.md
canonical_concept: topic-archive-lifecycle
aliases:
- topic archive
- archive lifecycle
- quiet preservation
- topics/.archive
- wiki archiving
summary: 'llm-wiki 的归档机制将整个 topic wiki 从 HUB/topics/<slug> 移动到 HUB/topics/.archive/<slug>，在 wikis.json 中标记 status: archived。归档是上下文过滤器而非删除：内容保留但从默认 query/compile/research/output/maintenance 工作流中隐藏。Deep query
  可展示归档索引匹配但不引用为活跃证据。恢复（restore）操作为反向移动。不归档单独文件或项目本地 .wiki/。'
related:
- hub-topic-wiki-isolation
- lint-as-schema-migration
- opinionated-inventory-dataset-layers
---
llm-wiki v0.9.0 引入的 topic archive lifecycle 实现了一种"静默保留"策略：

**核心语义**：归档是上下文过滤器（context filter），不是删除操作。[^src-1]

**操作机制**：
- `archive topic <slug>`: 将 `HUB/topics/<slug>` 移动到 `HUB/topics/.archive/<slug>`
- `wikis.json` 更新：`path: topics/.archive/<slug>`, `status: archived`, `archived: YYYY-MM-DD`
- `restore <slug>`: 反向移动并设置 `status: active`

**默认行为——归档 wiki 对以下工作流隐藏**[^src-2]：
- query, compile, ingest, research, output, plan, assess
- inventory, dataset, project, lessons-learned
- librarian, refresh（避免旧兴趣产生维护杂务）

**显式包含场景**：
- `--include-archived` 标志允许显式读取
- Deep query 可能展示归档索引匹配但作为单独"Archived Matches"部分，不引用为活跃证据
- audit 仅在被审计制品依赖归档材料时跟踪[^src-3]

**设计约束**：v1 中不归档单独 raw/ 或 wiki/ 文件，不归档项目本地 `.wiki/` 目录。

[^src-1]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "archive.md" -- "Archive is a context filter, not deletion: preserve the wiki, remove it from normal semantic workflows"
[^src-2]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "SKILL.md Core Principles" -- "Archive is quiet preservation. Archived topic wikis live under HUB/topics/.archive/<slug>/ and are hidden from normal semantic workflows."
[^src-3]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "README.md Key Design" -- "Archive-aware — archived topic wikis stay preserved under topics/.archive/ but are hidden from default query/compile/research/output"
