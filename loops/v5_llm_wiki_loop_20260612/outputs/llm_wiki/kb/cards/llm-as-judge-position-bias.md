---
id: llm-as-judge-position-bias
title: LLM-as-Judge 的顺序偏差问题
status: accepted
card_type: empirical-finding
tags:
- llm-as-judge
- position-bias
- order-sensitivity
- evaluation-pitfall
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-ragas
evidence_basis: experimental_paper
justification: ../justification/llm-as-judge-position-bias.md
canonical_concept: llm-judge-position-bias
aliases:
- LLM judge position bias
- LLM 评判顺序偏差
- order bias in LLM evaluation
summary: 当使用 LLM 在多个候选答案中选择最佳答案时，答案呈现的顺序会影响结果（position bias）。 Wang et al. (2023) 指出 "Large language models are not fair evaluators"——LLM 对候选的排列顺序敏感， 需要在评测设计中控制此偏差。RAGAS 的指标设计避免了直接让 LLM 做 pairwise ranking。
related:
- ragas-framework-overview
- rag-evaluation-motivation
---

当使用 LLM 直接在多个候选答案中选择最优时，呈现顺序（position/order）会影响判断结果。Wang et al. (2023b) 题为 "Large language models are not fair evaluators" 的研究揭示了这一问题。[^src-1]

**现象**：在 pairwise comparison 中，答案被放在前面还是后面会系统性地偏向某个位置，构成 position bias。[^src-2]

**对 RAGAS 设计的影响**：RAGAS 的三个指标均避免了直接让 LLM 做候选间 ranking。Faithfulness 用 claim-level verification (Yes/No)，Answer Relevance 用 reverse question generation + embedding cosine，Context Relevance 用 sentence extraction ratio——均绕开了 pairwise ranking 的顺序敏感性。[^card-1]

实验中的 GPT Ranking 基线恰恰使用了这种 pairwise ranking prompt，其表现最差（Faithfulness 0.54, AR 0.40, CR 0.52），似乎部分可归因于 position bias。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Related Work / Automated evaluation" P259 -- "care is needed with this approach, as the order in which the answers is presented can influence the result (Wang et al. 2023)"
[^src-2]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Related Work / Automated evaluation" P259 -- "the order in which the answers is presented can influence the result"
[^src-3]: `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt` -- "Experiments / Table 1" P388 -- "GPT Ranking 0.54 0.40 0.52"
[^card-1]: 见 [ragas-framework-overview] 各指标设计均避免直接 ranking
