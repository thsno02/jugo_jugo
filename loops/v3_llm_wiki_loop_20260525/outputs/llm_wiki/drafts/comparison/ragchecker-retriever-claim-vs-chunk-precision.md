---
schema: comparison_provenance.v3
draft_card: ../cards/ragchecker-retriever-claim-vs-chunk-precision.md
draft_provenance: ../provenance/ragchecker-retriever-claim-vs-chunk-precision.md
similarity_result: ../similarity/ragchecker-retriever-claim-vs-chunk-precision.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0
  - card_id: idea-file-share-the-idea
    card_path: llm_wiki/kb/cards/idea-file-share-the-idea.md
    score: 0.0
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0
decision: new_card
audit_required: false
created_time: 2026-05-26T16:16:00+08:00
edited_time: 2026-05-26T16:16:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "RAGChecker 检索端的非对称——claim-level recall vs chunk-level precision" **token 共享为空，score 全部 0.000**。三个候选都来自 Karpathy "llm wiki" launch 推文，是 v2 仅 15 张卡时算法的兜底排序。

## 2. draft 与候选在哪里不同

- draft 主题：RAGChecker 在 retriever 模块同时报 claim recall（claim 层）与 context precision（chunk 层）的非对称设计，论文以"工程现实而非美感"为理由。论据轴是 RAG 评测指标设计 + chunk-level vs claim-level 粒度选择。
- 候选 1 / 2 / 3：Karpathy 推文 idea file / health checks——与 retriever 评测指标毫无关联。

draft 与候选完全不在同一域。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 完全不含 RAG retriever metric / claim-level / chunk-level 任何内容 → `new_card`。draft 自带 CR / CP 公式、设计理由原文 quote、$k$ 扫描数字、误读警示、与 RAGAS / TruLens 对比，证据完整 → 不是 `revise_before_gate`。v2 无 RAGChecker / RAG eval 邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；与 `ragchecker-claim-entailment-decomposition`、`rag-chunk-level-faithfulness` 同 family related。

## 5. 备注

RAGChecker / RAG 评测设计主题在 v2 KB 完全缺席。
