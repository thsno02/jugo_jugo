---
id: selfcheckgpt-sampling-consistency
title: SelfCheckGPT 多次采样一致性检测幻觉
status: accepted
card_type: method-reference
tags:
- selfcheckgpt
- hallucination-detection
- sampling-consistency
- black-box
- closed-model
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-ragas
evidence_basis: experimental_paper
justification: ../justification/selfcheckgpt-sampling-consistency.md
canonical_concept: selfcheckgpt-sampling-consistency
aliases:
- SelfCheckGPT
- self-check GPT
- 采样一致性幻觉检测
summary: SelfCheckGPT (Manakul et al. 2023) 针对不提供 token probability 的 closed-model 提出幻觉检测方法： 多次采样答案，核心假设为事实性答案在不同采样间语义一致性更高，而幻觉答案的采样结果倾向于不一致。 属于 zero-resource black-box hallucination detection。
related:
- ragas-faithfulness-metric
- rag-evaluation-motivation
---

SelfCheckGPT (Manakul et al. 2023) 是面向不提供 token probability 的 closed-model（如 ChatGPT、GPT-4）的幻觉检测方法。[^src-1]

**核心思路**：对同一问题多次采样生成答案，基于观察——事实性答案在不同采样间语义相似度更高（factual answers are more stable），而幻觉答案的不同采样结果倾向于语义不一致。[^src-2]

该方法属于 zero-resource black-box hallucination detection，不需要外部知识库或 reference answer，仅依赖模型自身的采样一致性。[^card-1][^src-3]

RAGAS 论文将其作为 related work 引用，但 RAGAS Faithfulness 选择了不同路线（claim decomposition + context verification），不依赖多次采样。[^card-2]

[^src-1]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Related Work / Estimating faithfulness using LLMs" P256 -- "For models that do not provide access to token probabilities... SelfCheckGPT addresses this problem"
[^src-2]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Related Work / Estimating faithfulness using LLMs" P256-257 -- "factual answers are more stable: when an answer is factual, we can expect that different samples will tend to be semantically similar"
[^src-3]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Bibliography" P86-87 -- "Selfcheckgpt: Zero-resource black-box hallucination detection"
[^card-1]: 见 [rag-evaluation-motivation] closed-model 无 token probability 的问题
[^card-2]: 见 [ragas-faithfulness-metric] RAGAS 选择的不同方法
