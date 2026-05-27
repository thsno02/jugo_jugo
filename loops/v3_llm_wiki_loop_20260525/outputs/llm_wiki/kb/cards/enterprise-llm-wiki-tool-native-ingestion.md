---
id: enterprise-llm-wiki-tool-native-ingestion
title: 企业级 LLM Wiki 必须 tool-native 摄取，不能依赖 raw 目录
status: accepted
card_type: operational_rule
tags: [#enterprise, #llm-wiki, #ingestion, #github, #slack, #knowledge-graph]
created_time: 2026-05-26T11:48:00+08:00
edited_time: 2026-05-27T14:46:00+08:00
edited_entity: llm
source_ids: [falconer-enterprise-guide]
provenance_card: ../provenance/enterprise-llm-wiki-tool-native-ingestion.md
aliases: ["tool-native ingestion", "no curated raw folder"]
related: [enterprise-llm-wiki-four-properties, enterprise-llm-wiki-drift-detection-loop, retrieval-not-enough-for-stale-kb, my-llm-wiki-supported-source-types, llm-wiki-karpathy-multimodal-representation-path]
---

Karpathy 个人 LLM Wiki 之所以能跑通，关键之一是 `raw/` 目录由他本人有意识地维护——挑哪些文章塞进来、塞多少、什么时候塞，都由唯一一个 curator 决定。这种 curated capture 在企业里**结构上不可能存在**，不是纪律问题。Falconer 指南把这一点写成必要的设计转换：

- **个人版的 capture 模型**：`raw/` 目录 + 单一 curator + 显式的"保存这篇文章"动作。
- **企业版的 capture 模型**：tool-native ingestion——直接从工作发生的地方拉信息，不依赖任何人去 "saving sources"。具体连接对象包括 GitHub（代码与 PR）、Slack（决策线程）、Linear（工单与项目上下文）、Granola（会议记录 / 站会）、Google Drive（设计文档与 RFC）、已有 wiki（Notion / Confluence / 内部 markdown）。

转换的具体规则：

1. **没有 raw/ 目录**：如果系统设计里仍然存在一个"谁来填这个目录"的角色，企业落地就会复刻"原 wiki 没人更"的失败。
2. **连接性优先于覆盖深度**："The goal is full coverage, because partial coverage produces a partial graph." 半覆盖会让知识图谱出现盲区，agent / 人在查询时拿到自信但错误的答案。
3. **既有文档作为补充输入，而非清洗前提**："Teams don't have to clean up their existing docs first; the system uses the cleanup as part of the baseline."——把现存 Confluence/Notion 当 source 喂入，让系统在 ingest 过程中识别"哪些是 current / stale / canonical"。
4. **ingestion 必须持续运行**，不能"按 curator 的节奏"——每次 PR merge、Slack 线程结题、决策落地，都触发系统去识别哪些既有文档受影响并起草更新。

为什么这条规则成立：

- 组织知识的"原料"就是工作本身，而工作分散在十几种工具里同时实时发生。任何"集中存档"流程都会落后于工作速度，最终成为另一个被冷落的 KB。
- 单一 curator 即使存在，也会在新成员入职、人员流动、跨团队协作时形成知识断点（Falconer 引用："the engineer who wrote the runbook six months ago is on a different project; the senior engineer who knew the context has moved on"）。
- tool-native ingestion 让 wiki 的 capture 阶段与组织本身的工作流绑定，使得 wiki 内容的 freshness 是工作流的副产品而非额外工作。

边界 / 反例：

- 这条规则**不**说"不能再有人手动整理"——它说"不能依赖人手动整理"。手动补充仍然可以作为 ingest 的一条 channel，但不能成为唯一渠道。
- 不是所有工具都同等重要：文章特别点名 GitHub / Slack / Linear / Granola / Google Drive 为"工作实际发生的地方"，这一清单反映文章作者对工程组织的偏置；非工程团队（销售、客服）的工具栈不同。
- ingestion 连接器越多，跨工具实体解析（同一服务 / 同一团队 / 同一项目在不同工具的不同名字）压力越大。这一压力推动 link 属性从"vault 内反向链接"升级为"跨工具知识图谱"。

## References

- "Capture: the source folder doesn't exist at company scale"：`data/raw/webpage/falconer-enterprise-guide/text.txt` L46–52。
- "tool-native ingestion rather than curated folder import"：同文件 L78–80。
- 落地流程 Step 1 + Step 4 + Step 5：同文件 L100–122。
- 既有 doc 作为 baseline：同文件 L152–155（FAQ）。

## Footnotes

- `data/raw/webpage/falconer-enterprise-guide/text.txt` L52：`"For an enterprise LLM wiki to capture what the company knows, it has to ingest from where the knowledge actually lives rather than from a curated folder a single person maintains."`
- 同文件 L80：`"There's no raw/ folder for someone to populate; the tools themselves are the raw layer, and the ingestion runs continuously rather than on the schedule of whoever happens to be saving sources."`
- 同文件 L106：`"The goal is full coverage, because partial coverage produces a partial graph."`
- 同文件 L152-154：`"The system ingests existing wikis (Notion, Confluence, internal markdown) as additional sources... Teams don't have to clean up their existing docs first; the system uses the cleanup as part of the baseline."`
