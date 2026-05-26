---
schema: comparison_provenance.v3
draft_card: ../cards/mem0-rag-chunk-size-ablation.md
draft_provenance: ../provenance/mem0-rag-chunk-size-ablation.md
similarity_result: ../similarity/mem0-rag-chunk-size-ablation.json
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

三张候选属 v2 高频干扰簇，分数 0.05–0.059。Mem0 / RAG / chunk / text-embedding-small-3 / Overall J 等核心 token 在 v2 不出现。

## 2. draft 与候选在哪里不同

draft 是 Mem0 论文 Table 2 中 RAG 网格 chunk × k ablation 的总结：chunk ∈ {128…8192}, k ∈ {1, 2}；k=2 一致优于 k=1；最优在 chunk=256, k=2 得 J=60.97；曲线非单调（4096 跌谷底，8192 反弹）。"strongest RAG" J=60.97 是 Mem0 abstract 中"10% relative improvement"的参照点。

v2 三张候选是 Karpathy LLM Wiki 概念层卡，无任何 RAG ablation、chunk size、k 值实验。

## 3. 下一步的核心依据

(1) (2) 共同表明无重叠。draft 完整、数字详尽。结论 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；与 mem0 系列其他卡互相 cite。

## 5. 备注

无。
