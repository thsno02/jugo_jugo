---
id: llm-wiki-mcp-etag-cas
title: llm-wiki-mcp 乐观并发控制机制
status: accepted
card_type: concurrency-mechanism
tags:
- etag
- cas
- optimistic-concurrency
- conflict-resolution
- wiki
created_time: 2026-06-12 19:00:00+08:00
edited_time: 2026-06-12 19:00:00+08:00
edited_entity: llm
source_ids:
- pypi-llm-wiki-mcp
evidence_basis: documentation
justification: ../justification/llm-wiki-mcp-etag-cas.md
canonical_concept: llm-wiki-mcp-etag-cas
aliases:
- etag CAS
- optimistic concurrency
- WikiConflictError
- etag conflict check
summary: 'llm-wiki-mcp 使用 etag (sha256(body)||mtime_ns) 实现乐观并发控制。 wiki_write_page 要求提供读时获得的 etag，不匹配则 raise WikiConflictError， agent 需 re-read、merge、retry。创建新页面时传 etag=null。原子写入通过 tmp-file + fsync + rename
  实现。日志追加使用 O_APPEND 单次写入保证完整性。 路径安全通过 slug regex + realpath 对比 wiki root 实现，阻止 symlink-escape 类攻击 (CVE-2025-53109)。日志行格式锁定为 ## [YYYY-MM-DD] operation | Title。'
related:
- llm-wiki-mcp-architecture
- llm-wiki-mcp-storage-protocol
---

llm-wiki-mcp 的 server 层强制四项机制保障，其中乐观并发控制是多 agent 协作场景的核心。[^src-1] [^card-1]

## Etag CAS 机制

每个 wiki page 拥有 etag，计算方式为 `sha256(body) || mtime_ns`（body 内容哈希拼接纳秒级修改时间戳）。[^src-2]

写入流程：
1. Agent 通过 wiki_read 获取页面内容及当前 etag
2. Agent 修改内容后调用 wiki_write_page，提供读时 etag
3. Server 比对 etag：匹配则原子写入成功，返回新 etag；不匹配则 raise `WikiConflictError`
4. 冲突时 agent 需 re-read 最新版本、merge 变更、retry 写入

创建新页面时传 `etag=null` 表示预期页面不存在。

## 原子写入保障

- **Pages**: tmp-file + fsync + rename（先写临时文件，fsync 刷盘，再 rename 覆盖目标路径）
- **Log entries**: O_APPEND 模式单次写入，保证条目完整性

## 路径安全 (Path Containment)

两层防护：[^src-3]
1. Slug 正则校验——拒绝含非法字符的路径
2. Resolved path 对比 wiki root 的 realpath——阻止 symlink-escape 类攻击

据文档描述，此设计对标 CVE-2025-53109 symlink-escape 类漏洞。

## 日志行格式锁定

日志条目格式固定为 `## [YYYY-MM-DD] operation | Title`。operation 名为自由字符串，仅拒绝会破坏行结构的字符。[^src-4]

[^src-1]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- "Design boundary" P1 -- "The server enforces mechanics, not content shape"
[^src-2]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- "Design boundary" P2 -- "Every page has an etag (sha256(body) || mtime_ns). Updates supply the etag they read; a mismatch raises WikiConflictError, and the agent re-reads, merges, and retries."
[^src-3]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- "Design boundary" P3 -- "Slugs are regex-validated. Resolved paths are checked against the realpath of the root, blocking the CVE-2025-53109 symlink-escape class."
[^src-4]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- "Design boundary" P4 -- "## [YYYY-MM-DD] operation | Title. Operation names are free strings; only characters that would break the line shape are rejected."

[^card-1]: [[llm-wiki-mcp-architecture]] — 本机制是该架构机制层的核心组成
