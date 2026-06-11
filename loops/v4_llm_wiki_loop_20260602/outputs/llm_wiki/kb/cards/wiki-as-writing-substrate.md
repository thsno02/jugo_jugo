---
id: wiki-as-writing-substrate
title: Wiki 作为写作底料的生产力循环
status: accepted
card_type: mechanism
tags: [llm-wiki, writing, productivity, compounding, personal-workflow]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [openaitoolshub-six-months]
justification: ../justification/wiki-as-writing-substrate.md
canonical_concept: wiki-as-writing-substrate
aliases: [写作底料, writing substrate, wiki驱动写作, wiki-to-blog pipeline, 引用自身思考]
summary: >-
  wiki-as-writing-substrate（写作底料 / writing substrate / wiki驱动写作 / wiki-to-blog pipeline /
  引用自身思考）指将 LLM Wiki 作为写作的上下文底料：grep 概念、拉取 TL;DR 进入上下文，
  Claude 以用户自身历史决策为引用起草文章，使写作「扎实而非泛泛」
related: [tldr-context-optimization, output-compounding-loop, wiki-compounding-artifact, originals-verbatim-capture]
---

LLM Wiki 不仅是知识管理工具，还是**写作生产力的放大器**。作者发现的工作流是[^src-1]：

1. 坐下来写博客文章时，先 `grep` wiki 中相关概念
2. 将相关页面的 TL;DR 拉入 Claude 的上下文
3. Claude 以用户**自身历史决策**作为引用起草文章

核心效果：「我的草稿现在引用了我自己的历史决策，正是这一步使写作感觉扎实而非泛泛」（grounded instead of generic）[^src-2]。

作者明确将「复利资产」的框架称为「不是比喻——而是真实的生产力循环」（not a metaphor — it's a real productivity loop）[^src-3]。写作输出（如这篇博文本身）又回馈成为新的知识输入，形成正反馈。

这一机制区别于 llm-wiki.net 的产出复利循环[^card-1]：后者是工具层面的自动化管道（产出回写进 wiki 索引），本卡描述的是**人类认知层面的体验**——wiki 使人类写作者能够「引用自身」，这是一种独特的知识复利的主观感受和实践方式。TL;DR 摘要优化[^card-2]为这一工作流提供了关键的工程支撑——正是因为每页有 <=50 字符摘要，grep + 拉取摘要才能在单次上下文中完成。originals/ 逐字保留[^card-3]确保了这些被引用的「自身历史决策」保持原始认知形态而非被 LLM 平滑化。

## Footnotes

[^src-1]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- L56 -- "When I sit down to publish a blog post (this one, for instance), I grep my wiki for the relevant concepts, pull TL;DRs into context, and Claude drafts with citations to my own prior thinking."
[^src-2]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- L56 -- "My drafts now reference my own historical decisions, which is the move that makes the writing feel grounded instead of generic."
[^src-3]: `data/raw/webpage/openaitoolshub-six-months/markdown.md` -- L56 -- "The 'compounding asset' framing isn't a metaphor — it's a real productivity loop."
[^card-1]: [产出复利循环](output-compounding-loop.md) -- 该卡描述工具层面的自动化产出管道（产出回写 wiki 索引），本卡描述人类认知层面的写作体验——wiki 使写作者能引用自身历史思考，两者从不同抽象层展示 wiki 的产出放大效应
[^card-2]: [TL;DR 摘要的上下文窗口优化作用](tldr-context-optimization.md) -- 本卡的写作工作流依赖 TL;DR 摘要的快速扫描能力，该卡论证了 TL;DR 为何是上下文压缩的承重结构
[^card-3]: [原创思考的逐字保留](originals-verbatim-capture.md) -- 本卡中被引用的「自身历史决策」之所以保有原始认知价值，依赖于该卡确立的逐字保留规则
