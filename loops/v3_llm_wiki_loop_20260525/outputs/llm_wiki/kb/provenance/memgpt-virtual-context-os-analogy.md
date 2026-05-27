---
schema: accepted_card_provenance.v3
card: ../cards/memgpt-virtual-context-os-analogy.md
material_id: arxiv-memgpt
digest_id: digest_arxiv-memgpt
source_paths:
  - data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt
draft_card: ../../drafts/cards/memgpt-virtual-context-os-analogy.md
draft_provenance: ../../drafts/provenance/memgpt-virtual-context-os-analogy.md
similarity_result: ../../drafts/similarity/memgpt-virtual-context-os-analogy.json
comparison_provenance: ../../drafts/comparison/memgpt-virtual-context-os-analogy.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:42:00+08:00
  gate_notes: 6/6 项通过；OS 类比四元映射与 verbatim 源严格对应。
created_time: 2026-05-26T11:20:00+08:00
edited_time: 2026-05-27T14:42:00+08:00
edited_entity: llm
---

## 源证据

- abstract（行 1197）："To enable using context beyond limited context windows, we propose virtual context management, a technique drawing inspiration from hierarchical memory systems in traditional operating systems which provide the illusion of an extended virtual memory via paging between physical memory and disk."
- intro（行 1555–1557）："Our approach borrows from the idea of virtual memory paging that was developed to enable applications to work on datasets that far exceed the available memory by paging data between main memory and disk. We leverage the recent progress in function calling abilities of LLM agents to design MemGPT, an OS-inspired LLM system for virtual context management."
- intro（行 1572–1575）："we treat context windows as a constrained memory resource, and design a memory hierarchy for LLMs analogous to memory tiers used in traditional OSes ... To provide a similar illusion of longer context length (analogous to virtual memory), we allow the LLM to manage what is placed in its own context (analogous to physical memory) via an 'LLM OS', which we call MemGPT."
- method（行 1633–1637）："MemGPT's OS-inspired multi-level memory architecture delineates between two primary memory types: main context (analogous to main memory/physical memory/RAM) and external context (analogous to disk memory/disk storage)."
- experiments（行 1515）：嵌套 KV 任务 GPT-3.5 不能完成、GPT-4 不受嵌套层数影响——印证抽象对底层模型函数调用能力的依赖。
- conclusion（行 709）："MemGPT, a novel LLM system inspired by operating systems to manage the limited context windows of large language models."

## 卡片范围是否成立

本卡只覆盖"OS 类比 + virtual context management 这一概念框架"，不展开 main/external 内部结构（留给 memgpt-main-vs-external-context）、不展开 queue 驱逐（留给 memgpt-queue-eviction-policy）。核心主张全部来自 abstract/intro/method/conclusion。"OS 类比有限、page fault 是用户态"是引申性观察，仅作为 boundary 提示，不是论文主张。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:42:00+08:00
- 检查要点：
  - 标题已表达概念主张；正文展开四元映射 + 对比线 + 操作含义 + 边界。
  - 知识密度足。
  - 源支撑：abstract / intro / method / conclusion 4 段 verbatim。
  - References + Footnotes 双在。
  - frontmatter 完整；related 含 6 张同/邻系列卡。

## 备注

- 与 v2 可能已有 MemGPT 简介卡有重叠，但本卡聚焦"为什么是 OS 类比"这条线，应保留。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/memgpt-virtual-context-os-analogy.md`
- draft provenance: `../../drafts/provenance/memgpt-virtual-context-os-analogy.md`
- similarity: `../../drafts/similarity/memgpt-virtual-context-os-analogy.json`
- comparison provenance: `../../drafts/comparison/memgpt-virtual-context-os-analogy.md`
