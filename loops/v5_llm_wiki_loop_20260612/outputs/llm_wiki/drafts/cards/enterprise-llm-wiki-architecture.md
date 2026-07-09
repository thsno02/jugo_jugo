---
id: enterprise-llm-wiki-architecture
title: 企业 LLM Wiki 架构要素
status: draft
card_type: architecture-pattern
tags: [enterprise-llm-wiki, tool-native-ingestion, drift-detection, ssot, ownership-routing]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [falconer-enterprise-guide]
evidence_basis: practitioner_report
justification: ../justification/enterprise-llm-wiki-architecture.md
canonical_concept: enterprise-llm-wiki-architecture
aliases: [enterprise LLM wiki, 企业LLM维基架构, company-scale LLM wiki]
summary: >-
  企业 LLM wiki 五步架构：连接源工具实现 tool-native ingestion；系统自动映射跨工具 knowledge graph；设定 SSOT canonical 文档并监控；团队正常工作系统自动检测漂移草拟更新路由给 document owner；人类与 AI agent 通过 Claude MCP 查询同一图谱
related: [personal-to-enterprise-scaling-barriers, cross-tool-entity-resolution, continuous-drift-detection]
---

材料描述的企业 LLM wiki 架构由五个步骤组成，镜像 Karpathy 模式但以企业级摄入和自动化取代个人策展。[^card-1]

**Step 1 - 连接源工具**：替代 raw/ 文件夹的是直接连接 GitHub、Slack、Linear、Granola、Google Drive 和现有 wiki（Notion/Confluence）。目标是完全覆盖，因为部分覆盖产生部分图谱。[^src-1]

**Step 2 - 系统映射知识图谱**：自动读取已连接源并生成知识图谱，标识什么是当前的、过时的、权威的、完全缺失的（团队在 Slack 中讨论但从未文档化的话题）。[^src-2]

**Step 3 - 设定 SSOT**：指定每个领域的权威文档（架构决策、runbook、onboarding 指南、产品规格、API 参考）。一旦标记为 canonical，系统从此刻起监控它，将冲突源视为补充上下文而非竞争真相。[^src-3]

**Step 4 - 正常工作**：团队不改变工作方式。PR 合并、Slack 讨论解决、决策落地时，系统检测受影响文档并草拟更新提案，文档 owner 数秒内审批接受或拒绝。知识图谱作为工作的副产品增长，而非额外工作。[^src-4]

**Step 5 - 查询 wiki**：工程师、PM 和 AI coding agent 查询同一图谱。Agent 通过 Claude MCP 等协议查询，使其输出 grounded 在团队运作的同一当前上下文中。[^src-5]

[^card-1]: 参见 [[personal-to-enterprise-scaling-barriers]] 中四维障碍是此架构要解决的问题
[^src-1]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Step 1: Connect your sources" P51 -- "The goal is full coverage, because partial coverage produces a partial graph."
[^src-2]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Step 2: Let the system map the knowledge graph" P53 -- "it reads the connected sources and produces a knowledge graph that knows what's current, what's stale, what's canonical, and what's missing entirely"
[^src-3]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Step 3: Set sources of truth" P55 -- "Once a doc is marked canonical, the system monitors it from that point forward"
[^src-4]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Step 4: Ship normally" P57 -- "The knowledge graph grows as a byproduct of work, not as additional work."
[^src-5]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Step 5: Query the wiki" P59 -- "AI coding agents through protocols like Claude MCP"
