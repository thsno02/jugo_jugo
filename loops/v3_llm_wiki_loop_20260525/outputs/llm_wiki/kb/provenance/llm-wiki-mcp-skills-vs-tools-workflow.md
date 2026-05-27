---
schema: accepted_card_provenance.v3
card: ../cards/llm-wiki-mcp-skills-vs-tools-workflow.md
material_id: pypi-llm-wiki-mcp
digest_id: digest_pypi-llm-wiki-mcp
source_paths:
  - data/raw/pypi/pypi-llm-wiki-mcp/text.txt
draft_card: ../../drafts/cards/llm-wiki-mcp-skills-vs-tools-workflow.md
draft_provenance: ../../drafts/provenance/llm-wiki-mcp-skills-vs-tools-workflow.md
similarity_result: ../../drafts/similarity/llm-wiki-mcp-skills-vs-tools-workflow.json
comparison_provenance: ../../drafts/comparison/llm-wiki-mcp-skills-vs-tools-workflow.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:32:00+08:00
  gate_notes: 6/6 项通过；skill 表 + 每次重读 schema + 跳过 bookkeeping 退化 + 客户端选型规则齐备。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T10:32:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/pypi/pypi-llm-wiki-mcp/text.txt:115` —— "Four MCP tools (...) plus four Claude Code skills (wiki-init, wiki-ingest, wiki-query, wiki-lint)."
2. `text.txt:138-151` —— Skills 表格化描述。
3. `text.txt:139` —— "Each skill reads wiki/CLAUDE.md for the active schema on every run."
4. `text.txt:151` —— "wiki-init is a one-shot scaffolder; the other three are Karpathy's three operations."
5. `text.txt:153` —— 没 skill 的 client 会跳过 bookkeeping。
6. `text.txt:195` —— skill 可通过 `importlib.resources` 装载到非 Claude agent。

## 卡片范围是否成立

- 卡片严格围绕"两层分工 + skill 表 + 为何 skill 必要 + 分发"展开，与 four-tools / design-boundary 卡职责分离。
- "用户用 Claude Desktop / Cursor 时应自己 prompt 模拟 skill" 是基于"没有 workflow guard 会退化"的合理操作引申。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:32:00+08:00
- 检查要点：
  - distinction 卡正面切分 tool 层与 skill 层，非标题复述。
  - 知识密度合格：四 skill 表 + 为何 skill 必要 + 重读 schema 设计 + 分发与客户端选型。
  - source_ids 含 `pypi-llm-wiki-mcp`，正文锚回 text.txt:115 / 138-151 / 139 / 153 / 195。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 6 张相关卡。

## 备注

- 与 v2 卡片 `llm-knowledge-base-five-stage-workflow` 在"操作流程"主题上语义相邻，但本卡聚焦工程实现层（skill vs tool），互补不重叠。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/llm-wiki-mcp-skills-vs-tools-workflow.md`
- draft provenance: `../../drafts/provenance/llm-wiki-mcp-skills-vs-tools-workflow.md`
- similarity: `../../drafts/similarity/llm-wiki-mcp-skills-vs-tools-workflow.json`
- comparison provenance: `../../drafts/comparison/llm-wiki-mcp-skills-vs-tools-workflow.md`
