---
id: langgraph-tool-runtime-store-access
title: LangGraph ToolRuntime 访问 Store 模式
status: draft
card_type: integration-pattern
tags: [langgraph, toolruntime, store, agent, tool]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [langchain-long-term-memory-docs]
evidence_basis: documentation
justification: ../justification/langgraph-tool-runtime-store-access.md
canonical_concept: langgraph-tool-runtime-store-access
aliases: [ToolRuntime, runtime.store, tool store access, Tool 中访问 Store]
summary: >-
  LangGraph agent tool 通过 ToolRuntime 参数访问 store。Tool 函数声明 runtime: ToolRuntime[Context] 参数，
  runtime.store 为传给 create_agent 的同一 store 实例，runtime.context 提供运行时上下文（如 user_id）。
  context_schema 为 dataclass 定义，调用 agent 时通过 context= 传入。支持读取（store.get）和写入（store.put）。
related: [langgraph-store-data-model, langgraph-long-term-memory-concept]
---

LangGraph 中 agent tool 通过 `ToolRuntime` 参数访问 store：[^src-1]

1. Tool 函数声明 `runtime: ToolRuntime[Context]` 参数
2. `runtime.store` 即为传给 `create_agent` 的同一 store 实例
3. `runtime.context` 提供运行时上下文信息

Context 通过 `context_schema` 定义（dataclass），在调用 agent 时通过 `context=Context(user_id="...")` 传入。[^src-1]

读取模式：`runtime.store.get(("users",), user_id)` 返回 StoreValue 对象，通过 `.value` 访问数据。[^src-1]

写入模式：`runtime.store.put(("users",), user_id, dict(user_info))` 存入结构化数据（常用 TypedDict 定义 schema）。[^src-2]

[^src-1]: `data/raw/webpage/langchain-long-term-memory-docs/markdown.md` -- "Read from store" P1 -- "def get_user_info(runtime: ToolRuntime[Context]) -> str: ... user_info = runtime.store.get((\"users\",), user_id)"
[^src-2]: `data/raw/webpage/langchain-long-term-memory-docs/markdown.md` -- "Write to store" P1 -- "def save_user_info(user_info: UserInfo, runtime: ToolRuntime[Context]) -> str: ... store.put((\"users\",), user_id, dict(user_info))"

[^card-1]: ToolRuntime 是在 tool 层面操作 [langgraph-store-data-model] 的桥梁。
