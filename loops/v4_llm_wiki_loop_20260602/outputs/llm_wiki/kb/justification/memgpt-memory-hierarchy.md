---
schema: justification_journal.v1
card: ../cards/memgpt-memory-hierarchy.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`
源证据：
- sections/method_rewrite.tex — "MemGPT's OS-inspired multi-level memory architecture delineates between two primary memory types: main context (analogous to main memory/physical memory/RAM) and external context (analogous to disk memory/disk storage)."
- sections/method_rewrite.tex — "External context refers to any information that is held outside of the LLMs fixed context window."
范围论证：两级内存层次结构是 MemGPT 的架构基础，main context 与 external context 的区分是理解所有后续机制（queue manager、function chaining 等）的前提，作为独立架构概念提取。
