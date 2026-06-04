---
id: wiki-compounding-artifact
title: Wiki 作为复利型知识制品
status: accepted
card_type: mechanism
tags: [llm-wiki, compounding, knowledge-accumulation]
created_time: 2026-06-04T22:30:00+08:00
edited_time: 2026-06-04T22:30:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/wiki-compounding-artifact.md
canonical_concept: wiki-compounding-artifact
aliases: [复利型制品, compounding artifact, 知识积累机制]
summary: >-
  wiki-compounding-artifact 指 LLM Wiki 中持续积累的五类结构：交叉引用、已标记矛盾、
  综合叙述、实体/概念页面、回查询归档的分析，每次新增资料或提问都使 wiki 更丰富
related: []
---

LLM Wiki 中的 wiki 是一个**持久化的复利型制品（compounding artifact）**[^src-1]。具体而言，以下结构在 wiki 中持续积累：

1. **交叉引用（cross-references）**——wiki 页面之间的互链，由 LLM 在整合新资料时建立和维护
2. **已标记的矛盾（flagged contradictions）**——当新资料与已有主张冲突时，wiki 记录这一矛盾而非要求每次重新发现
3. **演化中的综合（evolving synthesis）**——wiki 维护一个融合所有已读资料的综合叙述
4. **实体页面、概念页面、摘要、比较和概览**——LLM 生成的具体页面类型[^src-2]
5. **归档的查询答案**——好的查询回答可以作为新页面归入 wiki，使探索像资料摄入一样产生复利效应[^src-3]

每次添加新资料或提出新问题，wiki 都变得更丰富。这与 RAG 的根本区别在于：RAG 没有积累机制，每次查询都从原始片段重新开始。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" 第3段 -- "the wiki is a persistent, compounding artifact"
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Architecture > The wiki" -- "Summaries, entity pages, concept pages, comparisons, an overview, a synthesis"
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations > Query" -- "good answers can be filed back into the wiki as new pages"
