---
schema: comparison_provenance.v3
draft_card: ../cards/mem0-tool-call-add-update-delete-noop.md
draft_provenance: ../provenance/mem0-tool-call-add-update-delete-noop.md
similarity_result: ../similarity/mem0-tool-call-add-update-delete-noop.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.1176
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1053
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0588
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选共享 token 仅为 `llm`、`的`（top 3 仅 `的`）。draft 的核心 token `Mem0`、`ADD`、`UPDATE`、`DELETE`、`NOOP`、`记忆` 等没有任何候选覆盖。纯主题/虚词机械撞分。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-three-layer-architecture`：Karpathy gist 的三层架构。与 Mem0 的 update 操作语义无关。
- 候选 #2 `llm-wiki-schema-configuration-document`：schema 是配置文档。无关。
- 候选 #3 `idea-file-abstract-vague`：idea file 抽象性。无关。
- draft 来源是 `arxiv-mem0` Algorithm 1 (appendix 第 911–966 行) + §3.1（第 1155 行），论点是 Mem0 用 LLM tool call 把 ADD/UPDATE/DELETE/NOOP 决策当语义任务做，含 ClassifyOperation 伪代码、InformationContent 门槛、与传统 CRUD / memory-as-metabolism governance 的差别。v2 KB 中没有任何 Mem0 卡或 update operation 机制卡。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 无 Mem0 / memory update mechanism 卡。
- 不是 `provenance_delta`：候选都是 Karpathy gist 元事实，与 Mem0 算法无对接面。
- 不是 `duplicate_skip`：无重叠。
- 不是 `revise_before_gate`：draft 已有四操作表、ClassifyOperation 伪代码、InformationContent 门槛、与 memory-as-metabolism 的对比、边界标注（两方对话假设 / 无 audit 通道）；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控可核 Algorithm 1 伪代码字面是否逐行对齐论文 appendix。

## 5. 备注

- 与同批次的 memory-as-metabolism 系列形成"两种记忆 update 立场"对照（mem0 直觉 vs 元-metabolism 显式 AUDIT），未来 v3 wiki 主题页可基于此组卡片成做对照表。
- jaccard 0.1176 完全由"llm/的"产生，不反映任何内容关系。
