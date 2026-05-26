---
schema: draft_card_provenance.v3
draft_card: ../cards/karpathy-llm-wiki-three-layers.md
material_id: marvin-hn-persistent-knowledge
digest_id: digest_marvin-hn-persistent-knowledge
source_paths:
  - data/raw/webpage/marvin-hn-persistent-knowledge/text.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/webpage/marvin-hn-persistent-knowledge/text.txt:29` —— 三层定义全文。
2. `text.txt:31` —— 三操作 Ingest / Query / Lint 完整描述。
3. `text.txt:31` —— index.md 与 log.md 的双特殊文件定位。

## 卡片范围是否成立

- 卡片同时覆盖"三层 + 三操作 + 两个特殊文件"，因为这三件事在 gist 里是同一个架构的不同切面，强行拆分会让 reader 失去整体感。
- "任何一层缺失都失效" 是基于三层职责正交的合理推断。
- "Ingest ≠ INSERT、Query ≠ SELECT、Lint ≠ housekeeping"是对原文的解读引申，强调 gist 的 CRUD 拓扑不同于传统数据库。
- "起步先写 schema.md" 是 openaitoolshub 经验文章共识，已隐式标注；marvin 原文没直接说"先写 schema"但与 schema-as-rules 的定位一致。

## 发表门控结果

本轮未运行。

## 备注

- 与 v2 卡 `llm-knowledge-base-five-stage-workflow` 主题相邻：五阶段是更细的工作流分解；本卡是 Karpathy 原始三层三操作。两卡互补，应交叉引用。
