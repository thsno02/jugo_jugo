---
id: memgpt-working-context-usage
title: MemGPT Working Context 的对话场景应用
status: draft
card_type: mechanism
tags: [memgpt, working-context, persona, user-facts, memory-correction]
created_time: 2026-06-12T10:22:00+08:00
edited_time: 2026-06-12T10:22:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: peer-reviewed
justification: ../justification/experiment/memgpt-working-context-usage.md
canonical_concept: working-context-conversational-usage
aliases: [工作上下文应用, working context usage, persona storage, user fact management]
summary: >-
  MemGPT working-context-conversational-usage 在对话中用作存储用户/persona 关键事实的固定大小区域，LLM 自主决定何时更新（含纠正过时信息）；对 conversation opener 质量至关重要，但容量有限。
related: [memgpt-main-context-structure, memgpt-conversation-opener-results, memgpt-self-directed-memory-editing]
---

Working context 在 MemGPT 对话场景中扮演"即时记忆"角色：

**存储内容**：关于用户和 agent persona 的关键事实、偏好和重要信息，使 agent 在不检索外部存储的情况下即可参考核心交互历史。[^src-1]

**更新机制**：仅通过 MemGPT 函数调用写入，LLM 自主决定何时更新。论文展示了 MemGPT 主动更正 working context 中过时信息的例子——当用户纠正了之前陈述的事实时，agent 更新对应条目。[^src-2]

**对 engagement 的贡献**：论文观察到 working context 中存储的信息对生成 engaging conversation openers "至关重要"——agent 需要直接可用的用户信息来生成个性化开场白，而非每次都从 archival storage 检索。[^src-3]

然而，working context 是固定大小的——当用户交互信息量超出容量时，LLM 面临决策困难：哪些信息保留在 working context（低延迟直接可用），哪些转存到 archival storage（高延迟需主动检索）。这一取舍的质量完全依赖 LLM 的判断力。论文未讨论 working context 的最优大小设置或信息优先级策略。[^src-1]

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Main context -- "Working context is a fixed-size read/write block of unstructured text, writeable only via MemGPT function calls. In conversational settings, working context is intended to be used to store key facts, preferences, and other important information"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Figure: example-memory-correction -- "An example conversation snippet where MemGPT (left) updates stored information. Here the information is stored in working context memory"
[^src-3]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Conversation opener -- "storing information in working context is key to generating engaging openers"
[^card-1]: -> memgpt-main-context-structure -- 本卡聚焦 working context 在对话中的具体用途，该卡描述 working context 作为三段结构之一的总体设计
[^card-2]: -> memgpt-conversation-opener-results -- 本卡说明 working context 对 engagement 的贡献，该卡报告 opener 任务的数值结果
