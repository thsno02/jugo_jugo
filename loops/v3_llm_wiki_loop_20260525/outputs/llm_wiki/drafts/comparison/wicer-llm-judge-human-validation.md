---
schema: comparison_provenance.v3
draft_card: ../cards/wicer-llm-judge-human-validation.md
draft_provenance: ../provenance/wicer-llm-judge-human-validation.md
similarity_result: ../similarity/wicer-llm-judge-human-validation.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.1111
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0556
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

共享 token 仅 `llm`、`的`。draft 的核心 token `WiCER`、`LLM-as-judge`、`人评`、`Pearson`、`r=0.94`、`n=100` 都不出现在候选标题。jaccard 0.1111 完全由 `llm/的` 撞分。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-three-layer-architecture`：Karpathy gist 的三层架构。与 LLM-as-judge 校准无关。
- 候选 #2 `llm-wiki-schema-configuration-document`：schema 配置文档定义。无关。
- 候选 #3 `idea-file-abstract-vague`：idea file 抽象性。无关。
- draft 来源是 `arxiv-wicer` Appendix F，论点轴是 LLM-as-judge（Claude Sonnet）相对人评的可靠性校准——n=100 分层样本、Pearson r=0.94、per-condition r≥0.89、唯一 >1 分歧 case 的人工复查、与 §7.3 NeurIPS checklist statistical significance 项的张力。这是 methodology 类卡，v2 KB 完全没有评测方法卡。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 无 LLM judge / evaluation methodology 系列卡。
- 不是 `provenance_delta`：候选都是 Karpathy gist 元事实，无对接面。
- 不是 `duplicate_skip`：无重叠。
- 不是 `revise_before_gate`：draft 已有 Table tab:human_corr 完整数字、per-condition 表、唯一 >1 case 引文、与 statistical significance limitation 的合成观察、边界（只校准 Claude Sonnet / 仅一位 expert / WiCER 条件小样本）；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控阶段建议核 r/ρ/τ 与论文 Table tab:human_corr 是否逐字对齐。

## 5. 备注

- 与 ARES 等 LLM-as-judge 方法学卡（draft 自身 provenance 中已提及）形成方法学对照族，但目前不在 v2 KB 范围。
- jaccard 0.1111 完全由"llm/的"产生，是中文小池子下典型机械撞分。
