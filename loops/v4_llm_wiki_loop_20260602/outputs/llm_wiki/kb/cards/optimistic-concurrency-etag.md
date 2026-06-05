---
id: optimistic-concurrency-etag
title: 乐观并发控制（Etag CAS）
status: accepted
card_type: mechanism
tags: [llm-wiki, concurrency, etag, atomic-write, conflict-resolution]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [pypi-llm-wiki-mcp]
justification: ../justification/optimistic-concurrency-etag.md
canonical_concept: optimistic-concurrency-etag
aliases: [乐观并发, etag CAS, 乐观锁, optimistic locking, WikiConflictError]
summary: >-
  optimistic-concurrency-etag（乐观并发 / etag CAS / 乐观锁 / WikiConflictError）
  是 llm-wiki-mcp 的写入冲突检测机制：每页 etag = sha256(body)||mtime_ns，
  更新时提交读取时获得的 etag，不匹配则抛 WikiConflictError，agent 执行 re-read-merge-retry
related: [server-mechanics-boundary]
---

llm-wiki-mcp 通过**乐观并发控制（optimistic concurrency）**解决 wiki 页面的写入冲突[^src-1]。

**Etag 计算**：每个页面拥有一个 etag，由 `sha256(body) || mtime_ns` 计算得出。`wiki_read` 工具在返回页面正文时同时返回该 etag[^src-2]。

**CAS（Compare-And-Swap）写入协议**：
- **创建页面**：传入 `etag=null`[^src-3]
- **更新页面**：传入读取时获得的 etag。服务器比对当前 etag——若匹配，执行原子写入（tmp-file + fsync + rename）；若不匹配，抛出 `WikiConflictError`[^src-4]
- **冲突恢复**：agent 在收到冲突错误后执行 re-read、merge、retry 循环[^src-5]

**原子写入实现**：页面写入采用 tmp-file + fsync + rename 确保原子性；日志追加采用 `O_APPEND` 单次写入[^src-6]。

此机制属于服务器强制执行的「力学层」，与内容验证无关。

## Footnotes

[^src-1]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L180 -- "Optimistic concurrency. Every page has an etag (sha256(body) || mtime_ns)."
[^src-2]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L159 -- "wiki_read read-only, idempotent Read one page. Returns body, parsed frontmatter, outgoing links, etag."
[^src-3]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L160 -- "wiki_write_page destructive, idempotent Atomic create or update with etag CAS. Pass etag=null to create, the read etag to update."
[^src-4]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L181 -- "Updates supply the etag they read; a mismatch raises WikiConflictError"
[^src-5]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L181 -- "the agent re-reads, merges, and retries"
[^src-6]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L179 -- "Atomic writes. tmp-file + fsync + rename for pages. O_APPEND single-write for log entries."
