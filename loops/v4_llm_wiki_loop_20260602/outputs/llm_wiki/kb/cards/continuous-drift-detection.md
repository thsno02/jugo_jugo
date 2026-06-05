---
id: continuous-drift-detection
title: 持续偏移检测
status: accepted
card_type: mechanism
tags: [enterprise-wiki, drift-detection, health-check, automation]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [falconer-enterprise-guide]
justification: ../justification/continuous-drift-detection.md
canonical_concept: continuous-drift-detection
aliases: [持续偏移检测, continuous drift detection, 自动漂移检测, 企业级健康检查]
summary: >-
  continuous-drift-detection（持续偏移检测 / continuous drift detection / 自动漂移检测 / 企业级健康检查）
  是个人 LLM Wiki 按需巡检在企业规模下的演化：从用户触发变为后台循环自动运行，
  检测跨千篇文档和百万行代码的偏移，按团队可操作的节奏（周度而非季度）呈现结果
related:
  - lint-operation
  - retrieval-vs-maintenance
  - single-curator-bottleneck
---

个人 LLM Wiki 的健康检查是按需触发的：Karpathy 要求 LLM 查找来源之间的不一致、填补缺失信息、标记与新材料矛盾的页面。在个人规模下，一个人看到巡检输出并采取行动，这种模式行之有效[^src-1]。

在企业规模下，这一方式无法泛化。健康检查必须从**按需**变为**持续**[^src-2]。具体变化包括：

1. **触发方式**：从人工要求变为后台循环自动运行
2. **检测范围**：跨越数千份文档和数百万行代码的偏移检测
3. **呈现节奏**：按团队可操作的节奏呈现标记内容——**周度审查而非季度审计**
4. **检测内容**：LLM 执行与 Karpathy 在个人 vault 上运行的相同类型的不一致检查，只是以匹配企业变更速率的节奏进行[^src-3]

此外，企业复合要求系统不仅能发现矛盾，还需**理解所有权和路由**：当新 PR 与 runbook 矛盾时，系统需要检测矛盾、起草更新、并将更新路由到文档所有者进行审查。Karpathy 的 vault 通过将矛盾呈现给他本人来处理；企业 wiki 必须将矛盾呈现给**正确的人**[^src-4]。

Anthropic 工程团队将上下文描述为 AI agent 最稀缺的资源：agent 需要即时访问当前、准确的上下文才能在真实工作中可靠执行。一年没有健康检查的知识图谱是 agent 可能的最差输入[^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/falconer-enterprise-guide/text.txt` -- "Stay current: health checks need to run automatically" 段 -- "At the personal scale, that works well: one person sees the lint output and acts on it."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/falconer-enterprise-guide/text.txt` -- "What an enterprise LLM wiki has to do differently" 段 -- "The health check changes from on-demand to continuous."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/falconer-enterprise-guide/text.txt` -- "What an enterprise LLM wiki has to do differently" 段 -- "It runs as a background loop, surfacing flagged content on a schedule the team can act on (weekly review rather than quarterly audit), with the LLM doing the same kind of inconsistency-checking Karpathy runs on his vault, just at a cadence that matches enterprise change rates."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/falconer-enterprise-guide/text.txt` -- "What an enterprise LLM wiki has to do differently" 段 -- "the system needs to detect the contradiction, draft an update, and route it to the document owner for review... an enterprise wiki has to surface them to the right person, which means the system has to understand ownership and routing."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/falconer-enterprise-guide/text.txt` -- "Stay current: health checks need to run automatically" 段 -- "agents need just-in-time access to current, accurate context to perform reliably on real work. A knowledge graph that hasn't had a health check in a year is the worst possible input for an agent."
