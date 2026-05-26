---
schema: comparison_provenance.v3
draft_card: ../cards/poisonedrag-existing-defenses-insufficient.md
draft_provenance: ../provenance/poisonedrag-existing-defenses-insufficient.md
similarity_result: ../similarity/poisonedrag-existing-defenses-insufficient.json
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
created_time: 2026-05-26T16:15:30+08:00
edited_time: 2026-05-26T16:15:30+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "四类现成防御都挡不住 PoisonedRAG" **token 共享为空，score 全部 0.000**。三个候选都来自 Karpathy "llm wiki" launch 推文，是 v2 仅 15 张卡时算法的兜底排序。

## 2. draft 与候选在哪里不同

- draft 主题：PoisonedRAG 论文逐一测试 Paraphrasing / PPL detection / Duplicate filtering / Knowledge expansion 四类 RAG 投毒防御并解释失败模式（retriever 鲁棒性悖论 / 攻击文本是 GPT-4 生成 / dedup 易绕过 / 大 k 反而被压回）。论据轴是 RAG 投毒攻击 + 防御设计原则。
- 候选 1 / 2 / 3：Karpathy 推文 idea file / health checks——与 RAG 投毒防御毫无关联。

draft 与候选完全不在同一域。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 完全不含 RAG 投毒 / 防御失效内容 → `new_card`。draft 自带 NQ / HotpotQA / MS-MARCO ASR 对比表、PPL detection 原文 quote、扩 k 失败的 41% / 43% 数字、三条防御设计原则，证据完整 → 不是 `revise_before_gate`。v2 无 RAG 安全邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；与 `poisonedrag-knowledge-database-attack-surface`、`poisonedrag-retrieval-generation-two-conditions` 同 family related。

## 5. 备注

PoisonedRAG / RAG 投毒主题在 v2 KB 完全缺席。
