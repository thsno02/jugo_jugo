---
id: ukpa-coreference-disruption
title: UKPA：通过破坏指代链让 GraphRAG 的实体合并全面失败
status: draft
card_type: mechanism
tags: [#graphrag, #security, #coreference, #universal-attack]
created_time: 2026-05-26T11:10:00+08:00
edited_time: 2026-05-26T11:10:00+08:00
edited_entity: llm
source_ids: [arxiv-graph-poisoning]
provenance_card: ../provenance/ukpa-coreference-disruption.md
aliases: ["Universal Knowledge Poisoning Attack", "通用知识投毒"]
related: [graphrag-manipulation-only-attack-surface, tkpa-graph-guided-targeted-poisoning, ukpa-edit-distance-stealth-tradeoff, gragpoison-additive-vs-edit-attack, graphrag-text-defense-blind-spot, graphrag-pipeline-formalism, graphrag-global-sensemaking-pipeline]
---

UKPA（Universal Knowledge Poisoning Attack）的目标不是改一个答案，而是**让 GraphRAG 在所有查询上一起退化**。它的关键洞察来自 NLP：跨 chunk 的实体合并（entity linking）几乎完全靠**共指线索**——代词、定指描述、其他指代表达——来判断"散落在不同段落里的提及"是否同一个实体。这些信号是脆弱、上下文敏感的；轻微改写就能让共指模型不再聚类同一实体。UKPA 把这种语言学弱点武器化，攻击者**完全在文本域**操作，从不接触最终图，却能让构图阶段就出大量裂解。

四步流水线：

1. **逐 chunk 语言学分析**——对每个 chunk 用 LLM 抽 coreference chain，列出所有 mention→entity 映射。这些链就是 GraphRAG 后续合并节点用的隐式骨架。
2. **扰动候选生成**——LLM 生成多个改写候选，必须满足三约束：保持语法流畅、保持局部语义、与原文编辑距离很小。典型改写包括把代词换成模糊名词短语、给指代表达加歧义、调整从句顺序。
3. **结构影响打分**（在不接触最终图的前提下做代理评估）：  
   $$\mathcal{I}_\mathrm{score} = \alpha S_\mathrm{entity} + \beta S_\mathrm{relation} + \gamma (1 - S_\mathrm{vec})$$  
   $S_\mathrm{entity}$ / $S_\mathrm{relation}$ 是原文与改写在 chunk 局部抽出的实体集 / 关系集的对称差，$S_\mathrm{vec}$ 是嵌入余弦相似度。默认 $(\alpha,\beta,\gamma)=(0.25,0.25,0.5)$——优先**结构改变大、但语义仍接近原文**的候选。
4. **选择与写回**——每个 chunk 选分最高的改写替换原文。当 GraphRAG 再次构图时，"原本会合并成一个节点的若干提及"被切成多个孤立节点，关系散落，多跳推理链塌掉。

杀伤力的实测见两组数字：

- **拓扑层面**：在 *Russo-Ukrainian War* + Microsoft GraphRAG 上，边保留率从 1 跌到 0.2770，边 Jaccard 仅 0.1581；在 LightRAG + LP 上，边 Jaccard 0.1362。也就是图在节点数没大变的情况下，**拓扑几乎被重写**。
- **下游层面**：Microsoft GraphRAG 的 QA 准确率从 95% 掉到 50%，LightRAG 从 90% 掉到 45%。对照的 TextFooler-style Perturbation（TP，单纯做嵌入近义替换、忽略共指）只把两者拉到 85%，差距悬殊。
- **修改量**：LP 只动 32/94,496 词（0.033%），RUW 60/134,072 词（0.045%）——比 TKPA 还小。

边界与误读：

- UKPA 的"通用"是指**对所有查询同时变差**，不是"对所有 GraphRAG 系统等效有效"——两套 GraphRAG（Microsoft、LightRAG）的退化幅度并不完全一致，因为各自的实体合并策略不同。
- 攻击有效性的来源是 GraphRAG 把 coreference resolution 当成默认依赖；如果未来某天构图器换成更鲁棒的指代消解模型，这套攻击会被部分削弱。但论文同时指出：sentence-level 流畅度被保留，所以即使加强了构图器，也很难在文本层察觉。
- 不要把 UKPA 等同于 TextFooler 一类的同义替换攻击。TP 改的是"任意词"，UKPA 改的是"承担跨 chunk 实体连接的词"，前者对图谱几乎无影响。

## References

- 攻击动机、流水线四步与代理评分函数均见论文 §"Universal Knowledge Poisoning Attack"（`data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt`，第 475–551 行）。
- 拓扑退化数字见 Table~\ref{tab:graybox_structure}（L641–662）；QA 准确率见 Table~\ref{tab:ukpa_qa_accuracy}（L667–687）；修改词量见 Table~\ref{tab:Words_modification}（L769–789）。

## Footnotes

- L478–489：UKPA 关键观察——"GraphRAG depends heavily on linguistic coherence cues, particularly coreference chains"。
- L531–541：代理评分函数 $\mathcal{I}_\mathrm{score}$ 与默认 $(\alpha,\beta,\gamma)=(0.25,0.25,0.5)$。
- L651–657：节点保留率、边保留率、Jaccard 数字。
- L673–687：QA 准确率 95→50、90→45 与 TP 基线 85。
