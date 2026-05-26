---
schema: comparison_provenance.v3
draft_card: ../cards/ukpa-coreference-disruption.md
draft_provenance: ../provenance/ukpa-coreference-disruption.md
similarity_result: ../similarity/ukpa-coreference-disruption.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0667
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0625
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0556
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选分数 0.055–0.067，属于 v2 高频干扰卡簇。共享 token 仅为虚词。和 UKPA、共指链、entity linking、Microsoft GraphRAG / LightRAG 等关键概念无对应。

## 2. draft 与候选在哪里不同

draft 描述 UKPA：通过破坏 coreference chain 让 GraphRAG 的跨 chunk 实体合并普遍失效——四步流水线（逐 chunk 抽 coref → 候选生成 → 结构影响打分 I_score = α S_entity + β S_relation + γ (1 - S_vec) → 选择写回）。实测：QA 准确率从 95→50（Microsoft GraphRAG）、90→45（LightRAG），改动量 0.033–0.045%。

v2 三张候选是 Karpathy LLM Wiki 概念层，无任何 GraphRAG / coreference / 攻击相关内容。

## 3. 下一步的核心依据

(1) (2) 表明无论点重叠。draft 完整。结论 `new_card`。

不选 `merge_candidate` / `provenance_delta`：v2 无相关卡 body 或主张需要被合并/补充。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；与 `tkpa-graph-guided-targeted-poisoning` 形成"GraphRAG poisoning, targeted vs universal"对照对。

## 5. 备注

无。
