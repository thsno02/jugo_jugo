---
schema: comparison_provenance.v3
draft_card: ../cards/wikibase-item-property-snak-statement.md
draft_provenance: ../provenance/wikibase-item-property-snak-statement.md
similarity_result: ../similarity/wikibase-item-property-snak-statement.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0769
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0714
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0625
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.08，shared_tokens 仅为「的」。draft 标题的实质 token 是 Wikibase / Item / Property / Snak / Statement / 数据模型 / 核心结构，与 v2 候选（Karpathy LLM-wiki 元描述）无任何术语级重合。属于 jaccard 噪声。

## 2. draft 与候选在哪里不同

draft 是 concept 卡，来源 `wikibase-data-model`，论述 Wikibase 数据模型的四层结构（Item / Property / Snak / Statement）与 BNF、为什么不用三元组（Qualifier / Rank / Reference 直接做进 Statement 结构）、Datatype 非强类型与 Property 自由创建的边界。属于「结构化知识库 schema 设计」论点轴。

三张 v2 候选都是 Karpathy LLM-wiki 元描述。论点轴（结构化 wiki 数据模型 vs 个人 LLM wiki 模式）、来源（Wikibase 数据模型规范 vs Karpathy gist）、机制（人手编辑 Item/Statement + 强结构 vs LLM 写 markdown）完全不同。v2 卡都未涉及结构化数据建模。

## 3. 下一步的核心依据

shared_tokens 全是助词「的」，无语义关联。v2 候选 scope 严格限于 Karpathy 来源。draft 引文具体到 L311-321 / L423-447 / L467-475 / L528-545，scope 自洽，证据完整。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 sibling `wikibase-statement-rank-and-references` / `wikibase-three-snak-types` 是同 source 内的概念分层互引。
