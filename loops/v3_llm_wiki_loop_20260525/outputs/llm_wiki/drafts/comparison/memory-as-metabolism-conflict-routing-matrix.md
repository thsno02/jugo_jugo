---
schema: comparison_provenance.v3
draft_card: ../cards/memory-as-metabolism-conflict-routing-matrix.md
draft_provenance: ../provenance/memory-as-metabolism-conflict-routing-matrix.md
similarity_result: ../similarity/memory-as-metabolism-conflict-routing-matrix.json
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
created_time: 2026-05-26T16:13:00+08:00
edited_time: 2026-05-26T16:13:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "§5.0 冲突路由矩阵：把"mirror vs compensate"程序化为 7 类显式路由" **token 共享为空，score 全部 0.000**。三个候选都源自 Karpathy "llm wiki" launch 推文，是 v2 仅 15 张卡时算法的兜底排序。

## 2. draft 与候选在哪里不同

- draft 主题：Miteski (2026) §5.0 给出的 7 行冲突路由矩阵，把 mirror vs compensate 程序化——row 3 是 sycophancy 显式拦截、row 7 是 base-model correction 通道。论据轴是 companion system governance + procedural conflict rule。
- 候选 1 / 2：Karpathy 推文 idea file 抽象性 / 分享逻辑。
- 候选 3：LLM 对 wiki 跑 health checks 清理。

draft 与候选完全不在同一域：companion system 程序化治理 vs Karpathy llm-wiki 概念帖文。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 不含 companion system / mirror-compensate / conflict routing 任何内容 → `new_card`。draft 自带 7 行矩阵详解 + legend + 两条边界 + 三段原文 quote，证据完整 → 不是 `revise_before_gate`。v2 无相关 companion / governance 邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；与 `memory-as-metabolism-mirror-vs-compensate`、`memory-as-metabolism-architectural-separability`、`audit-by-suspension-against-entrenchment` 等同 family 卡 related。

## 5. 备注

memory-as-metabolism 系列在 v2 KB 完全缺席。
