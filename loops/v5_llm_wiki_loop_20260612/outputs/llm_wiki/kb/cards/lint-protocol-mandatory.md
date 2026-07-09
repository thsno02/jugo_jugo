---
id: lint-protocol-mandatory
title: Lint 协议不可省略
status: accepted
card_type: operational-lesson
tags:
- llm-wiki
- lint
- maintenance
- orphan-pages
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- openaitoolshub-six-months
evidence_basis: practitioner_report
justification: ../justification/lint-protocol-mandatory.md
canonical_concept: lint-protocol-mandatory
aliases:
- lint protocol
- weekly lint
- lint 不可省略
- quality-control protocol
summary: 'Lint 协议不可省略 lint-protocol-mandatory 指即使 wiki 表面看起来整洁也必须定期执行 lint。作者在 pitfall
  #1 中跳过 lint 导致三个 orphan 页面（无 inbound links）和一个未标记矛盾堆积，造成约一周"wait what''s the current
  view?"混乱。作者实践为每周日早 ~20 分钟。Rohit v2 称之为 quality-control protocol，GBrain 用夜间 Dream
  Cycle cron 自动化。'
related:
- kb-lint-deterministic-validation
- lint-as-quality-driver
- llm-kb-ingest-operation
---

即使 wiki 表面看起来整洁，也必须定期执行 lint [^src-1]。

**反面教训**（pitfall #1）：作者在 big ingest 周（周六一次 dump 6-8 篇）后跳过 lint，因为"everything looked tidy"。月 3 时发现：
- 3 个 orphan 页面（无 inbound links）
- 1 个未标记矛盾存在于两个 concepts/ 文件间
- 代价：约一周的"wait, what's the current view?"混乱 [^src-1]

**各版本实现**：
- v1：manual lint（Karpathy 原文有提及）
- Rohit v2：quality-control protocol
- GBrain：nightly Dream Cycle cron（全自动）
- 作者：weekly manual lint，周日早 ~20 分钟 [^src-2]

[^card-1]: 与 [schema-first-principle] 相关——lint 规则在 schema.md 中定义
[^card-2]: 与 [contradiction-as-asset] 相关——lint 是浮现标记矛盾的时机

[^src-1]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "4 Pitfalls I Hit" P58 -- "lint protocol isn't optional, even when nothing looks broken"
[^src-2]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "Methodology" P63-69 -- "I lint weekly (Sunday morning, ~20 min)"
