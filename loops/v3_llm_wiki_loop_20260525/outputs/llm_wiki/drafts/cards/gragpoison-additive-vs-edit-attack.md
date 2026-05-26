---
id: gragpoison-additive-vs-edit-attack
title: GraphRAG 投毒的两条家族：additive injection vs in-place edit
status: draft
card_type: distinction
tags: [#graphrag, #security, #poisoning, #attack-taxonomy]
created_time: 2026-05-26T11:42:00+08:00
edited_time: 2026-05-26T11:42:00+08:00
edited_entity: llm
source_ids: [arxiv-graph-poisoning]
provenance_card: ../provenance/gragpoison-additive-vs-edit-attack.md
aliases: ["GRAGPOISON vs TKPA/UKPA", "additive vs manipulation attack"]
related: [graphrag-manipulation-only-attack-surface, tkpa-graph-guided-targeted-poisoning, ukpa-coreference-disruption]
---

Wen 等人把 GraphRAG 投毒文献划成两条互补的"家族"：第一条是 GRAGPOISON（Liang 等，arXiv:2501.14050）代表的 **additive** 路线——往语料库里**加**新的 chunk，再让构图器把这些 chunk 抽出来的新实体/关系当成真知识；第二条是本论文提出的 **in-place edit** 路线（TKPA / UKPA）——**不加任何 chunk**，只改动语料中已有的少数词。两条家族在攻击者能力、可观察痕迹、可防御性上完全不同，混着谈会丢精度。

按维度对照：

| 维度 | additive（GRAGPOISON 系） | in-place edit（TKPA / UKPA） |
| --- | --- | --- |
| 改动类型 | 注入新 chunk / 重复已有关系 / 加伪叙述 | 仅改写已有文本中的少数词 |
| 受信源假设 | 攻击者能新增内容（如 PR、上传） | 攻击者能编辑受信源（如 Wikipedia 词条） |
| 影响传播 | 让构图器抽出"伪关系"，强化或新建图边 | 让构图器抽错实体/边，或让共指失败 |
| 文本可见痕迹 | 多出来的 chunk 可与"已知 trusted snapshot"做 diff 检出 | 改动散落在已有 chunk 内部，diff 噪声大 |
| 论文实测痕迹 | 论文未给具体词量；目标是关系层操控 | TKPA 改 48/94,496 词（0.06%）即 93.1% ASR；UKPA 改 60/134,072 词（0.05%）即 QA 95→50 |
| 防御切入点 | 写入审计 / 新 chunk 检测 / source provenance | 需对比"构图前后" entity-relation 集合差，文本层防御普遍失效 |

论文为什么要新立 in-place edit 这一类，原话讲得很直白：*"An unexplored question is whether GraphRAG is also vulnerable when the adversary cannot add new text, but is only able to make small, subtle modifications to the existing corpus."* GRAGPOISON 默认攻击者能加内容；in-place edit 把威胁降级到"我只能改 Wikipedia 几个词"，对应**更现实、更隐蔽**的场景。

操作含义：

- **威胁建模不能省略这条区分**。"防御 GraphRAG 投毒"按 additive 思路（写入审计、来源签名、新 chunk 异常检测）做完，对 in-place edit 几乎没有效果——论文的 §Stealthiness 表显示 PF/LLMDet/SCC 对 TKPA、UKPA 的 F1 ≤ 0.13。
- **审计指标也不同**。additive 攻击应监控 chunk 总数与新 chunk 来源分布；in-place 攻击应监控**同一份源在多次构图下生成的图差**（节点/边 Jaccard）。
- **攻击者效用曲线不同**。additive 系易于规模化（多投几条），但被发现的代价线性增加；in-place 系单点改动极少，但需要更深的领域 / 图论知识（TKPA）或共指敏感的语言学知识（UKPA）。

边界与误读：

- GRAGPOISON 自身也有"重复已有关系"的小变体，介于纯加内容与改内容之间，但 Wen 等人仍把它归在 additive 一边（"operates in an additive manner"），因为它的核心仍是"让某些关系被多次抽到"。
- 两类家族不互斥：现实攻击者可以两边都用——先注入一条引子 chunk，再回头改它周围的几个词加强抽取效果。论文没有研究复合攻击，但工程上应当假设两者会并行出现。
- 这条区分专门用于 GraphRAG。对普通 chunk-RAG 而言，由于不存在"构图"步骤，additive vs in-place 之分意义不大（in-place 攻击只能影响那一段 chunk 被检索时的回答，不会持久污染结构）。

## References

- GRAGPOISON 的 additive 策略描述与本论文的 in-place 立论见 Introduction（`data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` 第 193–205 行）。
- TKPA / UKPA 的修改词量数字见 Table~\ref{tab:Words_modification}（同文件 L769–789）。
- 文本层防御 F1 0.04–0.13 见 Table~\ref{tab:defense_evaluation}（L749–757）。

## Footnotes

- L193–198：*"Recent work has taken the first step toward poisoning GraphRAG: GRAGPOISON injects crafted chunks that create or amplify false relations ... While GRAGPOISON demonstrates that GraphRAG can indeed be poisoned, its attack strategies all operate in an additive manner ... An unexplored question is whether GraphRAG is also vulnerable when the adversary cannot add new text, but is only able to make small, subtle modifications to the existing corpus."*
- L226–230：贡献声明中"manipulation-only attack surface ... modifying a small number of words in the trusted corpus is sufficient"。
- L778–784：TKPA 与 UKPA 的逐数据集词量与修改比率。
- L749–757：PF / LLMDet / SCC 三类文本层防御 F1。
