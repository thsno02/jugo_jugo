---
id: context-rot-vs-compounding
title: 上下文腐烂与知识复利的对立
status: draft
card_type: concept-pair
tags: [compounding, context-rot, knowledge-decay, enterprise-knowledge]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [falconer-enterprise-guide]
evidence_basis: practitioner_report
justification: ../justification/context-rot-vs-compounding.md
canonical_concept: context-rot-vs-compounding
aliases: [stale context doesn't compound it rots, 知识腐烂, context rot, knowledge compounding]
summary: >-
  材料对比 compounding 复利与 rot 腐烂：有维护循环时每个新源集成进现有结构使整体更有用；无人集成时 each new doc adds to the pile rather than to the graph 新文档堆积而非丰富图谱；stale context doesn't compound it rots 是核心修辞对立
related: [maintenance-loop-as-core-innovation, personal-to-enterprise-scaling-barriers]
---

材料构建了一个核心修辞对立：**知识复利**（compounding）vs **上下文腐烂**（context rot）。[^card-1]

**复利路径**（有维护循环时）：每添加一个源材料，LLM 将其集成进现有结构——更新受影响页面、创建新页面、标记矛盾。每次添加使整体系统更有用。[^src-1]

**腐烂路径**（无维护循环时）：新文档被撰写但旧文档不被更新。"Each new doc adds to the pile rather than to the graph"——每篇新文档堆积在旧堆上，而非丰富知识图谱。材料以 "stale context doesn't compound, it rots" 作为该维度的概括性陈述。[^src-2]

这一对立是材料批判纯检索工具的理论基础：更好的检索指向腐烂的上下文，只会更快地产出错误答案。[^card-2]

[^card-1]: 参见 [[maintenance-loop-as-core-innovation]] 维护循环作为分水岭
[^card-2]: 参见 [[maintenance-loop-as-core-innovation]] 中 "notes stay true" 的论述
[^src-1]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Compound: stale context doesn't compound, it rots" P29 -- "Karpathy's wiki compounds because every new source he ingests gets integrated into the existing structure"
[^src-2]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Compound: stale context doesn't compound, it rots" P30 -- "Each new doc adds to the pile rather than to the graph"
