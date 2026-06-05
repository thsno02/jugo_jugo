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
related: [cognitive-deskilling-risk, human-llm-role-division, llm-as-maintenance-engine, source-faithfulness-risk, three-layer-architecture, writing-as-thinking]
---

Karpathy v1 存在一个结构性缺陷：它**隐含地假设用户只摄入外部文章**，未提供捕获用户自身思考的机制[^src-1]。然而，用户自己产生的内容——对论文的反直觉解读、在 Slack 中即兴构建的框架——往往是**最高价值的知识**[^src-2]。没有专门的收容空间，这些思考「流入 Notion 草稿然后消亡」[^src-3]。

GBrain（Garry Tan）通过设置专门的 `originals/` 文件夹解决了这一问题[^src-4]。但仅有文件夹不够——作者在第 3 个月经历了一次关键教训：Claude 在例行编辑中将他的原始表述「knowledge compounding ≠ knowledge hoarding」改写为「compound knowledge effectively」。措辞更干净了，但**原始认知形态完全丧失**[^src-5]。

由此得出的操作规则：`originals/` 文件夹必须是**纯逐字保留**（verbatim-only），通过 `do-not-rewrite` 标签和 schema.md 中的显式禁令，阻止 LLM 在该文件夹中进行任何编辑[^src-6]。核心原则是：**语言本身就是洞见**（the language is the insight）——这正是该文件夹存在的全部理由[^src-7]。

「语言即洞见」的原则与「书写即思考」的论点在深层逻辑上一致：两者都主张人类的原始认知形态具有不可替代的价值[^card-1]。从风险角度看，本规则可视为对认知去技能化的实践层缓冲——即使 LLM 处理了大量维护工作，至少用户自身最高价值的思考不会因改写而丧失[^card-2]。同时，本规则也为 LLM 维护引擎的职责范围划定了明确边界：维护引擎可以触及知识库的一切结构性内容，但 originals/ 文件夹是其不可逾越的禁区[^card-3]。

## Footnotes

[^card-1]: [书写即思考](writing-as-thinking.md) -- 本卡从操作规则层确立 originals/ 逐字保留，该卡从理论层论证为何人类原始表述具有不可替代的认知价值——「语言即洞见」的理论基础
[^card-2]: [认知去技能化风险](cognitive-deskilling-risk.md) -- 本卡通过逐字保留规则保护人类原创思考，该卡揭示了若不加保护、过度委托将导致的认知退化后果
[^card-3]: [LLM 作为维护引擎的角色重构](llm-as-maintenance-engine.md) -- 本卡为维护引擎划定不可触碰的边界（originals/ 禁止编辑），该卡定义维护引擎的职责范围——两卡共同界定了 LLM 维护角色的权限边界

[^src-1]: `data/raw/webpage/openaitoolshub-six-months/text.txt` -- L86 -- "Karpathy's v1 has a hole around capturing your own thoughts... v1 implicitly assumes you're ingesting external articles."
[^src-2]: `data/raw/webpage/openaitoolshub-six-months/text.txt` -- L86 -- "the highest-value content I generate is my own takes — the contrarian read on a paper, the framework I improvised in a Slack DM."
[^src-3]: `data/raw/webpage/openaitoolshub-six-months/text.txt` -- L86 -- "Without an originals/ folder those go into Notion drafts and die."
[^src-4]: `data/raw/webpage/openaitoolshub-six-months/text.txt` -- L86 -- "GBrain's originals/ folder is the patch."
[^src-5]: `data/raw/webpage/openaitoolshub-six-months/text.txt` -- L94 -- "Claude, doing its usual editing pass, rewrote it to 'compound knowledge effectively'. Cleaner prose, completely lost the original cognitive shape."
[^src-6]: `data/raw/webpage/openaitoolshub-six-months/text.txt` -- L94 -- "I added a do-not-rewrite tag and updated schema.md to forbid LLM edits in that folder."
[^src-7]: `data/raw/webpage/openaitoolshub-six-months/text.txt` -- L94 -- "The language is the insight — that's the whole point of the folder."
