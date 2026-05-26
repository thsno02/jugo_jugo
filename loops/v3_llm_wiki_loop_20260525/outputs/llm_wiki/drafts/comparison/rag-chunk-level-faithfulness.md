---
schema: comparison_provenance.v3
draft_card: ../cards/rag-chunk-level-faithfulness.md
draft_provenance: ../provenance/rag-chunk-level-faithfulness.md
similarity_result: ../similarity/rag-chunk-level-faithfulness.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.1
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0909
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0769
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选共享 token 仅为 `的`。draft 的核心 token `RAG`、`chunk`、`faithfulness`、`生成器` 都不出现在任何候选标题。jaccard 0.1 完全由虚词撞分。

## 2. draft 与候选在哪里不同

- 候选 #1 `idea-file-abstract-vague`：idea file 抽象性事实。无关。
- 候选 #2 `llm-wiki-three-layer-architecture`：Karpathy gist 三层架构。无关。
- 候选 #3 `llm-wiki-schema-configuration-document`：schema 配置文档定义。无关。
- draft 来源是 `arxiv-ragchecker` Main Results（行 780–784），论点是 RAGChecker 在 8 个系统 × 10 个领域上反复观察到的 "chunk-level faithfulness" 现象——LLM 信任以 chunk 为单位、relevant noise sensitivity 系统性高于 irrelevant noise sensitivity，并由此推出 retriever recall × generator noise 的折衷与 fixed-size chunking 的 hidden cost。v2 KB 无 RAGChecker / RAG 评测细节卡。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 无 RAG 评测 / chunk faithfulness 系列卡。
- 不是 `provenance_delta`：候选都是 Karpathy gist 元事实，无对接面。
- 不是 `duplicate_skip`：无重叠。
- 不是 `revise_before_gate`：draft 已有现象原文 verbatim、retriever-noise 折衷引文、数据库质量结论、操作含义（claim-level 过滤）、边界（量化未给 / 模型差异显著）；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控阶段建议核 "a relevant chunk is trusted as a whole" 一句的 verbatim 是否对齐论文 L782–783。

## 5. 备注

- 与 draft 自身 related `ragchecker-generator-trilemma`、`ragchecker-claim-entailment-decomposition` 构成 RAGChecker 三联视图。
- top 1 候选 `idea-file-abstract-vague` 又一次出现在 LOW 批的高频"虚词撞分"位置。
