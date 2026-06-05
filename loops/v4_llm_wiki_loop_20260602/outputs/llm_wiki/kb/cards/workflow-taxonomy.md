---
id: workflow-taxonomy
title: 工作流五类分类法
status: accepted
card_type: concept
tags: [llm-wiki, workflows, operations, taxonomy]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [complete-tech-live-frontier]
justification: ../justification/workflow-taxonomy.md
canonical_concept: workflow-taxonomy
aliases: [工作流分类, workflow categories, 操作分类, maintainer playbooks]
summary: >-
  workflow-taxonomy（工作流分类 / workflow categories / 操作分类 / maintainer playbooks）
  将 LLM Wiki 工作流组织为 create（ingest/batch-ingest/synthesize）、enrich（enrich/expand）、
  audit（gap-analysis/verification/lint/plugin-audit/schema-self-audit）、query、meta 五大类
related: []
---

LLM Wiki 的操作不只是散落的单项动作，可以组织为**五大类工作流**[^src-1]：

1. **Create（创建）**——ingest（单源摄入）、batch-ingest（批量摄入）、synthesize（综合生成）。这一类负责向 wiki 中添加新知识。
2. **Enrich（丰富）**——enrich（充实已有页面）、expand（扩展页面深度）。对已有知识进行补充与深化。
3. **Audit（审计）**——gap-analysis（缺口分析）、verification（核实）、lint（巡检）、plugin-audit（插件审计）、schema-self-audit（schema 自审）。确保 wiki 的健康度和一致性。
4. **Query（查询）**——利用 wiki 回答问题。
5. **Meta（元操作）**——关于 wiki 自身的操作（如决策树文档化）。

该分类法通过维护者手册（maintainer playbooks）落地，入口为 `workflows/README.md` 的决策树[^src-2]。相比逐个定义操作（如摄入[^card-1]、巡检[^card-2]），这一分类法提供了一个完整的操作组织框架。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/complete-tech-live-frontier/text.txt` -- "How Karpathy's pattern shows up in the build" -- "workflows/ — maintainer playbooks: create (ingest, batch-ingest, synthesize), enrich (enrich, expand), audit (gap-analysis, verification, lint, plugin-audit, schema-self-audit), query , meta ."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/complete-tech-live-frontier/text.txt` -- "How Karpathy's pattern shows up in the build" -- "Decision tree at workflows/README.md ."
[^card-1]: [摄入操作](ingest-operation.md) -- create 类的核心操作
[^card-2]: [巡检操作](lint-operation.md) -- audit 类的子操作之一
