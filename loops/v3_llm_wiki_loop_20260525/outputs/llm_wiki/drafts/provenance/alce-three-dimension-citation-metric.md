---
schema: draft_card_provenance.v3
draft_card: ../cards/alce-three-dimension-citation-metric.md
material_id: arxiv-alce
digest_id: digest_arxiv-alce
source_paths:
  - data/raw/arxiv/arxiv-alce/agent_source_bundle.txt
created_time: 2026-05-26T11:15:00+08:00
edited_time: 2026-05-26T11:15:00+08:00
edited_entity: llm
---

## 源证据

- `sections/evaluation.tex` L820-826：三维度定义。
- `sections/evaluation.tex` L833-841：MAUVE 用法和"仅做 sanity check"的说明，QAMPARI 跳过 MAUVE。
- `sections/evaluation.tex` L861-878：ASQA/QAMPARI/ELI5 各自 correctness 口径，sub-claim 由 InstructGPT 生成 + TRUE NLI 判 entailment。
- `sections/evaluation.tex` L897-920：citation recall / citation precision 用 NLI 判官，AIS 框架溯源。
- `sections/evaluation.tex` L975-979：作弊路径会被三维度互相牵制抓出来。
- `sections/appendix.tex` L307-310：MAUVE 在 ELI5 上截断 100 词。
- `sections/appendix.tex` L483-486：自动评估准确率 85.1% / 77.6%。
- `emnlp2023.tex` L106-114（Limitations）：MAUVE 不稳、NLI 无法识别部分支撑、覆盖范围限制。

## 卡片范围是否成立

卡片范围是"ALCE 评分由哪三个维度组成 + 为什么是三个"。所有主张直接来自论文：

- 三维度定义、MAUVE 用法、correctness 三套口径 → 直接对应论文 `evaluation.tex`。
- 作弊路径与三维度互锁机制 → 直接来自 robust to shortcut cases 章节。
- 自动评估准确率与 NLI 部分支撑局限 → 来自附录 + Limitations。

不在本卡：citation recall/precision 的精确定义留给姊妹卡 `alce-citation-recall-precision-nli`；prompting 路径留给 `alce-prompting-strategies`；3 数据集任务结构留给 `alce-three-evaluation-datasets`。

## 发表门控结果

本轮未运行。

## 备注

- v2 可能已有"带引用的 LLM 评估"主题；本卡的差别在于把三维度互锁这一机制讲透，而不是给具体 baseline 排名。
