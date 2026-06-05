---
id: namespace-key-memory-model
title: 命名空间-键值记忆数据模型
status: accepted
card_type: mechanism
tags: [long-term-memory, data-model, langchain, langgraph, namespace, key-value]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [langchain-long-term-memory-docs]
justification: ../justification/namespace-key-memory-model.md
canonical_concept: namespace-key-memory-model
aliases: [命名空间-键值存储, namespace-key store, LangGraph store 数据模型]
summary: >-
  namespace-key-memory-model（命名空间-键值存储 / namespace-key store / LangGraph store 数据模型）是 LangChain/LangGraph 用于持久化 agent 长期记忆的数据模型：以 JSON 文档为记忆单元，按层级命名空间（元组）+ 唯一键组织，支持精确过滤与向量相似度混合检索
related: [cross-session-continuity]
---

LangChain 的长期记忆基于 LangGraph store 构建，将记忆存储为 **JSON 文档**，并按**命名空间（namespace）+ 键（key）** 的层级结构组织[^src-1]。命名空间类似文件夹，键类似文件名；命名空间通常包含用户 ID、组织 ID 或应用上下文等标识信息，以元组形式表达，如 `(user_id, application_context)`[^src-2]。

该模型的检索能力包含两个维度：一是基于内容的精确过滤（`filter={"my-key": "my-value"}`），二是基于嵌入向量的语义相似度搜索（`query="language preferences"`），后者需通过 `IndexConfig` 配置嵌入函数与维度[^src-3]。跨命名空间的搜索通过内容过滤器实现[^src-4]。

存储后端可替换：开发阶段使用 `InMemoryStore`（内存字典），生产环境使用 `PostgresStore`（PostgreSQL 后端），两者共享相同的 API 接口[^src-5]。

该文档未讨论记忆的容量限制、淘汰策略、并发写入处理，也未讨论当相同 namespace+key 被重复写入时的合并或覆盖策略。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/langchain-long-term-memory-docs/text.txt` -- "Long-term memory" 概述段 -- "Long-term memory is built on LangGraph stores, which save data as JSON documents organized by namespace and key."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/langchain-long-term-memory-docs/text.txt` -- "Memory storage" 段 -- "Each memory is organized under a custom namespace (similar to a folder) and a distinct key (like a file name). Namespaces often include user or org IDs or other labels that makes it easier to organize information."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/langchain-long-term-memory-docs/text.txt` -- "Memory storage" 代码示例 -- "store.search(namespace, filter={\"my-key\": \"my-value\"}, query=\"language preferences\")"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/langchain-long-term-memory-docs/text.txt` -- "Memory storage" 段 -- "Cross-namespace searching is then supported through content filters."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/langchain-long-term-memory-docs/text.txt` -- "Usage" 段代码示例 -- "InMemoryStore saves data to an in-memory dictionary. Use a DB-backed store in production use."
