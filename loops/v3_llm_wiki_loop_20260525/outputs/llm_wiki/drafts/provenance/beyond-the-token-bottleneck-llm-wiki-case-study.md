---
schema: draft_card_provenance.v3
draft_card: ../cards/beyond-the-token-bottleneck-llm-wiki-case-study.md
material_id: complete-tech-live-frontier
digest_id: digest_complete-tech-live-frontier
source_paths:
  - data/raw/webpage/complete-tech-live-frontier/text.txt
created_time: 2026-05-26T11:20:00+08:00
edited_time: 2026-05-26T11:20:00+08:00
edited_entity: llm
---

## 源证据

- 标题与定位（行 88–94）：
  > "A 120-page Obsidian research wiki on latent-space reasoning and inter-agent latent communication — built using Andrej Karpathy's LLM Wiki pattern. 27 sources, 1400+ cross-references, schema-driven ingest. Apache + CC-BY."
- Karpathy 引用（行 92）：
  > "the tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping"
- 三层架构（行 120–128）：
  > "Karpathy's gist describes a three-layer architecture: raw sources (immutable inputs), the wiki (LLM-generated, mutable, the actual product), and the schema (configuration that tells the LLM what good looks like). The repo is laid out almost exactly that way:"
  > "raw/ — 26 source PDFs from arXiv, ACL, ICML, NeurIPS, plus a per-paper provenance index, an ingest checklist, and a bulk arXiv downloader. Read-only by convention. The LLM doesn't edit this layer."
  > "wiki/ — 120+ pages: source summaries, concept pages, entity profiles for 13 research groups, 9 Maps of Content (guided reading paths), 9 analysis/synthesis pages, an overview, a change log. 1400+ internal links knit the whole thing together."
  > "AGENTS.md — the schema. Page types, linking conventions, depth standards, what counts as 'done' for each page class."
  > "workflows/ — maintainer playbooks: create (ingest, batch-ingest, synthesize), enrich (enrich, expand), audit (gap-analysis, verification, lint, plugin-audit, schema-self-audit), query, meta."
- Ingest 循环（行 130）：
  > "One paper, ten to fifteen page touches, hundreds of new and updated links. That's the bookkeeping Karpathy was talking about, automated."
- 三条理由（行 136–140）。
- License split（行 148）：
  > "The repo is split-licensed: Apache 2.0 for code (workflows, scripts, schema), CC-BY 4.0 for content (the wiki itself)."

## 卡片范围是否成立

卡片把博客里所有具体数字、目录布局、引文直接复用，并明示"作者方法学归功 Karpathy"。"对其他人复用这一模式的启示"这一段是合理引申——直接由源材料中的 "schema-driven ingest"、"audit workflows"、"raw is read-only" 等明文要素总结而来。"未公开 ingest 总耗时 / 成本"是源材料事实空白，作为边界声明合适。

## 发表门控结果

本轮未运行。

## 备注

- 与 `llm-knowledge-base-five-stage-workflow` 是父-子关系：那张卡描述 Karpathy 抽象工作流，这张卡是一个真实实现。
- 与未来的 `nvk-llm-wiki-toolkit` 类卡可形成"模式 + 工具 + 案例" 的三角。
