---
schema: comparison_provenance.v3
draft_card: ../cards/wikibase-conceptual-not-serialization.md
draft_provenance: ../provenance/wikibase-conceptual-not-serialization.md
similarity_result: ../similarity/wikibase-conceptual-not-serialization.json
existing_cards:
  - card_id: raw-sources-readonly-source-of-truth
    card_path: llm_wiki/kb/cards/raw-sources-readonly-source-of-truth.md
    score: 0.0667
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0625
  - card_id: rag-document-qa-does-not-accumulate-synthesized-knowledge
    card_path: llm_wiki/kb/cards/rag-document-qa-does-not-accumulate-synthesized-knowledge.md
    score: 0.0588
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选 token 共享应该集中在"模型 / 数据 / 文档"等通用词上。Top 2 `llm-wiki-schema-configuration-document` 共享 `schema`（draft 标题里 "Wikibase 数据模型" 也有 schema 一词），是这批中最有可能误中的 jaccard 信号；但 v2 中 schema 指 Karpathy LLM Wiki 的工作流配置文档，与 Wikibase 的概念数据模型完全不同。

## 2. draft 与候选在哪里不同

draft 描述 Wikibase 数据模型文档的三层"不是什么"：不是 binding/实现规范、不是序列化（JSON/RDF 在别处）、不是形式语义；引入 UML class diagram 与 WON BNF 仅用于举例。论点轴是"conceptual / serialization / implementation 解耦让 Wikidata 能持续演化"。

Top 1 `raw-sources-readonly-source-of-truth` 描述 Karpathy LLM Wiki 中 raw sources 层（用户策展、不可变的源文档）；top 2 `llm-wiki-schema-configuration-document` 把 schema 描述为 LLM 工作流配置；top 3 `rag-document-qa-does-not-accumulate-synthesized-knowledge` 是对 RAG 式文档问答体验的批判。三者都没有讨论"概念模型 / 序列化 / 形式语义"三层解耦或 UML / WON。

特别地，v2 `llm-wiki-schema-configuration-document` 的 schema 是"指挥 LLM 行为的配置"，Wikibase 的 schema 是"描述数据结构的概念模型"——同名异指。

## 3. 下一步的核心依据

虽然两边都有 schema 一词，但它们的"schema"指向完全不同的对象（一个是 agent 的行为约束，一个是数据本体描述）。draft 是关于一个外部数据模型规范（Wikibase）的概念定位，与 Karpathy LLM Wiki 概念层无任何论点重叠。结论 `new_card`。

不选 `provenance_delta`：v2 schema 卡讨论的是 LLM 行为约束，不会因 Wikibase 设计原则获得新证据。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；本卡建立 Wikibase 数据模型主题入口。

## 5. 备注

"schema" 在两边都是核心词但语义不同——是本批中最值得提醒下游 audit 不要被误判的一对同名异指。
