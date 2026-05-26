---
schema: comparison_provenance.v3
draft_card: ../cards/memgpt-nested-kv-multi-hop.md
draft_provenance: ../provenance/memgpt-nested-kv-multi-hop.md
similarity_result: ../similarity/memgpt-nested-kv-multi-hop.json
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
created_time: 2026-05-26T16:12:00+08:00
edited_time: 2026-05-26T16:12:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "嵌套 KV 基准证明"上下文内多跳"瓶颈不是上下文长度而是迭代查询" **token 共享为空，score 全部 0.000**。三个候选都源自 Karpathy "llm wiki" launch 推文，是 v2 仅 15 张卡时算法的兜底排序。

## 2. draft 与候选在哪里不同

- draft 主题：MemGPT 论文中的 nested key-value retrieval benchmark——140 UUID 配对、嵌套 0–4 层 lookup、baseline 在 1–3 层崩盘 / MemGPT + GPT-4 在 4 层稳定。论据轴是 LLM multi-hop reasoning bottleneck + agent function chaining 外化。
- 候选 1 / 2：Karpathy 推文 idea file 抽象性 / 分享逻辑。
- 候选 3：LLM 对 wiki 做 health checks 清理。

draft 与候选完全不在同一域。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 不含 MemGPT / multi-hop / benchmark / function chaining 任何内容 → `new_card`。draft 自带任务设定、不同模型在嵌套层数下的表现、外化 multi-hop 的机制解释、行号引用与原文 quote，证据完整 → 不是 `revise_before_gate`。v2 无 MemGPT / agent runtime 邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；与 `memgpt-function-chaining-heartbeat`、`memgpt-queue-eviction-policy` 等同 family 卡 related。

## 5. 备注

MemGPT 系列在 v2 KB 完全缺席。
