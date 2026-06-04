---
id: source-faithfulness-risk
title: 源忠实性风险与不可变锚点
status: draft
card_type: distinction
tags: [llm-wiki, faithfulness, drift, verification]
created_time: 2026-06-04T22:45:00+08:00
edited_time: 2026-06-04T22:45:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/source-faithfulness-risk.md
canonical_concept: source-faithfulness-risk
aliases: [源忠实性, faithfulness drift, 知识漂移风险]
summary: >-
  source-faithfulness-risk 指 LLM Wiki 中 wiki 内容经多轮摘要/综合/交叉引用后
  逐渐偏离原始来源的风险；raw sources 作为不可变 source of truth 提供回溯锚点，
  但材料未定义系统性验证机制，lint 仅检测时效性而非忠实度
related: []
---

LLM Wiki 的 wiki 层完全由 LLM 生成，每次操作（摘要、综合、交叉引用、更新）都是有损变换。多轮迭代后，wiki 内容可能逐渐偏离原始来源的实际陈述——这是一种潜在的**知识漂移风险**。

材料的设计提供了一个**结构性锚点**：raw sources 层是不可变的——LLM 只读取不修改，它们是整个系统的 source of truth[^src-1]。这意味着理论上任何时候都可以回溯核查。

然而，材料未定义系统性的**忠实度验证机制**。Lint 操作检查的是时效性问题（「过时的主张」「缺失的交叉引用」），而非 wiki 内容是否偏离了原始来源的本意[^src-2]。源忠实度的保障在实践中可能依赖于人类的抽查——作者描述了自己 「跟随链接、检查图谱视图、阅读更新后的页面」的实践[^src-3]——但这不是一个形式化的验证步骤。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Architecture > Raw sources" -- "These are immutable — the LLM reads from them but never modifies them. This is your source of truth."
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations > Lint" -- "stale claims that newer sources have superseded"
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" 第4段 -- "I browse the results in real time — following links, checking the graph view, reading the updated pages"
