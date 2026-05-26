---
schema: draft_card_provenance.v3
draft_card: ../cards/llm-wiki-ingest-vs-query-workflow.md
material_id: anthemcreation-en-guide
digest_id: digest_anthemcreation-en-guide
source_paths:
  - data/raw/webpage/anthemcreation-en-guide/text.txt
created_time: 2026-05-26T15:05:00+08:00
edited_time: 2026-05-26T15:05:00+08:00
edited_entity: llm
---

## 源证据

- 第 92 行：workflow 拆为 ingestion / query 两步的开篇。
- 第 96-108 行：Ingestion 详细描述（建新 entity 页 / 更新 / 合成矛盾 / 自动 backlink）+ 角色分离。
- 第 110-112 行：Query phase 描述 + 多跳推理优势。
- 第 116-130 行：5 分钟 setup 步骤；Obsidian 可替代。
- 第 114 行 + 第 152 行：agents.md 是关键契约 / 模型质量决定可靠性。
- 第 176 行：价值在累积。

## 卡片范围是否成立

- 两阶段、角色分离、setup 步骤、agents.md 契约——全部直接出自页面对应小节。
- 与 karpathy-llm-wiki-source-executable-analogy 卡互补：那张卡讲"什么是"，本卡讲"怎么运作"。
- "写时贵、读时便宜"是对原文行为的归纳，没有跨外部资料综合。

## 发表门控结果

本轮未运行。

## 备注

- 同主题三卡（karpathy-... / my-llm-wiki-... / llm-wiki-ingest-...）应在 comparison_provenance 阶段统一术语并标 cross-links。
