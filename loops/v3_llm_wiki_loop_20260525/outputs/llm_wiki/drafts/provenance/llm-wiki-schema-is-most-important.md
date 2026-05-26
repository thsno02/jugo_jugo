---
schema: draft_card_provenance.v3
draft_card: ../cards/llm-wiki-schema-is-most-important.md
material_id: openaitoolshub-six-months
digest_id: digest_openaitoolshub-six-months
source_paths:
  - data/raw/webpage/openaitoolshub-six-months/text.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/webpage/openaitoolshub-six-months/text.txt:14` —— "the schema file as the most important file, which Karpathy's original gist underplays"。
2. `text.txt:50` —— "Schema first, content second... Rohit Ghumare put it bluntly: 'Schema is the most important file.' He's right."
3. `text.txt:98` —— Pitfall #4 完整描述（karpathy.md vs andrej-karpathy.md 双 slug）。
4. `text.txt:138` —— "Without it, the wiki devolves into a graveyard within two months."

## 卡片范围是否成立

- 卡片范围严格限定在"schema 为何最重要 + 应该写什么 + Karpathy gist 为何 underplay + 操作含义"，避免与 rohit-v2 / TL;DR / contradictions 三张兄弟卡重复（各自有独立主题）。
- "Karpathy gist 缺 schema 衰败更隐蔽" 是基于 raw / wiki / schema 三层缺失后果对比的合理引申，原文未直接论述。
- sample size = 1 的边界声明完全来自原文 methodology 段。

## 发表门控结果

本轮未运行。

## 备注

- 与 `llm-wiki-mcp-design-boundary-mechanics-not-content` 强互链：MCP server 不验 schema 正好把这个责任完整交还给 schema.md，本卡是对那条边界的"用户责任侧"补全。
