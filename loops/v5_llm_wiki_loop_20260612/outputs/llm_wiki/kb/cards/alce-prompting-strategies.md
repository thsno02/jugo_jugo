---
id: alce-prompting-strategies
title: ALCE 带引用生成的 Prompting 策略
status: accepted
card_type: method-comparison
tags:
- prompting
- Vanilla
- Summary
- Snippet
- Interact
- InlineSearch
- Rerank
- PostCite
- ClosedBook
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-alce
evidence_basis: experimental_paper
justification: ../justification/alce-prompting-strategies.md
canonical_concept: alce-prompting-strategies
aliases:
- Vanilla
- Summ
- Snippet
- Interact
- InlineSearch
- Rerank
- PostCite
- ClosedBook
- ALCE modeling approaches
summary: ALCE (alce-prompting-strategies) 探索了多种 prompting 策略：Vanilla（直接放入 top-k 段落并指示引用）、Summ/Snippet（用 ChatGPT 压缩段落以放入更多检索结果，平均压缩 6 倍）、Interact（允许模型检查全文的交互式方案）、InlineSearch（模型在生成过程中调用搜索）、ClosedBook（无检索直接生成）、PostCite（后置匹配引用）、Rerank（采样多个回答后按
  citation recall 排序选最优）。Vanilla 尽管简单但接近最优；Rerank 在引用质量上持续提升。
related:
- alce-benchmark-overview
- closedbook-posthoc-citation-gap
- retrieval-quality-bottleneck
---
ALCE 提出并比较了多种 prompting 策略用于带引用生成：[^src-1]

Vanilla：直接将 top-k 检索段落放入上下文，配合指令和 2 个 in-context 示例。4K 上下文最多放 5 篇段落。尽管简单，其性能接近所有策略中的最优。[^src-2]

Summ/Snippet：用 ChatGPT 对段落进行摘要或抽取式压缩（平均长度减少 6 倍），允许在相同上下文窗口中放入更多段落（如 10 篇）。二者提高正确性但由于有损压缩导致引用质量下降。[^src-3]

Interact：在 Summ/Snippet 基础上允许模型执行 "Check: Document [1][2]" 查看全文，但实验显示此交互并未带来显著提升，似乎当前 LLM 不擅长交互式使用。[^src-4]

InlineSearch：模型在生成过程中调用 "Search: {query}" 在 top-100 段落中检索。但性能不如 Vanilla，因为在未见段落的情况下难以提出详细查询。[^src-5]

Rerank：对每个问题采样 4 个回答，按自动 citation recall 选最优。实验和人类评估均验证其持续提升引用质量。[^src-6]

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Modeling" -- "we discuss three major modeling components for an ALCE system---retrieval, synthesis, and post-editing"
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Vanilla" -- "We simply provide the model with the top-k passages and instruct the model to cite accordingly"
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Summ/Snippet" -- "Summaries or snippets significantly reduce the passage length, allowing for more passages to fit in: for ASQA, they reduce passage length by 6x on average"
[^src-4]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Experiments" -- "Combining Interact with Summ/Snippet does not bring improvement...current LLMs are not proficient in an interactive usage"
[^src-5]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Experiments" -- "Vanilla outperforms InlineSearch on citation quality...it is challenging to ask detailed questions without seeing any passages"
[^src-6]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Rerank" -- "We randomly sample n_sample=4 responses...and select the best response using the automatic citation recall score"

[^card-1]: alce-benchmark-overview
