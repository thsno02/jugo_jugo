---
id: ares-ppi-confidence-bound
title: ARES 用 PPI 把小标注集放大成带置信区间的 RAG 排名
status: accepted
card_type: mechanism
tags: [#rag, #ares, #ppi, #statistical-inference, #evaluation]
created_time: 2026-05-26T11:10:00+08:00
edited_time: 2026-05-28T15:25:00+08:00
edited_entity: llm
source_ids: [arxiv-ares]
provenance_card: ../provenance/ares-ppi-confidence-bound.md
aliases: ["prediction-powered inference for RAG", "ARES rectifier function"]
related: [ares-three-judge-rag-evaluation, ares-synthetic-data-pipeline, ares-cross-domain-generalization-limits, ares-gpt4-vs-human-annotation-tradeoff]
---

ARES[^v3-1]报告的"RAG 得分"既不是 LLM 判官的原始平均预测，也不是把 150 条人工标注当 ground truth 拍出来的平均值。它是用 prediction-powered inference（PPI[^url1]）把这两件事缝起来：让小的 human preference validation set（150–300 条）给 LLM 判官在更大未标注集上的预测做一次"rectifier"校准，最终输出一个 95% 置信区间[^src1]。

PPI 的作用拆解：

- **没有 PPI 的纯判官**：在大未标注集上跑判官，取平均。问题是判官本身有错，平均值可能系统性偏移。
- **没有 PPI 的纯人工**：只用 150 条标注算每个被评 RAG 的得分。问题是样本太小，置信区间宽，且换一个 RAG 就要重标。
- **PPI 的折中**：用 LLM 判官在 human preference 验证集上跑一遍，学一个 rectifier function，估计判官的偏置[^src2]；再把这个 rectifier 应用到大未标注集上的判官预测，得到比"只用 150 条人工标注"更紧、且比"只用判官预测"更可靠的置信区间。

操作含义：

- **校准集复用**：同一份 human preference validation set 既用于早停判官 fine-tune[^v3-2]，又用于 PPI rectifier，再用于估置信区间。这是 ARES 把 150–300 条标注预算压到极致的根本原因。
- **排名用置信区间的中点**：当评多个 RAG 系统时，取每个 RAG 的 C.R. / A.F. / A.R. 置信区间的中点作为最终排序键[^src3]。
- **校准集大小阈值**：表 `tab:ppi_count` 给出经验下界——大约 100–150 条以下，PPI 已经不足以稳定区分相邻 RAG 系统。例如 NQ context relevance 在 25 条标注时 Kendall's τ 只有 0.44，到 300 条才达到 0.89[^src4]。
- **真实 RAG 上的置信宽度**：在 NQ/WoW/FEVER 实测中，PPI 置信区间平均宽度为 C.R. 7.4 个百分点 / A.R. 6.1 个百分点，并且 >95% 的时候真值都落在区间内[^src5]。

边界 / 反例：

- PPI 不能修正"判官预测系统性偏移**远超**校准集能反映的偏置"的情况。跨语言 / 文本→代码这类剧烈领域迁移时，即使打开 PPI，τ 也只剩 0.28–0.38[^v3-3]。
- PPI 收紧置信区间的代价是"判官 + 校准集"必须在同一分布上；换分布就要重新标注新的 human preference set。
- 用 GPT-4 生成 labels 替代 human preference set 时，PPI 仍能收紧区间，但 τ 在多数设定下降 0.05–0.30[^v3-4]——校准信号的质量是 PPI 紧度的硬约束。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` `methods.tex` "Ranking RAG Systems with Confidence Intervals" L744–765（关键 L753） — `"PPI is a recent statistical method that provides tighter confidence intervals on a small set of annotated datapoints (i.e., our validation set) by leveraging predictions on a much larger set of non-annotated datapoints."`
[^src2]: 同文件 L756 — `"PPI uses the LLM judges on the human preference validation set to learn a rectifier function for constructing a confidence set of the ML model's performance"`。
[^src3]: 同文件 L763 — `"With our ranking, we can compare different RAG systems ... we find the midpoint of each confidence interval and use the midpoints to rank the RAG systems."`
[^src4]: 同文件 `Tables/ppi_comparison_table.tex` L189–199 — PPI 校准集大小消融，NQ C.R. 在 25 条 τ=0.44，300 条 τ=0.89。
[^src5]: 同文件 `results.tex` "ARES Ranking of Existing RAG Systems" L873–876（关键 L875） — `"the PPI confidence intervals were 7.4 points wide for context relevance and 6.1 points wide for answer relevance"`。
[^url1]: <https://arxiv.org/abs/2301.09633> — Angelopoulos et al. 2023, "Prediction-Powered Inference"，ARES 在 `introduction.tex` L625 与 `methods.tex` L753 都引用该方法溯源。
[^v3-1]: [ares-three-judge-rag-evaluation](ares-three-judge-rag-evaluation.md) — ARES 的三个独立判官（C.R. / A.F. / A.R.）都通过 PPI 输出置信区间。
[^v3-2]: [ares-synthetic-data-pipeline](ares-synthetic-data-pipeline.md) — 同一份 human preference 验证集既用于 PPI 也用于判官 fine-tune 的早停。
[^v3-3]: [ares-cross-domain-generalization-limits](ares-cross-domain-generalization-limits.md) — 跨语言 / 文本→代码 / 抽取任务时 τ 跌到 0.28–0.38 的具体实测。
[^v3-4]: [ares-gpt4-vs-human-annotation-tradeoff](ares-gpt4-vs-human-annotation-tradeoff.md) — GPT-4 labels 替代 human preference set 时，PPI 仍能改善但 τ 下降 0.05–0.30 的成本曲线。
