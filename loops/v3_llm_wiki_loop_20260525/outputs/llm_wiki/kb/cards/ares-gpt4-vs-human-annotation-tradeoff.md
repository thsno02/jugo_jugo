---
id: ares-gpt4-vs-human-annotation-tradeoff
title: GPT-4 标注替代 human preference set：ARES 的 τ 退化 0.05–0.30 的成本
status: accepted
card_type: source_claim
tags: [#rag, #ares, #gpt4-labels, #annotation-cost, #ppi]
created_time: 2026-05-26T15:30:00+08:00
edited_time: 2026-05-27T14:20:00+08:00
edited_entity: llm
source_ids: [arxiv-ares]
provenance_card: ../provenance/ares-gpt4-vs-human-annotation-tradeoff.md
aliases: [ARES GPT-4 labels, annotation cost reduction, few-shot label generation]
related: [ares-synthetic-data-pipeline, ares-ppi-confidence-bound, ares-three-judge-rag-evaluation, wicer-llm-judge-human-validation, ragas-reference-free-rag-evaluation]
---

## 主张

Saad-Falcon 等（2024）做了一组消融：把 ARES 里需要的 human preference validation set（150–300 条人工标注）**完全用 GPT-4 标注替代**——使用 few-shot prompt 生成 500 条 GPT-4 labels。结果：Kendall's τ 在大多数设定下下降 **0.05–0.30**，**但人工标注成本从"几百条"降到"少于 10 条 few-shot 样本"**——这是 ARES 实际部署时一个有意义的成本/精度权衡。

## 数字对照（Table tab:gpt4_labels）

| 数据集 | 标注源 | C.R. τ | A.R. τ | PPI Range | Eval Accuracy |
| --- | --- | --- | --- | --- | --- |
| NQ | Human | 0.94 | 1.0 | — | — |
| NQ | GPT-4 | 0.78 | 1.0 | 9.2% / 6.8% | 79.3% / 96.7% |
| ReCoRD | Human | 0.83 | 0.89 | — | — |
| ReCoRD | GPT-4 | 0.78 | 0.72 | 8.2% / 9.0% | 88.4% / 78.3% |
| MultiRC | Human | 0.94 | 0.89 | — | — |
| MultiRC | GPT-4 | 0.89 | 0.78 | 7.7% / 8.3% | 85.8% / 82.5% |

**A.R. on ReCoRD 跌得最厉害（−0.17）**——这正好与 `ares-cross-domain-generalization-limits` 卡里"NQ→ReCoRD 已经是较硬的迁移"对应：在判官本就难做的设定上，GPT-4 标注的偏差被放大。

## 两个关键观察

1. **PPI 的 efficacy 随更多 GPT-4 labels 持续改善**——论文显式说"the efficacy of PPI continues improving as we generate more GPT-4 generated labels"，意味着这个权衡不是 binary，可以渐进调节：用 100 条 GPT-4 label 试水、不够再加。
2. **A.R. on NQ 没掉**（Human 1.0 vs GPT-4 1.0）——说明在"判官本身就训得好 + 数据集结构简单"的设定下，GPT-4 label 完全可用。GPT-4 标注的缺点是**集中在判官本就不稳定的设定上**。

## 操作含义（给"想省标注"的实践者）

- **生产环境下可用 GPT-4 labels 启动**：先用 100 条 GPT-4 label 跑 ARES，得到 baseline τ；若 τ 已经 ≥ 0.9 即可上线；若 < 0.85，补人工标注。
- **不要假设 GPT-4 标注总比 human 差几个百分点**：在 A.R. 简单设定下二者持平（NQ A.R. τ = 1.0 = 1.0）；在难设定上 GPT-4 可能差 17 个百分点。差距是 task-dependent，不是 uniform offset。
- **混合策略最优**：用 GPT-4 标注做粗筛 + few-shot 校正 + 用人工标注校验**判官最不确定的样本**。论文未实现这个混合，但消融数据支持这个方向。

## 边界与诚实

- 论文用的是 GPT-4（2023）的 few-shot 标注；GPT-4 后续版本 / GPT-5.2 等可能给出不同 quality。
- 0.05–0.30 区间是**少数大数据集的观察**（NQ / ReCoRD / MultiRC 三个），不能保证在其它领域同样适用。
- "成本 dropped from hundreds of annotations to less than ten for few-shot prompts"——说的是 **few-shot prompt 设计成本**降低，而**实际生成的 GPT-4 label 数**仍是 500 条。这两个成本不能混为一谈：前者是人时，后者是 API 钱。

## References

- §Cross-Domain / Mock-RAG Tables 中 GPT-4 labels 实验：`data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` 第 104–130 行（GPT4_Labeling.tex）。
- Table tab:gpt4_labels 数字：第 117–122 行。
- 论文 §Results 中关于此消融的简述：第 829–830 行。
- §Conclusion 中把这条作为"avenues to explore"之一：第 590–593 行。

## Footnotes

[^1]: 实验设计原文（第 124–129 行）：
    > "We wanted to explore the practicality of using GPT-4 generated labels instead of human annotations for our human preference validation set in ARES. In the experiments, we generated 500 GPT-4 labels as replacements for human labeling using few-shot prompts. While GPT-4 generated labels decreased Kendall's tau in most settings by 0.05 to 0.30, the ability to cheaply produce GPT-4 generated labels significantly reduces the cost of annotation, cutting it from hundreds of annotations to less than ten for few-shot prompts."

[^2]: PPI 持续改善原文（第 127–128 行）：
    > "Additionally, the efficacy of PPI continues improving as we generate more GPT-4 generated labels."

[^3]: §Results 引用此消融（第 829–830 行）：
    > "we explored whether GPT-4 generations could replace human annotations entirely, finding that GPT-4 is less good than humans in this role, though the idea arguably has promise."
