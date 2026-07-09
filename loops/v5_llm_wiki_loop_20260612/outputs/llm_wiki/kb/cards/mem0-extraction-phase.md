---
id: mem0-extraction-phase
title: Mem0 提取阶段机制
status: accepted
card_type: mechanism
tags:
- memory-extraction
- context-window
- conversation-summary
- llm-pipeline
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-mem0
evidence_basis: experimental_paper
justification: ../justification/mem0-extraction-phase.md
canonical_concept: mem0-extraction-phase
aliases:
- extraction phase
- memory extraction
- 提取阶段
- fact extraction
summary: Mem0 extraction phase 提取阶段在接收新消息对时启动，结合对话摘要 conversation summary S 和最近 m=10
  条消息作为上下文，通过 LLM 提取函数 phi 产出候选记忆集合 Omega。异步摘要生成模块定期刷新对话摘要，不阻塞主处理管线。双重上下文来源：全局主题理解
  + 精细时间上下文。
related:
- graphiti-entity-fact-extraction
- mem0-memory-architecture-overview
- mem0-update-phase-operations
---

Mem0 的提取阶段（extraction phase）在系统接收新消息对 $(m_{t-1}, m_t)$ 时启动。为建立适当的记忆提取上下文，系统采用两个互补来源：[^src-1]

1. **对话摘要** $S$：从数据库检索的摘要，封装了整个对话历史的语义内容
2. **近期消息序列** $\{m_{t-m}, m_{t-m+1}, ..., m_{t-2}\}$：$m$ 为控制近期窗口的超参数（实验中设为 10）

摘要 $S$ 提供跨整个对话的全局主题理解，而近期消息序列提供精细时间上下文。二者与新消息对共同构成综合提示 $P = (S, \{m_{t-m}, ..., m_{t-2}\}, m_{t-1}, m_t)$，输入 LLM 实现的提取函数 $\phi$。[^src-2]

函数 $\phi(P)$ 从新交互中提取显著记忆集合 $\Omega = \{\omega_1, \omega_2, ..., \omega_n\}$，同时保持对对话更广泛上下文的感知。系统还实现了异步摘要生成模块，独立于主处理管线运作，定期刷新对话摘要，确保记忆提取始终受益于最新上下文信息而不引入处理延迟。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/proposed_work.tex" P1153 -- "the system employs two complementary sources: (1) a conversation summary S retrieved from the database... (2) a sequence of recent messages"
[^src-2]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/proposed_work.tex" P1153 -- "While S provides global thematic understanding across the entire conversation, the recent message sequence offers granular temporal context"
[^src-3]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- "sections/proposed_work.tex" P1153 -- "we implement an asynchronous summary generation module that periodically refreshes the conversation summary. This component operates independently of the main processing pipeline"
