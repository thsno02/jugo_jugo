---
id: llm-wiki-mcp-architecture
title: llm-wiki-mcp 机制层与 schema 层分离架构
status: accepted
card_type: system-architecture
tags:
- mcp
- llm-wiki
- karpathy
- architecture
- separation-of-concerns
created_time: 2026-06-12 19:00:00+08:00
edited_time: 2026-06-12 19:00:00+08:00
edited_entity: llm
source_ids:
- pypi-llm-wiki-mcp
evidence_basis: documentation
justification: ../justification/llm-wiki-mcp-architecture.md
canonical_concept: llm-wiki-mcp-architecture
aliases:
- llm-wiki-mcp
- llm wiki mcp
- MCP wiki server
summary: llm-wiki-mcp (v0.1.1, alpha, MIT) 是 Karpathy LLM wiki gist 的工程实现， 提供 MCP
  server 四工具 (wiki_read, wiki_write_page, wiki_log_append, wiki_inventory) 加 Claude
  Code 四技能 (wiki-init, wiki-ingest, wiki-query, wiki-lint)。核心设计边界： server 只强制机制层（原子写入、etag
  乐观并发、路径限制、日志行格式），不做 frontmatter shape/schema 校验。内容 schema 完全委托 wiki/CLAUDE.md 由
  LLM 自主阅读与演化。 Skills 封装 bookkeeping 工作流（log entries, backlink audits），非 Claude Code
  客户端 仅有 tools 层，需 agent 自行推导工作流。
related:
- llm-wiki-mcp-etag-cas
- llm-wiki-mcp-storage-protocol
- llm-wiki-local-api-agent-skill
- mcp-multi-client-integration
---

llm-wiki-mcp 是 Karpathy LLM wiki gist 的工程实现，为 AI agent 提供基于 markdown 的持久化知识库基础设施。[^src-1]

## 架构分层

| 层级 | 职责 | 实现位置 |
|------|------|----------|
| 机制层 (L1) | 原子写入、etag CAS、路径限制、日志格式 | MCP server |
| 工作流层 (L2) | bookkeeping (log, backlink audit) | Claude Code skills |
| 内容 schema 层 (L3) | frontmatter shape、page categories、link targets | wiki/CLAUDE.md（LLM 自主演化） |

Server 刻意不做 L3 校验——继承 Karpathy gist "deliberately silent on content shape" 的哲学。[^src-2]

## 四工具 (MCP Tools)

- **wiki_read** — read-only, idempotent。返回 body、frontmatter、outgoing links、etag。
- **wiki_write_page** — destructive, idempotent。etag CAS 原子写入（etag=null 为创建）。
- **wiki_log_append** — not idempotent。追加 `## [YYYY-MM-DD] op | Title` 格式日志。
- **wiki_inventory** — read-only, idempotent。全图快照：pages/frontmatter/link edges/log entries + 可选 mention scan。

## 四技能 (Claude Code Skills)

- **wiki-init** — 一次性脚手架，不需 MCP server。
- **wiki-ingest** — 摄入源文档，对应 Karpathy 写操作。
- **wiki-query** — 查询知识库，对应 Karpathy 读操作。
- **wiki-lint** — 健康检查，对应 Karpathy 审计操作。

每个 skill 在每次运行时读取 wiki/CLAUDE.md 获取当前 schema，因此 schema 演化无需重新安装。[^src-3]

## Wiki 文件布局

```
project/
├── raw/          # 不可变源文件
└── wiki/         # --wiki-root 指向此处
    ├── pages/    # 每主题一个 markdown 页面
    ├── log.md    # append-only 会话日志
    ├── index.md  # LLM 策展浏览页
    └── CLAUDE.md # schema 文档
```

index.md 和 raw/ 不暴露为 MCP tool——index 由宿主 Read/Write 编辑，raw 层对 server 而言不可变。[^src-4]

[^src-1]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- "Project description" P1 -- "MCP server + Claude Code skills for Karpathy-style LLM wikis: persistent markdown knowledge bases your agent grows over time."
[^src-2]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- "Design boundary" P5 -- "The server does not validate frontmatter shape, page categories, or link targets. That layer lives in your wiki/CLAUDE.md schema doc and grows with the LLM."
[^src-3]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- "Claude Code skills" P2 -- "Each skill reads wiki/CLAUDE.md for the active schema on every run, so you can evolve the schema without re-installing anything."
[^src-4]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- "The four tools" P2 -- "index.md and raw/ are intentionally not exposed as tools."
