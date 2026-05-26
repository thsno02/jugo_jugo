---
schema: comparison_provenance.v3
draft_card: ../cards/locomo-three-task-evaluation-framework.md
draft_provenance: ../provenance/locomo-three-task-evaluation-framework.md
similarity_result: ../similarity/locomo-three-task-evaluation-framework.json
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
created_time: 2026-05-26T16:09:30+08:00
edited_time: 2026-05-26T16:09:30+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "LoCoMo 用 QA + 事件摘要 + 多模态对话三任务测量"长期记忆"" **无 token 共享，score 全部 0.000**。三个候选都来自 Karpathy "llm wiki" launch 推文（idea file / health checks），是 v2 仅 15 张卡时算法的兜底排序，与 draft 无实质邻近。

## 2. draft 与候选在哪里不同

- draft 主题：LoCoMo benchmark 的三任务设计（QA / Event Graph Summarization / Multi-Modal Dialog Generation）和五类 QA reasoning 分类。论据轴是 long-term memory evaluation + benchmark 设计。
- 候选 1：Karpathy 推文 idea file 抽象性的事实卡。
- 候选 2：同推文 idea file 分享逻辑的事实卡。
- 候选 3：LLM 对 wiki 做 health checks 的事实卡。

draft 与候选既无共享 underlying source，也无论点交叠。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 完全不含 long-term memory benchmark / LLM evaluation 主题 → `new_card`。draft 自带三任务定义、五类 reasoning 列举、long-context 反而失分的反直觉数据、原文 quote 与行号，证据完整 → 不是 `revise_before_gate`。v2 无 long-term memory eval 邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；在 v3 内与 `longmemeval-五大核心记忆能力` 等同 family 卡互联。

## 5. 备注

长期记忆 benchmark 主题在 v2 KB 完全缺席；本 draft 与同 family 的 LongMemEval / Mem0 等是首批引入。
