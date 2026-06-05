---
id: tool-mediated-memory-access
title: 工具中介的记忆访问模式
status: accepted
card_type: mechanism
tags: [long-term-memory, tool-use, agent-architecture, langchain, memory-access]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [langchain-long-term-memory-docs]
justification: ../justification/tool-mediated-memory-access.md
canonical_concept: tool-mediated-memory-access
aliases: [工具中介记忆访问, tool-mediated memory, runtime.store 访问模式]
summary: >-
  tool-mediated-memory-access（工具中介记忆访问 / tool-mediated memory / runtime.store 访问模式）是 LangChain agent 通过工具函数间接访问长期记忆的架构模式：agent 不直接读写 store，而是调用声明了 ToolRuntime 参数的工具函数，由工具代为执行 get/put/search 操作
related: [cross-session-continuity, memgpt-self-directed-memory, namespace-key-memory-model]
---

在 LangChain 的长期记忆架构中，agent 本身**不直接读写**记忆存储。所有对 store 的访问都通过**工具函数**中介完成[^src-1]。工具函数声明 `runtime: ToolRuntime[Context]` 参数，在运行时获得对 store 的引用（`runtime.store`），从而执行 `.get()`、`.put()`、`.search()` 等操作[^src-2][^src-3]。

这种间接访问模式带来几个架构后果：

1. **显式性**——agent 必须主动决定调用记忆工具，记忆的读写不会自动发生
2. **可观察性**——记忆操作作为工具调用出现在对话流中，可被追踪和审计
3. **上下文注入**——通过 `context_schema`（如含 `user_id` 的 dataclass），调用方在 agent 启动时注入运行时上下文，工具通过 `runtime.context` 获取，从而知道为哪个用户读写记忆[^src-4]

该文档未讨论 agent 如何决定**何时**调用记忆工具（是否有自动触发机制，还是完全依赖 LLM 的自主判断），也未讨论当 agent 未调用记忆工具时信息丢失的风险。MemGPT 的自主内存编辑机制代表了更激进的自主性设计——LLM 完全自主决定何时在内存层级间移动数据[^card-1]。

## Footnotes

[^card-1]: [MemGPT 自主内存编辑与检索](memgpt-self-directed-memory.md) -- LangChain 的工具中介模式（显式工具调用）与 MemGPT 的自主编辑模式（LLM 完全自主驱动）代表 agent 记忆访问自主性的两端

[^src-1]: `data/raw/webpage/langchain-long-term-memory-docs/text.txt` -- "Usage" 段 -- "Tools can then read from and write to the store using the runtime.store parameter."
[^src-2]: `data/raw/webpage/langchain-long-term-memory-docs/text.txt` -- "Read long-term memory in tools" 代码示例 -- "user_info = runtime.store.get((\"users\",), user_id)"
[^src-3]: `data/raw/webpage/langchain-long-term-memory-docs/text.txt` -- "Write long-term memory from tools" 代码示例 -- "store.put((\"users\",), user_id, dict(user_info))"
[^src-4]: `data/raw/webpage/langchain-long-term-memory-docs/text.txt` -- "Read long-term memory in tools" 代码示例 -- "agent.invoke({...}, context=Context(user_id=\"user_123\"))"
