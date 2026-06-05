---
schema: justification_journal.v1
card: ../cards/namespace-key-memory-model.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/langchain-long-term-memory-docs/text.txt`
源证据：
- "Long-term memory" 概述段 — "Long-term memory is built on LangGraph stores, which save data as JSON documents organized by namespace and key."
- "Memory storage" 段 — "Each memory is organized under a custom namespace (similar to a folder) and a distinct key (like a file name)."
- "Memory storage" 代码示例 — `store.search(namespace, filter=..., query=...)`
范围论证：本卡聚焦 LangGraph store 的数据模型设计（namespace+key+JSON document），包含其检索能力（过滤+向量相似度）。存储后端的可替换性作为该数据模型的工程属性一并记录。工具层面的访问模式（tool-mediated access）独立为另一张卡。
