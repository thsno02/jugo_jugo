---
schema: comparison_provenance.v3
draft_card: ../cards/tkpa-graph-guided-targeted-poisoning.md
draft_provenance: ../provenance/tkpa-graph-guided-targeted-poisoning.md
similarity_result: ../similarity/tkpa-graph-guided-targeted-poisoning.json
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

三张候选都属于经验提示中标记的"v2 高频干扰卡"，分数 0.055–0.067，token 共享仅在中文虚词层面。与 TKPA / GraphRAG / VCL / Ego-子图 / PageRank 等关键概念毫无对应。

## 2. draft 与候选在哪里不同

draft 是 TKPA（Targeted Knowledge Poisoning Attack）的机制详解：脆弱社区定位的 V_score 公式、ego-子图抽取、Chunk 评分函数（图结构 0.5 / 语义 0.3 / 情感 0.2 默认权重）、LLM 改写、最后给出 ASR 91.2% 与 5.9× 收益对照。论点轴是"在图域定位最脆弱小邻域，再把改动反映射回原文"。

v2 三张候选都是 Karpathy LLM Wiki 概念层卡，没有 GraphRAG 概念，没有攻击者模型，没有图论指标。

## 3. 下一步的核心依据

(1) (2) 共同支持 draft 与 v2 无任何论点重叠。卡片本身机制 + 数字 + 边界齐备。结论 `new_card`。

不选 `merge_candidate`：v2 无相关卡。
不选 `provenance_delta`：v2 无 body 可补充。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；与 `ukpa-coreference-disruption`、`poisonedrag-*` 形成 RAG/GraphRAG 投毒簇。

## 5. 备注

无。
