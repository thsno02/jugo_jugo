---
schema: comparison_provenance.v3
draft_card: ../cards/zep-dmr-benchmark-critique.md
draft_provenance: ../provenance/zep-dmr-benchmark-critique.md
similarity_result: ../similarity/zep-dmr-benchmark-critique.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.05
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0476
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0435
decision: new_card
audit_required: false
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

similarity 中三个 top 候选都只共享 `的`。分数完全是助词同形。

## 2. draft 与候选在哪里不同

- draft 是 source_claim 卡：Zep 论文对 MemGPT 团队提出的 DMR 基准的批判——全量 baseline 在 gpt-4o-mini 上拿 98.0%、单轮事实型问题、措辞含糊、不代表企业场景、复现性差——结论是 DMR 已不能区分长程记忆方法优劣，转用 LongMemEval。来源 `arxiv-zep`。
- top 1/2/3 是 Karpathy LLM Wiki 架构卡，与"记忆基准是否仍然有效"的方法论批判主题完全不同。

## 3. 下一步的核心依据

(1) 与 (2) 表明分数来自 `的`，主题无交集。判 `new_card`：直接走 publication_gate。draft 含 5 条批判论点、baseline 数字（94.4% / 98.0% / 18.5% LongMemEval 提升）、操作含义与诚实边界（MemGPT 算法本身不在批判范围；MemGPT 在 LongMemEval 上的对比未实现），发表条件齐备。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

无；典型 `的` 同形误中。
