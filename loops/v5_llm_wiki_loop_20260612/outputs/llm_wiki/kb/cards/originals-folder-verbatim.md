---
id: originals-folder-verbatim
title: Originals 文件夹与原始表述保护
status: accepted
card_type: design-pattern
tags:
- llm-wiki
- originals
- verbatim
- cognitive-shape
- gbrain
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- openaitoolshub-six-months
evidence_basis: practitioner_report
justification: ../justification/originals-folder-verbatim.md
canonical_concept: originals-folder-verbatim
aliases:
- originals/ folder
- originals 文件夹
- verbatim-only
- do-not-rewrite
- the language is the insight
summary: 'Originals 文件夹 originals-folder-verbatim 专门存放用户原始思维捕获，规则为 verbatim-only 禁止
  LLM 编辑。源于 GBrain 的设计（填补 v1/v2 均未处理的缺口）。作者在 pitfall #2 中因允许 Claude 平滑改写而丢失原始认知形态（"knowledge
  compounding ≠ knowledge hoarding"被改为"compound knowledge effectively"）。教训：the language
  is the insight，表达形式本身承载认知价值。通过 do-not-rewrite tag 和 schema.md 禁令实现保护。'
related:
- llm-wiki-immutable-raw-sources
- llm-wiki-three-layer-structure
- llm-wiki-compilation-process
---

originals/ 文件夹存放用户原始思维捕获（contrarian reads、improvised frameworks、Slack DM 中的洞见），规则为 verbatim-only [^src-1]。

**来源**：GBrain（Garry Tan）的设计。Karpathy v1 和 Rohit v2 均未处理"捕获自己的思考"这一场景——v1 隐含假设用户仅 ingest 外部文章 [^src-2]。

**反面教训**（pitfall #2）：作者有一条 hot take "knowledge compounding ≠ knowledge hoarding"，Claude 在编辑中改写为 "compound knowledge effectively"——prose 更干净但"completely lost the original cognitive shape" [^src-1]。

**核心原则**："The language is the insight"——原始措辞本身承载认知价值，不可被 LLM 平滑重写 [^src-1]。

**实现**：添加 `do-not-rewrite` tag + 更新 schema.md 禁止 LLM 编辑 originals/ 内容。

[^card-1]: 与 [llm-wiki-three-layer-structure] 相关——originals/ 是 wiki/ 下的子文件夹
[^card-2]: 与 [schema-first-principle] 相关——保护规则在 schema.md 中实现

[^src-1]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "4 Pitfalls I Hit" P59 -- "originals/ is verbatim-only. I added a do-not-rewrite tag...The language is the insight"
[^src-2]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- "What Surprised Me" P55 -- "Karpathy's v1 has a hole around capturing your own thoughts, and GBrain's originals/ folder is the patch."
