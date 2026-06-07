---
id: derived-index-concurrency-protocol
title: 派生索引与并发安全协议
status: accepted
card_type: mechanism
tags: [llm-wiki, index, concurrency, derived-cache, structural-guardian]
created_time: 2026-06-08T10:00:00+08:00
edited_time: 2026-06-08T10:00:00+08:00
edited_entity: llm
source_ids: [repo-nvk-llm-wiki]
justification: ../justification/derived-index-concurrency-protocol.md
canonical_concept: derived-index-concurrency-protocol
aliases: [派生索引协议, derived index protocol, 并发安全索引, index-as-cache]
summary: >-
  derived-index-concurrency-protocol（派生索引协议 / derived index protocol / 并发安全索引 / index-as-cache）
  是 llm-wiki 的索引设计原则：_index.md 是从文件 frontmatter 派生的缓存视图而非权威来源，
  多会话可安全并发读写而无需锁，因为任何读操作都能从磁盘文件重建索引
related: [llm-wiki-pattern, hub-resolution-algorithm, docs-as-code]
---

llm-wiki 将 `_index.md` 视为**派生缓存（derived cache）**而非权威数据源——真正的权威是各 `.md` 文件的 YAML frontmatter[^src-1]。这一设计使得多个 Claude Code 会话可以安全地同时读写同一个 wiki 而无需任何锁机制[^src-2]。

**核心不变量**：如果两个会话同时写入不同文章，下一次任何读操作检测到索引行数与目录实际文件数不匹配时，会自动从文件 frontmatter 重建索引。两个独立的重建都收敛到相同的正确结果[^src-3]。

**陈旧度检测（stale-check）协议**[^src-4]：
1. 每次读取任何 `_index.md` 前，计算目录中 `.md` 文件数量（排除 `_index.md` 自身）
2. 与索引表中的行数比较
3. 如不匹配 → 立即从文件 frontmatter 内联重建索引后再使用

**写操作的最佳努力（best-effort）模式**[^src-5]：
- 研究、摄入、编译等写操作在完成后尝试更新索引
- 如果更新被跳过或中断，不会丢失任何数据
- 下一次读操作会自动检测陈旧索引并重建

**log.md 的并发安全**：采用仅追加（append-only）模式配合小原子写入，并发追加是安全的[^src-6]。

**文章/来源文件的并发**：两个会话创建不同文件永不冲突。同一文件被两个会话编辑的情况极少且被 last-write-wins 处理——对于 wiki 来说可接受，因为内容始终可以从 raw 来源重建[^src-7]。

这种「索引是派生视图」的设计消除了对数据库、文件锁或协调服务的依赖，符合 llm-wiki「零外部依赖」的设计目标[^src-8]。与 docs-as-code 模式类似，索引作为可从源文件生成的制品，保证了系统在任何中断场景下的自我修复能力[^card-1]。

## Footnotes

[^card-1]: [Docs-as-code](docs-as-code.md) -- 派生索引协议与 docs-as-code 共享「文档/索引可从源文件确定性生成」的核心设计理念

[^src-1]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/skills/wiki-manager/SKILL.md -- "Indexes are a derived cache. The .md files and their YAML frontmatter are the source of truth. _index.md files are a cached view rebuilt on read when stale."
[^src-2]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/skills/wiki-manager/SKILL.md -- "Multiple Claude Code sessions can safely read and write to the same wiki simultaneously. No locks are needed."
[^src-3]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/skills/wiki-manager/SKILL.md -- "If two sessions write articles at the same time, the next read rebuilds the index from whatever files exist. Both rebuilds converge to the same correct result."
[^src-4]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/query.md -- "Before using any _index.md, verify it's current: count .md files in the directory (excluding _index.md) and compare against rows in the index table."
[^src-5]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/compile.md -- "Update indexes (best-effort)... If any index update is skipped or interrupted, no data is lost — the next read operation will detect the stale index and rebuild it from file frontmatter."
[^src-6]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/skills/wiki-manager/SKILL.md -- "log.md is append-only with small atomic writes. Concurrent appends are safe."
[^src-7]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/skills/wiki-manager/SKILL.md -- "Two sessions editing the same file is unlikely and handled by last-write-wins (acceptable for a wiki — the content is always rebuildable from raw sources)."
[^src-8]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: AGENTS.md -- "Zero dependencies — runs entirely on built-in tools (Claude Code, OpenCode, or Codex)."
