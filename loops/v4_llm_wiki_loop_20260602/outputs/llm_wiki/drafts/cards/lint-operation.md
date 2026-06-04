---
id: lint-operation
title: 巡检操作
status: draft
card_type: operational_rule
tags: [llm-wiki, operations, lint, maintenance]
created_time: 2026-06-04T22:30:00+08:00
edited_time: 2026-06-04T22:30:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/lint-operation.md
canonical_concept: lint-operation
aliases: [巡检操作, lint, wiki 健康检查, health-check]
summary: >-
  lint-operation 是 LLM Wiki 的定期健康检查操作：LLM 检测页面间矛盾、
  过时主张、孤立页面、缺失概念页、缺失交叉引用、数据缺口，
  并建议新问题和新资料来源
related: []
---

巡检（Lint）是 LLM Wiki 的三大操作之一，用于定期维护 wiki 的健康状态。用户触发后，LLM 检查以下问题[^src-1]：

- 页面之间的矛盾
- 已被新资料取代的过时主张
- 没有入站链接的孤立页面
- 被提及但缺少独立页面的重要概念
- 缺失的交叉引用
- 可通过网络搜索填补的数据缺口

LLM 还善于建议新的调查问题和新的资料来源[^src-2]。巡检保持 wiki 在增长过程中的健康状态。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations > Lint" -- "Look for: contradictions between pages, stale claims that newer sources have superseded, orphan pages with no inbound links, important concepts mentioned but lacking their own page, missing cross-references, data gaps that could be filled with a web search."
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations > Lint" -- "The LLM is good at suggesting new questions to investigate and new sources to look for."
