---
schema: comparison_provenance.v3
draft_card: ../cards/locomo-very-long-term-dialogue-dataset.md
draft_provenance: ../provenance/locomo-very-long-term-dialogue-dataset.md
similarity_result: ../similarity/locomo-very-long-term-dialogue-dataset.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0588
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0556
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.05
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选属 v2 高频干扰簇，分数 0.05–0.059。LoCoMo / MSC / Conversation Chronicles / 9K token / 19 session 等核心 token 在 v2 不出现。

## 2. draft 与候选在哪里不同

draft 锁定 LoCoMo 数据集的量级定义：平均 300 turn / 9,209 token / 19.3 session / 跨数月 / 50 段对话 / multi-modal——是 MSC 的约 9 倍 token / 6 倍 turn / 4 倍 session。论点轴是"超长期不是 token 量级，而是 session 数 + 时间跨度"。

v2 三张候选是 Karpathy LLM Wiki 概念层，无 dialogue dataset、long-term memory benchmark 相关内容。

## 3. 下一步的核心依据

(1) (2) 共同表明无重叠。draft 完整。结论 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；与 `locomo-persona-event-graph-pipeline`、`mem0-locomo-benchmark-evaluation` 等 LoCoMo 系列卡互相 cite。

## 5. 备注

无。
