---
id: ssot-designation-governance
title: SSOT 指定与所有权治理
status: accepted
card_type: mechanism
tags: [enterprise-wiki, ssot, ownership, canonical-document, governance]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [falconer-enterprise-guide]
justification: ../justification/ssot-designation-governance.md
canonical_concept: ssot-designation-governance
aliases: [SSOT 指定, SSOT designation, 权威文档指定, canonical document designation, 所有权元数据]
summary: >-
  ssot-designation-governance（SSOT 指定 / canonical document designation / 权威文档指定 / 所有权元数据）
  是企业 LLM Wiki 的治理机制：为每个领域指定权威文档并附加所有权元数据，系统从指定时刻起
  持续监控该文档，将冲突来源视为补充上下文而非竞争真相
related: [continuous-drift-detection, cross-tool-entity-resolution, knowledge-as-work-byproduct, three-layer-architecture, single-curator-bottleneck]
---

个人 LLM Wiki 的 CLAUDE.md schema 文件告诉 agent 如何操作 vault——这是个人规模下的"治理层"[^src-1]。企业等价物是**为每个领域指定哪些文档是权威的**：架构决策、runbook、onboarding 指南、产品规格、API 参考[^src-2]。

SSOT 指定的核心机制包含三个层次：

1. **指定（designation）**：将特定文档标记为特定领域的权威来源
2. **监控（monitoring）**：一旦文档被标记为权威，系统从该时刻起持续监控它
3. **冲突处理（conflict resolution）**：将与权威文档冲突的其他来源视为**补充上下文**（supplementary context）而非**竞争真相**（competing truth）[^src-3]

这一机制与个人 LLM Wiki 的 schema 层形成对比。在 Karpathy 的模式中，CLAUDE.md 是操作指令——告诉 LLM 该怎么做；在企业版本中，SSOT 指定是**所有权元数据**（ownership metadata），作为系统的一个属性被强制执行，而非依赖个人维护[^src-4]。

SSOT 指定治理还直接决定了持续偏移检测的优先级[^card-1]——被指定为权威的文档获得更密集的一致性检查和更快的更新路由。它也与跨工具实体解析[^card-2]互补：实体解析确定"什么是同一件事"，SSOT 指定确定"哪个版本是权威的"。

对单一策展人瓶颈[^card-3]而言，SSOT 指定是一种分布式解法：不依赖一个人判断什么是权威，而是将权威性声明式地编码为系统元数据，使得所有权可以跟随团队变化而分配和转移。

## Footnotes

[^src-1]: [data/raw/webpage/falconer-enterprise-guide/markdown.md](data/raw/webpage/falconer-enterprise-guide/markdown.md) -- "What Karpathy's LLM Wiki does" 段 -- "And there's a CLAUDE.md schema file that tells the agent how to operate on the vault."
[^src-2]: [data/raw/webpage/falconer-enterprise-guide/markdown.md](data/raw/webpage/falconer-enterprise-guide/markdown.md) -- "Step 3: Set sources of truth" 段 -- "The enterprise equivalent is designating which documents are canonical for each domain: architecture decisions, runbooks, onboarding guides, product specs, API references."
[^src-3]: [data/raw/webpage/falconer-enterprise-guide/markdown.md](data/raw/webpage/falconer-enterprise-guide/markdown.md) -- "Step 3: Set sources of truth" 段 -- "Once a doc is marked canonical, the system monitors it from that point forward and treats conflicting sources as supplementary context rather than competing truth."
[^src-4]: [data/raw/webpage/falconer-enterprise-guide/markdown.md](data/raw/webpage/falconer-enterprise-guide/markdown.md) -- 比较表 -- "SSOT designations and ownership metadata, enforced as a property of the system"
[^card-1]: [持续偏移检测](continuous-drift-detection.md) -- SSOT 指定决定偏移检测的监控优先级和更新路由目标
[^card-2]: [跨工具实体解析](cross-tool-entity-resolution.md) -- 实体解析确定"什么是同一件事"，SSOT 指定确定"哪个版本是权威的"，两者互补
[^card-3]: [单一策展人瓶颈](single-curator-bottleneck.md) -- SSOT 指定将权威性从个人判断转为声明式系统元数据，是对单一策展人瓶颈的分布式解法
