---
schema: justification_journal.v1
card: ../cards/memgpt-queue-eviction-policy.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`
源证据：
- sections/method_rewrite.tex — "When the prompt tokens exceed the 'warning token count'...the queue manager inserts a system message into the queue warning the LLM of an impending queue eviction"
- sections/method_rewrite.tex — "the queue manager flushes the queue to free up space in the context window: the queue manager evicts a specific count of messages...generates a new recursive summary"
范围论证：两阶段驱逐策略（memory pressure warning + flush）是 MemGPT 管理上下文溢出的具体机制，区别于内存层次结构的架构描述，是独立的运行时策略。
