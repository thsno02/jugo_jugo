---
schema: comparison_provenance.v3
draft_card: ../cards/longmemeval-five-core-memory-abilities.md
draft_provenance: ../provenance/longmemeval-five-core-memory-abilities.md
similarity_result: ../similarity/longmemeval-five-core-memory-abilities.json
existing_cards:
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1111
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0625
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0588
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

共享 token 仅 `是`、`的` 两个高频虚词。draft 的核心 token `LongMemEval`、`IE`、`MR`、`KU`、`TR`、`ABS`、`长期记忆`、`五种能力` 都不出现在候选标题。jaccard 0.1111 全由虚词产生。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-schema-configuration-document`：仅记录 Karpathy gist 的 schema 配置文档定义。和 long-term dialogue benchmark 完全无关。
- 候选 #2 `idea-file-abstract-vague`：idea file 抽象性事实卡。无关。
- 候选 #3 `llm-wiki-three-layer-architecture`：Karpathy gist 三层架构。无关。
- draft 来源是 `arxiv-longmemeval`，论点轴是 LongMemEval（Wu et al., ICLR 2025）把 long-term memory 切成 5 类核心能力（IE/MR/KU/TR/ABS）与 7 种问题类型，并以对比表（§977–984）说明 KU/ABS 是它独有覆盖。这是 benchmark 概念卡，v2 KB 完全没有评测卡。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 无 benchmark / 长期记忆评测系列卡。
- 不是 `provenance_delta`：候选都是 Karpathy gist 元事实，无对接面。
- 不是 `duplicate_skip`：无重叠。
- 不是 `revise_before_gate`：draft 已有五能力定义、7 问题类型、对比表行号锚（§977–984）、KU 失败的 pilot 引文（§1407 / §1629）与边界（"功能性切分，不映射到具体记忆架构"）；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控阶段建议核对 5 能力定义与论文 §3.2 itemize 是否逐字对齐。

## 5. 备注

- 与 draft 自身 related `locomo-three-task-evaluation-framework` 共同构成"长期记忆评测能力图谱"对照卡组。
- v2 KB 当前完全围绕 Karpathy 个人 LLM Wiki gist；benchmark 维度尚未引入。
