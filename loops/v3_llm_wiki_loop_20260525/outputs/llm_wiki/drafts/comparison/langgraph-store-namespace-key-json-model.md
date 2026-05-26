---
schema: comparison_provenance.v3
draft_card: ../cards/langgraph-store-namespace-key-json-model.md
draft_provenance: ../provenance/langgraph-store-namespace-key-json-model.md
similarity_result: ../similarity/langgraph-store-namespace-key-json-model.json
existing_cards:
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1333
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0769
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0714
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

top 1 共享 `文档` 与 `的`：draft 标题"…JSON 文档存储模型" vs 候选 "Schema 是 LLM Wiki 的配置文档"。这是因为两边都含"文档"这个高频通用名词。top 2/3 仅共享 `的`。draft 的核心 token `LangGraph`、`Store`、`namespace`、`键`、`命名空间` 等没有任何候选覆盖。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-schema-configuration-document`：仅记录 Karpathy gist 中 schema 层（结构/约定/工作流的配置文档）这一事实。是 wiki 维护层语义，不涉及任何 agent 框架的存储 API。
- 候选 #2 `idea-file-abstract-vague`：idea file 抽象性元事实卡，与 LangGraph Store API 无关。
- 候选 #3 `llm-wiki-three-layer-architecture`：Karpathy gist 的三层架构，与 LangGraph Store 的 namespace-key-JSON 模型不在同一概念体系。
- draft 来源是 `langchain-long-term-memory-docs/text.txt` L138–182，记录 LangGraph stores（InMemoryStore / PostgresStore / IndexConfig）以 namespace + key + JSON 文档为坐标的长期记忆存储模型，含 `put/get/search` 接口与向量索引示例代码。这是 v2 KB 完全没有的 agent 框架文档卡，论点轴与候选都不重合。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 无 LangGraph 系列卡。
- 不是 `provenance_delta`：候选都是 Karpathy gist 元事实，无法接收 LangGraph API 的反向引证。
- 不是 `duplicate_skip`：无任何重叠。
- 不是 `revise_before_gate`：draft 已有完整 namespace/key 定义、API 代码、IndexConfig 示例、使用边界（显式调用 / 跨命名空间 filter / 无遗忘机制）；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控阶段建议核 IndexConfig 示例代码片段与官方 doc 是否逐字对齐。

## 5. 备注

- "文档" token 与 v2 schema 卡撞分是典型 jaccard 误中：v2 卡里的"文档"指 schema 这一配置文件，与 draft 里的"JSON 文档"无任何概念关系。
- 与 draft 自身 related 列出的 `langgraph-tool-runtime-store-access` 一并构成 LangGraph 长期记忆系列首批卡。
