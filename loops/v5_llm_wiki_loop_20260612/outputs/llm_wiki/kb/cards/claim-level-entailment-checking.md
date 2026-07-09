---
id: claim-level-entailment-checking
title: Claim-level 蕴含检查机制
status: accepted
card_type: mechanism-definition
tags:
- claim-extraction
- entailment
- refchecker
- fine-grained-evaluation
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-ragchecker
evidence_basis: experimental_paper
justification: ../justification/claim-level-entailment-checking.md
canonical_concept: claim-level-entailment-checking
aliases:
- claim entailment
- claim-level checking
- 声明级蕴含检查
summary: Claim-level entailment checking 是 RAGChecker 的核心机制，包含 text-to-claim extractor 将文本 T 分解为 claim 集合 {c_i}，以及 claim-entailment checker 判断 claim c 是否被 reference text Ref 蕴含（记为 c in Ref 或 c not-in Ref）。RAGChecker
  实现中使用 Llama3-70B-Instruct 同时作为 extractor 和 checker，基于 RefChecker 框架。
related:
- ragchecker-framework-overview
- ragchecker-benchmark-design
- ragchecker-generator-metrics
- ragchecker-overall-metrics
- ragchecker-retriever-metrics
---
Claim-level entailment checking 是 RAGChecker 所有指标的计算基础。该机制包含两个操作：[^src-1]

1. **Text-to-claim extraction**: 将给定文本 T 分解为原子 claim 集合 {c_i}
2. **Claim-entailment checking**: 判断给定 claim c 是否被 reference text Ref 蕴含

蕴含结果记为 c ∈ Ref（蕴含）或 c ∉ Ref（不蕴含）。Reference text 可以是 model response、ground truth answer 或 retrieved chunks 中的任一项。[^src-2]

具体实现中，RAGChecker 使用 Llama3-70B-Instruct 同时担任 claim extractor 和 checker，基于开源框架 RefChecker 实现。[^src-3] 在 RefChecker benchmark 上的验证表明，该配置在 Zero Context、Noisy Context 和 Accurate Context 三种设置下均优于此前最优的纯开源组合。[^src-4]

[^src-1]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex Fine-grained Evaluation" -- "we introduce two components: 1) a text-to-claim extractor...and 2) a claim-entailment checker to determine whether a given claim c is entailed in a reference text Ref or not"
[^src-2]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/appendix_formulation.tex" -- "we decompose the text into a set of claims {c_i} and assess whether a specific claim c_i can entail or not entail a given reference text Ref, where Ref may represent m, gt, or {chunk_j}"
[^src-3]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/experiments.tex" -- "We employ Llama3-70B as both the claim extractor and checker models implemented by an open-sourced framework RefChecker"
[^src-4]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/appendix_refchecker_validation.tex" -- "Llama 3 based RefChecker outperforms the best purely open-sourced combinations reported in the RefChecker paper in all the three context settings"

[^card-1]: 参见 [ragchecker-framework-overview] 了解 RAGChecker 框架全貌
