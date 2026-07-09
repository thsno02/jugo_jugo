---
id: llm-kb-query-filing-back
title: LLM KB Query 与 Filing Back 机制
status: draft
card_type: operation-pattern
tags: [knowledge-management, llm-compiler, query, filing-back, wiki-operation]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [developersio-jp-pattern]
evidence_basis: practitioner_report
justification: ../justification/llm-kb-query-filing-back.md
canonical_concept: llm-kb-query-filing-back
aliases: [Query, filing back, 質問, クエリ, wiki query]
summary: >-
  LLM Knowledge Base 的 Query 操作: 向 wiki 提问并获回答, 回答作为新页面 filing back 到 wiki。使用即积累, wiki 因使用而成长。llm-kb-query-filing-back query filing-back 質問
related: []
---

Query(質問)是 LLM Knowledge Base 对 wiki 的第二种操作 [^src-1]:

- **触发条件**: 用户向 wiki 提问
- **执行内容**: LLM 基于 wiki 内容回答问题
- **副作用(filing back)**: 回答被作为新页面写回 wiki, 使探索/质问本身成为知识积累

这构成了一个正反馈循环: 使えば使うほど wiki が充実していく(越用越充实) [^src-1]。与传统搜索(查完即弃)不同, query 的结果成为 wiki 的永续组成部分 [^card-1]。

[^src-1]: `data/raw/webpage/developersio-jp-pattern/markdown.md` -- "3 つの操作" P20 -- "Query（質問）は、wiki に対して質問を投げ、回答を得る操作です。ここが面白いところで、回答を新たなページとして wiki に「filing back」することで、自分の探索や質問がそのまま知識として蓄積されます。使えば使うほど wiki が充実していく、というわけです。"
[^card-1]: 参见 [llm-kb-ingest-operation] — Ingest 也扩充 wiki, Query 则让"使用"本身成为扩充来源
