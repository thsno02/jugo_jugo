---
schema: draft_card_provenance.v3
draft_card: ../cards/ares-gpt4-vs-human-annotation-tradeoff.md
material_id: arxiv-ares
digest_id: digest_arxiv-ares
source_paths:
  - data/raw/arxiv/arxiv-ares/agent_source_bundle.txt
created_time: 2026-05-26T15:30:00+08:00
edited_time: 2026-05-26T15:30:00+08:00
edited_entity: llm
---

## 源证据

### Table tab:gpt4_labels 数字（第 117–122 行）

```
                        NQ           ReCoRD       MultiRC
                        C.R.   A.R.  C.R.   A.R.  C.R.   A.R.
Kendall's Tau           0.78   1.0   0.78   0.72  0.89   0.78
Human Labeled Approach  0.94   1.0   0.83   0.89  0.94   0.89
Average PPI Range       9.2%   6.8%  8.2%   9.0%  7.7%   8.3%
Accuracy on Eval Sets   79.3%  96.7% 88.4%  78.3% 85.8%  82.5%
```

### Table caption / 设计意图（第 124–129 行）

> "We wanted to explore the practicality of using GPT-4 generated labels instead of human annotations for our human preference validation set in ARES. In the experiments, we generated 500 GPT-4 labels as replacements for human labeling using few-shot prompts (see Sections gpt_prompting_for_context_relevance_scoring, gpt_prompting_for_answer_faithfulness_scoring, and gpt_prompting_for_answer_relevance_scoring). While GPT-4 generated labels decreased Kendall's tau in most settings by 0.05 to 0.30, the ability to cheaply produce GPT-4 generated labels significantly reduces the cost of annotation, cutting it from hundreds of annotations to less than ten for few-shot prompts. Additionally, the efficacy of PPI continues improving as we generate more GPT-4 generated labels."

### §Results 简述（第 829–830 行）

> "We also wanted to better understand the importance of human annotations for ARES. To this end, we conducted two sets of experiments. First, we used ARES with human annotation sets ranging in size from 25 to 400 and found that 150 is the minimum number required (Table ppi_count). Second, we explored whether GPT-4 generations could replace human annotations entirely, finding that GPT-4 is less good than humans in this role, though the idea arguably has promise."

### §Conclusion 中作为未来方向（第 590–593 行）

> "ARES is a flexible framework, and there may be variants of it that are even more powerful than the ones we explored here. Avenues to explore include GPT-4 as a replacement for human labeling (Table tab:gpt4_labels), more robust techniques for the synthetic datasets used in fine-tuning LLM judges, utilizing logits in LLM judge prediction to improve PPI confidence intervals, and testing more sophisticated LLMs as fine-tuned judges for ARES."

## 卡片范围是否成立

本卡聚焦 GPT-4 标注消融。现有三张 ARES 卡片：
- `ares-synthetic-data-pipeline` 讲合成训练数据，**未**涉及 PPI 校准集标注；
- `ares-ppi-confidence-bound` 提了 ppi_count 表（150 是下界），**未**涉及 GPT-4 替代；
- `ares-three-judge-rag-evaluation` 不涉及标注成本。

所有数字和论述直接来自 Table tab:gpt4_labels + caption + §Results。"混合策略最优"是合理引申，论文未明确实现但其消融数据支持这个方向。

## 发表门控结果

本轮未运行。

## 备注

- 与 `wicer-llm-judge-human-validation` 卡片有方法学呼应——都讨论"LLM 评估器/标注者与人工的差距"；可在 wiki 内做 cross-method 标注。
- 这条消融的实际意义：让 ARES 在"无 expert annotator"的领域（如金融、法律早期阶段）也能部署，先用 GPT-4 启动、再渐进补人工。
