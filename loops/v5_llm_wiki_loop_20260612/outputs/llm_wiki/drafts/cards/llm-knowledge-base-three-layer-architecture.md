---
id: llm-knowledge-base-three-layer-architecture
title: LLM Knowledge Base 三层架构
status: draft
card_type: architectural-pattern
tags: [knowledge-management, llm-compiler, architecture, karpathy]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [developersio-jp-pattern]
evidence_basis: practitioner_report
justification: ../justification/llm-knowledge-base-three-layer-architecture.md
canonical_concept: llm-knowledge-base-three-layer-architecture
aliases: [3層アーキテクチャ, LLM KB three layers, Raw sources / Schema / Wiki]
summary: >-
  Karpathy 提出的 LLM Knowledge Base 三层架构: Raw sources(不変精選ドキュメント, 人类收集) / Schema(wiki 構造・規約定義, 人类设计) / Wiki(LLM 生成 Markdown 群, summaries+entity pages+backlinks, 人間はほとんど直接書かない)。llm-knowledge-base-three-layer-architecture 3層 アーキテクチャ Raw Schema Wiki
related: []
---

Karpathy 将 LLM Knowledge Base 分为三个层次 [^src-1]:

**1. Raw sources（原始素材）**
- 定义: 不変の精選ドキュメント(記事/論文/リポジトリ/画像)
- 角色: 人类负责收集, 可用 Obsidian Web Clipper 转 Markdown + 本地保存关联画像
- 性质: 只增不改的输入层

**2. Schema（規約定義）**
- 定义: wiki の構造や規約を定義する設定ドキュメント
- 内容: カテゴリ分类、ファイル命名規則等
- 角色: 人类设计的"設計図"(蓝图), LLM 遵循

**3. Wiki（生成物）**
- 定义: LLM が生成した Markdown ファイル群
- 構成: summaries + 概念ごとのエンティティページ + バックリンク
- 角色: LLM の領域; "人間が直接書くことはほとんどない", 人类做キュレーションと方向づけ

[^src-1]: `data/raw/webpage/developersio-jp-pattern/markdown.md` -- "3 層アーキテクチャ" P14-16 -- "Raw sources は、記事、論文、リポジトリ、画像など、不変の精選ドキュメントです...Schema は、wiki の構造や規約を定義する設定ドキュメントです...Wiki は、LLM が生成した Markdown ファイル群です...人間が直接書くことはほとんどないという点。wiki は LLM の領域であり、人間はキュレーションや方向づけに集中します。"
