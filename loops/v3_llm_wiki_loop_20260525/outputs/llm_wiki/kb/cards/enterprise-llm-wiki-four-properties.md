---
id: enterprise-llm-wiki-four-properties
title: 企业级 LLM Wiki 必须同时具备 capture / link / compound / stay current 四性
status: accepted
card_type: concept
tags: [#enterprise, #llm-wiki, #karpathy, #knowledge-graph, #maintenance]
created_time: 2026-05-26T11:45:00+08:00
edited_time: 2026-05-28T10:56:00+08:00
edited_entity: llm
source_ids: [falconer-enterprise-guide]
provenance_card: ../provenance/enterprise-llm-wiki-four-properties.md
aliases: ["四属性框架", "capture link compound stay-current"]
related: [enterprise-llm-wiki-tool-native-ingestion, enterprise-llm-wiki-drift-detection-loop, retrieval-not-enough-for-stale-kb]
---

Falconer 的企业级 LLM Wiki 指南把 Karpathy 个人 LLM Wiki 工作流抽象成四个属性[^src1]，把 "personal pattern" 和 "enterprise pattern" 拉到同一个分析框架里。判断企业知识系统是否真的"像 Karpathy 工作流一样会复利"，看它有没有同时满足这四条：

- **Capture（捕获）**：把外部材料/工作产物变成 wiki 的输入。个人版的 capture 是 `raw/` 目录里的手动整理；企业版"原料是工作本身"——分散在 GitHub PR、Slack thread、Linear 工单、Granola 会议记录、Google Drive 设计文档等十几种工具里[^v3-1]。
- **Link（连接）**：在概念 / 实体之间建立可导航的反向链接。个人版用 Obsidian 的 vault 内 bidirectional links；企业版必须做 **跨工具的实体解析**——把 "the payments service" 在设计文档、`payments-service` 在 GitHub repo、`@payments-team` 在 Slack channel 识别为同一实体[^src3]。
- **Compound（复利）**：每一次新输入都让整个知识结构更有用，而不是堆成压不进上下文的 doc 堆。个人版靠 LLM 把新 source 合并进既有 wiki page；企业版要在新 PR 与既有 runbook 矛盾时**检测矛盾、起草更新、路由给 doc owner**——也就是 compound 必须处理冲突源，不能只做累加。
- **Stay current（保持新鲜）**：让系统对"已经过期 / 已经被推翻"的内容做主动维护。个人版靠 Karpathy 自己定期跑 lint；企业版必须**持续后台**做 drift detection[^v3-2]，因为没有任何单个员工有能力为整个组织扛维护。

这四个属性的关键 insight：

- **它们是必要而非充分集合**——任何企业 KB 缺其中一个就会塌掉。Confluence/Notion 的失败模式可以用这四个属性逐项归因（多数工具只命中 capture/link 两条）。
- **个人到企业的核心断点是 stay-current**。Falconer 引用 Stack Overflow 2024 调研：60% 以上专业开发者每天花 30 分钟以上找解决方案，68% 每周至少撞一次知识孤岛，经理这一比例更升到 73%[^src2]。这些数字直接量化了"stay current 缺位"的成本。
- **maintenance 必须从人移到系统**——Karpathy 之所以个人版能跑通，是因为 LLM 自动做了维护；企业版要把维护进一步从单个 LLM 调用移到"持续后台 + 路由到 doc owner 审阅"的循环里。

边界 / 反例：

- 这套属性框架**不直接给出实现路径**。文章给出的实现建议（连接 GitHub / Slack / Linear / Granola；用 SSOT 指定 canonical doc；继续 ship；按周 review drift）是 Falconer 产品形态的展示，不能与四属性框架本身混为一谈。
- 四属性属于"流程必要条件"，与具体工具栈、组织规模无关。给 1000 人公司用和给 10 人小队用都需要这四条同时成立。
- 文章承认：retrieval 类工具（Glean / Notion AI / Confluence AI search）通常只命中 link 与查询体验，无法解决 stay-current；这是为什么"语义搜索 over 过期 KB"会更快得出错误答案[^v3-3]。

## Footnotes

[^src1]: `data/raw/webpage/falconer-enterprise-guide/text.txt` L20-26 — "The same four properties that make it work at the personal level (capture, link, compound, stay current) are needed at the company level, but the maintenance model has to change."
[^src2]: 同文件 L66 — "Stack Overflow's 2024 developer survey of 65,000 professional developers found that more than 60 percent spend 30 minutes or more a day searching for solutions, and 68 percent encounter a knowledge silo at least once a week. The same survey found that for people managers (the most experienced engineers), the silo rate climbs to 73 percent."
[^src3]: 同文件 L82 — "the graph has to understand that 'the payments service' in a design doc is the same entity as 'payments-service' in a GitHub repo and '@payments-team' in a Slack channel."
[^v3-1]: [enterprise-llm-wiki-tool-native-ingestion](enterprise-llm-wiki-tool-native-ingestion.md) — capture 在企业版被改成 tool-native ingestion 的展开。
[^v3-2]: [enterprise-llm-wiki-drift-detection-loop](enterprise-llm-wiki-drift-detection-loop.md) — stay-current 在企业版的连续后台 drift detection + owner 路由展开。
[^v3-3]: [retrieval-not-enough-for-stale-kb](retrieval-not-enough-for-stale-kb.md) — "语义搜索 over 过期 KB" 错答更快的本卡。
