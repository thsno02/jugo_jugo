---
id: virtual-context-management
title: 虚拟上下文管理
status: accepted
card_type: mechanism
tags: [LLM, memory_management, OS_analogy, context_window, MemGPT]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
justification: ../justification/virtual-context-management.md
canonical_concept: virtual-context-management
aliases: [虚拟上下文, virtual context, 虚拟内存分页类比]
summary: >-
  virtual-context-management（虚拟上下文管理, virtual context）借鉴操作系统虚拟内存分页机制，通过在 LLM 有限上下文窗口（类比 RAM）与外部存储（类比磁盘）之间移动数据，为 LLM 提供无限上下文的幻觉
related: [ai-memory-operating-system, cross-session-continuity, memgpt-event-driven-control-flow, memgpt-memory-hierarchy, memgpt-queue-eviction-policy]
---

虚拟上下文管理（virtual context management）是 MemGPT 提出的核心技术，灵感来源于传统操作系统中的虚拟内存分页机制。在操作系统中，虚拟内存通过在物理内存（RAM）和磁盘之间分页数据，向应用程序提供"有更多内存资源可用"的幻觉 [^src-1]。MemGPT 将这一思路迁移到 LLM 系统：将 LLM 的固定上下文窗口视为"主内存"，将外部数据库视为"磁盘"，利用 LLM 的函数调用能力（function calling）在两者之间移动数据，从而使 LLM 能够处理远超其上下文窗口限制的任务 [^src-2]。

这一机制的关键洞察在于：与其直接扩展 transformer 的上下文长度（会带来二次方计算开销，且长上下文模型在利用中间位置信息方面表现不佳 [^src-3]），不如让 LLM 主动管理自己上下文中放置的内容，实现更灵活的内存架构 [^src-4]。

在更宏观的层面上，Jack Roberts 的 AI 记忆操作系统框架将这类 OS 类比提升为 AI 记忆架构的分类原则[^card-1]。具体到 MemGPT 内部，队列驱逐策略是虚拟上下文分页的核心实现[^card-2]，而事件驱动控制流则借鉴了 OS 中断机制来触发分页操作[^card-3]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/abstract.tex -- "a technique drawing inspiration from hierarchical memory systems in traditional operating systems which provide the illusion of an extended virtual memory via paging between physical memory and disk"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/intro.tex -- "We leverage the recent progress in function calling abilities of LLM agents to design MemGPT, an OS-inspired LLM system for virtual context management."
[^src-3]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/intro.tex -- "even if we could overcome the computational challenges of context scaling, recent research shows that long-context models struggle to utilize additional context effectively"
[^src-4]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/intro.tex -- "In this paper, we study how to provide the illusion of an infinite context while continuing to use fixed-context models."
[^card-1]: [AI 记忆操作系统框架](ai-memory-operating-system.md) -- 本卡是具体的 OS 虚拟内存分页机制，该卡将 OS 类比提升为 AI 记忆架构的宏观分类框架
[^card-2]: [MemGPT 队列驱逐与内存压力机制](memgpt-queue-eviction-policy.md) -- 本卡是虚拟上下文管理的总体概念，该卡详述其中的驱逐策略（两阶段：内存压力警告 → 队列刷新）
[^card-3]: [MemGPT 事件驱动控制流](memgpt-event-driven-control-flow.md) -- 本卡聚焦 OS 虚拟内存类比（分页式上下文管理），该卡聚焦 OS 中断类比（事件驱动控制流），两者是 MemGPT 对 OS 概念的互补借鉴
