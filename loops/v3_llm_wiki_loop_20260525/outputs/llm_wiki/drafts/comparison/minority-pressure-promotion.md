---
schema: comparison_provenance.v3
draft_card: ../cards/minority-pressure-promotion.md
draft_provenance: ../provenance/minority-pressure-promotion.md
similarity_result: ../similarity/minority-pressure-promotion.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0556
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0526
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0476
decision: new_card
audit_required: false
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

similarity 中三个 top 候选都只共享 `的`。分数完全来自中文助词同形。

## 2. draft 与候选在哪里不同

- draft 描述 Miteski (2026) 的 **minority-pressure promotion 机制**：CONSOLIDATE 的四 phase（buffer-internal scoring → wiki scoring → fuzzy 分桶 → minority promotion）、minority-hypothesis retention、Prediction 4 ("resurfacing-to-influence" 率)、与 LongMemEval / THEANINE TeaFarm 的区分、以及边界（噪声放大、Valley of Amnesia、单 agent 内不足以解 echo chamber）。来源 `arxiv-memory-as-metabolism`。
- top 1/2/3 是 Karpathy LLM Wiki 架构卡，论 wiki 层定义与 schema 配置，与 belief revision / consolidation 机制完全不同的论点轴、机制、来源类型。

## 3. 下一步的核心依据

(1) 与 (2) 表明分数来自 `的`，主题无交集。判 `new_card`：直接走 publication_gate。draft 含完整四 phase 流程、关键 footnote 引文（CONSOLIDATE MUST score buffer entries against each other...）、与 benchmark 区分论证、可证伪的 Prediction 4 定义，发表条件齐备。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

无；典型 `的` 同形误中。
