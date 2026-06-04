---
id: query-and-answer-filing
title: 查询操作与答案归档
status: accepted
card_type: operational_rule
tags: [llm-wiki, operations, query]
created_time: 2026-06-04T22:30:00+08:00
edited_time: 2026-06-04T22:30:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/query-and-answer-filing.md
canonical_concept: query-and-answer-filing
aliases: [查询操作, query operation, 答案归档, answer filing]
summary: >-
  query-and-answer-filing 是 LLM Wiki 的查询操作：LLM 搜索相关 wiki 页面并综合带引用的答案，
  关键洞见是好的答案应归档为新 wiki 页面，使探索像资料摄入一样产生复利效应
related: []
---

查询（Query）是 LLM Wiki 的三大操作之一。LLM 搜索相关 wiki 页面、阅读它们、并综合出带引用的答案。答案形式多样——markdown 页面、比较表格、幻灯片（Marp）、图表（matplotlib）、画布[^src-1]。

关键洞见在于：**好的答案应该作为新页面归档回 wiki**。用户请求的比较分析、发现的联系——这些都是有价值的，不应消失在聊天历史中。通过这种方式，用户的探索像摄入的资料一样在知识库中产生复利效应[^src-2]。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations > Query" -- "The LLM searches for relevant pages, reads them, and synthesizes an answer with citations. Answers can take different forms depending on the question — a markdown page, a comparison table, a slide deck (Marp), a chart (matplotlib), a canvas."
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations > Query" -- "good answers can be filed back into the wiki as new pages... This way your explorations compound in the knowledge base just like ingested sources do."
