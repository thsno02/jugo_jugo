---
card_id: llm-as-knowledge-compiler
decision: accepted
---

## 为何接受

1. **原子性**——聚焦 LLM 在 wiki 系统中的单一角色定义（编译器/综合者），不与架构层面的编译时vs查询时区分重叠。

2. **独特贡献**——现有 `compile-time-vs-query-time` 卡聚焦"何时装配知识"（架构时序），但不涉及"LLM 在装配过程中扮演什么角色"（agent 职能）。本卡填补了 agent 层面的空白：LLM 是主动综合者/维护者，不仅是查询应答者。

3. **机制层面**——具体描述了 raw/ -> 综合 -> wiki/ -> backlinks -> health check 的完整编译循环，这是一个可操作的机制描述，现有卡片中无对应。

4. **反向链接作为知识图谱边**——这一具体机制（backlinks as lightweight knowledge graph edges）在现有卡片中未被提取，是 wiki 可导航性的关键设计决策。

## 为何不与现有卡合并

- `compile-time-vs-query-time` 是一个架构区分卡（distinction），聚焦的是"LLM wiki 在编译时加载 vs RAG 在查询时检索"的时序差异。它不涉及 LLM 在编译过程中的主动综合角色。
- 本卡聚焦的是 LLM 的 agent 职能（编译器 = 综合 + 维护 + 自我修复），是 `compile-time-vs-query-time` 的下游机制细节。
- 两者形成清晰的层级关系：架构选择 -> 编译器角色机制。
