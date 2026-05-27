---
schema: accepted_card_provenance.v3
card: ../cards/llm-wiki-schema-is-most-important.md
material_id: openaitoolshub-six-months
digest_id: digest_openaitoolshub-six-months
source_paths:
  - data/raw/webpage/openaitoolshub-six-months/text.txt
draft_card: ../../drafts/cards/llm-wiki-schema-is-most-important.md
draft_provenance: ../../drafts/provenance/llm-wiki-schema-is-most-important.md
similarity_result: ../../drafts/similarity/llm-wiki-schema-is-most-important.json
comparison_provenance: ../../drafts/comparison/llm-wiki-schema-is-most-important.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:42:00+08:00
  gate_notes: 6/6 项通过；schema-first 主张、Pitfall #4、"graveyard" 警告、sample size = 1 边界齐备。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T10:42:00+08:00
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

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:42:00+08:00
- 检查要点：
  - operational_rule 卡给出经验主张 + 为何 + Karpathy gist underplay 诊断 + 操作含义 + 边界，非标题复述。
  - 知识密度合格。
  - source_ids 含 `openaitoolshub-six-months`，正文锚回 text.txt:14 / 50 / 98 / 138。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 7 张相关卡。

## 备注

- 与 `llm-wiki-mcp-design-boundary-mechanics-not-content` 强互链：MCP server 不验 schema 正好把这个责任完整交还给 schema.md，本卡是对那条边界的"用户责任侧"补全。
- comparison 已确认 draft 与 v2 schema 配置文档卡论点轴对立（"三层并列"vs"schema 最重要"），不构成 provenance_delta。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/llm-wiki-schema-is-most-important.md`
- draft provenance: `../../drafts/provenance/llm-wiki-schema-is-most-important.md`
- similarity: `../../drafts/similarity/llm-wiki-schema-is-most-important.json`
- comparison provenance: `../../drafts/comparison/llm-wiki-schema-is-most-important.md`
