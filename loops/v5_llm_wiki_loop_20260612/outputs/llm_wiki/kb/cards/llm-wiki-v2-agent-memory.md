---
id: llm-wiki-v2-agent-memory
title: LLM Wiki v2 agent-memory 扩展
status: accepted
card_type: tool_extension
tags:
- llm-wiki
- agent-memory
- rohitg00
- autonomous-agent
- scaling
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- anthemcreation-fr-guide
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-v2-agent-memory.md
canonical_concept: llm-wiki-v2-agent-memory
aliases:
- LLM Wiki v2
- rohitg00 agent memory
- agent-memory pattern
- LLM Wiki v2 持久记忆扩展
summary: rohitg00 发布的 LLM Wiki v2 在 Karpathy 原始概念基础上增加 agent-memory pattern——为自主编码 agent 提供持久记忆引擎。解决长期一致性（consistance à long terme）和规模扩展（scaling）问题，使 wiki 适合由自主 agent 持续自动维护。
related:
- llm-wiki-three-layer-architecture
- llm-wiki-ingestion-workflow
- llm-wiki-community-extensions
---

社区成员 rohitg00 在 GitHub Gist 发布的 LLM Wiki v2 是 Karpathy 原始概念的主要社区扩展 [^src-1]。

**扩展内容**：
- 引入 agent-memory pattern：为 AI 编码 agent 设计的持久记忆引擎
- 解决原始方案在自主 agent 场景下的 scaling 和长期一致性问题
- 使 wiki 从"人触发 ingestion"演进为"agent 自主持续维护"

这一扩展代表了 LLM wiki 从个人知识管理工具向自主 agent 基础设施演进的方向 [^card-1]。

[^src-1]: `data/raw/webpage/anthemcreation-fr-guide/markdown.md` -- "Extensions et évolutions du concept" P52 -- "LLM Wiki v2, publié sur GitHub Gist par rohitg00, étend le concept avec des patterns d'agentmemory : un moteur de mémoire persistante pensé pour les agents AI de codage. Cette version intègre des leçons sur le scaling et la consistance à long terme"
[^card-1]: [[llm-wiki-ingestion-workflow]] — 从人工触发 ingestion 到 agent 自主触发的演进
