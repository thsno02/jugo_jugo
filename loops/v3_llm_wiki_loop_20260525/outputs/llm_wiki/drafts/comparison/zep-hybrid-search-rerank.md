---
schema: comparison_provenance.v3
draft_card: ../cards/zep-hybrid-search-rerank.md
draft_provenance: ../provenance/zep-hybrid-search-rerank.md
similarity_result: ../similarity/zep-hybrid-search-rerank.json
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

similarity 中三个 top 候选只共享 `的`。分数完全是助词同形。

## 2. draft 与候选在哪里不同

- draft 描述 Zep 的图检索机制：$f(\alpha)=\chi(\rho(\varphi(\alpha)))$ 三阶段（search/reranker/constructor），search 三路（cos 语义 / BM25 词面 / BFS 上下文），5 种 reranker（RRF / MMR / graph-mention frequency / node distance / cross-encoder），1.6k vs 115k tokens 的实证数字。来源 `arxiv-zep`。
- top 1/2/3 是 Karpathy LLM Wiki 架构卡，与"图检索 + 多路 search + 多种 rerank"机制完全不同的论点轴、来源、机制。

## 3. 下一步的核心依据

(1) 与 (2) 表明分数来自 `的`，主题无交集。判 `new_card`：直接走 publication_gate。draft 含形式化定义、三路差异化（BFS 接受节点参数）、reranker 谱系、实证 token 数字与边界，发表条件齐备。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

无；典型 `的` 同形误中。
