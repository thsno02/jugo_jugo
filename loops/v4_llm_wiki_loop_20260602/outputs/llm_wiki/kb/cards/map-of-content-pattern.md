---
id: map-of-content-pattern
title: Map of Content 引导阅读路径
status: accepted
card_type: mechanism
tags: [llm-wiki, navigation, MOC, guided-reading]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [complete-tech-live-frontier]
justification: ../justification/map-of-content-pattern.md
canonical_concept: map-of-content-pattern
aliases: [MOC, Map of Content, 主题地图, 引导阅读路径, guided reading path]
summary: >-
  map-of-content-pattern（MOC / Map of Content / 主题地图 / 引导阅读路径）是 LLM Wiki
  中按主题组织的引导阅读路径，区别于 index.md 的平面目录；摄入新论文时自动更新以避免孤立节点
related: []
---

Map of Content（MOC）是 LLM Wiki 中的**主题性引导阅读路径**，区别于 index.md 的平面目录式导航[^card-1]。MOC 不是简单地列出所有页面，而是按特定主题或线索组织一组相关页面，提供有结构的阅读顺序。

在 BTTB wiki 的实践中，共创建了 9 个 MOC[^src-1]。MOC 的关键作用体现在摄入流程中：当新论文被摄入时，**MOC 会被更新**以确保新内容被放置在引导阅读路径中，而不是成为孤立节点[^src-2]。这意味着 MOC 不是静态的目录，而是随 wiki 增长而动态演化的导航结构。

例如，`wiki/mocs/communication-depth-spectrum.md` 是一个 10 级通信深度谱的逐级演练路径，被推荐为研究向读者的入口之一[^src-3]。这说明 MOC 兼具导航和教学功能——它不只告诉读者「有什么」，还建议「按什么顺序读」。

MOC 与 index.md 互补：index.md 是按类别组织的完整目录，MOC 是按主题组织的精选路径。前者回答「wiki 里有什么」，后者回答「如何理解某个主题」。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/complete-tech-live-frontier/text.txt` -- "How Karpathy's pattern shows up in the build" -- "9 Maps of Content (guided reading paths)"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/complete-tech-live-frontier/text.txt` -- "How Karpathy's pattern shows up in the build" -- "Maps of Content get updated so the new piece sits in a guided reading path, not just an orphan node."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/complete-tech-live-frontier/text.txt` -- "If you only do one thing" -- "the two entry points to bookmark are wiki/mocs/communication-depth-spectrum.md (the 10-level walkthrough)"
[^card-1]: [索引文件导航机制](index-based-navigation.md) -- MOC 与 index.md 是互补的导航机制：index 是平面目录，MOC 是主题路径
