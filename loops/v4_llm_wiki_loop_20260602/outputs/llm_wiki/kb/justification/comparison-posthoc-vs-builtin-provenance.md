---
card_id: comparison-posthoc-vs-builtin-provenance
---

## creation | 2026-06-05T15:00:00+08:00

生成方式：governance comparison pipeline
note: comparison/distinction 卡由 governance workflow 生成

## 为什么这张卡值得存在

这张区分卡捕捉了知识系统溯源设计中的一个核心架构决策：溯源能力应在数据写入时内建，还是在需要验证时事后遍历？

## 证据来源

- **LLM Wiki 审计**（来源：llm-wiki-net）：审计沿制品图 output->wiki->raw 事后遍历，检测漂移和验证可信度。溯源依赖已有的制品层次引用关系。
- **Graphiti 无损 episode 存储**（来源：arxiv-zep）：episode 与语义边在写入时建立双向索引，溯源是数据模型的固有属性。

## 为什么构成区分而非仅仅是「两个不同系统」

两者解决的是同一个问题（如何从知识制品追溯到原始来源），但在架构策略上做出了相反的权衡：
- 事后策略优先写入简单性，牺牲溯源的即时可用性
- 内建策略优先溯源的始终可用性，增加写入复杂度

这一区分对设计新的知识系统具有直接指导意义：选择事后还是内建溯源是一个需要显式做出的架构决策。
