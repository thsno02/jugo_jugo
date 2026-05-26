---
schema: comparison_provenance.v3
draft_card: ../cards/graphrag-global-sensemaking-pipeline.md
draft_provenance: ../provenance/graphrag-global-sensemaking-pipeline.md
similarity_result: ../similarity/graphrag-global-sensemaking-pipeline.json
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

三个候选 jaccard 都低于 0.07，shared_tokens 仅为「的」。draft 标题的实质 token（GraphRAG / RAG / 全局意义建构 / 两阶段 / 流水线）与 v2 候选（Karpathy LLM-wiki 元描述）无术语级重合。属于 jaccard 噪声。

## 2. draft 与候选在哪里不同

draft 是 mechanism 卡，来源 `arxiv-graphrag` (Edge et al. NeurIPS 2024)，论述 GraphRAG 把 RAG 改造成「索引时 + 查询时」两阶段流水线：索引五步（chunk → 实体关系 → 知识图 → Leiden 社群 → 社群摘要）+ 查询时 map-reduce；并量化 1M token 量级播客/新闻 comprehensiveness 与 diversity 胜率（72-83% / 62-82%）以及 directness 反向结果。属于「RAG 架构 / global sensemaking 算法」论点轴。

三张 v2 候选都是 Karpathy LLM-wiki 元描述。论点轴（GraphRAG 算法流水线 vs 个人 LLM wiki 模式）、来源、机制（图社群检测 + map-reduce vs LLM 写 markdown）完全不同。

## 3. 下一步的核心依据

shared_tokens 全是「的」，无语义关联。draft 引文具体到 L671-860 / L853-857 / L987-989 等多处，scope 自洽。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 sibling `graphrag-leiden-community-hierarchy` / `graphrag-vs-vector-rag-on-global-questions` 同 source 互引。
