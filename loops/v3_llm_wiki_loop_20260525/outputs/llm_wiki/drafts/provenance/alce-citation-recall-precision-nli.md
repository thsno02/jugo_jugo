---
schema: draft_card_provenance.v3
draft_card: ../cards/alce-citation-recall-precision-nli.md
material_id: arxiv-alce
digest_id: digest_arxiv-alce
source_paths:
  - data/raw/arxiv/arxiv-alce/agent_source_bundle.txt
created_time: 2026-05-26T11:20:00+08:00
edited_time: 2026-05-26T11:20:00+08:00
edited_entity: llm
---

## 源证据

- `sections/evaluation.tex` L926-938：citation recall 的形式化定义，"$\phi(\text{concat}(\mathcal{C}_i), s_i)=1$ implies that $s_i$ is true based solely on $\text{concat}(\mathcal{C}_i)$"，AIS 框架溯源 Rashkin 2021。
- `sections/evaluation.tex` L946-965：citation precision 的双条件 irrelevant 判定 + "we set recall=1 as a prerequisite for precision=1"。
- `sections/evaluation.tex` L955-961：irrelevant 的两条形式化条件 (a) 和 (b)。
- `sections/appendix.tex` L292-302：TRUE NLI 模型路径 + 拼接格式。
- `sections/evaluation.tex` 任务定义 L732-739：每条语句最多 3 个引用的实践约束。
- `sections/appendix.tex` L354-371：partial support 局限与 Liu 2023 三档评估的对比。
- `emnlp2023.tex` L106-110：Limitations 中"NLI 不能识别 partial support"的承认。
- `sections/human_eval.tex` L1036-1037：Cohen κ recall=0.698 / precision=0.525。
- `sections/appendix.tex` L484-486：识别 irrelevant 引用的 recall/precision 数字。

## 卡片范围是否成立

卡片范围是 ALCE citation 评估的**精确算子**——这是一个 operational rule，需要保留公式与边界条件原样，所以单独成卡是合理的。三维度总览卡只点到"citation quality 由 NLI 判"，没有给出公式。

未做的引申：

- 没有把 partial support 的解决方案推广到训练数据收集（论文显式说留给未来）。
- 没有把 NLI 的精度上限当作系统排名能力上限的推论（这是来自 `human_eval.tex` 的直接量化，不是引申）。

## 发表门控结果

本轮未运行。

## 备注

- 若 v2 已有"citation 评估通用规则"卡片，本卡的区分点：本卡只覆盖 ALCE 的精确算子（包括拼接、NLI 模型、minimal-set 不强制），不讨论其它系统。
