---
schema: comparison_provenance.v3
draft_card: ../cards/graphrag-manipulation-only-attack-surface.md
draft_provenance: ../provenance/graphrag-manipulation-only-attack-surface.md
similarity_result: ../similarity/graphrag-manipulation-only-attack-surface.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.1111
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.1
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0833
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

共享 token 只有 `的` 这一个高频虚词。draft 标题里的核心词 `GraphRAG`、`只改字`、`不加文`、`攻击面` 完全没有出现在任何候选标题里。jaccard 0.1111 完全由虚词撞分。

## 2. draft 与候选在哪里不同

- 候选 #1 `idea-file-abstract-vague`：idea file 抽象性事实。无关。
- 候选 #2 `llm-wiki-three-layer-architecture`：Karpathy gist 三层架构。无关。
- 候选 #3 `llm-wiki-schema-configuration-document`：schema 配置文档定义。无关。
- draft 来源是 `arxiv-graph-poisoning`，论点轴是 GraphRAG 的"只改字、不加文"manipulation-only 投毒攻击面（gray-box / 改 <0.06% 词量即 93.1% ASR）。与 v2 KB 的 Karpathy gist 视角完全不在同一维度。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 无任何 GraphRAG / 安全 / 投毒卡。
- 不是 `provenance_delta`：候选都是 Karpathy gist 事实卡，无对接面。
- 不是 `duplicate_skip`：无覆盖。
- 不是 `revise_before_gate`：draft 已有 manipulation-only 威胁建模、TKPA/UKPA 修改词数与 ASR 数字、与 prompt injection / chunk-RAG 的边界对比、论文行号锚（L157–230 / L284–296）；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控阶段建议核 TKPA 0.06% 与 UKPA 0.05% 数字与论文 contribution 列表是否逐字对齐。

## 5. 备注

- 与同批次 `poisonedrag-knowledge-database-attack-surface` 共同构成"RAG/GraphRAG 投毒攻击面"双卡，未来可在 v3 安全主题页互链。
- top 1 候选 `idea-file-abstract-vague` 是 LOW batch 里几张 draft 的常见 top1，说明该 v2 卡仅含 `的` 这类高频虚词导致系统性误中。
