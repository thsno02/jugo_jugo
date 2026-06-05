---
schema: justification_journal.v1
card: ../cards/tool-mediated-memory-access.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/langchain-long-term-memory-docs/text.txt`
源证据：
- "Usage" 段 — "Tools can then read from and write to the store using the runtime.store parameter."
- "Read long-term memory in tools" 代码示例 — `runtime.store.get(("users",), user_id)`
- "Write long-term memory from tools" 代码示例 — `store.put(("users",), user_id, dict(user_info))`
- "Read long-term memory in tools" 代码示例 — `context=Context(user_id="user_123")`
范围论证：本卡聚焦 agent 通过工具函数间接访问记忆的架构模式及其后果（显式性、可观察性、上下文注入）。底层的 namespace-key 数据模型独立为另一张卡（namespace-key-memory-model）。
