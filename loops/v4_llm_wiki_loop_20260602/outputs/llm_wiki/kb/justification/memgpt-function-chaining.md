---
schema: justification_journal.v1
card: ../cards/memgpt-function-chaining.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`
源证据：
- sections/method_rewrite.tex — "In MemGPT, functions can be called with a special flag that requests control be immediately returned to the processor after the requested function completes execution."
- Figure 2 caption — "function chaining is what allows MemGPT to perform multi-step retrieval to answer user queries."
范围论证：函数链/心跳机制是 MemGPT 控制流的关键创新，区别于一般的函数调用，request_heartbeat 标志实现了 LLM 自主的多步操作循环，是独立的控制流原子概念。
