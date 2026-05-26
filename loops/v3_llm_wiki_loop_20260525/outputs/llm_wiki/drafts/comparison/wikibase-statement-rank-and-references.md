---
schema: comparison_provenance.v3
draft_card: ../cards/wikibase-statement-rank-and-references.md
draft_provenance: ../provenance/wikibase-statement-rank-and-references.md
similarity_result: ../similarity/wikibase-statement-rank-and-references.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0833
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0769
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0667
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.09，shared_tokens 仅为「的」。draft 标题主体是 Statement / Rank / ReferenceRecord / 并存 / 多值 / 筛选 等 Wikibase 术语，与 v2 候选标题（全部是 Karpathy LLM-wiki 元描述）没有任何术语级重合。属于 jaccard 噪声。

## 2. draft 与候选在哪里不同

draft 是 mechanism 卡，来源 `wikibase-data-model`，论述 Wikibase Statement 的 preferred/normal/deprecated 三级 rank 与 best rank 规则、ReferenceRecord 的 BNF 结构（一组 Snak 构成一条 reference）、deprecated 与「statement 错」的语义区分、故意只设三级的设计意图。属于「结构化知识库 schema 设计」论点轴。

三张 v2 候选都是 Karpathy LLM-wiki 元描述。虽然 Karpathy 的「LLM Wiki」与 Wikibase 在抽象层都属于「知识库」，但论点完全不同：Karpathy 卡描述 LLM 自动生成 markdown wiki 的模式，draft 描述 Wikidata 用结构化 Statement+Reference 表达多源/多值/可疑事实的 schema 机制。受众（个人知识库管理者 vs 结构化知识库工程师）、来源（个人帖 vs Wikibase 数据模型规范）、机制（LLM 写 wiki vs 人手筛选多值 statement）都不同。

## 3. 下一步的核心依据

shared_tokens 仅是「的」，无语义重叠。draft 引文具体到 L575-585 / L588-592 / L313，scope 自洽，证据完整。无任何 v2 卡可 merge 或 provenance_delta。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate。

## 5. 备注

- 与 sibling 卡 `wikibase-item-property-snak-statement` 紧密相关（前者描述基础结构，本卡描述其上的筛选机制），属于同 source 内部互引。
