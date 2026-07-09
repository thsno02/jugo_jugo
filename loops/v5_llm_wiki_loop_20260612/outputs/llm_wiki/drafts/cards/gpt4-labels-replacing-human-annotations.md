---
id: gpt4-labels-replacing-human-annotations
title: GPT-4 标注替代人工标注的可行性
status: draft
card_type: experimental-finding
tags: [gpt-4, annotation-cost, human-preference-validation, ppi, rag-evaluation]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ares]
evidence_basis: experimental_paper
justification: ../justification/gpt4-labels-replacing-human-annotations.md
canonical_concept: gpt4-labels-replacing-human-annotations
aliases: [GPT-4 labels, GPT-4 vs human labels, GPT-4 annotation replacement]
summary: >-
  ARES 探索用 500 个 GPT-4 生成标注替代 human preference validation set。结果：GPT-4 标注使 Kendall's tau 在多数场景下降 0.05-0.30，但将标注成本从数百个人工标注降至不到 10 个 few-shot prompt。PPI 效力随 GPT-4 标注数量增加而持续改善。据论文推测，此方向对降低评估成本有潜力。
related: []
---

论文探索 GPT-4 生成标注作为 human preference validation set 的廉价替代方案。使用 few-shot prompt 生成 500 个 GPT-4 标注。[^src-1]

结果：GPT-4 标注使 Kendall's tau 在多数配置下降 0.05-0.30（如 NQ C.R. 从 0.94 降至 0.78）。但标注成本从数百个人工标注降至不到 10 个 few-shot prompt。[^src-2]

PPI 效力随 GPT-4 标注数量增加而持续改善，据材料推测更多 GPT-4 标注可进一步缩小与人工标注的差距。[^src-3]

实验使用 DeBERTa-v3-Large fine-tuned judge 进行评估。[^src-4]

[^card-1]: [^ref→prediction-powered-inference-for-rag-ranking] PPI 与标注数量的关系
[^card-2]: [^ref→ares-ranking-accuracy-vs-baselines] 与人工标注的 tau 对比

[^src-1]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "Tables/GPT4_Labeling.tex" P124-125 -- "we generated 500 GPT-4 labels as replacements for human labeling using few-shot prompts"
[^src-2]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "Tables/GPT4_Labeling.tex" P126-127 -- "GPT-4 generated labels decreased Kendall's tau in most settings by 0.05 to 0.30...cutting it from hundreds of annotations to less than ten"
[^src-3]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "Tables/GPT4_Labeling.tex" P127-128 -- "the efficacy of PPI continues improving as we generate more GPT-4 generated labels"
[^src-4]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "Tables/GPT4_Labeling.tex" P129 -- "we use the fine-tuned LLM judge (DeBERTa-v3-Large) for evaluation"
