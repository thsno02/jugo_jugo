---
id: smart-fix-all-causality-order
title: Smart Fix All 因果序修复
status: accepted
card_type: mechanism
tags:
- llm-wiki
- lint
- automated-repair
- causality-order
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- obsidian-community-plugin
evidence_basis: documentation
justification: ../justification/smart-fix-all-causality-order.md
canonical_concept: smart-fix-all-causality-order
aliases:
- Smart Fix All
- 一键修复
- causality-ordered fix
- 因果序修复
summary: Smart Fix All 按因果顺序执行批量修复：修复污染页面 → 补全别名 → 合并重复 → 修复死链 → 链接孤儿页 → 扩展空页面。v1.9.0+ 引入。因果序确保每步前置条件已满足。
related:
- semantic-tiered-duplicate-detection
- wiki-page-aliases
---

Smart Fix All（v1.9.0+）按因果序执行一键批量修复，确保每步的前置条件已被前一步满足：[^src-1]

1. 修复污染页面（文件夹前缀误入文件名）
2. 补全别名
3. 合并重复
4. 修复死链
5. 链接孤儿页
6. 扩展空页面

这一设计避免了修复步骤间的循环依赖——例如必须先补全别名才能有效检测重复，必须先合并重复才能修复死链。[^src-2] [^card-1]

[^src-1]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "What does Smart Fix All do?" P1 -- "Fix polluted pages → Complete aliases → Merge duplicates → Fix dead links → Link orphans → Expand empty pages"
[^src-2]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Smart Fix All" P1 -- "Causality-ordered batch fix: duplicates merged → dead links resolved → orphans linked → empty pages expanded"
[^card-1]: 参见 [[semantic-tiered-duplicate-detection]] 和 [[wiki-page-aliases]] 了解因果序中关键步骤的机制
