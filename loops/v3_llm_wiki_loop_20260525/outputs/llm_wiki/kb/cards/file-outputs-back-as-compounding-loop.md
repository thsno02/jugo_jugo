---
id: file-outputs-back-as-compounding-loop
title: 把查询输出回写进 wiki 形成复利循环
status: accepted
card_type: operational_rule
tags: [#llm-wiki, #knowledge-system, #compounding, #workflow]
created_time: 2026-05-25T22:05:00+08:00
edited_time: 2026-05-28T11:00:00+08:00
edited_entity: llm
source_ids: [karpathy-x-launch-post]
provenance_card: ../provenance/file-outputs-back-as-compounding-loop.md
aliases: ["问答结果回写", "输出即下一次输入"]
related: [llm-knowledge-base-five-stage-workflow, idea-file-as-agent-era-artifact, knowledge-compounding-three-mechanisms, karpathy-llm-kb-three-operations, llm-wiki-ingest-vs-query-workflow]
---

Karpathy 的 setup 里"不显眼但关键"的一步发生在查询答案产生**之后**。作者不把答案当作终态输出。答案会被渲染成 markdown 文件（或幻灯、或图像），回到 Obsidian 里查看，并且经常被"归档"回 wiki，让 wiki 在下一次查询时更强。

由此带来的结构性效果是：每一次研究会话结束后，wiki 的能力都严格地比之前更强。作者原话是："我自己的探索和查询总是在知识库里'累加'。"

操作层面如何落实这条规则：

- 把每一次查询答案当成"候选新文章"，而不是聊天回复。从一开始就把它渲染成 `.md`/`.slides`/`.png`，以便后续归档。
- 评审后，把这份产物放进相关概念目录之下。反向链接由 LLM 在下一轮 ingest 或 lint 中自动补齐。
- 后续查询应当被允许把这些归档过的答案当作一等公民来检索，和原始导入文档同等对待。Wiki 不区分"源材料知识"和"答案知识"。

为什么重要：没有"回写"这一步，wiki 就只是原始语料的静态衍生物，每次查询都从同一个基线开始。引入回写之后，wiki 和用户的实际专长在一同复利增长。代价只是"每次查询多归档一步"；收益是答案质量单调上升。

边界：被归档的答案只有在 linting 能够发现它和源材料的矛盾时才安全。失去了健康检查的兜底，回写会把一个错误答案放大成"下一次查询会依赖的事实"。

## References

- Karpathy 引用推文中的 Output 章节（`data/raw/webpage/karpathy-x-launch-post/text.txt`，JSON 指针 `$.tweet.quote.text`）。

## Footnotes

- `data/raw/webpage/karpathy-x-launch-post/text.txt` — JSON 指针 `$.tweet.quote.text`，"Output:" 章节（`"Often, I end up \"filing\" the outputs back into the wiki to enhance it for further queries. So my own explorations and queries always \"add up\" in the knowledge base."`）。
