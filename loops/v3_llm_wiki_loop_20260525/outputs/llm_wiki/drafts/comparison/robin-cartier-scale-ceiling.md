---
schema: comparison_provenance.v3
draft_card: ../cards/robin-cartier-scale-ceiling.md
draft_provenance: ../provenance/robin-cartier-scale-ceiling.md
similarity_result: ../similarity/robin-cartier-scale-ceiling.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.15
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1364
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0952
decision: new_card
audit_required: false
created_time: 2026-05-26T12:28:00+08:00
edited_time: 2026-05-26T12:28:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选 jaccard 0.15 / 0.1364 / 0.0952，全部来自高频 token `llm`、`wiki`（top1/top2 多 `的`）。draft 标题里的关键词 `200`、`100K tokens`、`实战上限`、`降级`、`子 wiki`、`RAG` 在三张候选标题中都没出现。属典型功能词撞分。

## 2. draft 与候选在哪里不同

- **来源不同**：本 draft 取自 `robin-cartier-llm-knowledge-bases`（Robin Cartier 2026-04-08 "Practitioner's Verdict" 博客）；v2 三张候选全部出自 karpathy gist / x post 家族。
- **类型与论点不同**：本 draft 是 `operational_rule`，给出四条具体可量化的工程局限（200 页 / 100K tokens 规模上限、去重 LLM-dependent 且 fragile、单一 `last_updated` 时间信号过弱、单用户无 access control / merge conflict / audit trail），并附 Robin 的"何时用 wiki / 何时用关系型 KB / 何时用 RAG"三档选择矩阵和四条强项侧（可靠性、零基础设施、可读性、git 版本控制）。v2 三张候选都是 karpathy 视角的 known_fact 概念卡，**没有任何**关于规模天花板或工程局限的内容。
- 关键数字（200 页 / 100K tokens）、关键短语（"the wiki will accumulate near-duplicate pages over time"、"no audit trail beyond the log file"）在 v2 完全没有。
- 与 `karpathy-gist-bookkeeping-burden`（同批 draft）互补：那张说"维护成本 → 0"，本卡说"这个主张有规模边界"——两张正反对照，但都属 v3 新卡，不涉 v2。

## 3. 下一步的核心依据

(1) 三张候选都没有规模上限 / 工程局限的内容；(2) draft 来自全新源（Robin Cartier 实战 verdict），是对 karpathy 模式的批评性补充；(3) operational_rule 类卡天然以"硬约束 + 触发条件 + 选择矩阵"组织，与 v2 已有 known_fact 概念卡不可合并。结论是 `new_card`。

不是 `provenance_delta`：尽管本 draft 是对 karpathy 模式（v2 多卡涉及）的工程裁决，它不是给 v2 任一卡补一段证据——它是 v3 引入的另一作者的独立 verdict，自带完整论证（四条局限 + 三档选择矩阵 + 强项侧）。也不是 `merge_candidate`：v2 没有规模上限 / 操作规则类卡可合并。不是 `revise_before_gate`：每条局限都引到行号、200 页"经验值受模型上下文窗口影响"的弱化声明明确、显式标注"不是反对 wiki 模式而是选择合适的工具到合适的规模"的合理使用边界。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；建议在 sources 索引加入 `robin-cartier-llm-knowledge-bases`；与同批 `karpathy-gist-bookkeeping-burden` 做 related 双向 cross-link（"主张"↔ "实战边界"）；与 `karpathy-llm-wiki-source-executable-analogy`（同批，含 "百文档以上 vector search 重新划算"）做 related 互链。

## 5. 备注

- 200 页规则是经验值且依赖模型上下文窗口大小；如未来模型上下文显著增长，本卡数字应触发 v3 audit 而非 silent stale。
- 选择矩阵子主题（"何时用关系型 KB"）若未来需要扩展，可考虑切独立卡，本卡决策维持 new_card。
