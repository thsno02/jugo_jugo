---
schema: comparison_provenance.v3
draft_card: ../cards/graphrag-root-community-token-efficiency.md
draft_provenance: ../provenance/graphrag-root-community-token-efficiency.md
similarity_result: ../similarity/graphrag-root-community-token-efficiency.json
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
created_time: 2026-05-26T16:07:30+08:00
edited_time: 2026-05-26T16:07:30+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "GraphRAG 根级社群摘要（C0）以 ~2% token 成本接近全局方法效果" **没有 token 共享，score 全部 0.000**。三个候选都来自 Karpathy "llm wiki" launch 推文，是 v2 15 张卡时算法的兜底排序，本质上跟 draft 无邻近。

## 2. draft 与候选在哪里不同

- draft 主题：GraphRAG 根级 community summary（C0）作为 sensemaking 索引——9–43× token 节省 + 对 vector RAG 仍 72%/62% 胜率。论据轴是 cost efficiency + iterative sensemaking + Leiden community 层级。
- 候选 1：Karpathy 推文中 `idea file` 的抽象性表述。
- 候选 2：同推文对 `idea file` 分享逻辑的表述。
- 候选 3：LLM 对 wiki 跑 `health checks` 做数据清理。

draft 完全在"图谱-社群摘要-成本压缩"语义域；候选完全在"Karpathy llm-wiki 设计帖文"语义域，无任何论据共享。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 不涉及 GraphRAG / community summary / token budget 任何方面 → `new_card`。draft 自带 community summaries 数字表 + 胜率引用 + 行号 + 边界声明，证据完整 → 不是 `revise_before_gate`。v2 无邻近卡可反向链接 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；在 v3 内与 `graphrag-leiden-community-hierarchy`、`graphrag-context-window-8k-optimal` 相互 related。

## 5. 备注

GraphRAG 系列在 v2 KB 中没有任何前置卡——本 draft 是与该系列其他 draft 一起首批引入的。
