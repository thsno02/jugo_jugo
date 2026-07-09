---
id: context-window-degradation-limits
title: 大 Context Window 的退化瓶颈
status: draft
card_type: empirical-observation
tags: [context-window, llm-limitations, degradation, long-context]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [hacker-news-original-thread]
evidence_basis: community_discussion
justification: ../justification/context-window-degradation-limits.md
canonical_concept: context-window-degradation
aliases: [context degradation, context forgetting, 上下文退化, 长上下文遗忘]
summary: >-
  即使 context window 达到 1M tokens，模型在 200K-300K 处开始遗忘/退化，因此 10M context 未必让中间知识层过时。目标不是每次保持全部 context，而是让记忆可查询——像 data lake 但用于 ideas 和 decisions。
related: [llm-wiki-write-loop-vs-static-rag, dual-audience-wiki-artifact]
---

即使 context window 已达 1M tokens（或 800K），模型在约 200K-300K mark 处就开始"遗忘"内容。因此，10M context 在退化从 200K-300K 开始的前提下意义有限。[^src-1]

这一观察反驳了"下一代模型的超大 context 将使 wiki 中间层过时"的论点。[^src-2]

据材料中另一评论者指出，LLM Wiki 的目标不是每次保持全部 context，而是让记忆可查询（queryable）——像 data lake 但用于个人的 ideas 和 decisions。[^src-3]

[^card-1]: 参见 [dual-audience-wiki-artifact] -- wiki 提供结构化查询能力弥补 context 退化

[^src-1]: `data/raw/hacker_news/hacker-news-original-thread/text.txt` -- "lelanthran comment" -- "We've already got 1m context, 800k context, and they still start 'forgetting' things around the 200k - 300k mark. What use is 10M context if degradation starts at 200k - 300k?"
[^src-2]: `data/raw/hacker_news/hacker-news-original-thread/text.txt` -- "Imanari comment" -- "I think next gen models with 10M context and/or 1000tps will make this obsolete."
[^src-3]: `data/raw/hacker_news/hacker-news-original-thread/text.txt` -- "khalic comment" -- "The goal isn't to keep the context every time, it's to make the memory queryable. Like a data lake but for your ideas and decisions"
