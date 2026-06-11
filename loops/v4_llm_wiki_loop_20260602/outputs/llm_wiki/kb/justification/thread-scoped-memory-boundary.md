---
card_id: thread-scoped-memory-boundary
decision: accept
---

## 为什么接受

1. **原子性**：该卡聚焦于一个明确的架构概念——"线程"作为短期/长期记忆的分界线——与已有的 namespace-key-memory-model（关注数据模型结构）和 tool-mediated-memory-access（关注访问模式）在概念层级不重叠。

2. **来源支撑**：文档开篇明确给出定义："Unlike short-term memory, which is scoped to a single thread, long-term memory persists across threads and can be recalled at any time."

3. **知识增量**：
   - namespace-key-memory-model 描述长期记忆"怎么存"（JSON + namespace + key）
   - tool-mediated-memory-access 描述长期记忆"怎么访问"（通过工具函数）
   - 本卡填补"短期 vs 长期的边界在哪里"这一分类学空白

4. **连接性**：与 cross-session-continuity（讨论跨会话持久化的通用机制）形成对话——LangChain 的"thread"概念是其对"session boundary"的具体实现定义。

## 不确定性标注

- "thread"在 LangGraph 中的精确生命周期语义需查阅 LangGraph Persistence 文档确认
- 短期记忆是否有线程内持久化机制（如 checkpointing）未从本文档获证
