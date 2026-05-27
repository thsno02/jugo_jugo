---
schema: accepted_card_provenance.v3
card: ../cards/llm-wiki-mcp-design-boundary-mechanics-not-content.md
material_id: pypi-llm-wiki-mcp
digest_id: digest_pypi-llm-wiki-mcp
source_paths:
  - data/raw/pypi/pypi-llm-wiki-mcp/text.txt
draft_card: ../../drafts/cards/llm-wiki-mcp-design-boundary-mechanics-not-content.md
draft_provenance: ../../drafts/provenance/llm-wiki-mcp-design-boundary-mechanics-not-content.md
similarity_result: ../../drafts/similarity/llm-wiki-mcp-design-boundary-mechanics-not-content.json
comparison_provenance: ../../drafts/comparison/llm-wiki-mcp-design-boundary-mechanics-not-content.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:25:00+08:00
  gate_notes: 6/6 项通过；server vs schema 二分、CVE-2025-53109 防护、WikiStorage Protocol 扩展点均锚到 text.txt 行号。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T10:25:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/pypi/pypi-llm-wiki-mcp/text.txt:117` —— "The server handles the boring layer LLMs keep getting wrong... The wiki schema lives in your own wiki/CLAUDE.md and grows with your domain. There is no Layer 3 schema validation in the server."
2. `text.txt:177-187` —— Design boundary 整段。
3. `text.txt:184` —— CVE-2025-53109 防护描述。
4. `text.txt:191-195` —— WikiStorage Protocol 扩展点。

## 卡片范围是否成立

- 卡片专门讲"哪条是 server 干的、哪条是 schema 干的"这一边界，不与 four-tools 卡（讲具体工具契约）重复。
- "用户不写 schema 则 wiki 会退化" 用到了同源材料未直接论述的判断——这是从 openaitoolshub-six-months 的同主题观察借来的引申，已在卡片中"实践含义"段标注。
- "扩展责任：换 storage backend 通过 Protocol" 直接来自 text.txt:191-195。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:25:00+08:00
- 检查要点：
  - distinction 卡正面切分 mechanics 与 content shape，非标题复述。
  - 知识密度合格：server 责任 / server 不负责 / 设计原因 / 实践含义 / 边界四节齐备。
  - source_ids 含 `pypi-llm-wiki-mcp`，正文锚回 text.txt:117 / 177-187 / 184 / 191-195。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 6 张相关卡。

## 备注

- 与 `llm-wiki-schema-is-most-important` 主题强互补；comparison_provenance 阶段建议交叉引用。
- adoption 阶段确认 draft 与 v2 schema 卡是"引用关系"非"事实重叠"，不构成 provenance_delta。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/llm-wiki-mcp-design-boundary-mechanics-not-content.md`
- draft provenance: `../../drafts/provenance/llm-wiki-mcp-design-boundary-mechanics-not-content.md`
- similarity: `../../drafts/similarity/llm-wiki-mcp-design-boundary-mechanics-not-content.json`
- comparison provenance: `../../drafts/comparison/llm-wiki-mcp-design-boundary-mechanics-not-content.md`
