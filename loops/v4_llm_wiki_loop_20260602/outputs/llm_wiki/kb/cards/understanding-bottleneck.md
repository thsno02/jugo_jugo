---
id: understanding-bottleneck
title: 理解瓶颈
status: accepted
card_type: concept
tags: [llm-wiki, cognition, human-understanding, karpathy]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [robin-cartier-llm-knowledge-bases]
justification: ../justification/understanding-bottleneck.md
canonical_concept: understanding-bottleneck
aliases: [理解瓶颈, understanding bottleneck, 理解不可外包, cannot outsource understanding]
summary: >-
  understanding-bottleneck（理解瓶颈 / understanding bottleneck / 理解不可外包）是 Karpathy
  在 Sequoia 访谈中提出的认知论点：即使 LLM 可以外包思维，人类无法外包理解；wiki 式投射帮助信息进入人类心智模型
related:
  - writing-as-thinking
  - llm-wiki-pattern
  - cognitive-deskilling-risk
---

Karpathy 在 Sequoia 访谈中提出了 LLM Wiki 模式成立的**认知层面理由**：即使 LLM 可以代替人类执行思维任务（outsource thinking），人类**无法外包理解（understanding）**[^src-1]。Wiki 式的知识投射（wiki-style projections）帮助信息进入人类自身的心智模型，而非仅仅存在于外部系统中。

这一论点与 HN 社区的「书写即思考」批评[^card-1]形成有趣的对照：两者都承认人类认知不可完全委托给 LLM，但方向不同。「书写即思考」认为**做**摘要和交叉引用的过程本身就是理解产生的场所，因此不应外包；而理解瓶颈论点则认为 wiki 作为**结构化投射**帮助人类阅读和吸收知识，即使 wiki 由 LLM 构建，阅读它仍然促进人类理解。前者反对自动化过程，后者支持自动化产出。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/robin-cartier-llm-knowledge-bases/text.txt` -- L31 -- "Karpathy's Sequoia interview adds the cognitive reason this pattern matters: even when LLMs can outsource thinking, humans cannot outsource understanding, and wiki-style projections help information make it into the human's own mental model [src-055]."
[^card-1]: `writing-as-thinking` -- 书写即思考：HN 社区关于过程即理解的反驳论点
