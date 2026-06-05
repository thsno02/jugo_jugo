---
id: agent-memory-lifecycle-phases
title: Agent 记忆四阶段生命周期
status: accepted
card_type: concept
tags: [agent-memory, lifecycle, evidence, consolidation, decay, teaching, cognition]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [cognitionus-llm-wiki-guide]
justification: ../justification/agent-memory-lifecycle-phases.md
canonical_concept: agent-memory-lifecycle-phases
aliases: [agent记忆生命周期, memory lifecycle phases, 证据-整合-衰退-教学循环]
summary: >-
  agent-memory-lifecycle-phases（agent记忆生命周期 / memory lifecycle phases / 证据-整合-衰退-教学循环）Cognition 产品提出 agent 记忆的四阶段模型：Evidence（会话痕迹成为类型化学习事件）→ Consolidation（原始痕迹压缩为人工审批的技能）→ Decay（召回率与新鲜度随时间建模）→ Teaching（下一个 agent 获得路由：哪个技能、谁的判断、如何应用）
related: [sleep-consolidation-architecture, cross-session-continuity]
---

Cognition 将 agent 记忆系统区分为四个阶段，而非简单的存储-检索模型[^src-1]。

**Evidence（证据）**：会话中的 prompts、文件、tool calls、决策和结果成为**类型化学习事件**（typed learning events）[^src-2]。这强调原始信号不是无差别的日志，而是带有类型信息的结构化事件。

**Consolidation（整合）**：原始痕迹被压缩为经过人工审批的技能（skills），包含步骤、检查点和失败模式[^src-3]。整合的产出是 SKILL.md 文件，等待人类审批后才进入团队共享[^src-4]。

**Decay（衰退）**：召回率（recall）和新鲜度（freshness）随时间被建模，过时的指引可以主动询问或刷新[^src-5]。材料未详述衰退的具体机制（如半衰期、使用频率权重），仅表明存在此设计意图。

**Teaching（教学）**：下一个 agent 不是收到一堆笔记，而是获得一条**路由**——指明使用哪个技能、依据谁的判断、以及如何应用[^src-6]。

该四阶段模型的核心主张是：agent 记忆不应是静态的上下文存储，而应是将工作视为学习信号的动态系统[^src-7]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "why this is not another company brain" section -- "Memory that decays, consolidates, and teaches back."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "Evidence" section -- "Prompts, files, tool calls, decisions, and outcomes become typed learning events."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "Consolidation" section -- "Raw traces compress into human-approved skills with steps, checks, and failure modes."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "Save skills" step -- "Cognition drafts the SKILL.md and waits for a human yes before sharing it."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "Decay" section -- "Recall and freshness are modeled over time, so stale guidance can ask first or refresh."
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "Teaching" section -- "The next agent receives a route: which skill, whose judgment, and how to apply it."
[^src-7]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- product description -- "Cognition treats work as learning signal: sessions become approved skills, skills get freshness and outcome history, and agents retrieve executable guidance instead of a pile of notes."
