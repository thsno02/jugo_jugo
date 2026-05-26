---
schema: comparison_provenance.v3
draft_card: ../cards/alce-citation-recall-precision-nli.md
draft_provenance: ../provenance/alce-citation-recall-precision-nli.md
similarity_result: ../similarity/alce-citation-recall-precision-nli.json
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

三张候选分数 0.05–0.059，都在 v2 高频干扰簇。token 共享仅在虚词层。ALCE / NLI / AIS / TRUE / SNLI / MNLI / Cohen κ 等核心 token 在 v2 不出现。

## 2. draft 与候选在哪里不同

draft 描述 ALCE 的 citation quality 评估：用 TRUE NLI 模型（在 SNLI/MNLI/Fever/Scitail/PAWS/VitaminC 上 fine-tune 的 T5-11B）执行二元 entailment 判定，给出 citation recall / precision 的形式化定义；列出 passage 拼接格式 `"Title: {TITLE}\n{TEXT}"`、最多 3 个引用、partial support false-positive 等边界，以及 Cohen κ recall 0.698 / precision 0.525。

v2 三张候选是 Karpathy LLM Wiki 概念层卡，无任何 citation 评估、NLI 模型、AIS 框架概念。

## 3. 下一步的核心依据

(1) (2) 共同表明无重叠。draft 完整、操作规则清晰。结论 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；与 RAG 评估指标簇互相 cite。

## 5. 备注

无。
