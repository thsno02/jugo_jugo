---
id: memgpt-memory-hierarchy-overview
title: MemGPT 层级内存架构总览
status: draft
card_type: architecture
tags: [memgpt, memory-hierarchy, main-memory, disk-memory, os-analogy, tiered-storage]
created_time: 2026-06-12T10:26:00+08:00
edited_time: 2026-06-12T10:26:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: peer-reviewed
justification: ../justification/experiment/memgpt-memory-hierarchy-overview.md
canonical_concept: memory-hierarchy-architecture
aliases: [层级内存架构, memory hierarchy, tiered memory, main context vs external context]
summary: >-
  MemGPT memory-hierarchy-architecture 区分 main context（类比 RAM，即 prompt tokens，in-context）和 external context（类比 disk，archival+recall storage，out-of-context），数据必须显式移入 main context 才能被 LLM 访问。
related: [memgpt-main-context-structure, memgpt-archival-vs-recall-storage, memgpt-os-analogy-limitations]
---

MemGPT 的核心架构是 OS 风格的两级内存层次：

**Main Context（类比 RAM/物理内存）**：即 LLM 的 prompt tokens——所有在 main context 中的信息被视为 "in-context"，可在推理时被 LLM processor 直接访问。包含 system instructions、working context、FIFO queue。[^src-1]

**External Context（类比 Disk/磁盘存储）**：任何保存在 LLM 固定上下文窗口之外的信息。这些 "out-of-context" 数据必须通过函数调用显式移入 main context 才能被 LLM 在推理中使用。由 archival storage（任意文本数据库）和 recall storage（消息历史数据库）组成。[^src-1]

**设计原则**：MemGPT 通过函数调用使 LLM processor 无需用户干预即可自行管理内存——决定何时 page in（从 external 检索到 main）、何时 page out（从 main 存储到 external），以及何时修改 main context 内容。[^src-2]

然而，与真正的 OS 内存层次不同，MemGPT 的层级间没有硬件强制的一致性保证。OS 中 page table 确保虚拟地址总是映射到正确的物理位置；MemGPT 中 LLM 可能"忘记"某条信息已存储在 archival storage，或不知道需要检索什么——系统的一致性完全依赖 LLM 的"记忆"和推理能力。[^src-1]

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Method -- "MemGPT's OS-inspired multi-level memory architecture delineates between two primary memory types: main context (analogous to main memory/physical memory/RAM) and external context (analogous to disk memory/disk storage)."
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Method -- "MemGPT provides function calls that the LLM processor to manage its own memory without any user intervention."
[^card-1]: -> memgpt-main-context-structure -- 本卡概述层级架构全貌，该卡深入 main context 的内部三段结构
[^card-2]: -> memgpt-archival-vs-recall-storage -- 本卡概述两级架构，该卡深入 external context 的两种存储类型
[^card-3]: -> memgpt-os-analogy-limitations -- 本卡使用 OS 类比描述架构，该卡分析这一类比的局限
