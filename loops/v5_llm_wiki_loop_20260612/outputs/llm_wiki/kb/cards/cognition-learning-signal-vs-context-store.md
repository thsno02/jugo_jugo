---
id: cognition-learning-signal-vs-context-store
title: Learning Signal 与 Context Store 的区分
status: accepted
card_type: design-principle
tags:
- agent-memory
- learning-signal
- knowledge-management
- executable-guidance
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- cognitionus-llm-wiki-guide
evidence_basis: practitioner_report
justification: ../justification/cognition-learning-signal-vs-context-store.md
canonical_concept: learning-signal-vs-context-store
aliases:
- learning signal vs context store
- executable guidance vs notes
- not another company brain
summary: Cognition learning-signal-vs-context-store 设计原则：generic company brain 仅存储 context， Cognition 将工作视为 learning signal — session 转化为 approved skills，skill 带有 freshness 和 outcome history，agent 检索到的是
  executable guidance 而非 "a pile of notes"。 区别在于信号经过审批、带衰减模型、保留作者归因。
related:
- cognition-agent-memory-skill-loop
- cognition-memory-lifecycle
---
Cognition 明确将自身与 "generic company brain" 区分 [^src-1]：

- **Generic company brain** — 存储 context（文档/笔记/wiki），agent 从中检索文本片段。
- **Cognition** — 将工作（work）视为 learning signal：session 经审批后转化为 skill，skill 具有 freshness 和 outcome history，agent 检索到的是 executable guidance。

据材料描述，关键差异在于 [^card-1]：
1. 信号经过人类审批才进入共享池
2. 带有时间衰减模型（Decay），过时知识可主动刷新
3. 保留作者归因（person-specific retrieval），使 agent 遵循特定人的判断品味

材料用 "a pile of notes" 形容传统方案的检索结果，暗示其缺乏结构化和可执行性。

[^src-1]: `data/raw/webpage/cognitionus-llm-wiki-guide/markdown.md` -- "why this is not another company brain" P47-48 -- "Generic company brains store context. Cognition treats work as learning signal: sessions become approved skills, skills get freshness and outcome history, and agents retrieve executable guidance instead of a pile of notes."
[^card-1]: cognition-agent-memory-skill-loop
