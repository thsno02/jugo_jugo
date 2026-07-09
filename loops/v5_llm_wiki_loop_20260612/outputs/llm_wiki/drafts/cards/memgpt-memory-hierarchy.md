---
id: memgpt-memory-hierarchy
title: MemGPT 内存层级架构
status: draft
card_type: system-architecture
tags: [llm-memory, context-window, os-inspired, memory-hierarchy]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: experimental_paper
justification: ../justification/memgpt-memory-hierarchy.md
canonical_concept: memgpt-memory-hierarchy
aliases: [MemGPT memory hierarchy, MemGPT 内存层级, OS-inspired memory hierarchy for LLMs]
summary: >-
  MemGPT memgpt-memory-hierarchy 内存层级架构 将LLM系统划分为主上下文(main context,
  类比RAM/物理内存)和外部上下文(external context, 类比磁盘存储)两个层级。
  主上下文即prompt tokens, 外部上下文包括archival storage和recall storage,
  数据必须显式移入主上下文才能被LLM processor在推理时访问。
related: [memgpt-virtual-context-management, memgpt-main-context-structure]
---

MemGPT 采用受操作系统启发的多层级内存架构，区分两种主要内存类型：**主上下文** (main context) 和**外部上下文** (external context)。[^src-1]

主上下文对应 LLM 的 prompt tokens -- 位于主上下文中的任何内容被视为"in-context"，可被 LLM processor 在推理过程中直接访问。外部上下文则指保存在 LLM 固定上下文窗口之外的所有信息。这些"out-of-context"数据必须被显式移入主上下文后，才能在推理时传递给 LLM processor。[^src-1]

这一层级的 OS 类比关系：
- 主上下文 = 主内存 / 物理内存 / RAM
- 外部上下文 = 磁盘存储 [^src-2]

MemGPT 提供函数调用接口，使 LLM processor 能够在无用户干预的情况下自主管理其内存。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/method_rewrite.tex" -- "MemGPT's OS-inspired multi-level memory architecture delineates between two primary memory types: main context (analogous to main memory/physical memory/RAM) and external context (analogous to disk memory/disk storage)"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/intro.tex" -- "we treat context windows as a constrained memory resource, and design a memory hierarchy for LLMs analogous to memory tiers used in traditional OSes"
[^card-1]: [memgpt-virtual-context-management] 虚拟上下文管理是本层级架构的上层设计理念
