---
id: memgpt-virtual-context-management
title: 虚拟上下文管理
status: accepted
card_type: system-design-concept
tags:
- llm-memory
- context-window
- os-inspired
- paging
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-memgpt
evidence_basis: experimental_paper
justification: ../justification/memgpt-virtual-context-management.md
canonical_concept: virtual-context-management
aliases:
- virtual context management
- 虚拟上下文管理
summary: MemGPT virtual-context-management 虚拟上下文管理 借鉴操作系统虚拟内存分页机制, 通过在主上下文(prompt tokens)与外部存储之间进行数据页入页出(paging), 为固定上下文窗口的LLM提供扩展上下文长度的错觉。该技术使LLM能处理远超其原生上下文限制的任务。
related:
- memgpt-memory-hierarchy
- memgpt-function-chaining
- memgpt-context-scaling-diminishing-returns
- memgpt-deep-memory-retrieval
---
虚拟上下文管理 (virtual context management) 是 MemGPT 提出的核心技术，其设计灵感来自操作系统中虚拟内存分页的原理。[^src-1]

在传统操作系统中，虚拟内存通过在物理内存与磁盘之间分页来提供超出实际物理内存容量的资源错觉。类似地，虚拟上下文管理允许 LLM 在其固定长度上下文窗口（类比物理内存）与外部存储系统之间移动数据，从而提供更长上下文长度的错觉。[^src-2]

该技术利用 LLM agent 的函数调用能力来实现自主的数据读写与上下文管理：LLM 可以从外部存储中检索相关历史数据放入上下文中，也可以将不那么相关的数据从上下文驱逐到外部存储系统。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/abstract.tex" -- "To enable using context beyond limited context windows, we propose virtual context management, a technique drawing inspiration from hierarchical memory systems in traditional operating systems"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/intro.tex" -- "Our approach borrows from the idea of virtual memory paging that was developed to enable applications to work on datasets that far exceed the available memory by paging data between main memory and disk"
[^src-3]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- "sections/intro.tex" -- "MemGPT enables the LLM to retrieve relevant historical data missing from what is placed in-context, and also evict less relevant data from context and into external storage systems"
