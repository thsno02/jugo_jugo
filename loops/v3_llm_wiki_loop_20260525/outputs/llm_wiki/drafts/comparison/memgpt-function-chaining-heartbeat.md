---
schema: comparison_provenance.v3
draft_card: ../cards/memgpt-function-chaining-heartbeat.md
draft_provenance: ../provenance/memgpt-function-chaining-heartbeat.md
similarity_result: ../similarity/memgpt-function-chaining-heartbeat.json
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

三张候选属 v2 高频干扰簇，分数 0.05–0.059。MemGPT / request_heartbeat / function chaining / multi-hop retrieval 等核心 token 在 v2 不出现。

## 2. draft 与候选在哪里不同

draft 描述 MemGPT 的 `request_heartbeat=true` 关键字参数：函数调用完成后立即触发下一次 LLM inference，使多跳检索可行（DocQA 翻页、嵌套 KV 多层 lookup）；保留 yield 语义（不带 heartbeat 的"终结性"函数仍正常 yield）；事件驱动控制流（user message、system message、user interaction、scheduled interrupt、heartbeat 都是 events）。

v2 三张候选是 Karpathy LLM Wiki 概念层，无 function-calling、heartbeat、agent control flow 概念。

## 3. 下一步的核心依据

(1) (2) 共同表明无重叠。draft 完整。结论 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；与 `memgpt-dmr-task-evaluation` 等 MemGPT 系列卡互相 cite。

## 5. 备注

无。
