---
schema: accepted_card_provenance.v3
card: ../cards/llm-wiki-rohit-v2-improvements.md
material_id: openaitoolshub-six-months
digest_id: digest_openaitoolshub-six-months
source_paths:
  - data/raw/webpage/openaitoolshub-six-months/text.txt
draft_card: ../../drafts/cards/llm-wiki-rohit-v2-improvements.md
draft_provenance: ../../drafts/provenance/llm-wiki-rohit-v2-improvements.md
similarity_result: ../../drafts/similarity/llm-wiki-rohit-v2-improvements.json
comparison_provenance: ../../drafts/comparison/llm-wiki-rohit-v2-improvements.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:34:00+08:00
  gate_notes: 6/6 项通过；三件事 + 共同主题表 + 维护成本边界齐备并锚到 text.txt 行号。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T10:34:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/webpage/openaitoolshub-six-months/text.txt:52-58` —— Memory Lifecycle / Typed wikilinks / Contradiction protocol 三段完整描述。
2. `text.txt:72-85` —— v1 / Rohit v2 / GBrain / Jim 实际方案对比表（维护时间、Storage、Lint 等列）。
3. `text.txt:96` —— Pitfall #3 完整描述。

## 卡片范围是否成立

- 卡片完整覆盖 v2 三件事，并把它们抽象到"v1 隐式 → v2 显式合同化"的共同主题；与 `llm-wiki-contradictions-are-assets` 兄弟卡（专门讲第 3 件事）有部分重叠，但本卡作为 mechanism overview 卡保留对 3 件事的并列概述，兄弟卡聚焦其哲学含义。
- 维护时间数字（~5 min / ~10 min）直接来自原文表。
- "6 种 link type 数量是 Rohit/Jim 经验值" 来自原文 "Six relationship types total"。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:34:00+08:00
- 检查要点：
  - 三件事各自给出 v1 痛点 + v2 机制，非标题复述。
  - 知识密度合格：机制 + 实证 + 共同主题表 + 边界。
  - source_ids 含 `openaitoolshub-six-months`，正文锚回 text.txt:52-58 / 72-85 / 96。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 6 张相关卡。

## 备注

- 本卡是 v2 的"机制 overview"，`llm-wiki-contradictions-are-assets` 是其中一条机制的"哲学放大版"；两卡互链。
- adoption 阶段确认 v2 候选 scope 仅限 Karpathy gist 架构，无法承载 Rohit v2 改进，正确判 new_card。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/llm-wiki-rohit-v2-improvements.md`
- draft provenance: `../../drafts/provenance/llm-wiki-rohit-v2-improvements.md`
- similarity: `../../drafts/similarity/llm-wiki-rohit-v2-improvements.json`
- comparison provenance: `../../drafts/comparison/llm-wiki-rohit-v2-improvements.md`
