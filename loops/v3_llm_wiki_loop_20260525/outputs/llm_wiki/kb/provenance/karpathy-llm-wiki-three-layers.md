---
schema: accepted_card_provenance.v3
card: ../cards/karpathy-llm-wiki-three-layers.md
material_id: marvin-hn-persistent-knowledge
digest_id: digest_marvin-hn-persistent-knowledge
source_paths:
  - data/raw/webpage/marvin-hn-persistent-knowledge/text.txt
draft_card: ../../drafts/cards/karpathy-llm-wiki-three-layers.md
draft_provenance: ../../drafts/provenance/karpathy-llm-wiki-three-layers.md
similarity_result: ../../drafts/similarity/karpathy-llm-wiki-three-layers.json
comparison_provenance: ../../drafts/comparison/karpathy-llm-wiki-three-layers.md
gate:
  type: fusion_audit
  result: passed
  decided_at: 2026-05-27T14:42:00+08:00
  gate_notes: 四项判据全部通过；draft 作为 marvin-hn 编辑团队对 Karpathy gist 的二次转述，在 v2 三层架构卡 scope 外补充三操作 Ingest/Query/Lint 整合视角 + index.md/log.md 双特殊文件 + 任何一层缺失都失效的工程边界。
v2_anchor:
  card_id: llm-wiki-three-layer-architecture
  card_path: loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
  comparison_decision: provenance_delta
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T14:42:00+08:00
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

- 类型：fusion_audit
- 结果：passed
- 决定时间：2026-05-27T14:42:00+08:00
- 检查要点：
  - 三问被实质回答：comparison 明确 v2 三层架构卡（Karpathy gist 一手）与 draft（marvin-hn 二次转述）共享三层事实，draft 额外覆盖三操作 + 两特殊文件。
  - v2 anchor body 已读：v2 卡 statement 与 draft "三层架构"节对照，draft 用 marvin-hn 的转述措辞「AGENTS.md or CLAUDE.md」比原 gist 更具体。
  - draft 不破坏 v2 scope：三层核心与 v2 一致；draft 新加 (a) 三操作 Ingest/Query/Lint 整合视角（v2 KB 仅 health-checks 触及 Lint 子集）、(b) index.md / log.md 双特殊文件（v2 KB 完全缺失）、(c) "任何一层缺失都失效"工程边界 + CRUD 拓扑差异——均在 v2 紧致 scope 外。
  - provenance 链可追溯：本文件显式记录 v2_anchor + comparison_provenance 路径。

## 备注

- 与 v2 卡 `llm-knowledge-base-five-stage-workflow` 主题相邻：五阶段是更细的工作流分解；本卡是 Karpathy 原始三层三操作。两卡互补，应交叉引用。
- adoption 阶段观察：draft 提到的 index.md / log.md 双正交文件是 v2 KB 完全缺失的事实，未来 loop 可单独拆卡。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/karpathy-llm-wiki-three-layers.md`
- draft provenance: `../../drafts/provenance/karpathy-llm-wiki-three-layers.md`
- similarity: `../../drafts/similarity/karpathy-llm-wiki-three-layers.json`
- comparison provenance: `../../drafts/comparison/karpathy-llm-wiki-three-layers.md`
