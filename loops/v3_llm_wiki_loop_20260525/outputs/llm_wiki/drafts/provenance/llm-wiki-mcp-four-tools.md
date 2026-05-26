---
schema: draft_card_provenance.v3
draft_card: ../cards/llm-wiki-mcp-four-tools.md
material_id: pypi-llm-wiki-mcp
digest_id: digest_pypi-llm-wiki-mcp
source_paths:
  - data/raw/pypi/pypi-llm-wiki-mcp/text.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/pypi/pypi-llm-wiki-mcp/text.txt:115` —— "Four MCP tools (wiki_read, wiki_write_page, wiki_log_append, wiki_inventory) plus four Claude Code skills..."
2. `text.txt:155-167` —— 四工具表格化描述（含 annotation）。
3. `text.txt:167` —— "index.md and raw/ are intentionally not exposed as tools."
4. `text.txt:180-181` —— 原子写、etag CAS、O_APPEND 实现细节。
5. `text.txt:185` —— log line 的格式锁定。

## 卡片范围是否成立

- 卡片范围只覆盖"四个 tool 是什么 + 各自契约 + 为什么这样切"，不混入 skill 层或设计哲学（那些在另外两张兄弟卡）。
- annotation 表的 (destructive / idempotent) 标注来自原文。
- "wiki_inventory 适合做会话起始 mental map" 是合理的工程使用建议，原文未直说，已隐式以"操作含义"标注。

## 发表门控结果

本轮未运行。

## 备注

- 与 `llm-wiki-mcp-design-boundary-mechanics-not-content` 互补：本卡列工具契约，兄弟卡讲"server 故意不管的事"。
- 与 `llm-wiki-mcp-skills-vs-tools-workflow` 互补：本卡讲 tool，兄弟卡讲 skill。
