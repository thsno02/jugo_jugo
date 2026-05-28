---
id: alce-citation-recall-precision-nli
title: ALCE 用 NLI 模型把 citation recall / precision 算成可重复的二元判定
status: accepted
card_type: operational_rule
tags: [#citation, #alce, #nli, #evaluation, #ais]
created_time: 2026-05-26T11:20:00+08:00
edited_time: 2026-05-28T15:00:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
provenance_card: ../provenance/alce-citation-recall-precision-nli.md
aliases: ["AIS-style citation evaluation", "ALCE citation 二元判定"]
related: [alce-three-dimension-citation-metric, ragas-faithfulness-metric, ragchecker-claim-entailment-decomposition]
---

ALCE 的"citation quality"得分[^v3-1]不是模糊打分，而是两个严格的二元判定，全部由 TRUE（一个在 SNLI/MNLI/Fever/Scitail/PAWS/VitaminC 上 fine-tune 的 T5-11B NLI 模型）执行[^src3]。规则化的定义如下，其中 $\phi(\text{premise}, \text{hypothesis})=1$ 当且仅当 premise 蕴含 hypothesis：

**Citation recall（每条语句 $s_i$ 给 0/1）：**

$$\text{recall}(s_i)=1 \Leftrightarrow \mathcal{C}_i \neq \emptyset \;\wedge\; \phi(\text{concat}(\mathcal{C}_i),\, s_i)=1$$

即：必须至少有一个引用，并且**所有引用拼起来作为单一 premise** 能蕴含语句。整体得分对所有语句求平均。这对应 Rashkin 2021 的 AIS（Attributable to Identified Sources）框架[^src1]。

**Citation precision（每条引用 $c_{i,j}$ 给 0/1）：**

先定义"irrelevant"：$c_{i,j}$ irrelevant 当且仅当
1. $\phi(c_{i,j}, s_i)=0$（这条引用单独无法支撑语句），且
2. $\phi(\text{concat}(\mathcal{C}_i \setminus \{c_{i,j}\}), s_i)=1$（去掉它之后其它引用仍能支撑语句）。

然后：$c_{i,j}$ 的 precision=1 当且仅当 $s_i$ 的 recall=1 且 $c_{i,j}$ 不是 irrelevant。整体得分对所有引用求平均[^src2]。

操作含义 / 用法约束：

- **citation 拼接方式**：每个 passage 用 `"Title: {TITLE}\n{TEXT}"` 格式化，多个 passage 用 `\n` 拼接后整体喂给 NLI。这是 ALCE 输出 citation 分数的标准约定，复现实验时不能换格式[^src3]。
- **citation 数量上限**：实践上每条语句最多 3 个引用——更多并不能进一步提升被支撑率[^src4]。
- **precision 评估必须先有 recall=1**：这是 condition (b) 成立的前提；否则会把"语句根本不被任何子集支撑"的情况错当成"某引用是 redundant"。
- **不强制 minimum citation set**：评估容许 redundant 引用，因为人类写作里多冗余引用是增强可信度的合法手段。

反例 / 已知失败模式：

- **partial support 问题**：如果 $c_{i,j}$ 只部分支撑 $s_i$、剩余部分被 $c_{i,4}, c_{i,5}$ 也覆盖，按上述定义 $c_{i,j}$ 被误判为 irrelevant。这是 NLI 模型不能区分 fully / partially support 的直接后果。论文显式说明这条 false positive，并在 `app_sec:citation_recall` 留作未来工作[^src6]。
- 实际人工检验里，ALCE 在"识别 irrelevant 引用"上 recall=75.6% / precision=66.1%，因此粗算时 precision 偏低、citation 系统会被低估。
- 实测 Cohen's κ vs 人工：recall 0.698（substantial），precision 0.525（moderate）。这是 ALCE 自动分能直接当人类判断用的上限范围[^src5]。

这种"先拆原子断言、再用 NLI 验证蕴含"的范式并不为 ALCE 独有：Ragas 的 faithfulness[^v3-2]与 RAGChecker 的 claim entailment[^v3-3]走的是同一条路线，只不过把判官换成了 LLM-as-judge 或 Llama3-70B；ALCE 选 NLI 是为了让 citation 评分**在固定 T5-11B 上完全可重复**。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` — `sections/evaluation.tex` "Citation Quality"（L897–965，关键定义在 L926–938） — citation recall/precision 形式化定义与 AIS（Rashkin 2021）框架对齐。
[^src2]: 同文件 L946-963 — irrelevant 的双条件定义和"recall=1 是 precision=1 的前提"。
[^src3]: 同文件 `sections/appendix.tex` "Implementation Details / NLI model"（L291–303，关键 L292–302） — TRUE NLI 模型来自 `google/t5_xxl_true_nli_mixture`，passage 拼接格式 `"Title: {TITLE}\n{TEXT}"`。
[^src4]: 同文件 L739（task 设置） — `"In practice, we allow at most 3 citations for each statement as more citations usually do not help."`
[^src5]: 同文件 `sections/human_eval.tex` L1030–1037（关键 L1036-1037） — Cohen κ recall=0.698 / precision=0.525。
[^src6]: 同文件 `sections/appendix.tex` "Citation Recall Discussion"（L354–371）以及 `emnlp2023.tex` Limitations（L106–110） — partial support 局限。
[^v3-1]: [alce-three-dimension-citation-metric](alce-three-dimension-citation-metric.md) — 本卡描述的 citation recall / precision 是 ALCE 三维度评估中"citation quality"那一维的内部机制。
[^v3-2]: [ragas-faithfulness-metric](ragas-faithfulness-metric.md) — 同样是先拆原子断言再做蕴含判定，但 judge 用的是 LLM-as-judge 而非固定 NLI 模型。
[^v3-3]: [ragchecker-claim-entailment-decomposition](ragchecker-claim-entailment-decomposition.md) — 同一类 claim + entailment 范式，extractor / checker 都换成 Llama3-70B（RefChecker 框架）。
