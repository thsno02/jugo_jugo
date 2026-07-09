---
id: source-id-repair-mechanism
title: 源标识修复机制
status: accepted
card_type: mechanism
tags:
- source-id
- repair
- migration
- deterministic
- manifest
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- clawhub-llm-wiki-karpathy
evidence_basis: documentation
justification: ../justification/source-id-repair-mechanism.md
canonical_concept: source-id-repair-mechanism
aliases:
- kb_repair_source_ids
- source-id repair
- 源标识修复
- stable non-ASCII source ids
summary: source-id-repair-mechanism 源标识修复通过 kb_repair_source_ids 修复 stale source doc
  ids、 source note paths 和 raw hashes，无需丢弃可读现有 id。支持 stable non-ASCII source ids 和
  deterministic repair workflows，将 legacy src-untitled-* 记录迁移为有意义标识。 提供 dry-run 和
  --apply 两种模式。
related:
- runtime-agent-responsibility-boundary
---

## 源标识修复机制

`kb_repair_source_ids` 解决知识库演化中的标识漂移问题 [^src-1]：

- 修复 stale source doc ids、source note paths 和 raw hashes
- 无需丢弃可读的现有 id（保持向后兼容）
- 支持 stable non-ASCII source ids（非 ASCII 字符的稳定处理）
- 将 legacy `src-untitled-*` 记录迁移为有意义的标识

命令支持两种模式 [^src-2]：
- **Dry-run**（默认）: `kb_repair_source_ids --vault-root /vault`
- **Apply**: `kb_repair_source_ids --vault-root /vault --apply`

[^src-1]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "What 0.4.4 Implements" P18-19 -- "source-id repair through kb_repair_source_ids, so stale source doc ids..."
[^src-2]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "CLI Commands" P75-76 -- "kb_repair_source_ids --vault-root /vault" and "--apply"
[^card-2]: [[runtime-agent-responsibility-boundary]] — id 修复属于 runtime 的 canonical IDs 职责
