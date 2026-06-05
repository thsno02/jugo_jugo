---
id: companion-knowledge-system
title: 伴侣知识系统
status: accepted
card_type: concept
tags: [companion-memory, llm-wiki, design-class, normative-governance, personal-knowledge]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
justification: ../justification/companion-knowledge-system.md
canonical_concept: companion-knowledge-system
aliases: [伴侣知识系统, companion system, companion knowledge system, companion memory, 伴侣记忆系统, 单用户伴侣 wiki]
summary: >-
  companion-knowledge-system（伴侣知识系统 / companion system / companion memory）是一种服务于单一用户的持久化 LLM 记忆系统设计类别，其规范性治理义务是：在操作维度上镜像用户（词汇、结构、上下文连续性），在认知失败维度上补偿用户（固化、证据压制、库恩式僵化）
related: [llm-wiki-pattern, three-layer-architecture, mirror-vs-compensate-principle]
---

伴侣知识系统（companion knowledge system）是 Miteski 提出的一个规范性定义的系统设计类别，指服务于单一用户长期使用的 LLM 记忆系统[^src-1]。其核心设计目标不是追踪客观真理，而是在操作维度上镜像用户、在认知失败维度上补偿用户[^src-2]。

该类别的定义建立在三个独立论断之上[^src-3]：

1. **描述性论断**：基于增量 wiki 编译的个人 LLM 记忆系统已经展现出用户耦合的保留动态，会随时间积累为漂移
2. **分类论断**：这种漂移足以构成指定保留治理义务的理由，使个人单用户 LLM 记忆成为一个独立设计类别
3. **规范性论断**：伴侣记忆的保留策略应遵循特定设计原则——镜像操作维度、补偿认知失败模式

"伴侣"一词本身并非新概念——MemoryBank 使用"companion scenario"、Second Me 明确为单用户构建、LongMemEval 将评估与个性化辅助场景绑定[^src-4]。缺失的不是术语，而是**规范性规格**：系统必须镜像什么、必须补偿什么、可分离性要求什么，以及为什么这些义务使该类别具有可设计性[^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Abstract" -- "Personal memory is a companion system --- its job is to serve one user over the long haul, not to track objective truth."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Abstract" -- "the system should mirror its user on operational dimensions (working vocabulary, load-bearing structure, continuity of context) and compensate on epistemic failure modes (entrenchment, suppression of contradicting evidence, the Kuhnian ossification described above)"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 1.1" -- "Much of the difficulty in current LLM memory literature comes from conflating three distinct claims. We separate them."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 1.1" -- "MemoryBank (arXiv:2305.10250) already uses 'long-term AI Companion scenario' as a primary capability descriptor."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 1.1" -- "What is missing is not the word companion but a normative specification of what retention-governance obligations follow from treating a system as one"
