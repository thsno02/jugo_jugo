---
id: obsidian-wiki-four-stage-pipeline
title: obsidian-wiki 四阶段知识处理流水线
status: draft
card_type: architecture-mechanism
tags: [knowledge-pipeline, ingest, extract, resolve, schema-emergence]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-ar9av-obsidian-wiki]
evidence_basis: code_implementation
justification: ../justification/obsidian-wiki-four-stage-pipeline.md
canonical_concept: obsidian-wiki-ingest-extract-resolve-schema
aliases: [four stages, Ingest Extract Resolve Schema, 四阶段流水线]
summary: >-
  obsidian-wiki 每次 ingest 经历四阶段流水线（obsidian-wiki-ingest-extract-resolve-schema）：
  (1) Ingest 直接读取源材料（md/PDF/JSONL/图片），无需预处理管道；
  (2) Extract 提取概念/实体/声明/关系/开放问题，生成 1-2 句 summary；
  (3) Resolve 将新知识与已有 wiki 合并，已有页更新不重复，源追踪于 frontmatter；
  (4) Schema 结构不预设而从源涌现演进，保持分类/wikilinks/索引一致性。
related: [obsidian-wiki-compile-not-retrieve-pattern]
---

obsidian-wiki 的每次知识摄入执行四个阶段[^src-1]：

**1. Ingest（摄入）**：代理直接读取源材料——markdown、PDF（含页范围）、JSONL 对话导出、纯文本日志、会议记录、图片（截图/白板照片/图表，需视觉模型）。无需预处理步骤或额外管道[^src-2]。

**2. Extract（提取）**：从原始源中提取概念、实体、声明、关系和开放问题。噪声被丢弃，信号被保留。每页在写入时生成 1-2 句 `summary:` frontmatter 字段[^src-3]。

**3. Resolve（解析/合并）**：新知识与已有 wiki 合并。若概念页已存在则更新（合并新信息、标注矛盾、强化交叉引用）；若为全新概念则创建页面。不产生重复。源通过 frontmatter 追踪以保持每个声明可归因[^src-4]。

**4. Schema（模式演进）**：wiki 结构不预先固定，而是从源涌现并随添加演进。代理维护一致性：分类保持稳定，wikilinks 指向真实页面，索引反映实际内容。添加新领域时 schema 扩展以适应，不破坏已有结构[^src-5]。

[^card-1]: [obsidian-wiki-compile-not-retrieve-pattern] — 四阶段流水线是"编译式知识管理"理念的具体实施机制

[^src-1]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "How it works" P1 -- "Every ingest runs through four stages"
[^src-2]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "How it works" P2 -- "The agent reads your source material directly. It handles whatever you throw at it: markdown files, PDFs (with page ranges), JSONL conversation exports..."
[^src-3]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "How it works" P3 -- "From the raw source, the agent pulls out concepts, entities, claims, relationships, and open questions."
[^src-4]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "How it works" P4 -- "New knowledge gets merged against what's already in the wiki. If a concept page exists, the agent updates it..."
[^src-5]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "How it works" P5 -- "The wiki schema isn't fixed upfront. It emerges from your sources and evolves as you add more."
