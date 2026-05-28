---
id: langgraph-store-namespace-key-json-model
title: LangGraph Store 的命名空间-键-JSON 文档存储模型
status: accepted
card_type: concept
tags: [#langchain, #langgraph, #long-term-memory, #store, #api-model]
created_time: 2026-05-26T12:15:00+08:00
edited_time: 2026-05-28T14:10:00+08:00
edited_entity: llm
source_ids: [langchain-long-term-memory-docs]
provenance_card: ../provenance/langgraph-store-namespace-key-json-model.md
aliases: [LangGraph Store, InMemoryStore, PostgresStore, namespace and key]
related: [langgraph-tool-runtime-store-access]
---

## 模型

LangChain 的 long-term memory 通过 **LangGraph stores** 实现。store 把每条记忆存为一份 JSON 文档，并以两段坐标定位 [^src1]：

- **namespace（命名空间）**：类似文件夹，一个元组（tuple），常包含 user id、组织 id 或其他业务标签，用于做**层级化组织** [^src2]。
- **key（键）**：命名空间内的唯一标识符，类似文件名。

写入接口三件套：

```python
store.put(namespace, key, value_dict)
store.get(namespace, key)
store.search(namespace, filter={...}, query="...")
```

`value_dict` 是任意可序列化为 JSON 的字典；search 支持**内容过滤**（filter）与**自然语言 query**（按向量相似度排序，需要在 store 上配置 embedding index）。

## 与 short-term memory 的关键差别

- **short-term memory** 绑定在**单个 thread** 上，会话结束就丢；
- **long-term memory** 绑定在 store 上，**跨线程、跨会话持久**，可在任何时刻被任何 agent 调用回放。

这是 LangChain 在 agent 设计中明确分层的两类记忆——短期是对话级状态机的工作内存；长期是面向应用层的持久知识。

## 实现选项

| Store 类 | 用途 | 持久化 |
| --- | --- | --- |
| `InMemoryStore` | 开发/测试 | 进程内字典，重启即丢 |
| `PostgresStore` | 生产 | PostgreSQL，需 `langgraph-checkpoint-postgres`，启动时调用 `.setup()` |

两者共享同一 API（`.put` / `.get` / `.search` / IndexConfig），切换是配置变更而非代码重写。

## 索引配置（向量检索）

要让 `store.search(..., query="language preferences")` 走向量相似度，需在 store 构造时传 `IndexConfig` [^src3]：

```python
from langgraph.store.base import IndexConfig

store = InMemoryStore(
    index=IndexConfig(embed=embed_fn, dims=2),
)
```

`embed_fn` 接收文本序列、返回 embedding 列表（实际可换成任意 LangChain embeddings 对象）。dims 必须匹配实际 embedding 维度。

## 使用边界

- store 是**显式调用**模型——agent 不会自动把每条消息写入 store，需通过工具调用 [^v3-1] 或外部代码主动 `.put`。
- 跨命名空间搜索通过**内容过滤**而非天然支持的"全局搜索"——namespace 是隔离边界，不是索引前缀。
- 文档没有规定 store 的"遗忘"机制（衰减、TTL 等），这一层由开发者自己实现。

## Footnotes

[^src1]: `data/raw/webpage/langchain-long-term-memory-docs/text.txt` — 第 148 行 verbatim："Long-term memory is built on LangGraph stores, which save data as JSON documents organized by namespace and key."
[^src2]: `data/raw/webpage/langchain-long-term-memory-docs/text.txt` — 第 172 行 verbatim："Each memory is organized under a custom namespace (similar to a folder) and a distinct key (like a file name). Namespaces often include user or org IDs or other labels that makes it easier to organize information. This structure enables hierarchical organization of memories. Cross-namespace searching is then supported through content filters."
[^src3]: `data/raw/webpage/langchain-long-term-memory-docs/text.txt` — 第 178 行附近，InMemoryStore 块的 IndexConfig 示例代码。
[^v3-1]: [langgraph-tool-runtime-store-access](langgraph-tool-runtime-store-access.md) — 工具读写 store 的官方接入路径（ToolRuntime + runtime.store）。
