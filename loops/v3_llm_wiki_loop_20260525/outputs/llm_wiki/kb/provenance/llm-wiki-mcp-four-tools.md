---
schema: accepted_card_provenance.v3
card: ../cards/llm-wiki-mcp-four-tools.md
material_id: pypi-llm-wiki-mcp
digest_id: digest_pypi-llm-wiki-mcp
source_paths:
  - data/raw/pypi/pypi-llm-wiki-mcp/text.txt
draft_card: ../../drafts/cards/llm-wiki-mcp-four-tools.md
draft_provenance: ../../drafts/provenance/llm-wiki-mcp-four-tools.md
similarity_result: ../../drafts/similarity/llm-wiki-mcp-four-tools.json
comparison_provenance: ../../drafts/comparison/llm-wiki-mcp-four-tools.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:27:00+08:00
  gate_notes: 6/6 项通过；四工具表格 + annotation + CAS 协议 + 故意留白均锚到原文行号。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T10:27:00+08:00
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

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:27:00+08:00
- 检查要点：
  - 四工具表格 + 设计要点 + 故意留白 + 操作含义层次清晰，非标题复述。
  - 知识密度合格：契约、CAS 协议、log 非幂等、inventory 用法。
  - source_ids 含 `pypi-llm-wiki-mcp`，正文锚回 text.txt:115 / 155-167 / 180-181。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 6 张相关卡。

## 备注

- 与 `llm-wiki-mcp-design-boundary-mechanics-not-content` 互补：本卡列工具契约，兄弟卡讲"server 故意不管的事"。
- 与 `llm-wiki-mcp-skills-vs-tools-workflow` 互补：本卡讲 tool，兄弟卡讲 skill。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/llm-wiki-mcp-four-tools.md`
- draft provenance: `../../drafts/provenance/llm-wiki-mcp-four-tools.md`
- similarity: `../../drafts/similarity/llm-wiki-mcp-four-tools.json`
- comparison provenance: `../../drafts/comparison/llm-wiki-mcp-four-tools.md`
