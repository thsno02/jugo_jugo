---
id: wiki-storage-protocol
title: WikiStorage 可插拔存储协议
status: accepted
card_type: mechanism
tags: [llm-wiki, storage, protocol, pluggable-backend, composition-root]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [pypi-llm-wiki-mcp]
justification: ../justification/wiki-storage-protocol.md
canonical_concept: wiki-storage-protocol
aliases: [WikiStorage, 可插拔存储, pluggable storage, storage backend, LocalFilesystemStorage]
summary: >-
  wiki-storage-protocol（WikiStorage / 可插拔存储 / pluggable storage / LocalFilesystemStorage）
  是 llm-wiki-mcp 的存储抽象层：实现 WikiStorage Protocol 的 6 个方法即可替换后端（SQLite/Notion/GDrive/test fake），
  build_server 作为组合根接受存储实例
related: [server-mechanics-boundary, optimistic-concurrency-etag]
---

llm-wiki-mcp 通过 Python 的 `Protocol` 类型定义了 **WikiStorage 接口**，将 MCP 服务器逻辑与具体存储后端解耦[^src-1]。

**接口方法**（6 个）：
- `read_page(slug) -> PageRead` — 读取单页
- `write_page(slug, body, expected_etag=None) -> str` — 写入页面（含可选 etag 检查）
- `list_pages() -> list[str]` — 列出所有页面
- `append_log(entry: LogEntry) -> None` — 追加日志
- `read_log() -> str` — 读取完整日志
- `write_raw_file(name, data) -> None` — 写入原始文件（通常 raise，因 raw 层不可变）[^src-2]

**组合根模式**：`build_server` 是组合根（composition root），接受一个 `WikiStorage` 实例并构建完整的 MCP 服务器。CLI 的 `main()` 函数只是一个薄调用者——从 `--wiki-root` 参数构造 `LocalFilesystemStorage` 并传入[^src-3]。

**可替换后端**：通过实现 `WikiStorage Protocol`，可以接入 SQLite、Notion、Google Drive 或测试用 fake 等后端[^src-4]。

此外，内置的 Claude Code 技能以 package data 形式存放于 `llm_wiki_mcp/skills/`，通过 `importlib.resources` 加载，支持在非 Claude Code agent 中复用。包根还导出类型化的领域错误（`WikiConflictError`、`WikiNotFoundError`、`WikiPermissionError`、`WikiPathError`、`WikiSchemaViolationError`）[^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L191 -- "implement the WikiStorage Protocol and pass an instance to build_server"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L192 -- "class MyStorage: async def read_page(self, slug: str) -> PageRead... async def write_page... async def list_pages... async def append_log... async def read_log... async def write_raw_file"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L193 -- "build_server is the composition root. The CLI main() is a thin caller that constructs LocalFilesystemStorage from --wiki-root and hands it in."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L191 -- "wrap the MCP server with your own storage backend (SQLite, Notion, GDrive, a test fake)"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L195 -- "The bundled Claude Code skills ship as package data under llm_wiki_mcp/skills/ and load via importlib.resources... Typed domain errors (WikiConflictError, WikiNotFoundError, WikiPermissionError, WikiPathError, WikiSchemaViolationError) are importable from the package root"
