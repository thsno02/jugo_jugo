---
schema: accepted_card_provenance.v3
card: ../cards/langgraph-store-namespace-key-json-model.md
material_id: langchain-long-term-memory-docs
digest_id: digest_langchain-long-term-memory-docs
source_paths:
  - data/raw/webpage/langchain-long-term-memory-docs/text.txt
draft_card: ../../drafts/cards/langgraph-store-namespace-key-json-model.md
draft_provenance: ../../drafts/provenance/langgraph-store-namespace-key-json-model.md
similarity_result: ../../drafts/similarity/langgraph-store-namespace-key-json-model.json
comparison_provenance: ../../drafts/comparison/langgraph-store-namespace-key-json-model.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:27:00+08:00
  gate_notes: 6/6 项通过：namespace/key/JSON 模型 + put/get/search 三件套 + IndexConfig 代码 + 使用边界。
created_time: 2026-05-26T12:15:00+08:00
edited_time: 2026-05-27T10:27:00+08:00
edited_entity: llm
---

## 源证据

- 第 148 行 verbatim："Long-term memory lets your agent store and recall information across different conversations and sessions. Unlike short-term memory, which is scoped to a single thread, long-term memory persists across threads and can be recalled at any time. Long-term memory is built on LangGraph stores, which save data as JSON documents organized by namespace and key."
- 第 152–164 行：`create_agent(..., store=store)` 写法 + InMemoryStore / PostgresStore 切换代码。
- 第 172 行 verbatim："Each memory is organized under a custom namespace (similar to a folder) and a distinct key (like a file name) ... Cross-namespace searching is then supported through content filters."
- 第 178 行：`InMemoryStore(index=IndexConfig(embed=embed, dims=2))` 实例代码及 `store.put / get / search` 三件套示例。

## 卡片范围是否成立

- 卡片以 concept 类型记录"长期记忆的存储模型"，与官方文档"Memory storage"一节正面对应。
- 直接来自源：JSON 文档、namespace/key、跨 namespace 用 filter、InMemoryStore / PostgresStore 同 API、IndexConfig。
- 引申点："文档没有规定遗忘机制，这一层由开发者自己实现"是对页面缺席的诚实标注，未引入新主张。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:27:00+08:00
- 检查要点：
  - 非标题复述：以模型 + 与短期记忆差别 + 实现选项表 + 索引配置 + 使用边界五段实质展开。
  - 知识密度：API 三件套代码 + InMemoryStore/PostgresStore 对照 + IndexConfig 维度匹配规则。
  - 源支撑：langchain-long-term-memory-docs 行 138-182 verbatim。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 6 个 v3 draft id。

## 备注

- 与 `langgraph-tool-runtime-store-access` 构成连续的"模型 → 工具读写"序列；两卡专注不同 layer。
- v2 卡片中无 LangGraph 相关条目，无重叠。
- Adoption 阶段观察："文档" token 与 v2 schema 卡撞分是 jaccard 误中（两个"文档"语义不同）。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/langgraph-store-namespace-key-json-model.md`
- draft provenance: `../../drafts/provenance/langgraph-store-namespace-key-json-model.md`
- similarity: `../../drafts/similarity/langgraph-store-namespace-key-json-model.json`
- comparison provenance: `../../drafts/comparison/langgraph-store-namespace-key-json-model.md`
