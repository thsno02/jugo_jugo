---
id: langgraph-tool-runtime-store-access
title: 通过 ToolRuntime 让工具读写 LangGraph Store
status: accepted
card_type: operational_rule
tags: [#langchain, #langgraph, #tool-calling, #agent-runtime]
created_time: 2026-05-26T12:20:00+08:00
edited_time: 2026-05-28T14:12:00+08:00
edited_entity: llm
source_ids: [langchain-long-term-memory-docs]
provenance_card: ../provenance/langgraph-tool-runtime-store-access.md
aliases: [ToolRuntime, runtime.store, agent tool memory access]
related: [langgraph-store-namespace-key-json-model, mem0-tool-call-add-update-delete-noop, mem0-extract-update-pipeline, memgpt-function-chaining-heartbeat, memory-as-metabolism-five-operations, llm-wiki-mcp-four-tools]
---

## 接入方式

LangChain 让工具访问 long-term memory 的官方路径是：

1. 在 `create_agent(..., store=store)` 中把 store 传入；
2. 工具函数声明 `runtime: ToolRuntime[Context]` 形参；
3. 在工具内通过 `runtime.store` 调用 `.get / .put / .search`。

`ToolRuntime[Context]` 是泛型，`Context` 是开发者自定义的 dataclass，承载例如 `user_id` 之类的运行时上下文，在 agent.invoke 时通过 `context=Context(user_id=...)` 传入。

## 读：典型工具示例

```python
from dataclasses import dataclass
from langchain.tools import ToolRuntime, tool

@dataclass
class Context:
    user_id: str

@tool
def get_user_info(runtime: ToolRuntime[Context]) -> str:
    """Look up user info."""
    assert runtime.store is not None
    user_id = runtime.context.user_id
    user_info = runtime.store.get(("users",), user_id)
    return str(user_info.value) if user_info else "Unknown user"
```

- namespace 由代码硬定（这里 `("users",)`），key 来自 runtime 上下文的 `user_id`；
- 返回的 `StoreValue` 对象同时携带 value 和 metadata。

## 写：把对话中提取的事实存入 store

```python
class UserInfo(TypedDict):
    name: str

@tool
def save_user_info(user_info: UserInfo, runtime: ToolRuntime[Context]) -> str:
    """Save user info."""
    assert runtime.store is not None
    runtime.store.put(("users",), runtime.context.user_id, dict(user_info))
    return "Successfully saved user info."
```

agent 被指示更新 user 信息时，会自动调用这个工具——LLM 决定**何时**写、写**什么**，工具只负责把决定落库。

## 关键设计选择

- **store 不自动写**：所有写入须经显式工具调用；这与 ChatGPT memory 的"自动检测重要事实"相反，把写入主动权交给开发者/agent 推理。
- **context 不在 prompt 里**：`user_id` 通过 `runtime.context` 传递，不需要把它注入对话 prompt——避免敏感字段进入 LLM 输入。
- **dataclass 作为 Context**：编译期类型安全；如果 `runtime.context.user_id` 没传，运行期立刻报错而不是默默用错 key。

## 与 model 解耦

文档展示了同一段工具代码在 Google / OpenAI / Anthropic / OpenRouter / Fireworks / Baseten / Ollama 多种模型下都可用（页面以选项卡形式列出）——`create_agent` 的 `model` 参数只换字符串，工具与 store 调用代码不变。这是 LangGraph 把记忆 API **从模型 vendor 解耦**的具体体现。

## 局限

- `runtime.store is not None` 的断言必须在每个工具里写——文档建议但未在签名层强制；
- 工具调用次数 = LLM 推理次数 × 平均工具数，对**高频写**场景需注意 token / 延迟成本；
- 文档示例都是单 key 单 value，对**批量更新**或**事务性更新**没有给出推荐模式。

## References

- 来源页面：`data/raw/webpage/langchain-long-term-memory-docs/text.txt`。
- 第 186–208 行：Read long-term memory in tools（`get_user_info` 完整示例 + 多模型选项卡）。
- 第 212–234 行：Write long-term memory from tools（`save_user_info` 完整示例）。

## Footnotes

[^1]: 读工具完整代码 verbatim 节选（第 206 行）："@tool def get_user_info(runtime: ToolRuntime[Context]) -> str: ... user_info = runtime.store.get(('users',), user_id); return str(user_info.value) if user_info else 'Unknown user'"

[^2]: 写工具调用方式 verbatim（第 232 行）："agent.invoke({'messages': [{'role': 'user', 'content': 'My name is John Smith'}]}, context=Context(user_id='user_123'))"

[^3]: 多模型选项卡（第 192–204 行）列出 InMemoryStore / PostgreSQL / Google / OpenAI / Anthropic / OpenRouter / Fireworks / Baseten / Ollama 等，证明工具/store 代码与 model 无关。
