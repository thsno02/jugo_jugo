---
id: graphrag-leiden-community-hierarchy
title: 分层 Leiden 社群作为 GraphRAG 的"全局摘要索引"
status: accepted
card_type: mechanism
tags: [#graphrag, #community-detection, #leiden, #summary-hierarchy]
created_time: 2026-05-26T11:01:00+08:00
edited_time: 2026-05-28T11:15:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
provenance_card: ../provenance/graphrag-leiden-community-hierarchy.md
aliases: ["GraphRAG community summary", "C0/C1/C2/C3 levels"]
related: [graphrag-global-sensemaking-pipeline, graphrag-root-community-token-efficiency, wicer-cegar-compile-evaluate-refine]
---

GraphRAG[^v3-1] 的核心索引产物不是知识图本身，而是知识图上的**分层社群摘要**。论文用 Leiden 算法（Traag 2019，graspologic 实现）在抽好的实体图上做递归社群检测：每层都是对全图节点的"互斥且穷尽"（MECE）的划分，直到某层社群不可再分[^src1][^src2]。这棵社群树支撑"分而治之的全局摘要"。

**为何要分层、不直接全图摘要？** GraphRAG 利用图的内在模块性（modularity，Newman 2006）：紧密相连的实体往往谈同一个主题。分层 Leiden 把"主题—子主题"切成嵌套的盒子，从而把"对整个语料的摘要"分解成"对每个主题盒子的小摘要再聚合"。

**摘要生成的递归构造规则[^src3]：**

- *叶社群*：把"element 摘要"（节点描述、边描述、claim 描述）按"源节点度 + 目标节点度降序"排序，依次塞入 LLM 上下文直到 token 上限；
- *上层社群*：若所有子社群的 element 摘要总长能塞进上下文，就直接当叶社群处理；否则按 element 摘要 token 数降序，逐个用更短的"子社群摘要"替换更长的 element 摘要，直到塞得下。

**四个层级在论文里被命名为 C0–C3：**

- **C0**：根社群层（Podcast 34 个 / News 55 个）；
- **C1–C3**：依次往下细分，叶层（C3）社群最多（Podcast 1310 / News 2142）。

数据集规模：8,564 节点 / 20,691 边（Podcast）、15,754 / 19,520（News）[^src4]。

**实践含义：**

- 每个查询都不会把整个图塞进上下文；只有"被选中层级"的社群摘要参与 map-reduce。
- 同一查询可以选不同层级回答——根级提供宏观主题、叶级提供细粒度证据；论文发现叶级的 C3 在 News 数据集上回答 comprehensiveness 胜率更高，但 C0 在 token 成本上低 9–43 倍[^v3-2]。
- 因为是 MECE 划分，加新文档时只需要增量更新被影响的社群子树，而不必重算整棵树——这是它"可滚动增长"的结构基础。这种"被诊断的局部失败 → 增量编译"的反馈风格，与 WiCER 的 CEGAR 反例制导细化算法[^v3-3] 同源。

边界：本节描述的是论文报告的实现，使用 Leiden + 度数排序 + token 上限。换其他社群算法（Louvain、谱聚类）或换 element 排序规则，结果会变。

## Footnotes

[^v3-1]: [graphrag-global-sensemaking-pipeline](graphrag-global-sensemaking-pipeline.md) — 本卡是该流水线索引阶段第 4–5 步的展开
[^v3-2]: [graphrag-root-community-token-efficiency](graphrag-root-community-token-efficiency.md) — C0 与 C3 的 token 成本对照与"9–43 倍"数字出处
[^v3-3]: [wicer-cegar-compile-evaluate-refine](wicer-cegar-compile-evaluate-refine.md) — WiCER 把 wiki 编译当作 CEGAR 抽象细化，与 MECE 增量更新的反馈风格同源
[^src1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` — Edge et al., NeurIPS 2024，§3.1.4–3.1.5（行 821–844）；行 823–824："we use Leiden community detection in a hierarchical manner, recursively detecting sub-communities within each detected community until reaching leaf communities that can no longer be partitioned"
[^src2]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` — 行 826："Each level of this hierarchy provides a community partition that covers the nodes of the graph in a mutually exclusive, collectively exhaustive way"。社群分层可视化见 appendix `\subsection{Example Community Detection}`（行 80–82）
[^src3]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` — 行 838–843（叶/上层社群构造规则）。C0–C3 单元数与 token 数详见 `tab:community summaries`（行 438–446）
[^src4]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` — 行 980（Podcast 与 News 数据集的节点/边规模）
