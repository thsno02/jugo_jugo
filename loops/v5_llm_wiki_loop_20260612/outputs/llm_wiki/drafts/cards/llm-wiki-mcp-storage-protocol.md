---
id: llm-wiki-mcp-storage-protocol
title: WikiStorage Protocol 可插拔后端接口
status: draft
card_type: api-design
tags: [protocol, pluggable-backend, python, mcp, wiki-storage]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [pypi-llm-wiki-mcp]
evidence_basis: documentation
justification: ../justification/llm-wiki-mcp-storage-protocol.md
canonical_concept: llm-wiki-mcp-storage-protocol
aliases: [WikiStorage, WikiStorage Protocol, build_server, LocalFilesystemStorage]
summary: >-
  llm-wiki-mcp 通过 WikiStorage Protocol（Python Protocol 类）实现存储后端可插拔。
  接口包含 read_page, write_page, list_pages, append_log, read_log, write_raw_file
  六个异步方法。通过 build_server(storage=instance) 组合根注入。默认实现为
  LocalFilesystemStorage（由 CLI --wiki-root 参数构造）。可替换为 SQLite、Notion、
  GDrive 或 test fake。领域错误类型 WikiConflictError, WikiNotFoundError,
  WikiPermissionError, WikiPathError, WikiSchemaViolationError 可从包根导入。
related: [llm-wiki-mcp-architecture, llm-wiki-mcp-etag-cas]
---

llm-wiki-mcp 的存储层通过 Python Protocol 类 `WikiStorage` 定义接口，实现后端可插拔。[^src-1] [^card-1]

## 接口定义

WikiStorage Protocol 要求实现六个异步方法：

| 方法 | 签名 | 用途 |
|------|------|------|
| `read_page` | `(slug: str) -> PageRead` | 读取单页，返回内容+etag |
| `write_page` | `(slug, body, expected_etag=None) -> str` | 原子写入，返回新 etag |
| `list_pages` | `() -> list[str]` | 列出所有页面 slug |
| `append_log` | `(entry: LogEntry) -> None` | 追加日志条目 |
| `read_log` | `() -> str` | 读取完整日志 |
| `write_raw_file` | `(name, data) -> None` | 写入 raw 文件（通常 raises） |

## 组合根模式

`build_server` 是唯一的组合根（composition root）。CLI 的 `main()` 仅构造 `LocalFilesystemStorage`（从 `--wiki-root` 参数）并传入 `build_server`。自定义后端只需满足 Protocol 接口，无需继承具体类。[^src-2]

## 领域错误类型

包根导出五个 typed domain errors，供调用方在自身边界捕获：
- `WikiConflictError` — etag 不匹配
- `WikiNotFoundError` — 页面不存在
- `WikiPermissionError` — 权限拒绝
- `WikiPathError` — 路径逃逸
- `WikiSchemaViolationError` — schema 违规

## 适用后端示例

文档提到 SQLite、Notion、GDrive、test fake 作为可替换后端场景。[^src-3]

[^src-1]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- "Python API" P1 -- "If you want to wrap the MCP server with your own storage backend (SQLite, Notion, GDrive, a test fake), implement the WikiStorage Protocol and pass an instance to build_server"
[^src-2]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- "Python API" P2 -- "build_server is the composition root. The CLI main() is a thin caller that constructs LocalFilesystemStorage from --wiki-root and hands it in."
[^src-3]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- "Python API" P1 -- "SQLite, Notion, GDrive, a test fake"

[^card-1]: [[llm-wiki-mcp-architecture]] — 本 Protocol 是该架构可插拔设计的具体实现
