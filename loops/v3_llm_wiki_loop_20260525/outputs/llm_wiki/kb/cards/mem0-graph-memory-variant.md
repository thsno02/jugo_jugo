---
id: mem0-graph-memory-variant
title: Mem0g 图记忆变体：实体-关系三元组 + 冲突解决，专攻时序与开放域
status: accepted
card_type: mechanism
tags: [#memory, #mem0, #knowledge-graph, #neo4j, #temporal-reasoning]
created_time: 2026-05-26T11:40:00+08:00
edited_time: 2026-05-28T10:50:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0]
provenance_card: ../provenance/mem0-graph-memory-variant.md
aliases: [Mem0g, mem0 graph variant, entity-relationship memory]
related: [mem0-extract-update-pipeline, mem0-locomo-benchmark-evaluation, mem0-tool-call-add-update-delete-noop, zep-graphiti-three-tier-graph, zep-bi-temporal-edges]
---

## 数据结构

Mem0g 把记忆表示为**有向带标签图** $G = (V, E, L)$[^src1]：

- **节点 V**：实体（如 `Alice`、`San_Francisco`）。每个实体节点存 (1) 实体类型分类（Person / Location / Event 等），(2) 嵌入向量 $e_v$，(3) 创建时间戳 $t_v$ 等元数据。
- **边 E**：实体间关系（如 `lives_in`）。
- **标签 L**：节点的语义类型（如 `Alice` 是 Person，`San_Francisco` 是 City）。

关系以三元组 $(v_s, r, v_d)$ 存储，源点+标签边+目标点。

## 抽取管线（两阶段 LLM）

1. **实体抽取器（Entity Extractor）**：从对话文本识别一组实体及类型——人物、地点、对象、概念、事件、属性等。判断依据是语义重要性、唯一性、跨会话持久性。论文用旅行计划场景作例：目的地（城市/国家）、交通方式、日期、活动、参与者偏好。
2. **关系生成器（Relationship Generator）**：在抽取实体之上推断有意义连接，输出关系三元组。基于语言模式、上下文线索、领域知识；评估每对实体潜在关系并贴标签（如 `lives_in` / `prefers` / `owns` / `happened_on`）。

prompt engineering 指导 LLM 同时考虑**显式陈述**与**隐含信息**，使三元组捕捉对话语义结构。

## 整合与冲突

新三元组写入时：

- 对源点与目标点分别计算嵌入；
- 查找语义相似超过阈值 $t$ 的现有节点；
- 根据存在性创建两点、单点或复用已有节点，再以适当元数据建立关系；
- **冲突检测机制**识别可能矛盾的现有关系，由 LLM 的 **update resolver** 判断某些关系是否应**标记为 invalid**（**不物理删除**），以保留时序推理能力[^src2]。

这是与 Mem0 base 版的关键不同：base 版的 DELETE 直接移除矛盾事实[^v3-1]，Mem0g 选择"打无效标记 + 保留"，让"事件 A 在 2023 年发生但在 2024 年改变"这类时序态可推理。这一选择与 Zep Graphiti 的 bi-temporal edges 思路同向[^v3-2]。

## 双路检索

Mem0g 检索时同时跑两条路径[^src3]：

- **实体中心法（Entity-centric）**：先识别查询中的关键实体，按语义相似性定位图节点，然后系统地探索入边/出边，构造包含相关上下文的子图。
- **语义三元组法（Semantic triplet）**：将整个查询编码为稠密嵌入，与图中每条关系三元组的文本编码做匹配，返回超过阈值的三元组并按相似度排序。

实体中心适合"目标实体明确"的问题；语义三元组适合"广义概念查询"——两者在 retrieval 时联合使用。Zep Graphiti 用三层图 (episode/semantic/community) + hybrid search 走的是另一种结构化路线[^v3-3]。

## 实现要点

- 图数据库：**Neo4j**；
- LLM 接口：**GPT-4o-mini** + function calling，做实体/关系结构化抽取与 update 决策；
- 与 base 版共享上下文窗口与 update 阶段框架。

## 性能侧的权衡（来自 LOCOMO 评估）

- **temporal** 与 **open-domain** 类题目上 Mem0g 是表中最高 J 分（J=58.13 / 75.71），比 base Mem0 高 2–3 个点；
- **single-hop** 与 **multi-hop** 上 Mem0g **不如** base Mem0（J=65.71 vs 67.13；J=47.19 vs 51.15），论文解释为"关系结构对单 turn 检索增益有限，可能引入冗余"；
- token 占用约 14k/对话（base Mem0 7k 的两倍），但仍远小于 Zep 的 600k+；
- 端到端 p50/p95 时延 1.091s / 2.590s（base Mem0 0.708s / 1.440s）——图开销可控但确实增加。

详细评估在 [mem0-locomo-benchmark-evaluation](mem0-locomo-benchmark-evaluation.md)。

## References

- §3.2（`sections/proposed_work.tex` 第 1163–1188 行）：图结构定义、抽取与冲突解决、双路检索、Neo4j 实现。
- §4 评估表（`sections/result.tex` 第 1047–1085 行）：各类型题目 Mem0 vs Mem0g 的 F1/B1/J 对比。
- 来源：`data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt`。

## Footnotes

[^1]: 冲突解决保留时序推理原文（第 1184 行）："An LLM-based *update resolver* determines if certain relationships should be obsolete, marking them as invalid rather than physically removing them to enable temporal reasoning."

[^2]: 双路检索原文（第 1186 行）："The memory retrieval functionality in Mem0g implements a dual-approach strategy for optimal information access. The entity-centric method first identifies key entities within a query ... the semantic triplet approach takes a more holistic view by encoding the entire query as a dense embedding."

[^3]: Mem0g 在 single-hop / multi-hop 上不优于 base 原文（§4 `result.tex` 第 1201–1204 行）："the addition of graph memory in Mem0g does not provide performance gains here, indicating potential inefficiencies or redundancies in structured graph representations for complex integrative tasks compared to dense natural language memory alone."
