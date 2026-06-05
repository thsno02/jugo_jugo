---
id: originals-verbatim-capture
title: 原创思考的逐字保留
status: accepted
card_type: operational_rule
tags: [llm-wiki, originals, verbatim, cognitive-preservation]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
justification: ../justification/originals-verbatim-capture.md
canonical_concept: originals-verbatim-capture
aliases: [原创逐字保留, originals folder, verbatim capture, 用户原创思考, do-not-rewrite]
summary: >-
  originals-verbatim-capture（原创逐字保留 / originals folder / verbatim capture / 用户原创思考 /
  do-not-rewrite）指 LLM Wiki 中设置 originals/ 文件夹保存用户自己的原始思考，禁止 LLM 编辑，
  因为「语言本身就是洞见」；弥补 v1 仅假设摄入外部文章的缺陷
related: [source-faithfulness-risk, human-llm-role-division, three-layer-architecture]
---

Karpathy v1 存在一个结构性缺陷：它**隐含地假设用户只摄入外部文章**，未提供捕获用户自身思考的机制[^src-1]。然而，用户自己产生的内容——对论文的反直觉解读、在 Slack 中即兴构建的框架——往往是**最高价值的知识**[^src-2]。没有专门的收容空间，这些思考「流入 Notion 草稿然后消亡」[^src-3]。

GBrain（Garry Tan）通过设置专门的 `originals/` 文件夹解决了这一问题[^src-4]。但仅有文件夹不够——作者在第 3 个月经历了一次关键教训：Claude 在例行编辑中将他的原始表述「knowledge compounding ≠ knowledge hoarding」改写为「compound knowledge effectively」。措辞更干净了，但**原始认知形态完全丧失**[^src-5]。

由此得出的操作规则：`originals/` 文件夹必须是**纯逐字保留**（verbatim-only），通过 `do-not-rewrite` 标签和 schema.md 中的显式禁令，阻止 LLM 在该文件夹中进行任何编辑[^src-6]。核心原则是：**语言本身就是洞见**（the language is the insight）——这正是该文件夹存在的全部理由[^src-7]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/openaitoolshub-six-months/text.txt` -- L86 -- "Karpathy's v1 has a hole around capturing your own thoughts... v1 implicitly assumes you're ingesting external articles."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/openaitoolshub-six-months/text.txt` -- L86 -- "the highest-value content I generate is my own takes — the contrarian read on a paper, the framework I improvised in a Slack DM."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/openaitoolshub-six-months/text.txt` -- L86 -- "Without an originals/ folder those go into Notion drafts and die."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/openaitoolshub-six-months/text.txt` -- L86 -- "GBrain's originals/ folder is the patch."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/openaitoolshub-six-months/text.txt` -- L94 -- "Claude, doing its usual editing pass, rewrote it to 'compound knowledge effectively'. Cleaner prose, completely lost the original cognitive shape."
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/openaitoolshub-six-months/text.txt` -- L94 -- "I added a do-not-rewrite tag and updated schema.md to forbid LLM edits in that folder."
[^src-7]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/openaitoolshub-six-months/text.txt` -- L94 -- "The language is the insight — that's the whole point of the folder."
