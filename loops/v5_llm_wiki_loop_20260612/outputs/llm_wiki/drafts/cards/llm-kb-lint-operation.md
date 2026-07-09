---
id: llm-kb-lint-operation
title: LLM KB Lint 健全性检查
status: draft
card_type: operation-pattern
tags: [knowledge-management, llm-compiler, lint, wiki-operation, maintenance]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [developersio-jp-pattern]
evidence_basis: practitioner_report
justification: ../justification/llm-kb-lint-operation.md
canonical_concept: llm-kb-lint-operation
aliases: [Lint, 健全性チェック, wiki lint, ヘルスチェック]
summary: >-
  LLM Knowledge Base 的 Lint 操作: wiki 全体健全性检查。LLM 检测矛盾数据、过时主张、孤立页面、缺失链接并提案修正。核心洞察——LLM 不会对保守任务(相互参照/一貫性チェック/統合更新)感到退屈而放弃。llm-kb-lint-operation lint 健全性チェック
related: []
---

Lint（健全性チェック）是 LLM Knowledge Base 对 wiki 的第三种操作 [^src-1]:

- **触发条件**: 定期或手动执行
- **检测项目**: 矛盾数据、古くなった主張(过时主张)、孤立ページ、欠落リンク
- **执行内容**: LLM 检出问题并提案修正

Karpathy 的关键洞察: "LLM は人間が退屈に感じる保守タスク——相互参照、一貫性チェック、統合の更新——を放棄しない" [^src-1]。人类容易对枯燥维护任务懈怠, 而 LLM 不存在此问题, 这使得 wiki 的长期健康性得到保障 [^card-1]。

[^src-1]: `data/raw/webpage/developersio-jp-pattern/markdown.md` -- "3 つの操作" P21 -- "Lint（健全性チェック）は、wiki 全体に対するヘルスチェックです。矛盾するデータ、古くなった主張、孤立したページ、欠落したリンクなどを LLM が検出し、修正を提案します。Karpathy 氏は「LLM は人間が退屈に感じる保守タスク——相互参照、一貫性チェック、統合の更新——を放棄しない」と書いています。"
[^card-1]: 参见 [llm-knowledge-base-three-layer-architecture] — 人机分工: LLM 管维护, 人类管方向
