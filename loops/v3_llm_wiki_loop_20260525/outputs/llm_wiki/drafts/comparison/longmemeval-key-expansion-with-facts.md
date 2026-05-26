---
schema: comparison_provenance.v3
draft_card: ../cards/longmemeval-key-expansion-with-facts.md
draft_provenance: ../provenance/longmemeval-key-expansion-with-facts.md
similarity_result: ../similarity/longmemeval-key-expansion-with-facts.json
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
created_time: 2026-05-26T16:10:30+08:00
edited_time: 2026-05-26T16:10:30+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "K = V + fact 比裸 value 平均 +9.4% recall、+5.4% QA 准确率" **token 共享为空，score 全部 0.000**。三个候选都源自 Karpathy "llm wiki" launch 推文，是 v2 仅 15 张卡时算法的兜底排序。

## 2. draft 与候选在哪里不同

- draft 主题：LongMemEval §5.2 七种 key 设计实验确认 K = V + fact（document expansion）平均 +9.4% recall@k、+5.4% QA。论据轴是 RAG indexing 工程优化 + dense vs sparse retriever。
- 候选 1 / 2：Karpathy 推文中 `idea file` 抽象性 / 分享逻辑的事实卡。
- 候选 3：LLM 对 wiki 跑 health checks 清理。

完全不重叠的两个域：long-term memory indexing 优化 vs Karpathy llm-wiki 帖文。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 不含任何 RAG indexing / key design / document expansion 内容 → `new_card`。draft 自带 round / session × K=V / K=fact / K=V+fact 的实测表、+9.4% / +5.4% 原文 quote、rank merging 失败原因，证据完整 → 不是 `revise_before_gate`。v2 无 RAG indexing 邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；与 `longmemeval-three-stage-memory-framework` 等同 family 卡相互 related。

## 5. 备注

LongMemEval 系列在 v2 KB 完全缺席；本卡是该系列首批 draft 之一。
