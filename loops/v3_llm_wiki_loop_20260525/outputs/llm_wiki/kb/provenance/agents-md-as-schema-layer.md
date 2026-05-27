---
schema: accepted_card_provenance.v3
card: ../cards/agents-md-as-schema-layer.md
material_id: complete-tech-live-frontier
digest_id: digest_complete-tech-live-frontier
source_paths:
  - data/raw/webpage/complete-tech-live-frontier/text.txt
draft_card: ../../drafts/cards/agents-md-as-schema-layer.md
draft_provenance: ../../drafts/provenance/agents-md-as-schema-layer.md
similarity_result: ../../drafts/similarity/agents-md-as-schema-layer.json
comparison_provenance: ../../drafts/comparison/agents-md-as-schema-layer.md
gate:
  type: fusion_audit
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 四项判据全部通过；draft 在 v2 schema 配置卡 scope 外补充了 AGENTS.md 命名、四类配置维度、schema-self-audit 工作流与四条工程理由。
v2_anchor:
  card_id: llm-wiki-schema-configuration-document
  card_path: loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
  comparison_decision: provenance_delta
created_time: 2026-05-26T11:21:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
edited_entity: llm
---

## 源证据

- schema 段（行 124–126）：
  > "AGENTS.md — the schema. Page types, linking conventions, depth standards, what counts as 'done' for each page class. This is what makes the LLM's output predictable and the wiki maintainable across many ingest passes."
- workflows audit 列表（行 128）：
  > "workflows/ — maintainer playbooks: create (ingest, batch-ingest, synthesize), enrich (enrich, expand), audit (gap-analysis, verification, lint, plugin-audit, schema-self-audit), query , meta."

## 卡片范围是否成立

卡片只展开"schema 层"这一概念，所有具体维度（page types / linking / depth / done）都来自源材料的列举。"实践含义"段是从源材料的"makes the LLM's output predictable and the wiki maintainable across many ingest passes"做的合理推广。"边界与误用"明示了源材料未提的取舍（schema 太严 vs 太宽），作为概念卡的必要边界。

## 发表门控结果

- 类型：fusion_audit
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 三问被实质回答：comparison 三节均 substantive，明确指出 v2 卡来源 Karpathy gist 第 33 行而 draft 来源 CompleteTech BTTB 文章。
  - v2 anchor body 已读：v2 卡 statement「schema 是配置文档，告诉 LLM wiki 的结构、约定、ingest/query/maintenance 工作流」已与 draft 对照。
  - draft 不破坏 v2 scope：draft 没有改写 v2 的核心定义，而是在其外加 (a) AGENTS.md 命名约定、(b) 四类配置维度、(c) schema-self-audit workflow 名称、(d) "为何写进文件而非 prompt"四条工程理由。
  - provenance 链可追溯：本文件显式记录 v2_anchor + comparison_provenance 路径，构成反向链接锚点。

## 备注

- 与 `beyond-the-token-bottleneck-llm-wiki-case-study` 是案例 → 概念的关系，可在比较阶段合并或保持分卡。
- v2 中可能已有"AGENTS.md / GEMINI.md / CLAUDE.md / spec-driven dev"卡，比较阶段处理。
- adoption 阶段观察：v2 schema 配置卡的 single-source 边界（仅 Karpathy gist 第 33 行）使得本 draft 适合作为独立的"实施级"补强卡，而非合并入 v2 卡 body。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/agents-md-as-schema-layer.md`
- draft provenance: `../../drafts/provenance/agents-md-as-schema-layer.md`
- similarity: `../../drafts/similarity/agents-md-as-schema-layer.json`
- comparison provenance: `../../drafts/comparison/agents-md-as-schema-layer.md`
