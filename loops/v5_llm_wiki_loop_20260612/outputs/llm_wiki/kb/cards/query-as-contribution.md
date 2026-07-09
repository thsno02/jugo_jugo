---
id: query-as-contribution
title: Query 回写：探索性问答作为知识贡献
status: accepted
card_type: design_principle
tags:
- llm-wiki
- query
- knowledge-compounding
- exploration
created_time: 2026-06-12 15:03:00+08:00
edited_time: 2026-06-12 15:03:00+08:00
edited_entity: llm
source_ids:
- karpathy-gist-llm-wiki
evidence_basis: practitioner_report
justification: ../justification/query-as-contribution.md
canonical_concept: query-as-contribution
aliases:
- query filing
- 查询回写
- explorations compound
- 探索性复合
summary: query-as-contribution 是 LLM Wiki 的设计原则：好的查询答案（对比、分析、发现的联系）应回写为 wiki 新页面，使探索性问答像 ingest 一样为知识库贡献复合价值
related:
- persistent-compounding-artifact
- ingest-operation
---

LLM Wiki 中 Query 操作不仅消费知识，还能产出知识。核心设计原则：好的答案应作为新页面回写到 wiki 中。[^src-1]

"A comparison you asked for, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history." 这使得用户的探索性活动——对比、分析、发现联系——像摄入 source 一样为知识库贡献复合价值。[^src-2] [^card-1]

查询答案可以采取多种形式：markdown 页面、对比表格、幻灯片（Marp）、图表（matplotlib）、canvas。形式取决于问题本身。[^src-3]

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations" P3 -- "good answers can be filed back into the wiki as new pages."
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations" P3 -- "A comparison you asked for, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history. This way your explorations compound in the knowledge base just like ingested sources do."
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations" P3 -- "Answers can take different forms depending on the question — a markdown page, a comparison table, a slide deck (Marp), a chart (matplotlib), a canvas."
[^card-1]: [persistent-compounding-artifact](persistent-compounding-artifact.md) -- query 回写是 compounding 的另一种机制
