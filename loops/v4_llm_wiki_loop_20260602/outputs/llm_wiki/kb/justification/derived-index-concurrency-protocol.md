---
schema: justification_journal.v1
card: ../cards/derived-index-concurrency-protocol.md
created_time: 2026-06-08T10:00:00+08:00
---

## creation | 2026-06-08T10:00:00+08:00

生成方式：Mode A extraction from repo source bundle
来源：`data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt`
源证据：
- FILE: claude-plugin/skills/wiki-manager/SKILL.md — "Indexes are a derived cache. The .md files and their YAML frontmatter are the source of truth."
- FILE: claude-plugin/skills/wiki-manager/SKILL.md — "Concurrency" 完整章节：无锁设计、index 收敛性、log.md append-only、last-write-wins
- FILE: claude-plugin/commands/query.md — "Before using any _index.md, verify it's current: count .md files... compare against rows in the index table"
- FILE: claude-plugin/commands/compile.md — "If any index update is skipped or interrupted, no data is lost — the next read operation will detect the stale index and rebuild it"
范围论证：派生索引协议是 llm-wiki 零外部依赖和并发安全的设计基石。现有的 llm-wiki-pattern 卡描述"增量构建 wiki"的概念，docs-as-code 卡描述"文档可生成"的理念，但均未覆盖索引作为派生缓存的具体实现机制和并发安全保证。这是一个独立的架构决策值得单独记录。
