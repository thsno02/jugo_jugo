---
id: derived-index-concurrency-protocol
title: 派生索引协议与无锁并发安全
status: draft
card_type: protocol-mechanism
tags: [llm-wiki, concurrency, derived-index, stale-detection, eventual-consistency]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-nvk-llm-wiki]
evidence_basis: code_implementation
justification: ../justification/derived-index-concurrency-protocol.md
canonical_concept: derived-index-concurrency-protocol
aliases: [Derived Index Protocol, index stale detection, concurrent-safe wiki, _index.md cache protocol]
summary: >-
  llm-wiki 的 _index.md 文件是派生缓存而非数据源（source of truth）。过期检测：比较目录内 .md 文件计数与索引表行数，不匹配则内联重建。这使得多个 Claude Code 会话可无锁并发写入同一 wiki——两次重建从相同磁盘文件派生，结果收敛至相同正确状态。log.md 采用 append-only 小原子写入，天然并发安全。
related: [hub-topic-wiki-isolation, llm-as-knowledge-compiler-metaphor, lint-as-schema-migration]
---

llm-wiki 的索引系统采用"派生缓存"模式实现无锁并发安全：

**核心原则**：`.md` 文件及其 YAML frontmatter 是真实数据源；`_index.md` 只是派生视图，读取时按需重建。[^src-1]

**过期检测（3-Hop Strategy 前置检查）**：
1. 计算目录中 `.md` 文件数（排除 `_index.md`）
2. 计算 `_index.md` 内容表行数
3. 若不匹配 -> 索引过期 -> 从 frontmatter 内联重建后继续操作[^src-2]

**并发安全机制**：
- 两个会话同时写入不同文章：文件写入互不冲突
- 索引可能短暂过期或被互相覆盖重建——但因两次重建从相同磁盘文件派生，结果收敛至相同正确状态
- `log.md` 为 append-only 小原子写入，并发追加安全
- 无需锁、无过期锁清理、无会话间协调[^src-3]

**写操作**：写入文件含正确 frontmatter（数据源），索引更新为"尽力而为"（best-effort）——跳过或被覆盖不丢数据。
**读操作**：始终先检查过期再信任索引。

[^src-1]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "SKILL.md Core Principles" -- "Indexes are a derived cache. The .md files and their YAML frontmatter are the source of truth."
[^src-2]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "indexing.md Stale Detection" -- "Count .md files in the directory (excluding _index.md)... If counts differ → index is stale → rebuild inline"
[^src-3]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "SKILL.md Concurrency" -- "Multiple Claude Code sessions can safely read and write to the same wiki simultaneously. No locks are needed."
