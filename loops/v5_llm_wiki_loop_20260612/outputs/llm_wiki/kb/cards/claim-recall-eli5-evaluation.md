---
id: claim-recall-eli5-evaluation
title: ELI5 子声明召回率评测方法
status: accepted
card_type: evaluation-metric
tags:
- claim-recall
- ELI5
- InstructGPT
- sub-claims
- NLI
- correctness-metric
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-alce
evidence_basis: experimental_paper
justification: ../justification/claim-recall-eli5-evaluation.md
canonical_concept: claim-recall-eli5-evaluation
aliases:
- claim recall
- sub-claims evaluation
- ELI5 correctness metric
- 子声明召回率
summary: ALCE 为 ELI5 数据集提出 claim recall 评测方法 (claim-recall-eli5-evaluation)，解决长文本 QA 正确性评估难题。方法流程：(1) 用 InstructGPT (text-davinci-003) 从人类参考答案生成 3 个 sub-claims（平均 14 词/条）；(2) 用 TRUE NLI 模型检验模型输出是否蕴含这些 sub-claims。人工检验显示
  93.33% 的生成子声明忠实且相关，NLI 判断准确率达 80%。该方法优于 ROUGE-L：top-1 passage 直接输出可获 19.1 ROUGE-L 但 claim recall 仅 3.0%，有效避免了 ROUGE 可被游戏的问题。
related:
- alce-three-dimensional-evaluation
- nli-based-citation-quality-metrics
- ragchecker-retriever-metrics
---

ELI5 数据集不提供短实体答案，传统 ROUGE-L 无法有效衡量正确性（可被检索段落直接输出所游戏）。ALCE 提出 claim recall 方法。[^src-1]

具体流程：使用 InstructGPT (text-davinci-003) 对每个参考答案生成 3 个 sub-claims，平均长度 14 词，通常为单句事实陈述。然后用 TRUE NLI 模型判断模型输出是否蕴含这些 sub-claims。[^src-2]

质量验证：人工检查 120 条生成子声明，93.33%（112/120）被判定为相关且忠实。NLI 模型在 120 对 output-claim 上的判断准确率为 80.0%。[^src-3]

Claim recall 比 ROUGE-L 更能准确反映正确性：直接输出 top-1 BM25 段落可获 19.1 ROUGE-L（接近 ChatGPT 的 20.6），但 claim recall 仅 3.0%（远低于 ChatGPT 的 12.0%），因为单段落无法覆盖答案的多个方面。[^src-4]

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Correctness" -- "the ELI5 dataset does not provide short entity answers...ROUGE for evaluation, which does not reflect the correctness well"
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Generating Claims for ELI5" -- "we use text-davinci-003 to generate the sub-claims...the average number of words in the generated sub-claims is 14 words"
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Generating Claims for ELI5" -- "112 out of the 120 (93.33%) sub-claims received a score of 1...the NLI model achieved an accuracy of 80.0%"
[^src-4]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "tables/eli5_rouge.tex" -- "Top-1 passage: ROUGE-L 19.1, Claim recall 3.0; ChatGPT Vanilla: ROUGE-L 20.6, Claim recall 12.0"

[^card-1]: alce-three-dimensional-evaluation
[^card-2]: nli-based-citation-quality-metrics
