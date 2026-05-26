---
schema: comparison_provenance.v3
draft_card: ../cards/audit-by-suspension-against-entrenchment.md
draft_provenance: ../provenance/audit-by-suspension-against-entrenchment.md
similarity_result: ../similarity/audit-by-suspension-against-entrenchment.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.05
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0476
  - card_id: raw-sources-readonly-source-of-truth
    card_path: llm_wiki/kb/cards/raw-sources-readonly-source-of-truth.md
    score: 0.0455
decision: new_card
audit_required: false
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

similarity 中 top 1/2 共享 `的`，top 3 共享 `事实`（draft "用**反事实**悬挂..."，候选 "Raw sources 是只读**事实**来源"）。分数 ≤0.05 是通用 token 同形。

## 2. draft 与候选在哪里不同

- draft 描述 Miteski (2026) 的 **AUDIT-by-Suspension 机制**：慢周期反事实悬挂的伪代码（suspend / re-run / restore / reduce gravity / archive 三分支）、Kuhn 范式 entry-level 翻译、ShortGPT 类比（结构居中 ≠ 功能必要）、§9 中 AUDIT 灵敏度作为最关键开放问题，以及在 §5.0 冲突路由矩阵中作为决胜者的角色。来源 `arxiv-memory-as-metabolism`。
- top 1/2 是 Karpathy 架构卡。
- top 3 `raw-sources-readonly-source-of-truth`：Karpathy 的 raw sources 层定义为只读事实来源。此处的"事实"指文档级别 source of truth；draft 中"反事实"指 counterfactual suspension。两者只是字面 `事实` 同形，含义层级完全不同。

## 3. 下一步的核心依据

(1) 与 (2) 表明分数来自 `的` / `事实` 同形，主题无交集。判 `new_card`：直接走 publication_gate。draft 含伪代码、三分支决策映射、Kuhn 与 ShortGPT 双类比、§9 limitations 的诚实承认与 §5.0 决胜者角色，发表条件齐备。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进入 publication_gate。

## 5. 备注

`事实` 与 `反事实` 在 jaccard 上被切成同一 token，是典型的中文分词同形误中。
