---
schema: accepted_card_provenance.v3
card: ../cards/llm-wiki-tldr-load-bearing.md
material_id: openaitoolshub-six-months
digest_id: digest_openaitoolshub-six-months
source_paths:
  - data/raw/webpage/openaitoolshub-six-months/text.txt
draft_card: ../../drafts/cards/llm-wiki-tldr-load-bearing.md
draft_provenance: ../../drafts/provenance/llm-wiki-tldr-load-bearing.md
similarity_result: ../../drafts/similarity/llm-wiki-tldr-load-bearing.json
comparison_provenance: ../../drafts/comparison/llm-wiki-tldr-load-bearing.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:44:00+08:00
  gate_notes: 6/6 项通过；TL;DR 主张 + 对比表 + 50 字符工程意义 + 操作含义 + 边界齐备。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T10:44:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/webpage/openaitoolshub-six-months/text.txt:38` —— TL;DR 主张完整段落。
2. `text.txt:36` —— wiki 规模与结构（35 页 + 80 raw + log.md + schema.md）。

## 卡片范围是否成立

- 卡片范围限定在"TL;DR 强制规则为何 load-bearing + 工程意义 + 操作含义 + 边界"，与 schema-first / rohit-v2 / contradictions 兄弟卡职责分离。
- "index 解决发现、TL;DR 解决筛选/召回" 是基于二者功能差异的合理工程区分，原文未直接如此切分，已隐式作为 mechanism 分析。
- 字符上限对页排版 / 一屏可见的解释，是基于 50 字符 ≈ 一行宽这一物理事实的合理延伸。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:44:00+08:00
- 检查要点：
  - 主张明确（TL;DR ≤50 字符 load-bearing），非标题复述。
  - 知识密度合格：主张 + 对比表 + 工程意义 + 操作含义 + 边界。
  - source_ids 含 `openaitoolshub-six-months`，正文锚回 text.txt:38。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 5 张相关卡。

## 备注

- 该卡 card_type 选 operational_rule：TL;DR 强制是 schema-level 可执行规则。
- comparison 已确认与 v2 候选论点轴不同（health checks vs TL;DR enforcement），且 v2 没收录 Karpathy "TL;DR-on-top" 一笔带过的事实，因此无 provenance_delta 对接面。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/llm-wiki-tldr-load-bearing.md`
- draft provenance: `../../drafts/provenance/llm-wiki-tldr-load-bearing.md`
- similarity: `../../drafts/similarity/llm-wiki-tldr-load-bearing.json`
- comparison provenance: `../../drafts/comparison/llm-wiki-tldr-load-bearing.md`
