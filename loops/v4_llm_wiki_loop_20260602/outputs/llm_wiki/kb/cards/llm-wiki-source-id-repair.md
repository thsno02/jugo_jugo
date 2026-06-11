---
id: llm-wiki-source-id-repair
title: LLM Wiki 源 ID 修复机制
status: accepted
card_type: mechanism
tags: [llm-wiki, source-id, repair, migration, non-ascii, deterministic]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [clawhub-llm-wiki-karpathy]
justification: ../justification/llm-wiki-source-id-repair.md
canonical_concept: llm-wiki-source-id-repair
aliases: [kb_repair_source_ids, 源ID修复, source-id repair, 非ASCII源ID, 确定性修复工作流]
summary: >-
  llm-wiki-source-id-repair（kb_repair_source_ids / 源ID修复）llm-wiki-karpathy 运行时通过确定性修复工作流迁移过时源 ID，支持稳定非 ASCII 源 ID，将遗留 src-untitled-* 记录向前迁移而非保留过时清单状态
related: [runtime-agent-boundary, llm-wiki-vault-three-layer-shape]
---

llm-wiki-karpathy 运行时提供 `kb_repair_source_ids` 操作，用于确定性地修复过时的源文档标识符[^src-1]。该机制解决了知识库演进中的一个核心问题：当原始资料被重命名、重新组织或 ID 生成规则变更时，已有的源笔记和清单记录中的旧 ID 如何迁移。

**修复范围**[^src-2]：
- 过时的源文档 ID（source doc ids）
- 过时的源笔记路径（source note paths）
- 过时的原始哈希（raw hashes）

**关键设计决策**：
- 支持稳定的非 ASCII 源 ID——中文、日文等非拉丁字符可直接作为源 ID 的一部分，无需转写为 ASCII[^src-3]
- 遗留的 `src-untitled-*` 记录会被向前迁移到新的 ID 格式，而非被过时的清单状态永久保留[^src-3]
- 提供 dry-run 和 apply 两种模式：不带 `--apply` 仅预览修复计划，带 `--apply` 执行实际修改[^src-4]

这一机制使得知识库可以在不丢弃已有可读 ID 的前提下，随时修复引用断裂。修复是确定性的——同样的输入状态总是产生同样的修复结果，保证可审计性[^src-2]。

## Footnotes

[^src-1]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "CLI Commands" -- "llm-wiki-karpathy kb_repair_source_ids --vault-root /vault" 和 "llm-wiki-karpathy kb_repair_source_ids --vault-root /vault --apply"
[^src-2]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "What 0.4.4 Implements" -- "source-id repair through kb_repair_source_ids, so stale source doc ids, source note paths, and raw hashes can be repaired without throwing away readable existing ids"
[^src-3]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "What 0.4.4 Implements" -- "stable non-ASCII source ids plus deterministic repair workflows, so legacy src-untitled-* records are migrated forward instead of being preserved by stale manifest state"
[^src-4]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "CLI Commands" -- "llm-wiki-karpathy kb_repair_source_ids --vault-root /vault" 和 "llm-wiki-karpathy kb_repair_source_ids --vault-root /vault --apply"
