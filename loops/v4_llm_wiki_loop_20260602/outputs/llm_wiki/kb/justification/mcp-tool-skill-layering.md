---
schema: justification_journal.v1
card: ../cards/mcp-tool-skill-layering.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/pypi/pypi-llm-wiki-mcp/text.txt`
源证据：
- L115 — "Four MCP tools (wiki_read, wiki_write_page, wiki_log_append, wiki_inventory) plus four Claude Code skills (wiki-init, wiki-ingest, wiki-query, wiki-lint)."
- L153 — "The agent has to derive the workflow from tool descriptions alone, which works for one-off reads and writes but tends to skip the bookkeeping (log entries, backlink audits) the skills make explicit."
- L167 — "index.md and raw/ are intentionally not exposed as tools."
范围论证：此卡聚焦于 llm-wiki-mcp 的双层架构设计决策（工具层提供原子原语、技能层编排工作流），与 multi-platform-skill-portability（跨运行时的部署策略）和 three-layer-architecture（raw/wiki/schema 的数据分层）均为不同维度的架构概念
