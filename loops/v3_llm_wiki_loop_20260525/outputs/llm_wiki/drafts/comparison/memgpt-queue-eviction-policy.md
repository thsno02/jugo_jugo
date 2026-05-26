---
schema: comparison_provenance.v3
draft_card: ../cards/memgpt-queue-eviction-policy.md
draft_provenance: ../provenance/memgpt-queue-eviction-policy.md
similarity_result: ../similarity/memgpt-queue-eviction-policy.json
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
created_time: 2026-05-26T16:12:30+08:00
edited_time: 2026-05-26T16:12:30+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "MemGPT 用"警告水位—溢出—递归摘要"三段策略管 FIFO 队列驱逐" **token 共享为空，score 全部 0.000**。三个候选都来自 Karpathy "llm wiki" launch 推文，是 v2 仅 15 张卡时算法兜底排序。

## 2. draft 与候选在哪里不同

- draft 主题：MemGPT queue manager 的双水位策略——warning ≈ 70% / flush ≈ 100%，flush 时递归摘要 + recall storage 无损副本。论据轴是 context overflow 管理 + 工程化驱逐策略。
- 候选 1 / 2 / 3：Karpathy 推文 idea file / health checks，与上下文窗口管理 / 队列驱逐毫无关联。

draft 与候选完全无论点交叠、无共享 underlying source。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 完全不含 queue manager / context overflow / recursive summary 任何内容 → `new_card`。draft 自带三段流程描述、水位百分比、原文 quote、边界与误用，证据完整 → 不是 `revise_before_gate`。v2 无 MemGPT / context management 邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；与同 family 的 `memgpt-main-vs-external-context`、`memgpt-function-chaining-heartbeat` related。

## 5. 备注

MemGPT 系列在 v2 KB 完全缺席。
