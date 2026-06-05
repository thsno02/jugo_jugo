---
id: mcp-tool-skill-layering
title: MCP 工具与技能的双层设计
status: accepted
card_type: mechanism
tags: [llm-wiki, mcp, architecture, tools, skills]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [pypi-llm-wiki-mcp]
justification: ../justification/mcp-tool-skill-layering.md
canonical_concept: mcp-tool-skill-layering
aliases: [工具与技能分层, tool-skill separation, MCP tools vs skills]
summary: >-
  mcp-tool-skill-layering（工具与技能分层 / tool-skill separation / MCP tools vs skills）
  是 llm-wiki-mcp 的双层架构：4 个 MCP 工具提供跨客户端可移植的原子原语（read/write/log/inventory），
  4 个 Claude Code 技能在其上编排工作流（init/ingest/query/lint）；缺少技能层时 agent 倾向跳过簿记
related: [three-layer-architecture, schema-as-configuration, multi-platform-skill-portability]
---

llm-wiki-mcp 将功能拆分为两层[^src-1]：

**工具层（MCP Tools）**——四个通过 MCP 协议暴露的原子操作：`wiki_read`（只读，返回正文、frontmatter、出链、etag）、`wiki_write_page`（带 etag CAS 的原子写入）、`wiki_log_append`（追加日志条目）、`wiki_inventory`（整个图谱快照：页面、frontmatter、链接边、日志条目，可选全文 mention 扫描）[^src-2]。工具层具有跨客户端可移植性——Claude Desktop、Cursor 等非 Claude Code 客户端均可使用。

**技能层（Claude Code Skills）**——四个以插件形式安装的工作流编排：`wiki-init`（一次性脚手架生成器，不依赖 MCP 服务器）、`wiki-ingest`、`wiki-query`、`wiki-lint`。后三者对应 Karpathy 的三种操作[^src-3]。每个技能在每次运行时读取 `wiki/CLAUDE.md` 获取当前 schema，因此 schema 演化无需重新安装[^src-4]。

**缺失技能层的后果**：仅有工具的客户端「必须仅从工具描述推导工作流，这对一次性读写有效，但倾向于跳过技能所显式化的簿记——日志条目和反向链接审计」[^src-5]。这表明工具层提供能力（capability），技能层提供纪律（discipline）。

`index.md` 和 `raw/` 目录被有意地排除在工具之外：index 是 LLM 策展的内容，通过宿主的 Read/Write 编辑；raw 层从服务器视角是不可变的[^src-6]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L115 -- "Four MCP tools (wiki_read, wiki_write_page, wiki_log_append, wiki_inventory) plus four Claude Code skills (wiki-init, wiki-ingest, wiki-query, wiki-lint)."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L157-165 -- "wiki_read read-only, idempotent Read one page... wiki_write_page destructive, idempotent Atomic create or update with etag CAS... wiki_log_append not idempotent Append one entry to log.md... wiki_inventory read-only, idempotent Snapshot the whole graph"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L151 -- "wiki-init is a one-shot scaffolder; the other three are Karpathy's three operations."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L139 -- "Each skill reads wiki/CLAUDE.md for the active schema on every run, so you can evolve the schema without re-installing anything."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L153 -- "The agent has to derive the workflow from tool descriptions alone, which works for one-off reads and writes but tends to skip the bookkeeping (log entries, backlink audits) the skills make explicit."
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L167 -- "index.md and raw/ are intentionally not exposed as tools. The index is LLM-curated content edited via the host's Read / Write. The raw layer is immutable from the server's perspective."
