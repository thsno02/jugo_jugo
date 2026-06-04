---
schema: justification_journal.v1
card: ../cards/llm-wiki-pattern.md
created_time: 2026-06-04T22:30:00+08:00
---

## creation | 2026-06-04T22:30:00+08:00

生成方式：Mode A questioning loop, round 1
问题：RAG 与持久化 wiki 的区别——wiki 中积累了什么 RAG 无法积累的东西？
来源：`data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`

源证据：
- "The core idea" 第1段 — "the LLM is rediscovering knowledge from scratch on every question"
- "The core idea" 第2段 — "the LLM incrementally builds and maintains a persistent wiki"
- "The core idea" 第2段 — "The knowledge is compiled once and then kept current, not re-derived on every query"

范围论证：本卡聚焦 LLM Wiki 的核心模式定义及其与 RAG 的对比。
wiki 中具体积累的结构类型归入兄弟卡 wiki-compounding-artifact。
