---
schema: accepted_card_provenance.v3
card: ../cards/llm-wiki-contradictions-are-assets.md
material_id: openaitoolshub-six-months
digest_id: digest_openaitoolshub-six-months
source_paths:
  - data/raw/webpage/openaitoolshub-six-months/text.txt
draft_card: ../../drafts/cards/llm-wiki-contradictions-are-assets.md
draft_provenance: ../../drafts/provenance/llm-wiki-contradictions-are-assets.md
similarity_result: ../../drafts/similarity/llm-wiki-contradictions-are-assets.json
comparison_provenance: ../../drafts/comparison/llm-wiki-contradictions-are-assets.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:08:00+08:00
  gate_notes: 6/6 项通过；矛盾哲学、protocol 操作规则、compliance 反例边界齐备并锚回 text.txt 行号。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T10:08:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/webpage/openaitoolshub-six-months/text.txt:96` —— Pitfall #3 完整段（"contradictions are assets, not errors"）。
2. `text.txt:136` —— compliance 场景下哲学不适用的明确边界。

## 卡片范围是否成立

- 卡片聚焦"为何矛盾是资产 + 如何标 + compliance 边界"，与 `llm-wiki-rohit-v2-improvements`（v2 三件事概览）兄弟卡形成"概览 vs 哲学放大"的互补。
- "矛盾承载三类信息（决策演化 / 领域结构信号 / 检验后续判断锚点）" 是基于哲学的合理引申，原文未列出但与原文 spirit 一致。
- "lint pass 应优先列未解决矛盾" 是 schema 协议的合理延伸；原文未指定 lint 实现。
- "frontmatter do-not-rewrite: true" 是借自 Pitfall #2（originals 折页）的 schema-level 工程做法，已隐式标注。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:08:00+08:00
- 检查要点：
  - distinction 卡正面对比两个视角，非标题复述。
  - 知识密度合格：哲学、protocol、compliance 反例与可操作 schema 含义层层递进。
  - source_ids 含 `openaitoolshub-six-months`，正文直接引到 text.txt 行号。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 6 张相关卡。

## 备注

- 与 `llm-wiki-rohit-v2-improvements` 互链：v2 卡讲三件事；本卡放大第 3 件事的哲学含义与 compliance 边界。comparison 已确认保留两卡而非合并。
- compliance 边界声明（regulated 领域不适用）是本卡的硬约束，将来任何引用本卡的下游决策都应保留这条 boundary。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/llm-wiki-contradictions-are-assets.md`
- draft provenance: `../../drafts/provenance/llm-wiki-contradictions-are-assets.md`
- similarity: `../../drafts/similarity/llm-wiki-contradictions-are-assets.json`
- comparison provenance: `../../drafts/comparison/llm-wiki-contradictions-are-assets.md`
