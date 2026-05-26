---
schema: comparison_provenance.v3
draft_card: ../cards/alce-prompting-strategies.md
draft_provenance: ../provenance/alce-prompting-strategies.md
similarity_result: ../similarity/alce-prompting-strategies.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0909
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0833
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0714
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选共享 token 仅为 `的`。draft 的核心 token `ALCE`、`prompting`、`策略`、`取舍`、`五种` 都不出现在候选标题。jaccard 0.0909 完全由虚词撞分——这是本批中最低分的几张之一。

## 2. draft 与候选在哪里不同

- 候选 #1 `idea-file-abstract-vague`：idea file 抽象性事实。无关。
- 候选 #2 `llm-wiki-three-layer-architecture`：Karpathy gist 三层架构。无关。
- 候选 #3 `llm-wiki-schema-configuration-document`：schema 配置文档定义。无关。
- draft 来源是 `arxiv-alce` (intro L1138–1143 + appendix L327–331 + L511–644 + header L206–225)，论点是 ALCE 实验里 Vanilla / Summ / Snippet / Interact / InlineSearch / Rerank / ClosedBook+PostCite 的取舍——给出 "summary/snippet 改 correctness 不改 citation quality"、"Interact 没有帮助"、"Rerank 用 metric 当选择器改 citation quality（4× 成本）"、"ClosedBook+PostCite 不替代生成时检索" 等结论。v2 KB 完全无 ALCE / prompting strategy 卡。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 无 prompting / RAG 策略对比系列卡。
- 不是 `provenance_delta`：候选都是 Karpathy gist 元事实，无对接面。
- 不是 `duplicate_skip`：无重叠。
- 不是 `revise_before_gate`：draft 已有 7 种策略定义、各自取舍结论、行号锚（L1138–1143 / L327–331 / L511–644）与边界（仅三数据集 / 模型缩放 / Rerank 成本）；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控阶段建议核 intro L1138–1143 的结论项目化罗列是否对齐。

## 5. 备注

- 与同源 `alce-retriever-and-context-utilization-gap`、`alce-three-dimension-citation-metric` 共同构成 ALCE 系列卡。
- top 1 候选 `idea-file-abstract-vague` 又一次是 LOW 批高频虚词撞分。
