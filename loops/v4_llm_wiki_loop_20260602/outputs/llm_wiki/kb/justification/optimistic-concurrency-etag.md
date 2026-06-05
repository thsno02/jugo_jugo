---
schema: justification_journal.v1
card: ../cards/optimistic-concurrency-etag.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/pypi/pypi-llm-wiki-mcp/text.txt`
源证据：
- L180-181 — "Optimistic concurrency. Every page has an etag (sha256(body) || mtime_ns). Updates supply the etag they read; a mismatch raises WikiConflictError, and the agent re-reads, merges, and retries."
- L179 — "Atomic writes. tmp-file + fsync + rename for pages. O_APPEND single-write for log entries."
- L160 — "Atomic create or update with etag CAS. Pass etag=null to create, the read etag to update."
范围论证：乐观并发控制是 llm-wiki-mcp 的核心写入安全机制，包含 etag 计算方式、CAS 协议、冲突恢复流程三个紧密耦合的子概念，适合作为单张原子卡
