---
schema: comparison_provenance.v3
draft_card: ../cards/memory-as-metabolism-contextualize-depth-fitted.md
draft_provenance: ../provenance/memory-as-metabolism-contextualize-depth-fitted.md
similarity_result: ../similarity/memory-as-metabolism-contextualize-depth-fitted.json
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
created_time: 2026-05-26T16:13:30+08:00
edited_time: 2026-05-26T16:13:30+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "CONTEXTUALIZE：把外部源按用户当前 working-context depth 压缩，强制保留 linkout" **token 共享为空，score 全部 0.000**。三个候选都源于 Karpathy "llm wiki" launch 推文，是 v2 仅 15 张卡时算法的兜底排序。

## 2. draft 与候选在哪里不同

- draft 主题：Miteski (2026) CONTEXTUALIZE 操作——depth-fitted compression、linkout MUST、dream cycle 调度、cold memory 第三层、metabolism 比喻、与 D-Mem 区分。论据轴是 companion memory operation + selective absorption + storage tier。
- 候选 1 / 2 / 3：Karpathy 推文 idea file / health checks——无任何关于 depth-fitted compression / cold memory / linkout 的论述。

draft 与候选完全不在同一域。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 与 CONTEXTUALIZE / cold memory / D-Mem 完全无关 → `new_card`。draft 自带三层存储模型、与 D-Mem 区分、§7.5 conformance MUST 原文、§9 失败模式、metabolism 比喻，证据完整 → 不是 `revise_before_gate`。v2 无相关 memory operation 邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；与 memory-as-metabolism family 内其它 draft related。

## 5. 备注

memory-as-metabolism 系列在 v2 KB 完全缺席。
