---
schema: draft_card_provenance.v3
draft_card: ../cards/agents-md-as-schema-layer.md
material_id: complete-tech-live-frontier
digest_id: digest_complete-tech-live-frontier
source_paths:
  - data/raw/webpage/complete-tech-live-frontier/text.txt
created_time: 2026-05-26T11:21:00+08:00
edited_time: 2026-05-26T11:21:00+08:00
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

本轮未运行。

## 备注

- 与 `beyond-the-token-bottleneck-llm-wiki-case-study` 是案例 → 概念的关系，可在比较阶段合并或保持分卡。
- v2 中可能已有"AGENTS.md / GEMINI.md / CLAUDE.md / spec-driven dev"卡，比较阶段处理。
