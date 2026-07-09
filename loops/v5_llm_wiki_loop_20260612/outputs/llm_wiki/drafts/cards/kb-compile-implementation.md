---
id: kb-compile-implementation
title: kb-compile 实装案例
status: draft
card_type: implementation-example
tags: [knowledge-management, claude-code, kb-compile, mem0, pgvector, practitioner]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [developersio-jp-pattern]
evidence_basis: practitioner_report
justification: ../justification/kb-compile-implementation.md
canonical_concept: kb-compile-implementation
aliases: [/kb-compile, kb-compile, Claude Code 知識管理実装]
summary: >-
  作者(クラスメソッド 森茂)基于 Karpathy LLM KB 概念的 Claude Code 实装: workspace/knowledge/ (Raw) + CLAUDE.md (Schema) + workspace/wiki/ (Wiki) + Memory MCP (Mem0+pgvector) 检索层。/kb-compile 命令执行编译, 支持 --all 和 --lint。kb-compile-implementation Claude-Code mem0 pgvector
related: []
---

作者基于 Karpathy 三层概念构建的 Claude Code 实装 [^src-1]:

**目录对应**:
- Raw sources → `workspace/knowledge/` (日報/リサーチ/セッションログ)
- Schema → 各ディレクトリの CLAUDE.md
- Wiki → `workspace/wiki/` (\_index.md, \_recent.md, projects/)

**附加层(Karpathy 原案にない)**: Memory MCP (Mem0 + pgvector) — RAG 式检索与 wiki 并用

**编译命令**:
- `/kb-compile [project]` — 特定 project 编译
- `/kb-compile --all` — 全体一括更新
- `--lint` — 矛盾検出/リンク切れチェック/古い記事検出

**实装局限**(作者自评) [^src-2]:
- 手動実行しないと更新されない(非自动)
- プロジェクト横断のトピック記事は未着手
- Lint 自動実行は未仕組み化
- "hacky collection of scripts の域を出ていない"

[^src-1]: `data/raw/webpage/developersio-jp-pattern/markdown.md` -- "自分は Claude Code でこう組み込んでいる" P37-46 -- "workspace/knowledge/ が Raw sources、各ディレクトリに置いた CLAUDE.md が Schema、workspace/wiki/ が Compiled Wiki に相当します。さらに自分の場合は Memory MCP（Mem0 + pgvector）という検索レイヤーが間に入っていて"
[^src-2]: `data/raw/webpage/developersio-jp-pattern/markdown.md` -- "自分は Claude Code でこう組み込んでいる" P58 -- "hacky collection of scripts の域を出ていない"
[^card-1]: 参见 [llm-knowledge-base-three-layer-architecture] — Karpathy 原始三层定义
