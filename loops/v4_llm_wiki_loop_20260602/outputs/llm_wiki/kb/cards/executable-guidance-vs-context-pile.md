---
id: executable-guidance-vs-context-pile
title: 可执行指引 vs 上下文堆积
status: accepted
card_type: distinction
tags: [agent-memory, knowledge-retrieval, executable-skill, context-store, company-brain]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [cognitionus-llm-wiki-guide]
justification: ../justification/executable-guidance-vs-context-pile.md
canonical_concept: executable-guidance-vs-context-pile
aliases: [可执行指引与上下文堆积, executable guidance vs notes pile, 技能检索与上下文存储]
summary: >-
  executable-guidance-vs-context-pile（可执行指引与上下文堆积 / executable guidance vs notes pile）Cognition 的核心区分：通用知识库（company brain）存储上下文，agent 记忆系统应提供可执行指引——包含步骤、检查点、失败模式、作者归属和结果历史的结构化技能，而非一堆笔记
related: [agent-memory-lifecycle-phases, confirm-first-skill-capture]
---

Cognition 明确将自身与「通用公司知识库」（generic company brain）区分：通用知识库存储上下文（store context），而 Cognition 将工作视为学习信号，输出的是**可执行指引**（executable guidance）而非**一堆笔记**（a pile of notes）[^src-1]。

这一区分的关键差异在于输出形态。通用知识库的输出是被动的上下文片段——需要 agent 自行判断如何使用。Cognition 的输出是结构化的技能，包含：步骤（steps）、检查点（checks）和失败模式（failure modes）[^src-2]。此外，技能附带**新鲜度和结果历史**（freshness and outcome history），使 agent 能够评估技能的时效性和可靠性[^src-3]。

在检索端，agent 收到的不是一段原始文本，而是一条**路由**——指明使用哪个技能、依据谁的判断、以及如何应用[^src-4]。技能保留了教授者的身份和其判断成功的原因，使 agent 能够遵循正确的品味（follow the right taste）[^src-5]。

该区分隐含一个假设：结构化的可执行技能比原始上下文更能减少 agent 的「猜测」行为。材料中多次提到「before guessing」[^src-6]，将猜测视为 agent 缺乏可复用知识时的退化行为。

## Footnotes

[^src-1]: `data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- product description -- "Generic company brains store context. Cognition treats work as learning signal: sessions become approved skills, skills get freshness and outcome history, and agents retrieve executable guidance instead of a pile of notes."
[^src-2]: `data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "Consolidation" section -- "Raw traces compress into human-approved skills with steps, checks, and failure modes."
[^src-3]: `data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- product description -- "skills get freshness and outcome history"
[^src-4]: `data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "Teaching" section -- "The next agent receives a route: which skill, whose judgment, and how to apply it."
[^src-5]: `data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "Person-specific retrieval" section -- "Skills keep who taught them and why their judgment worked, so agents can follow the right taste."
[^src-6]: `data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` -- "For organizations" section -- "let every agent ask the brain before guessing"
