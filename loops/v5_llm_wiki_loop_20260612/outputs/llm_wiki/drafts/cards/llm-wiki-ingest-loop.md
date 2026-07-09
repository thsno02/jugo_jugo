---
id: llm-wiki-ingest-loop
title: LLM Wiki 摄入循环
status: draft
card_type: workflow
tags: [knowledge-management, llm-application, automation, ingest]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [complete-tech-live-frontier]
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-ingest-loop.md
canonical_concept: llm-wiki-ingest-loop
aliases: [ingest loop, 摄入循环, ingestion loop]
summary: >-
  LLM Wiki 摄入循环 (llm-wiki-ingest-loop) 是系统的核心承重流程：新论文进入 raw/ → LLM 按 schema 写源摘要 → 提取实体和概念（新建或扩展页面）→ 交叉引用穿线至所有相关页 → Maps of Content 更新。一篇论文触发 10-15 页面修改和数百新/更新链接。自动化了 Karpathy 所说的 bookkeeping。
related: [llm-wiki-pattern, llm-wiki-three-layer-architecture]
---

摄入循环（ingest loop）是 LLM Wiki 的核心承重流程，自动化了 Karpathy 所指的 bookkeeping 工作：[^src-1]

1. 新论文放入 `raw/pdf/`
2. LLM 读取并按 schema 写源摘要
3. 提取实体和概念，给予独立页面或扩展现有页面
4. 交叉引用线程穿过所有提及新工作的页面
5. Maps of Content 更新，使新材料置入导读路径而非孤立节点

规模指标：一篇论文 → 10-15 页面修改 → 数百新/更新链接。[^src-2]

[^card-1]: 参见 [llm-wiki-three-layer-architecture] 了解各层在摄入中的角色

[^src-1]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- "How Karpathy's pattern shows up in the build" P20 -- "The ingest loop is the load-bearing one. A new paper drops into raw/pdf/; the LLM reads it and writes a source summary against the schema; entities and concepts get extracted..."
[^src-2]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- "How Karpathy's pattern shows up in the build" P20 -- "One paper, ten to fifteen page touches, hundreds of new and updated links. That's the bookkeeping Karpathy was talking about, automated."
