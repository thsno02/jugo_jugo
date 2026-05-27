---
schema: accepted_card_provenance.v3
card: ../cards/beyond-the-token-bottleneck-llm-wiki-case-study.md
material_id: complete-tech-live-frontier
digest_id: digest_complete-tech-live-frontier
source_paths:
  - data/raw/webpage/complete-tech-live-frontier/text.txt
draft_card: ../../drafts/cards/beyond-the-token-bottleneck-llm-wiki-case-study.md
draft_provenance: ../../drafts/provenance/beyond-the-token-bottleneck-llm-wiki-case-study.md
similarity_result: ../../drafts/similarity/beyond-the-token-bottleneck-llm-wiki-case-study.json
comparison_provenance: ../../drafts/comparison/beyond-the-token-bottleneck-llm-wiki-case-study.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:34:00+08:00
  gate_notes: 6/6 通过；27 源 / 120+ 页 / 1400+ 内链 / 10-15 page touches 等关键数字全部锁到博客原文行号；三层架构 + workflows 第四层映射齐全。
created_time: 2026-05-26T11:20:00+08:00
edited_time: 2026-05-27T14:34:00+08:00
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

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:34:00+08:00
- 检查要点：
  - 不是标题复述：含规模数字 + 三层架构映射 + 第四 workflows 层 + ingest 副作用量化 + 三条复用启示 + 边界。
  - 知识密度足够：数字 + 架构 + 机制 + 操作启示 + 边界。
  - 源支撑齐全：每个数字和引文锁到博客原文行号。
  - References 与 Footnotes 双章节存在。
  - frontmatter 完整合法，example_pattern 类型与正文一致。
  - related 已链 v3 draft 卡（五阶段 / agents-md / Obsidian plugin 等）。

## 备注

- 与 `llm-knowledge-base-five-stage-workflow` 是父-子关系：那张卡描述 Karpathy 抽象工作流，这张卡是一个真实实现。
- 案例规模数字（1400+ 内链、一篇论文 10–15 页 touches）特别值得引——这是少见的把 Karpathy "bookkeeping" 抽象概念量化的公开数据。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/beyond-the-token-bottleneck-llm-wiki-case-study.md`
- draft provenance: `../../drafts/provenance/beyond-the-token-bottleneck-llm-wiki-case-study.md`
- similarity: `../../drafts/similarity/beyond-the-token-bottleneck-llm-wiki-case-study.json`
- comparison provenance: `../../drafts/comparison/beyond-the-token-bottleneck-llm-wiki-case-study.md`
