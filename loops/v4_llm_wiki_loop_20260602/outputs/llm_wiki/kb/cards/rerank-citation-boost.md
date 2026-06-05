---
id: rerank-citation-boost
title: Rerank 策略：多次采样并按引用 recall 选优以提升引用质量
status: accepted
card_type: mechanism
tags: [reranking, citation-quality, sampling, post-editing, self-consistency]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
justification: ../justification/rerank-citation-boost.md
canonical_concept: rerank-citation-boost
aliases: [Rerank引用提升, citation reranking, 多采样引用择优]
summary: >-
  rerank-citation-boost（Rerank引用提升, 多采样引用择优）对每个问题随机采样4次回答，按自动 citation recall 分数选最优，在 ASQA 上将 citation recall 从 73.6% 提升至 84.8%（+11.2pp），在 ELI5 上从 51.1% 提升至 69.3%（+18.2pp），经人工评估确认有效
related: [citation-support-gap, nli-based-citation-verification]
---

ALCE 提出的 Rerank 策略是一种简单但有效的后编辑方法，通过多次采样并按引用质量排序来提升最终输出的引用质量 [^src-1]。

**具体做法**：对每个问题随机采样 n_sample = 4 个回答，然后使用自动 citation recall 分数选择最佳回答 [^src-2]。

**效果**：Rerank 在引用质量上带来一致且显著的提升 [^src-3]：
- ASQA：citation recall 从 73.6% 提升至 84.8%（+11.2pp），citation precision 从 72.5% 提升至 81.6%（+9.1pp）
- ELI5：citation recall 从 51.1% 提升至 69.3%（+18.2pp），citation precision 从 50.0% 提升至 67.8%（+17.8pp）
- 正确性基本不受影响（ASQA EM：40.4% → 40.2%）

**人工验证**：由于 Rerank 使用自动 citation recall 进行选择，其自动评估分数可能存在偏差。因此作者额外进行了人工评估，确认 Rerank 的有效性——人工 citation recall 在 ASQA 上从 74.7% 提升至 79.3%，在 ELI5 上从 50.8% 提升至 59.7% [^src-4]。

这一策略的成功暗示了 LLM 的引用能力在不同采样中存在较大方差，选择性策略可以在不修改模型的情况下获得可观收益。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/model.tex -- "We randomly sample n_sample=4 responses for each question, and select the best response using the automatic citation recall score."
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/model.tex -- "we expect Rerank to improve the citation quality."
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- tables/asqa.tex, tables/eli5.tex -- Rerank numerical results
[^src-4]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- tables/human_asqa_all.tex, tables/human_eli5_all.tex -- "ChatGPT Vanilla human Rec. 74.7 → w/ Rerank 79.3"
