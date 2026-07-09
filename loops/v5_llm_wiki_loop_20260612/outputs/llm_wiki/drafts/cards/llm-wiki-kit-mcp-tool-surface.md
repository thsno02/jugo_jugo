---
id: llm-wiki-kit-mcp-tool-surface
title: llm-wiki-kit MCP 工具接口集
status: draft
card_type: api-surface
tags: [mcp, tool-use, agent-integration]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-iamsashank-llm-wiki-kit]
evidence_basis: code_implementation
justification: ../justification/llm-wiki-kit-mcp-tool-surface.md
canonical_concept: llm-wiki-kit-mcp-tool-surface
aliases: [llm-wiki-kit MCP tools, wiki MCP server, wiki_ingest wiki_search]
summary: >-
  llm-wiki-kit 通过 MCP 协议暴露 8 个工具给 agent: wiki_ingest（处理 PDF URL
  YouTube markdown 源）、wiki_write_page（创建或更新页面）、wiki_read_page（读页面）、
  wiki_search（SQLite FTS5 全文搜索）、wiki_lint（断链孤儿矛盾检查）、wiki_status（页面数
  源数近期活动概览）、wiki_log（追加操作日志）、wiki_graph（交互式 HTML 知识图谱）。
  通过 llm-wiki-kit serve 命令启动 MCP server，兼容 Claude Desktop Codex Cursor
  Windsurf 等 agent 的 MCP 配置格式。
related: [llm-wiki-kit-persistent-agent-memory, llm-wiki-kit-wiki-architecture]
---

llm-wiki-kit 通过 MCP（Model Context Protocol）协议将知识库操作暴露为标准化工具接口，供任何 MCP 兼容 agent 调用 [^src-1]。

## 工具清单

| 工具 | 功能 |
|------|------|
| `wiki_ingest` | 处理任意源文件（PDF、URL、YouTube、Markdown） |
| `wiki_write_page` | 创建或更新 wiki 页面 |
| `wiki_read_page` | 读取指定页面内容 |
| `wiki_search` | 基于 SQLite FTS5 的全文搜索 |
| `wiki_lint` | 检测断链、孤儿页、空页、矛盾 |
| `wiki_status` | 展示页面数量、源数量、近期活动概览 |
| `wiki_log` | 向操作日志追加条目 |
| `wiki_graph` | 生成交互式 HTML 图谱可视化 |

[^src-1]

## 连接方式

MCP server 通过 `llm-wiki-kit serve --root <path>` 命令启动。各 agent 的配置方式 [^src-2]:

- **Claude Desktop**: `claude_desktop_config.json` 中添加 mcpServers 条目
- **Codex**: `codex mcp add` 命令
- **Cursor**: `.cursor/mcp.json`
- **Windsurf**: `~/.codeium/windsurf/mcp_config.json`

## 搜索能力

wiki_search 底层使用 SQLite FTS5 提供全文检索，README 描述为 "Agent finds relevant pages instantly" [^src-3] [^card-1]。

[^src-1]: `data/raw/github_repo/repo-iamsashank-llm-wiki-kit/repo/README.md` -- "Available Tools" P211-223 -- "wiki_ingest | Process any source... wiki_search | Full-text search across all pages"
[^src-2]: `data/raw/github_repo/repo-iamsashank-llm-wiki-kit/repo/README.md` -- "Quickstart" P65-111 -- "Add to Claude Desktop config... codex mcp add... .cursor/mcp.json... ~/.codeium/windsurf/mcp_config.json"
[^src-3]: `data/raw/github_repo/repo-iamsashank-llm-wiki-kit/repo/README.md` -- "What Makes This Different" P138 -- "Full-text search | Agent finds relevant pages instantly (SQLite FTS5)"
[^card-1]: llm-wiki-kit-persistent-agent-memory -- 该工具是持久记忆方案的接口层
