---
id: ukpa-edit-distance-stealth-tradeoff
title: UKPA 的"编辑距离 ≤3"甜点：再大就只涨困惑度、不涨攻击力
status: accepted
card_type: source_claim
tags: [#graphrag, #security, #ablation, #ukpa]
created_time: 2026-05-26T11:44:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
edited_entity: llm
source_ids: [arxiv-graph-poisoning]
provenance_card: ../provenance/ukpa-edit-distance-stealth-tradeoff.md
aliases: ["UKPA edit distance ablation", "small-edit sweet spot"]
related: [ukpa-coreference-disruption, graphrag-text-defense-blind-spot, tkpa-graph-guided-targeted-poisoning, gragpoison-additive-vs-edit-attack, graphrag-manipulation-only-attack-surface]
---

UKPA 在生成扰动候选时硬性约束了"编辑距离要小"。Wen 等人做了一项 ablation 验证这个约束的具体取值：把允许的编辑距离上限 $d_{\text{edit}}$ 设到 1、3、5，分别观察攻击效果与文本异常度。结论可以一句话概括——**$d_{\text{edit}} \leq 3$ 已经把 QA 从 0.95 打到 0.50，再放大到 $\leq 5$ 攻击力几乎不再涨，但 perplexity 显著升高，把隐蔽性丢掉**。

这给出了一条具体的"攻击效率 sweet spot"：

- $d_{\text{edit}} = 1$（只允许换 1 个 token / 词）：扰动空间太窄，找不到能同时破坏共指又不太背离原意的候选；攻击力大幅下降。
- $d_{\text{edit}} \leq 3$（论文默认）：刚好覆盖典型的"代词换名词短语 / 加歧义指代 / 微调短语序"等共指破坏手段，QA 0.50（MS GraphRAG）/ 0.45（LightRAG）。
- $d_{\text{edit}} \leq 5$：候选空间变大，UKPA 偶尔选到改动更大的句子，**perplexity 涨幅明显**但 entity-relation 局部破坏没多大额外收益——攻击 ROI 反而变差。

为什么会这样？UKPA 的目标信号是"共指失败"，而共指模型对**少数关键词**（代词、定指 NP、专名形式）特别敏感；这些信号都能在 1–3 个 token 的改动内被打掉。再多的编辑等于在改"和共指无关"的词，对图破坏没贡献，但每多改一个词都会让"原文 vs 改写"的语言模型分布偏离原始领域。perplexity 与编辑距离正相关，攻击力却饱和——所以增大 $d_{\text{edit}}$ 是纯亏。

操作含义：

- 这条 ablation 解释了为什么 UKPA 在 Table 4 里只动 0.033–0.045% 的词就能让 QA 腰斩——它在每个被选中的 chunk 内**也**只动 1–3 个 token。"修改总量小"与"每处修改小"是同一原则的两个尺度。
- 对防御侧，这给出了一个微弱但具体的检测线索：**对 trusted snapshot 做 token-level diff，若改动落在代词/指代上但语义相近，应警惕**。可惜既有的文本层防御没有专门检测共指 token 的能力。
- 对攻击者复现这套攻击的"超参选择"：默认 $d_{\text{edit}}=3$、$(\alpha, \beta, \gamma)=(0.25, 0.25, 0.5)$ 是论文给的工程默认；改大不会让攻击更强，只会让攻击更可疑。

边界与误读：

- 编辑距离的度量在论文未给出严格定义（character-level 还是 token-level 没明说，但从其他章节的"修改词数"统计推断更接近 token-level）。
- "$\leq 5$ 攻击力不再涨"是在 RUW + Microsoft GraphRAG / LightRAG 两个数据集上的观察；不能保证所有领域都呈现完全相同的饱和曲线，但相同模型上的两数据集都同向，可作为强经验。
- 这条结论**只适用于 UKPA**。TKPA 的等价 ablation 是"top-k 改写多少个 chunk"——论文显示 $k=3$ 时 ASR 已达 91.2%、再增大也平台化（见 TKPA 卡）。

## References

- 编辑距离 ablation 的描述与"$\leq 3$ 已打到 0.50 / 更大只升 PPL"的判断见 §"Ablation Study of UKPA's Parameters" 与对应配图（`data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` 第 807–820 行；图 `edit_distance_plot.png` 编号为 `fig:edit_distance_plot`）。
- 默认权重 $(\alpha,\beta,\gamma)=(0.25,0.25,0.5)$ 与该约束的关联见同论文 §"Models \& Parameters"（同文件 L570–577）。

## Footnotes

- L817–820：*"while small edits (distance $\leq 3$) already cause a drastic drop in QA accuracy (from 0.95 to 0.50), larger edits increase perplexity significantly without further improving attack impact. This results justifies the constraint on small edit distances to ensure stealthiness."*
- L815–816：等权 vs 默认权重的 QA 数字（0.55 vs 0.50），与本卡的"sweet spot"互证——结构破坏与语义保留必须并重。
- L576–577：默认 $(\alpha,\beta,\gamma)=(0.25,0.25,0.5)$，γ=0.5 即明显偏向"语义接近度"以维持小编辑。
