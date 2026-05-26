---
id: tkpa-graph-guided-targeted-poisoning
title: TKPA：用图论结构定位"该改哪一段"的定向投毒
status: draft
card_type: mechanism
tags: [#graphrag, #security, #poisoning, #targeted-attack]
created_time: 2026-05-26T11:05:00+08:00
edited_time: 2026-05-26T11:05:00+08:00
edited_entity: llm
source_ids: [arxiv-graph-poisoning]
provenance_card: ../provenance/tkpa-graph-guided-targeted-poisoning.md
aliases: ["Targeted Knowledge Poisoning Attack", "定向知识投毒"]
related: [graphrag-manipulation-only-attack-surface]
---

TKPA（Targeted Knowledge Poisoning Attack）的核心立场是：要让 GraphRAG 对**特定查询**给出攻击者想要的答案，最有效的不是在文本层随机改字，而是**先在图域定位最脆弱的小邻域，再把改动反映射回原文**。它把投毒抽象为"网络干预"问题，整个流水线四步：

1. **脆弱社区定位 (VCL)**——攻击者先用 LLM 抽出查询的 target entity，再为每个包含它的社区算脆弱度  
   $$\mathcal{V}_\mathrm{score} = \frac{(1+D_e)(1+C_e)}{\log(1+\mathrm{TLen})}$$  
   分子用度 $D_e$ 与介数中心性 $C_e$ 衡量目标实体在该社区里的结构杠杆；分母用社区摘要长度 $\mathrm{TLen}$ 惩罚"要改太多字"的社区。最高分社区即入口。
2. **Ego-子图抽取**——在选中的社区里，只保留 target 节点的一跳邻居及它们之间的边，得到 $G_\mathrm{ego}(v_t)$。后续候选 chunk 全部限定在与该子图相关的文本，从而避免在远端浪费改动。
3. **Chunk 评分与选择**——对每个候选 chunk 计算  
   $$\mathcal{C}_\mathrm{score} = w_1 S_\mathrm{graph} + w_2 S_\mathrm{semantic} + w_3 S_\mathrm{attitude}$$  
   其中 $S_\mathrm{graph}$ 是该 chunk 对应实体在 $G_\mathrm{ego}$ 上的 PageRank，$S_\mathrm{semantic}$ 是 chunk 与 query 的 cosine 相似度，$S_\mathrm{attitude}$ 是 chunk 的情感倾向。默认权重 $(0.5,0.3,0.2)$ 把"图结构"放在首位。
4. **LLM 改写**——把 top-k chunk 交给 LLM 在保留语体、流畅度的前提下重写为符合攻击者意图的版本，写回语料。下一次 GraphRAG 重建图谱时，毒化叙述就被吸收进社区摘要里。

为什么这套设计有效，可以用三组实测数字概括：

- 默认权重 ASR 91.2%，相比"等权"基线 89.8% 提升不多，但相比"只用 graph / 只用 semantic / 只用 attitude"分别为 65.3% / 58.2% / 51.7%，说明**三种信号必须组合**，而结构信号要被显式优先。
- top-k 收益高度边际递减：$k=1$ 时 ASR 55.8%，$k=2$ 时 81.3%，$k=3$ 时 91.2%；之后曲线平台化。这是 TKPA "改极少字 + 精确定位"的关键依据。
- 在 *The Little Prince* 数据集，TKPA 改了 48/94,496 词（0.055%），ASR 即达 93.10%，QASD 0.85，均显著优于 PoisonedRAG（71.50% / 0.68）与 Naive Swap（18.20% / 0.15）。

边界与误读：

- TKPA 默认攻击者具备"理解 GraphRAG 会把抽取知识组织成社区"的中等领域知识；不需要看到具体图，但需要图论工具走前 3 步。
- $w_3$（情感）默认最小，是因为图结构本身已经定位了"会被读到的段落"；过度依赖情感会落回 Naive Swap 的等级。
- 不要把 TKPA 当成通用降级工具——它只对**单一查询**起作用。要广泛拖垮系统应当用 UKPA。

## References

- 攻击建模、四模块算法、vulnerability score 公式与 PageRank 选片均见论文 §"Targeted Knowledge Poisoning Attack"（`data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt`，第 321–471 行）。
- ASR / QASD 对照表与 ablation 数字见 Table~\ref{tab:whitebox_performance_revised} 与 §"Ablation Study"（同文件 L613–638、L793–798）。

## Footnotes

- L335–343：脆弱度公式 $\mathcal{V}_\mathrm{score}$ 的定义与"influence maximization per unit edit cost"的解读。
- L374–388：chunk 评分函数三项含义与默认权重 $(0.5,0.3,0.2)$。
- L620–633：TKPA / PRAG / NS 在 LP / FC08 / JAPB 三数据集上的 ASR、QASD 对照。
- L794–798：weight ablation 与 top-k ablation 数字（55.8 → 81.3 → 91.2）。
