---
schema: draft_card_provenance.v3
draft_card: ../cards/mem0-graph-memory-variant.md
material_id: arxiv-mem0
digest_id: digest_arxiv-mem0
source_paths:
  - data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt
created_time: 2026-05-26T11:40:00+08:00
edited_time: 2026-05-26T11:40:00+08:00
edited_entity: llm
---

## 源证据

- 第 1163–1170 行（图结构定义 verbatim）：
  > "memories are represented as a directed labeled graph G = (V, E, L), where: Nodes V represent entities ... Edges E represent relationships ... Labels L assign semantic types to nodes ..."
- 第 1181–1184 行（实体抽取器、关系生成器、冲突检测）。verbatim 节选：
  > "An LLM-based *update resolver* determines if certain relationships should be obsolete, marking them as invalid rather than physically removing them to enable temporal reasoning."
- 第 1186 行（双路检索 verbatim）。
- 第 1188 行（Neo4j + GPT-4o-mini 实现）：
  > "the system utilizes Neo4j as the underlying graph database. LLM-based extractors and update module leverage GPT-4o-mini with function calling capabilities."
- 第 1047–1085 行（评估表 verbatim）：Mem0 vs Mem0g 在四类问题上的 F1/B1/J 对比。
- 第 1259–1260 行（`tab:latency_comparison`）：token 与延迟数据。
  > "Mem0 1764 0.148 0.200 0.708 1.440 66.88 ± 0.15%"
  > "Mem0g 3616 0.476 0.657 1.091 2.590 68.44 ± 0.17%"

## 卡片范围是否成立

- 卡片以 Mem0g 的"图结构 + 抽取 + 冲突 + 检索 + 性能侧权衡"为主，与论文 §3.2 + §4 的章节范围一致。
- 直接来自源：节点/边/三元组定义、Neo4j 实现、冲突无效化、双路检索、单/多 hop 不如 base 的 LOCOMO 现象。
- 引申点："base 版 DELETE 直接移除、Mem0g 标记 invalid"的对比是基于两份内文 verbatim 的直接对照，不引入额外主张。

## 发表门控结果

本轮未运行。

## 备注

- 与同 batch `mem0-extract-update-pipeline`、`mem0-tool-call-add-update-delete-noop`、`mem0-locomo-benchmark-evaluation` 构成 Mem0 的四卡集——comparison_provenance 阶段应整体审视命名与覆盖。
- v2 卡片中无对应条目。
