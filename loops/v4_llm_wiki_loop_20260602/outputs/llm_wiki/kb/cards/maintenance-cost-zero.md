---
id: maintenance-cost-zero
title: 维护成本归零论点
status: accepted
card_type: source_claim
tags: [llm-wiki, maintenance, wiki-failure]
created_time: 2026-06-04T22:30:00+08:00
edited_time: 2026-06-04T22:30:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/maintenance-cost-zero.md
canonical_concept: maintenance-cost-zero
aliases: [维护成本归零, zero maintenance cost, wiki 失败原因, 知识库维护]
summary: >-
  maintenance-cost-zero 是 LLM Wiki 的核心论点：人类放弃 wiki 因为维护负担增长快于价值，
  而 LLM 不厌倦、不遗忘、可一次更新 15 个文件，使维护成本趋近于零
related: []
---

LLM Wiki 模式成立的核心经济论点是：维护知识库的困难部分不是阅读或思考，而是**簿记工作**——更新交叉引用、保持摘要时效性、标注新旧数据矛盾、在数十个页面间维持一致性[^src-1]。

人类放弃 wiki 的原因在于**维护负担的增长速度超过了价值的增长速度**。而 LLM 不会感到无聊、不会忘记更新交叉引用、可以一次操作触及 15 个文件。Wiki 得以维护是因为维护成本趋近于零[^src-2]。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Why this works" 第1段 -- "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages."
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Why this works" 第1段 -- "Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero."
