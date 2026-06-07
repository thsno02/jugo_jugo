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
related: [data-catalog-as-enterprise-wiki, documentation-merge-gate, entrenchment-under-user-coupled-drift, lint-operation, llm-as-maintenance-engine, retrieval-vs-maintenance, single-curator-bottleneck, source-faithfulness-risk]
---

LLM 被重构为维护引擎而非检索层[^card-3]，而持续偏移检测是这一角色在企业规模下的核心机制。个人 LLM Wiki 的健康检查是按需触发的：Karpathy 要求 LLM 查找来源之间的不一致、填补缺失信息、标记与新材料矛盾的页面。在个人规模下，一个人看到巡检输出并采取行动，这种模式行之有效[^src-1]。

在企业规模下，这一方式无法泛化。健康检查必须从**按需**变为**持续**[^src-2]。具体变化包括：

1. **触发方式**：从人工要求变为后台循环自动运行
2. **检测范围**：跨越数千份文档和数百万行代码的偏移检测
3. **呈现节奏**：按团队可操作的节奏呈现标记内容——**周度审查而非季度审计**
4. **检测内容**：LLM 执行与 Karpathy 在个人 vault 上运行的相同类型的不一致检查，只是以匹配企业变更速率的节奏进行[^src-3]

此外，企业复合要求系统不仅能发现矛盾，还需**理解所有权和路由**：当新 PR 与 runbook 矛盾时，系统需要检测矛盾、起草更新、并将更新路由到文档所有者进行审查。Karpathy 的 vault 通过将矛盾呈现给他本人来处理；企业 wiki 必须将矛盾呈现给**正确的人**[^src-4]。

Anthropic 工程团队将上下文描述为 AI agent 最稀缺的资源：agent 需要即时访问当前、准确的上下文才能在真实工作中可靠执行。一年没有健康检查的知识图谱是 agent 可能的最差输入[^src-5]。

然而，持续偏移检测在用户耦合漂移导致的固化场景下面临根本性挑战：固化的知识库在错误范式内可能保持内部一致性，使不一致检查无法有效发现问题[^dist-1]。持续偏移检测还面临一个更基础的覆盖缺口：它主要检测时效性偏移（新信息与旧内容的不一致），而 LLM Wiki 中的源忠实性风险——wiki 内容经多轮有损变换后偏离原始来源本意——需要不同的检测机制[^card-4]。

Atlan 提出的"数据目录即企业 wiki"映射中，持续偏移检测对应于数据目录的"主动元数据传播"——管线运行时自动推送更新，本质上是同一机制在不同领域的投射[^card-1]。Write the Docs 的文档合并门禁则提供了互补的时间点覆盖：门禁在变更创建时保障文档质量，偏移检测在后续持续发现漂移[^card-2]。

## Footnotes

[^src-1]: `data/raw/webpage/falconer-enterprise-guide/text.txt` -- "Stay current: health checks need to run automatically" 段 -- "At the personal scale, that works well: one person sees the lint output and acts on it."
[^src-2]: `data/raw/webpage/falconer-enterprise-guide/text.txt` -- "What an enterprise LLM wiki has to do differently" 段 -- "The health check changes from on-demand to continuous."
[^src-3]: `data/raw/webpage/falconer-enterprise-guide/text.txt` -- "What an enterprise LLM wiki has to do differently" 段 -- "It runs as a background loop, surfacing flagged content on a schedule the team can act on (weekly review rather than quarterly audit), with the LLM doing the same kind of inconsistency-checking Karpathy runs on his vault, just at a cadence that matches enterprise change rates."
[^src-4]: `data/raw/webpage/falconer-enterprise-guide/text.txt` -- "What an enterprise LLM wiki has to do differently" 段 -- "the system needs to detect the contradiction, draft an update, and route it to the document owner for review... an enterprise wiki has to surface them to the right person, which means the system has to understand ownership and routing."
[^src-5]: `data/raw/webpage/falconer-enterprise-guide/text.txt` -- "Stay current: health checks need to run automatically" 段 -- "agents need just-in-time access to current, accurate context to perform reliably on real work. A knowledge graph that hasn't had a health check in a year is the worst possible input for an agent."
[^card-1]: [数据目录作为企业级 Wiki 的结构等价物](data-catalog-as-enterprise-wiki.md) -- Atlan 将持续偏移检测映射为数据目录的"主动元数据传播"，两者是同一自动维护机制在不同领域的投射
[^card-2]: [文档合并门禁机制](documentation-merge-gate.md) -- 合并门禁在变更创建时保障文档质量，与持续偏移检测的后续漂移发现形成文档生命周期的互补覆盖
[^card-3]: [LLM 作为维护引擎的角色重构](llm-as-maintenance-engine.md) -- 本卡描述维护引擎角色在企业规模下的持续偏移检测机制，该卡定义这一角色的概念内涵
[^card-4]: [源忠实性风险与不可变锚点](source-faithfulness-risk.md) -- 本卡聚焦时效性偏移的持续检测（新信息 vs 旧内容），该卡识别源忠实性偏移（wiki 内容 vs 原始来源本意）；两种漂移类型需要不同的检测机制，持续偏移检测主要覆盖前者
[^dist-1]: [用户耦合漂移下的固化](entrenchment-under-user-coupled-drift.md) -- 本卡主张自动化不一致检测可发现偏移，该卡主张固化产生虚假内部一致性使检测失灵，区分点在于：检测机制对事实层不一致有效，但对范式层的结构性偏差无力
