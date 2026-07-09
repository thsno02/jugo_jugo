---
id: closedbook-posthoc-citation-gap
title: 闭卷生成后置引用的正确性与引用质量差距
status: draft
card_type: experimental-finding
tags: [ClosedBook, PostCite, hallucination, citation-gap, post-hoc-attribution]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
evidence_basis: experimental_paper
justification: ../justification/closedbook-posthoc-citation-gap.md
canonical_concept: closedbook-posthoc-citation-gap
aliases: [ClosedBook+PostCite, post-hoc citation, 后置引用, closed-book citation gap]
summary: >-
  ALCE 实验发现 ClosedBook+PostCite 策略 (closedbook-posthoc-citation-gap) 呈现正确性与引用质量的系统性鸿沟。ClosedBook 在 ELI5 上正确性达 18.6%（优于 Vanilla 的 12.0%），但 citation recall 仅 15.5%，远低于 Vanilla 的 51.1%。在 ASQA 上，PostCite 的 citation recall 比 Vanilla 低 47 个百分点（26.7% vs 73.6%）。原因有二：(1) 开卷模型易被无关段落干扰降低正确性；(2) ClosedBook 常生成正确但与检索段落不相似的文本，难以后置匹配引用。
related: [alce-prompting-strategies, alce-benchmark-overview]
---

ClosedBook+PostCite 策略呈现出系统性的正确性与引用质量差距。[^src-1]

在正确性方面，ClosedBook 在 ELI5 上达到 18.6% claim recall（最高），在 QAMPARI 上达到 32.9% recall-5，均优于 Vanilla。但在 ASQA 上仅与 Vanilla 有 2% 差距（38.3% vs 40.4%）。[^src-2]

然而 PostCite 无法弥补引用缺失：ASQA 上 citation recall 仅 26.7%，比 Vanilla 低 47 个百分点；ELI5 上仅 15.5%。[^src-3]

论文通过人工检查识别出两个根本原因：(1) 开卷模型容易被上下文中的无关段落干扰，生成正确性反而降低（与 Shi et al. 2023 的发现一致）；(2) ClosedBook 经常生成事实上正确但与任何检索段落在表述上不相似的文本，使得 GTR 后置匹配引用失败。[^src-4]

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Experiments" -- "ClosedBook+PostCite delivers strong correctness but poor citation quality"
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "tables/eli5.tex" -- "ClosedBook: 18.6 claim recall...15.5 citation recall"
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Experiments" -- "citation recall of ClosedBook+PostCite is lower than Vanilla by 47% on ASQA"
[^src-4]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Experiments" -- "(1) open-book models are easily distracted by irrelevant passages...a phenomenon also observed by Shi et al.; (2) ClosedBook often generates texts that are correct but not similar to any retrieved passages"

[^card-1]: alce-prompting-strategies
