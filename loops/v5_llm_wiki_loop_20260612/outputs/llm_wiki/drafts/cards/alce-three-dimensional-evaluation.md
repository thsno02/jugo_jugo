---
id: alce-three-dimensional-evaluation
title: ALCE 三维自动评测框架
status: draft
card_type: evaluation-methodology
tags: [citation-evaluation, fluency, correctness, citation-quality, NLI, MAUVE]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
evidence_basis: experimental_paper
justification: ../justification/alce-three-dimensional-evaluation.md
canonical_concept: alce-three-dimensional-evaluation
aliases: [ALCE evaluation framework, three-dimensional citation evaluation, 三维评测]
summary: >-
  ALCE (alce-three-dimensional-evaluation) 提出流畅性(fluency)、正确性(correctness)、引用质量(citation quality)三维自动评测框架。流畅性用 MAUVE 度量，正确性针对不同数据集采用 EM recall/precision/claim recall，引用质量通过 NLI 模型 TRUE 实现 citation recall 和 citation precision。三维组合能有效防止 shortcut 攻击——如仅输出 top-1 段落可获近乎完美引用分但流畅性和正确性骤降。
related: [alce-benchmark-overview]
---

ALCE 评测覆盖三个维度：流畅性（fluency）、正确性（correctness）和引用质量（citation quality）。[^src-1]

流畅性使用 MAUVE 评估生成文本与人类文本的分布差异，主要作为 sanity check 使用（因多数 LLM 已能产出流畅文本）。[^src-2]

正确性针对不同数据集采用不同指标：ASQA 用 EM recall（短答案是否出现在输出中）；QAMPARI 用 precision/recall-5；ELI5 用 claim recall（InstructGPT 生成子声明后用 NLI 模型 TRUE 验证蕴含关系）。[^src-3]

三维组合的鲁棒性在于防止 shortcut：直接输出 top-1 检索段落可获 99.4% 引用质量但 MAUVE 仅 20.8；仅取首两句则正确性降至 18.9%。[^src-4]

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Automatic Evaluation" -- "Our benchmark measures the following three dimensions of system responses"
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Fluency" -- "We use MAUVE to evaluate the fluency of the output...we mainly employ it as a sanity check"
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Correctness" -- "For ASQA...exact match recall...For QAMPARI...precision and recall...For ELI5...use TRUE...to check whether the model output entails the sub-claims"
[^src-4]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "ALCE Catches Shortcut Cases" -- "Using the top-1 passages or first two sentences of the top-1 passages induces almost perfect citation quality, but fluency and correctness are dramatically lower."

[^card-1]: alce-benchmark-overview
