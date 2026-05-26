---
schema: draft_card_provenance.v3
draft_card: ../cards/llm-wiki-tldr-load-bearing.md
material_id: openaitoolshub-six-months
digest_id: digest_openaitoolshub-six-months
source_paths:
  - data/raw/webpage/openaitoolshub-six-months/text.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
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

本轮未运行。

## 备注

- 该卡 card_type 选 operational_rule：TL;DR 强制是 schema-level 可执行规则。
