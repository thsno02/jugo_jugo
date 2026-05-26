---
schema: draft_card_provenance.v3
draft_card: ../cards/llm-wiki-mcp-skills-vs-tools-workflow.md
material_id: pypi-llm-wiki-mcp
digest_id: digest_pypi-llm-wiki-mcp
source_paths:
  - data/raw/pypi/pypi-llm-wiki-mcp/text.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
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

本轮未运行。

## 备注

- 与 v2 卡片 `llm-knowledge-base-five-stage-workflow` 在"操作流程"主题上语义相邻，但本卡聚焦工程实现层（skill vs tool），五阶段卡更偏抽象 workflow，互补不重叠。
