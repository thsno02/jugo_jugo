---
schema: justification_journal.v1
card: ../cards/memgpt-event-driven-control-flow.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`
源证据：
- sections/method_rewrite.tex — "In MemGPT, events trigger LLM inference: events are generalized inputs to MemGPT and can consist of user messages...system messages...user interactions...and timed events"
- sections/method_rewrite.tex — "MemGPT processes events with a parser to convert them into plain text messages"
范围论证：事件驱动控制流是 MemGPT OS 类比的另一支柱（与内存层次并列），定时事件使 LLM 可无人值守运行，这是独立于函数链的控制流概念。
