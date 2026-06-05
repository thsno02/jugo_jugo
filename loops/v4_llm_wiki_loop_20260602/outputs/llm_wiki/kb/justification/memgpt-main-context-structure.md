---
schema: justification_journal.v1
card: ../cards/memgpt-main-context-structure.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`
源证据：
- sections/method_rewrite.tex — "The prompt tokens in MemGPT are split into three contiguous sections: the system instructions, working context, and FIFO Queue."
- sections/method_rewrite.tex — "The first index in the FIFO queue stores a system message containing a recursive summary of messages that have been evicted from the queue."
范围论证：三段式主上下文结构是 MemGPT 的具体实现设计，system instructions / working context / FIFO queue 各有不同的读写属性和用途，构成一个完整的原子设计模式。
