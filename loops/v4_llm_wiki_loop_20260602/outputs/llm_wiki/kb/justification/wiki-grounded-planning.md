---
schema: justification_journal.v1
card: ../cards/wiki-grounded-planning.md
created_time: 2026-06-11T10:00:00+08:00
---

## creation | 2026-06-11T10:00:00+08:00

生成方式：source extraction pass
来源：`data/raw/webpage/llm-wiki-net/markdown.md`
源证据：
- L38 — "Wiki-grounded implementation plans. Reads the knowledge base, interviews you about requirements, fills gaps with targeted research, and produces a phased plan citing wiki articles as evidence. --format rfc|adr|spec."
- L147 — "/wiki:plan <goal> Wiki-grounded implementation plan. --format rfc|adr|spec."
范围论证：wiki-grounded planning 是一个独立的决策支持机制，区别于产出复利循环（后者描述产出回写的正反馈），也区别于并行研究（后者描述信息获取方式）。其核心独特性在于「证据锚定」——计划中的每个决策必须引用 wiki 文章作为依据，缺乏证据时主动发起补充研究而非凭空推断。三种格式输出（rfc/adr/spec）也表明这是一个面向软件工程决策的专门化工具。现有卡片无一涵盖此机制。
