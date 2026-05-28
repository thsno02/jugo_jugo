---
id: enterprise-llm-wiki-drift-detection-loop
title: 企业级 LLM Wiki 的 drift detection 必须连续运行并按 owner 路由
status: accepted
card_type: mechanism
tags: [#enterprise, #llm-wiki, #drift-detection, #maintenance, #ssot]
created_time: 2026-05-26T11:50:00+08:00
edited_time: 2026-05-28T10:10:00+08:00
edited_entity: llm
source_ids: [falconer-enterprise-guide]
provenance_card: ../provenance/enterprise-llm-wiki-drift-detection-loop.md
aliases: ["continuous drift detection", "doc owner routing", "SSOT designations"]
related: [enterprise-llm-wiki-four-properties, retrieval-not-enough-for-stale-kb, enterprise-llm-wiki-tool-native-ingestion, llm-wiki-contradictions-are-assets, nvk-llm-wiki-audit-and-librarian, karpathy-gist-bookkeeping-burden]
---

Karpathy 个人 LLM Wiki 的 health check 是 on-demand 的[^v3-1]——他想跑就跑、看到 lint 结果自己处理。Falconer 指南指出这个模型在企业里**不能直接放大**[^v2-1]，因为：

1. 写 runbook 的人六个月后已经去做别的项目，知道上下文的资深工程师已经离职，系统本身也被改写过两次[^src1]。
2. 不一致会"安静地"累积，直到一个新人按错误假设构建、或者一个 AI agent 读了陈旧 runbook 生成"2024 年还能跑"的代码。
3. Anthropic 工程团队把 "context as the scarcest resource for AI agents" 作为核心约束——一个一年没体检过的知识图谱是 agent 最差的输入。

企业级 LLM Wiki 因此必须把 health check 从"人触发"改成**连续后台循环**，并且把发现的问题**按 ownership 路由给具体 doc owner** 审阅。具体机制：

- **Continuous drift detection**：背景任务持续监控代码 / 线程 / 决策的变化，识别哪些既有文档因此过期或矛盾。频率匹配企业本身的变更速率（"weekly review rather than quarterly audit"）[^src3]，不再依赖人去发起体检。
- **Contradiction routing**：当新 PR 与既有 runbook 矛盾时，系统**起草更新草稿**，而不是只发"contradiction alert"[^src2]。草稿配上对应 doc 的 owner，让 owner 在数秒内 accept / reject。这意味着系统必须懂得 ownership 与路由——这是个人版没有的负担。
- **SSOT designations**：把"某文档对某领域是 canonical"作为 system property 显式登记（架构决策 / runbook / 入职指南 / 产品规格 / API 参考）。一旦 SSOT 被指定，系统从那时起监控它，而把其他相冲突的 source 当 supplementary context 而不是 competing truth[^src4]。SSOT 是 stay-current 循环的锚点——没有锚点就无法判断"谁该被更新"。
- **作为副产品的图谱增长**：团队不必改变工作方式（"the team doesn't change how it works"）；图谱在 PR merge、Slack thread 结题、决策落地时自动扩展[^src5]。这是"compounding without additional work"的关键。

操作含义：

- **drift detection 与 ownership 必须同时存在**。只检测不路由，等于把告警堆成另一种"无人处理的孤岛"；只路由不检测，等于把负担推回 doc owner 主动巡检。
- **review cadence 应该匹配组织变更率**。一个每天 50 个 PR 的工程组织无法用季度 audit；同理，把日审给低变更率的 ops 团队是过载。系统应让团队配置 review cadence，但 detection 永远 on。
- **AI agent 是消费者，不只是工具**。企业级 Wiki 的关键消费者已经不只是人——文章特别指出"agents query the same knowledge graph through Claude MCP"[^src6]。agent 在循环里既消费又（间接）生产 context，这让 stay-current 的失败影响放大。

边界 / 反例：

- 自动起草更新草稿 ≠ 自动 merge。草稿仍然需要 doc owner 决策，避免错误更新覆盖真正的 canonical truth。
- SSOT 指定本身是治理动作，不是技术动作。系统能监控 SSOT，但谁算 owner、谁有 SSOT 写权限是组织决定，文章未给具体治理模型。
- 跨工具实体解析的精度是 drift detection 的上限——如果系统把 `payments-service`（GitHub）与"the payments team"（Slack channel）错解析为同一实体，drift 告警会乱。

## References

- "Stay current: health checks need to run automatically"：`data/raw/webpage/falconer-enterprise-guide/text.txt` L68–74。
- 连续 drift detection 与按 owner 路由：同文件 L82–86。
- SSOT 指定与 "Step 3 / Step 4"：同文件 L112–118。
- agent 作为消费者：同文件 L120–122 + L150。
- Anthropic 关于 "context as the scarcest resource"：同文件 L74 + L150。

## Footnotes

- `data/raw/webpage/falconer-enterprise-guide/text.txt` L70-72：`"At the company scale, the same approach doesn't generalize. The engineer who wrote the runbook six months ago is on a different project; the senior engineer who knew the context has moved on; the system the doc described has been rewritten twice."`
- 同文件 L84：`"When a new PR contradicts the runbook, the system needs to detect the contradiction, draft an update, and route it to the document owner for review."`
- 同文件 L86：`"It runs as a background loop, surfacing flagged content on a schedule the team can act on (weekly review rather than quarterly audit)"`。
- 同文件 L112-116：`"designating which documents are canonical for each domain ... Once a doc is marked canonical, the system monitors it from that point forward and treats conflicting sources as supplementary context rather than competing truth."`
- 同文件 L118：`"As PRs merge, Slack threads resolve, and decisions land, the system detects which documents are now affected and drafts proposed updates."`
- 同文件 L122：`"AI coding agents through protocols like Claude MCP. The agents query the same knowledge graph the humans do"`。
