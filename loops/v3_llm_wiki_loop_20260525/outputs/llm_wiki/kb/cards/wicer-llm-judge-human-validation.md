---
id: wicer-llm-judge-human-validation
title: WiCER 的 LLM-as-judge 与人评 Pearson r=0.94 的 n=100 验证
status: accepted
card_type: source_claim
tags: [#llm-as-judge, #evaluation, #methodology, #human-validation, #wicer]
created_time: 2026-05-26T15:00:00+08:00
edited_time: 2026-05-28T11:50:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
provenance_card: ../provenance/wicer-llm-judge-human-validation.md
aliases: [WiCER human validation, LLM judge human agreement, Claude Sonnet judge calibration]
related: [wicer-cegar-compile-evaluate-refine, wicer-recovery-distribution-exceeds-fc-raw, ares-gpt4-vs-human-annotation-tradeoff, ragas-reference-free-rag-evaluation, graphrag-adaptive-benchmark-via-personas, ares-three-judge-rag-evaluation]
---

## 主张

WiCER 的所有质量数字都依赖 Claude Sonnet 做 1–5 分 LLM-as-judge。论文 Appendix F 用一份 100 条分层样本（覆盖 FC raw / RAG / Wiki blind / WiCER iter 1 / WiCER iter 2 五种条件）做了独立人评校准：**Pearson r = 0.94、Spearman ρ = 0.928、Kendall τ = 0.873、75% 完全一致、99% 在 ±1 分范围内、MAE = 0.26、判官系统偏置 +0.06（LLM 略高于人）**。

## 三项验证细节

1. **跨条件不掉**：每个条件 per-condition Pearson r ≥ 0.89，平均偏差 |Δmean| ≤ 0.17。
2. **唯一 >1 分歧的 case**：RAG 输出，judge 给 4、人给 2；人工复查确认回答漏掉关键细节，是 judge 偏宽松——不是 random noise，而是"judge 容忍部分缺失"的可识别偏置。
3. **样本分布**：n=100 是分层样本，覆盖最低质量（Wiki blind, n=31）和最高质量（FC raw, n=30）—— **不是只测了 wiki blind 这种 low-variance 区域**。

## 与论文一项 limitation 的张力

§7.3 NeurIPS checklist "Experiment statistical significance" 项写答 No——论文不报告任何置信区间或显著性测试，理由是"贪婪解码 T=0，within-topic 方差为零"。Appendix F 的 r=0.94 不是 confidence interval，而是 judge–human agreement 的点估计；论文承认 n=100 的 human evaluation 覆盖了"core claims"但样本量小。因此**这条 r=0.94 是"judge 不离谱"的可信门槛，但不是"WiCER 收益是统计显著"的证据**——这两件事在论文里分别处理。

## 操作含义（给 RAG / wiki 评测）

- **n=100 是 LLM judge 校准的可参考下界**：能稳得到 r > 0.9 的相关性，但单条最大分歧仍可能超 1 分；
- **分层覆盖优于纯随机**：包含极端条件（catastrophic failure 与 best-case）能让 judge bias 在边缘暴露；
- **bias 不一定致命**：+0.06 系统偏移在相对排名（ranking）任务里几乎无影响——这正是 ARES / WiCER 这类工作用 LLM-as-judge 做 ranking 比做 absolute scoring 更稳的原因。

## 边界

- 只校准了 Claude Sonnet 一个 judge；换 GPT-5 / Gemini 不能直接复用 r=0.94；
- 100 条总样本里 WiCER iter 1 仅 n=6、iter 2 仅 n=3——**对 WiCER 特定条件**的 judge 校准强度其实有限，r=0.937/1.000 主要是少样本下的点估计；
- 论文未做 inter-rater reliability（只有一个人评者），所以"r=0.94 vs human"实际等同于"r=0.94 vs 一个 domain expert"。

## References

- §F "Human Evaluation Validation"：`data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` 第 1446–1503 行。
- Table tab:human_corr（全表数字）：第 1454–1473 行。
- Table tab:human_cond（per-condition agreement）：第 1480–1495 行。
- 唯一 >1 分歧案例：第 1497–1502 行。

## Footnotes

[^1]: Table tab:human_corr 原文（第 1463–1473 行）：
    > "Pearson r 0.940 / Spearman ρ 0.928 (p < 10^-43) / Kendall τ 0.873 (p < 10^-25) / Exact agreement 75/100 (75.0%) / Within 1 point 99/100 (99.0%) / Mean absolute error 0.26 / Bias (LLM − Human) +0.06"

[^2]: 跨条件稳定性原文（第 1474–1478 行）：
    > "The judge is well-calibrated across all conditions, with per-condition Pearson r ≥ 0.89 and negligible bias (|Δmean| ≤ 0.17)."

[^3]: 唯一 >1 分歧 case 原文（第 1497–1502 行）：
    > "The single sample with >1 point disagreement was a RAG response scored 4 by the judge and 2 by the human rater; manual inspection confirmed the response omitted a key detail that the human considered essential."
