---
id: cognition-memory-lifecycle
title: Cognition 记忆生命周期四阶段
status: draft
card_type: mechanism
tags: [agent-memory, evidence, consolidation, decay, teaching, memory-lifecycle]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [cognitionus-llm-wiki-guide]
evidence_basis: practitioner_report
justification: ../justification/cognition-memory-lifecycle.md
canonical_concept: agent-memory-lifecycle
aliases: [Evidence Consolidation Decay Teaching, Cognition memory lifecycle, agent memory four stages]
summary: >-
  Cognition agent-memory-lifecycle 四阶段：Evidence（prompts/files/tool calls/decisions/outcomes
  成为 typed learning events）→ Consolidation（原始 trace 压缩为含 steps/checks/failure modes
  的人类审批 skill）→ Decay（recall 和 freshness 随时间建模，过时指导可刷新）→ Teaching（下一个
  agent 获得路由：哪个 skill、谁的判断、如何应用）。person-specific retrieval 保留作者归因和品味。
related:
  - cognition-agent-memory-skill-loop
  - cognition-learning-signal-vs-context-store
---

Cognition 将 agent memory 的生命周期建模为四个阶段 [^src-1]：

1. **Evidence** — prompts、files、tool calls、decisions 和 outcomes 成为 typed learning events。这是原始信号的结构化采集。
2. **Consolidation** — 原始 trace 被压缩为人类审批的 skill，包含 steps、checks 和 failure modes [^card-1]。
3. **Decay** — recall 和 freshness 随时间建模。过时的指导可以主动询问是否刷新，而非静默失效。
4. **Teaching** — 下一个 agent 获得一条路由：使用哪个 skill、遵循谁的判断、如何应用。

其中 person-specific retrieval 确保 skill 保留"谁教的"以及"为什么其判断有效"，使 agent 能遵循正确的品味（taste）而非泛化平均 [^src-2]。

[^src-1]: `data/raw/webpage/cognitionus-llm-wiki-guide/markdown.md` -- "Read the science" P49-56 -- "Prompts, files, tool calls, decisions, and outcomes become typed learning events... The next agent receives a route: which skill, whose judgment, and how to apply it."
[^src-2]: `data/raw/webpage/cognitionus-llm-wiki-guide/markdown.md` -- "Person-specific retrieval" P59-60 -- "Skills keep who taught them and why their judgment worked, so agents can follow the right taste."
[^card-1]: cognition-agent-memory-skill-loop
