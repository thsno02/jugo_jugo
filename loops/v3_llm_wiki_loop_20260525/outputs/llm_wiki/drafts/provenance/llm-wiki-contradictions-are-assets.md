---
schema: draft_card_provenance.v3
draft_card: ../cards/llm-wiki-contradictions-are-assets.md
material_id: openaitoolshub-six-months
digest_id: digest_openaitoolshub-six-months
source_paths:
  - data/raw/webpage/openaitoolshub-six-months/text.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
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

本轮未运行。

## 备注

- 与 `llm-wiki-rohit-v2-improvements` 互链：v2 卡讲三件事；本卡放大第 3 件事的哲学含义与 compliance 边界。建议 comparison_provenance 阶段保留两卡而非合并——其切片角度不同。
