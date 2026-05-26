---
schema: comparison_provenance.v3
draft_card: ../cards/alce-eli5-claim-recall-design.md
draft_provenance: ../provenance/alce-eli5-claim-recall-design.md
similarity_result: ../similarity/alce-eli5-claim-recall-design.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0526
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.05
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0455
decision: new_card
audit_required: false
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

similarity 中三个 top 候选都只共享 `的`。分数完全是助词同形误中。

## 2. draft 与候选在哪里不同

- draft 描述 ALCE 论文在 ELI5 上的 correctness 评估设计：用 InstructGPT 抽 3 条 sub-claim、用 TRUE NLI 模型判蕴含；含反 ROUGE 论证（BM25 top-1 passage 可拿 ROUGE-L=19.1 但 claim recall 只有 3.0）、120 sub-claim 人工校验数字（93.33% 抽取质量 / 80% NLI 准确率）、操作含义与已知失败模式。来源 `arxiv-alce`。
- top 1/2/3 是 Karpathy LLM Wiki 架构卡，与"long-form QA 的 correctness 评估机制"完全不同的论点轴、来源、机制。

## 3. 下一步的核心依据

(1) 与 (2) 表明分数来自 `的`，主题无交集。判 `new_card`：直接走 publication_gate。draft 含完整两步流程、反 ROUGE 反例表、两条人工校验数字、操作含义与边界，发表条件齐备。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

无；典型 `的` 同形误中。
