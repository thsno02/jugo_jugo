---
id: ares-human-preference-validation-set
title: ARES 人工偏好验证集的角色与需求
status: draft
card_type: design-choice
tags: [human-annotation, validation-set, ppi, data-efficiency, rag-evaluation]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ares]
evidence_basis: experimental_paper
justification: ../justification/ares-human-preference-validation-set.md
canonical_concept: ares-human-preference-validation-set
aliases: [human preference validation set, ARES annotation requirement, PPI labeled set]
summary: >-
  ARES 的 human preference validation set 是约 150-300 个人工标注的 query-passage-answer 三元组，包含正负例，用于 PPI rectifier function 学习和 judge 训练的 early stopping。最低有效门槛约 150 个标注（低于 100 时 tau 急剧下降）；400 个进一步提升。相比传统标注方法（每系统 150 个，共需 1350+），ARES 少用 78% 标注。此 set 需领域专家标注，是 ARES 的主要人力成本。
related: []
---

Human preference validation set 是 ARES 三大输入之一，承担两个角色：(1) PPI 中学习 rectifier function 的锚点，(2) judge 微调时的 early stopping 评估集。[^src-1]

构成：约 150+ 个人工标注的 query-passage-answer 三元组，包含 context relevance、answer faithfulness、answer relevance 的正负例标签。[^src-2]

最低有效门槛实验：150 个标注为推荐最低量。低于 100 时 Kendall's tau 急剧下降（NQ C.R. 从 0.72 降至 0.44）。400 个时部分配置达到 tau=1.0。[^src-3]

数据效率：传统方法需每个 RAG 系统 150 个标注（9 个系统共 1350 个），ARES 仅需 300 个共享标注，少用 78%。[^src-4]

局限：专业领域（法律/医学/金融）需具有专业知识的标注者。[^src-5]

[^card-1]: [^ref→prediction-powered-inference-for-rag-ranking] PPI 使用此 set 做校正
[^card-2]: [^ref→ares-llm-judge-finetuning] early stopping 使用此 set

[^src-1]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "methods.tex" P690-695 -- "a human preference validation set of approximately 150 annotated datapoints (or more)"
[^src-2]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "introduction.tex" P634 -- "approximately 150 annotated datapoints or more that designate both positive and negative examples"
[^src-3]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "Tables/ppi_comparison_table.tex" P197 -- "below about 100-150 datapoints...ARES cannot meaningfully distinguish"
[^src-4]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P821-822 -- "using 78% less annotations than the baseline approach"
[^src-5]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "limitations.tex" P668-670 -- "more specialized domains...may require annotators with specialized expertise"
