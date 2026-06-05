---
schema: justification_journal.v1
card: ../cards/context-scaling-diminishing-returns.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt`
源证据：
- sections/intro.tex — "Directly extending the context length of transformers incurs a quadratic increase in computational time and memory cost"
- sections/intro.tex — "long-context models struggle to utilize additional context effectively"
- sections/experiments.tex — "many documents easily surpass these lengths...more flexible memory architectures like MemGPT are needed."
范围论证：上下文扩展的递减收益是 MemGPT 的核心立论基础，也是 LLM 系统设计中的独立问题，涉及计算开销、注意力分布、实际需求三个维度，作为独立的 distinction 卡提取。
