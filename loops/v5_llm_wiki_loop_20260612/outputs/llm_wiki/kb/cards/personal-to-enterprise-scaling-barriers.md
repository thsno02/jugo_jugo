---
id: personal-to-enterprise-scaling-barriers
title: 个人知识模式到企业的四维扩展障碍
status: accepted
card_type: analysis-framework
tags:
- enterprise-knowledge
- scaling-barriers
- capture
- link
- compound
- stay-current
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- falconer-enterprise-guide
evidence_basis: practitioner_report
justification: ../justification/personal-to-enterprise-scaling-barriers.md
canonical_concept: personal-to-enterprise-scaling-barriers
aliases:
- 四属性扩展问题
- capture-link-compound-current barriers
summary: Karpathy LLM Wiki 四属性 capture/link/compound/stay-current 在企业场景各有结构性障碍；capture 无等价 raw/ 文件夹知识散布多工具；link 需跨工具实体解析而非文件内双向链接；compound 无人集成则新文档堆积不复利而是腐烂；stay-current 健康检查需自动化因文档作者已换组
related:
- karpathy-llm-wiki-pattern
- context-rot-vs-compounding
- continuous-drift-detection
- cross-tool-entity-resolution
- enterprise-llm-wiki-architecture
---
Karpathy LLM Wiki 的四个有效属性（capture、link、compound、stay current）在企业场景各遇到结构性障碍，而非单纯的纪律问题。[^card-1]

**Capture**：企业不存在等价的 raw/ 文件夹。组织知识散布于 GitHub PR、Slack threads、Linear tickets、Granola 会议记录、Google Drive 设计文档、Notion retrospectives 等十余工具。材料强调这"不是纪律失败——是结构性差异"。[^src-1]

**Link**：Obsidian 的双向链接仅限 vault 内文件。企业知识图谱需要跨工具语义链接——Slack 中的决策需连接实施它的 PR、追踪它的 Linear ticket、记录它的 Notion 文档。这些链接默认不存在，且当工具变更时不会存活。[^src-2]

**Compound**：无人做集成工作时，"each new doc adds to the pile rather than to the graph"。Stack Overflow 2024 开发者调查（65,000 专业开发者）显示：>60% 每天花 30+ 分钟搜寻解决方案，68% 每周遇到知识孤岛，管理者（最资深工程师）孤岛率达 73%。[^src-3]

**Stay current**：个人尺度的健康检查有效，但在企业尺度不 generalize——文档作者已换项目、了解上下文的资深工程师已离开、文档描述的系统已重写两次。[^src-4]

[^card-1]: 参见 [[karpathy-llm-wiki-pattern]] 中四项循环操作对应的四个属性
[^src-1]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Capture: the source folder doesn't exist at company scale" P21-22 -- "that's not a failure of discipline — it's a structural difference"
[^src-2]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Link: bidirectional connections need cross-tool semantics" P27 -- "an enterprise knowledge graph has to link across tools, not just across files"
[^src-3]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Compound: stale context doesn't compound, it rots" P30 -- "Stack Overflow's 2024 developer survey of 65,000 professional developers found that more than 60 percent spend 30 minutes or more a day searching"
[^src-4]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Stay current: health checks need to run automatically" P33 -- "The engineer who wrote the runbook six months ago is on a different project"
