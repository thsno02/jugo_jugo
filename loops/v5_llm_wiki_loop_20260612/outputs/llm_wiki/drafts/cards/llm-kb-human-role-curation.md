---
id: llm-kb-human-role-curation
title: LLM KB 中人类角色——策展与方向设定
status: draft
card_type: role-division
tags: [knowledge-management, human-ai-collaboration, curation, maintenance]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [developersio-jp-pattern]
evidence_basis: practitioner_report
justification: ../justification/llm-kb-human-role-curation.md
canonical_concept: llm-kb-human-role-curation
aliases: [キュレーション, 方向づけ, curation, human role in LLM KB]
summary: >-
  LLM KB 中的人机分工: LLM 承担人类易厌烦的保守任务(index 更新/cross-reference/一貫性チェック/統合更新); 人类专注策展(キュレーション)和方向设定(方向づけ)——source 收集/schema 设计/意思决定。核心前提: LLM 不会对枯燥重复任务放弃。llm-kb-human-role-curation キュレーション 方向づけ 人間 役割
related: []
---

LLM Knowledge Base 中的人机角色分工是材料反复强调的核心论点 [^src-1][^src-2]:

**LLM 负责(保守任务)**:
- Wiki 页面生成与更新
- Index 维护
- 相互参照(cross-reference)管理
- 一貫性チェック(一致性检查)
- 統合の更新(整合更新)

**人类负责(策展与方向)**:
- Source 收集与选定
- Schema 设计
- 方向性意思決定
- キュレーション(策展: 判断什么重要、什么保留)

**核心前提**: "LLM は人間が退屈に感じる保守タスクを放棄しない" — LLM 不存在对枯燥任务的厌倦, 这是分工的认知基础 [^src-1]。

这种分工模式使人类从 O(n) 的维护劳动中解放, 专注于 O(1) 的方向性判断 [^card-1]。

[^src-1]: `data/raw/webpage/developersio-jp-pattern/markdown.md` -- "3 つの操作" P21 -- "LLM は人間が退屈に感じる保守タスク——相互参照、一貫性チェック、統合の更新——を放棄しない"
[^src-2]: `data/raw/webpage/developersio-jp-pattern/markdown.md` -- "まとめ" P61 -- "人間は退屈な保守タスクから解放されて、キュレーションと方向づけに集中する。"
[^card-1]: 参见 [llm-knowledge-base-three-layer-architecture] — 三层架构中 Wiki 层"人間はほとんど直接書かない"
