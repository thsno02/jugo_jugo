---
schema: draft_card_provenance.v3
draft_card: ../cards/llm-wiki-rohit-v2-improvements.md
material_id: openaitoolshub-six-months
digest_id: digest_openaitoolshub-six-months
source_paths:
  - data/raw/webpage/openaitoolshub-six-months/text.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
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

本轮未运行。

## 备注

- 本卡是 v2 的"机制 overview"，`llm-wiki-contradictions-are-assets` 是其中一条机制的"哲学放大版"；两卡互链。
