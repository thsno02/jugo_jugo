---
id: llm-wiki-curation-over-retrieval
title: 策展优于检索的论证
status: draft
card_type: design-rationale
tags: [knowledge-management, llm-application, curation, rag-alternative, literature-velocity]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [complete-tech-live-frontier]
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-curation-over-retrieval.md
canonical_concept: llm-wiki-curation-over-retrieval
aliases: [curator over librarian, 策展优于检索]
summary: >-
  策展优于检索的论证 (llm-wiki-curation-over-retrieval): 材料给出三条动机——(1) 文献增速超过人工策展能力，论文间连接才是真正信号，手工文献目录在发布前就过时；(2) 分析框架（如 depth spectrum）需要活的家，手动维护相当于四分之一人力，schema 驱动下 LLM 在摄入时作为副产品完成；(3) 生产级参考实现比再写一篇第二大脑随想更有用。
related: [llm-wiki-pattern, bttb-production-reference]
---

材料为"策展优于检索"（LLM Wiki vs RAG/手动维护）提供了三条构建动机：[^src-1]

1. **文献增速超过人工策展能力** — 潜推理和潜通信是同一前沿的两面，论文间的连接才是真正信号。手工文献目录在发布前就过时。LLM 维护的深度交叉引用 wiki 在吸收新工作时不丢失结构。

2. **分析框架需要"活的家"** — 如 10-level 通信深度分类法，只有当领域中每个方法被放置其上并相互链接时才有意义。手动维护相当于四分之一人力投入；schema 驱动下，LLM 在摄入时作为副产品完成此工作。

3. **生产参考实现的价值** — 展示 120 页、1400 链接、schema 纪律化实现（含审计工作流、插件列表、许可分拆）比再写一篇"第二大脑"随想更有用。

[^card-1]: 参见 [llm-wiki-pattern] 了解模式定义
[^card-2]: 参见 [latent-communication-depth-spectrum] 了解动机 2 中提到的 depth spectrum

[^src-1]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- "Why we built it, beyond 'the pattern is good'" P22-25 -- "Three reasons: The literature is moving faster than human curation can keep up with...The depth spectrum needed somewhere to live...Karpathy's gist deserves a working production reference."
