---
id: citation-partial-support-limitation
title: 引用评估中"部分支持"检测的缺失问题
status: accepted
card_type: distinction
tags: [citation-precision, partial-support, NLI-limitation, evaluation-gap]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
justification: ../justification/citation-partial-support-limitation.md
canonical_concept: citation-partial-support-limitation
aliases: [部分支持检测缺失, partial support detection gap, 引用精度评估局限]
summary: >-
  citation-partial-support-limitation（部分支持检测缺失, partial support detection gap）ALCE 的 NLI 引用精度评估无法区分"部分支持"与"不支持"：当引用 [2] 部分蕴含陈述 s3 且 [4][5] 完全覆盖时，[2] 被错误判为无关；尝试用 ChatGPT 做三级判断效果差，留为未来工作
related: [citation-quality-tri-dimension, nli-based-citation-verification, claim-level-entailment-evaluation]
---

ALCE 的引用精度（citation precision）评估存在一个已知的结构性局限：NLI 模型只能做二元蕴含判断（支持/不支持），无法检测"部分支持"（partial support）的情况 [^src-1]。

**问题场景**：考虑陈述 s3 引用了 [2][4][5]。如果 [2] 蕴含 s3 的部分信息，而 [4][5] 也蕴含了这部分信息，那么按照 ALCE 的精度算法：(a) phi([2], s3) = 0（[2]单独不能完全支持 s3），(b) phi([4][5], s3) = 1（去掉 [2] 后 [4][5] 仍支持 s3），因此 [2] 被判定为"无关"——但实际上它提供了部分支持，不应被惩罚 [^src-2]。

**Liu et al. 的替代方案**：另一项并行工作提出了三级判断方案——对每个引用判断是否"完全支持"、"部分支持"或"不支持"。引用被视为精确的条件是：(a) 该引用完全支持陈述，或 (b) 所有引用联合完全支持且该引用部分支持且无单一引用能独立完全支持 [^src-3]。

**自动化的困难**：作者尝试用 ChatGPT 进行三级判断，但效果不佳。目前没有现成的模型能自动判断"部分支持"，训练这样的判别器需要专门的监督数据，被留为未来工作 [^src-4]。

这一局限导致 ALCE 的 citation precision 系统性地低于人工评估——自动评估的 citation precision 准确率为 77.6%，且存在较高的假阳性率（将部分支持的引用错误标记为无关）[^src-5]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/evaluation.tex -- "Note that this algorithm overlooks the scenario when one citation partially supports the statement."
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/appendix.tex -- "if [2] entails partial information of s3 that [4][5] also entails, [2] will be counted as 'irrelevant' while it should not be penalized."
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/appendix.tex -- "For each citation, they ask annotators to judge whether the citation (1) fully support, (2) partially support, or (3) does not support s_i."
[^src-4]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/appendix.tex -- "it is challenging to conduct such evaluation automatically, as there is no existing model that can judge whether a citation 'partially' supports a claim. We also explore prompting ChatGPT to conduct such a task, which yields poor results."
[^src-5]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/appendix.tex -- "regarding detecting 'irrelevant' citations, ALCE has a recall of 75.6% and a precision of 66.1%---ALCE is effective in detecting 'irrelevant' citations, but due to the limitation of the NLI model (cannot detect 'partial support'), it has a relatively high false positive rate."
[^card-claim-level-entailment-evaluation]: [声明级蕴含检验评估方法](claim-level-entailment-evaluation.md) -- RAGChecker 的声明级分解方法为本卡所述"部分支持"问题提供了一种间接解决路径：将陈述拆解为原子声明后，每个声明可独立判断是否被蕴含，从而将"部分支持"还原为"子集声明被完全蕴含"，规避了三级判断的建模困难
