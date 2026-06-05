---
schema: justification_journal.v1
card: ../cards/wiki-storage-protocol.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/pypi/pypi-llm-wiki-mcp/text.txt`
源证据：
- L191 — "implement the WikiStorage Protocol and pass an instance to build_server"
- L193 — "build_server is the composition root. The CLI main() is a thin caller that constructs LocalFilesystemStorage from --wiki-root and hands it in."
- L195 — "Typed domain errors (WikiConflictError, WikiNotFoundError, WikiPermissionError, WikiPathError, WikiSchemaViolationError) are importable from the package root"
范围论证：WikiStorage Protocol 是 llm-wiki-mcp 的存储抽象层设计，包含接口定义、组合根模式、可替换后端三个紧密耦合的子概念，构成单一原子卡；与 server-mechanics-boundary 互补（后者关注服务器做什么，本卡关注如何让存储层可替换）
