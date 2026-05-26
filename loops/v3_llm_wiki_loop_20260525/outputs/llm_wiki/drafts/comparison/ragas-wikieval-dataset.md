---
schema: comparison_provenance.v3
draft_card: ../cards/ragas-wikieval-dataset.md
draft_provenance: ../provenance/ragas-wikieval-dataset.md
similarity_result: ../similarity/ragas-wikieval-dataset.json
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

similarity 中三个候选都只共享 `的`。分数完全是助词同形误中。

## 2. draft 与候选在哪里不同

- draft 描述 **WikiEval**：Ragas 论文为验证 reference-free 指标构造的 50 题 Wikipedia 数据集；含构造流程（2022 年后的页面、6 条出题规则、pairwise 标注 ~95% 一致率）、三维度对照样本的具体生成手法（无 context / 不完整 prompt / 反链注水）、与 SQuAD 类基准的方向正交性，以及对后续 metric 研究者的操作建议。来源 `arxiv-ragas`。
- top 1/2/3 都是 Karpathy LLM Wiki 架构卡，关注 wiki 范式的层定义，与"评测数据集构造"主题没有重叠。

## 3. 下一步的核心依据

(1) 与 (2) 表明分数来自 `的`，主题层零交集。判 `new_card`：直接走 publication_gate。draft 含构造细节、对照样本 trick、一致率数字与操作含义，是 RAG 评估系列中的关键例子卡。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

无；典型 `的` 同形误中。
