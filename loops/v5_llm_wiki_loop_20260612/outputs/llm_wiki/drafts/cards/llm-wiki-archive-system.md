---
id: llm-wiki-archive-system
title: Topic Wiki 归档系统
status: superseded
superseded_by: topic-archive-lifecycle
card_type: mechanism
tags: [llm-wiki, archive, topic-lifecycle, context-management]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
evidence_basis: documentation
justification: ../justification/llm-wiki-archive-system.md
canonical_concept: topic-wiki-archive-system
aliases: [archive, topic archive, .archive/, 归档系统, archive lifecycle]
summary: >-
  topic-wiki-archive-system：整个 topic wiki 移至 topics/.archive/ 保留源历史文章输出日志但从默认查询编译研究输出维护上下文隐藏，深度查询可浮现索引命中，显式 --include-archived 才能读写，可 restore 恢复
related: [llm-wiki-topic-wiki-isolation, llm-wiki-hub-architecture]
---

llm-wiki 的归档系统管理 topic wiki 的生命周期。通过 `/wiki:archive topic <slug> --reason "why"` 将整个 topic wiki 移至 topics/.archive/。[^src-1]

归档保留了源历史、文章、输出和日志——知识保持结构可维护状态，但从默认的查询、编译、研究、输出和维护上下文中隐藏。[^src-2]

深度查询可以浮现归档索引的命中。需要显式 --include-archived 标志才能读写归档材料。归档的 topic 可通过 `archive restore` 命令恢复到活跃状态。[^src-3]

所有归档感知工具（query、ingest、compile、research、output、inventory、dataset、project、lessons-learned、librarian、refresh、audit、lint、init 和路由）都区分活跃材料与显式包含的归档上下文。[^src-4]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Archive" P32 -- "Move whole topic wikis to topics/.archive/."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Archive" P32 -- "Preserved knowledge stays structurally maintainable but out of default query, compile, research, output, and maintenance context."
[^src-3]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Architecture" P202 -- "Archive (topics/.archive/) is for whole topic wikis the user no longer wants in normal context."
[^src-4]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Changelog" P287 -- "Archive-aware tools. Query, ingest, compile, research, output, inventory, dataset, project, lessons-learned, librarian, refresh, audit, lint, init, and routing now distinguish active material from explicitly included archived context."
