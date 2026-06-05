---
id: complexity-collapse-threshold
title: 复杂度崩溃阈值
status: accepted
card_type: mechanism
tags: [llm-wiki, complexity, collapse, scalability, maintenance]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [hacker-news-original-thread]
justification: ../justification/complexity-collapse-threshold.md
canonical_concept: complexity-collapse-threshold
aliases: [复杂度崩溃, 临界点, critical collapse point, wiki可扩展性极限]
summary: >-
  complexity-collapse-threshold（复杂度崩溃 / 临界点 / critical collapse point / wiki可扩展性极限）指 LLM Wiki 系统存在一个临界点，超过该点 agent 无法维护 wiki、开发者也无法理解 wiki；人类能处理 10 单位复杂度+LLM 处理 20 单位时，用户倾向于构建 30 单位复杂度的系统并在失控前无法察觉
related: [lint-operation, maintenance-cost-zero]
---

社区讨论识别出 LLM Wiki 模式存在一个**临界复杂度阈值**：超过该点，系统对人和 agent 都变得不可管理。

首先，wiki 规模增长到一定程度后会出现双重崩溃：agent 无法再保持 wiki 的更新，同时开发者也无法再理解 wiki 的内容[^src-1]。

其次，这个问题被框架化为一个更普遍的**复杂度叠加陷阱**：如果人类能处理 10 单位复杂度、LLM 能处理 20 单位，用户倾向于构建 30 单位复杂度的系统——而在为时已晚之前无法察觉失控[^src-2]。模块化、关注点分离等原则对人类大脑至关重要，但人们没有意识到这些原则同样适用于当前的 AI。系统的复杂度增长会远远超过可管理的范围，除非被积极管控[^src-3]。

第三，当前 LLM 的具体局限被指出：LLM「当然无法管理任何非局部复杂度」，反而在以前所未有的速度增加技术债务和复杂度[^src-4]。

一位部署了多用户 Obsidian 结构化系统的实践者对此做了关键区分：中间知识层「有损、混乱、会过时，但非常有效」地捕获设计意图与实现之间的偏差。然而，完全自治的自引用层则「毫无价值」——真正的价值在于系统支持人类介入并说「系统应该这样运行」[^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/hacker_news/hacker-news-original-thread/text.txt` -- kubb 评论 -- "there's a critical point beyond which things collapse: the agent can't keep the wiki up to date anymore, the developer can't grok it anymore."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/hacker_news/hacker-news-original-thread/text.txt` -- kaashif 评论 -- "If a human can understand 10 units of complexity and their LLM can do 20, then they might just build a system that's 30 complex and not understand the failure modes until it's too late."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/hacker_news/hacker-news-original-thread/text.txt` -- kaashif 评论 -- "systems grow in complexity far past the point where the system is gummed up and no-one can do anything, unless it's actively managed."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/hacker_news/hacker-news-original-thread/text.txt` -- stingraycharles 评论 -- "The LLM can certainly not manage any non-local complexity right now, and succeed in increasing the technical debt and complexity faster than ever before."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/hacker_news/hacker-news-original-thread/text.txt` -- SOLAR_FIELDS 评论 -- "The intermediate layer is lossy, it's messy, it goes out of date, but it's highly effective... A self referential layer like this that's entirely autonomous does feel completely valueless"
