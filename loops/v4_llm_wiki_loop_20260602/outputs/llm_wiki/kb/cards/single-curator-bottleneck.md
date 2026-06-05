---
id: single-curator-bottleneck
title: 单一策展人瓶颈
status: accepted
card_type: distinction
tags: [enterprise-wiki, scaling, curator, personal-vs-enterprise]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [falconer-enterprise-guide]
justification: ../justification/single-curator-bottleneck.md
canonical_concept: single-curator-bottleneck
aliases: [单一策展人瓶颈, single curator bottleneck, 个人策展失效]
summary: >-
  single-curator-bottleneck（单一策展人瓶颈 / single curator bottleneck / 个人策展失效）
  是个人 LLM Wiki 向企业扩展时的核心结构性障碍：个人模式成功依赖一个有动力的人控制策展，
  企业依赖单一策展人则重新制造它试图解决的 wiki 问题
related:
  - human-llm-role-division
  - maintenance-cost-zero
---

个人 LLM Wiki 之所以有效，是因为**一个有动力的人策展它**——控制什么进入 raw/ 文件夹，引导分析方向，运行健康检查。这种策展本身就是个人模式的特性[^src-1]。

但在企业层面，**依赖单一策展人会重新制造该系统试图解决的 wiki 问题**[^src-2]。公司的"原始资料"分散在 GitHub PR、Slack 线程、Linear ticket、Granola 会议记录、Google Drive 设计文档、Notion 事故复盘和 Zendesk 客户对话中——这不是纪律的失败，而是**结构性差异**[^src-3]。

这一瓶颈在维护维度尤为突出：六个月前写 runbook 的工程师已在另一个项目上，了解上下文的资深工程师已离开，文档描述的系统已被重写了两次。Karpathy 通过刻意的健康检查发现的不一致，在企业知识中会悄然积累，直到新员工基于错误假设开发，或 AI agent 读取陈旧的 runbook 产出 2024 年的代码[^src-4]。

因此，企业版本必须将策展和维护从**个人责任**转变为**系统自动化**：摄入来自工作实际发生的工具，健康检查作为后台循环自动运行[^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/falconer-enterprise-guide/text.txt` -- "Capture: the source folder doesn't exist at company scale" 段 -- "That curation is a feature of the personal pattern — it works because one person controls what goes in."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/falconer-enterprise-guide/text.txt` -- "Key takeaways" 段 -- "A company can't depend on a single curator without recreating the wiki problem it's trying to solve."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/falconer-enterprise-guide/text.txt` -- "Capture: the source folder doesn't exist at company scale" 段 -- "that's not a failure of discipline — it's a structural difference."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/falconer-enterprise-guide/text.txt` -- "Stay current: health checks need to run automatically" 段 -- "The engineer who wrote the runbook six months ago is on a different project; the senior engineer who knew the context has moved on; the system the doc described has been rewritten twice."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/falconer-enterprise-guide/text.txt` -- "What an enterprise LLM wiki has to do differently" 段 -- "the maintenance has to be automatic and the ingestion has to come from the tools where work actually happens."
