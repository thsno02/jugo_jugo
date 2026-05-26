---
schema: comparison_provenance.v3
draft_card: ../cards/longmemeval-chain-of-note-and-json-reading.md
draft_provenance: ../provenance/longmemeval-chain-of-note-and-json-reading.md
similarity_result: ../similarity/longmemeval-chain-of-note-and-json-reading.json
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
created_time: 2026-05-26T16:10:00+08:00
edited_time: 2026-05-26T16:10:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "Chain-of-Note + JSON 结构化 prompt 即使在 oracle 检索下也能涨 10 分" **token 共享为空，score 全部 0.000**。三个候选都源自 Karpathy "llm wiki" launch 推文，是 v2 仅 15 张卡时算法的兜底排序。

## 2. draft 与候选在哪里不同

- draft 主题：LongMemEval §5.4 reading-phase ablation：CoN + JSON 合用即便在 oracle retrieval 下仍能 +10 分 absolute。论据轴是 RAG reading strategy + 结构化 prompt + reader LLM 错误分布。
- 候选 1 / 2：Karpathy 推文 idea file 抽象性 / 分享逻辑。
- 候选 3：LLM 对 wiki 跑 health checks。

draft 与候选完全不在同一域，没有共享 underlying source（draft 来自 `arxiv-longmemeval`）也没有论点交叠。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 与 reading strategy / CoN / JSON prompt 任一方面无关 → `new_card`。draft 自带 oracle vs 真实检索对比、不同 reader（GPT-4o / Llama 3.1 8B）数字、error 分布百分比、原文 quote，证据完整 → 不是 `revise_before_gate`。v2 无 long-term memory / reading strategy 邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；在 v3 内与 `longmemeval-three-stage-memory-framework` 等 family 卡 related。

## 5. 备注

LongMemEval family 在 v2 KB 完全缺席；同 batch 内还有该 family 多张 draft。
