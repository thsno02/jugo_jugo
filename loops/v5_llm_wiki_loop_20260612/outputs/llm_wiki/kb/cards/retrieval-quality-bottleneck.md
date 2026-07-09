---
id: retrieval-quality-bottleneck
title: 检索质量是带引用生成的性能瓶颈
status: accepted
card_type: experimental-finding
tags:
- retrieval
- GTR
- DPR
- BM25
- oracle-passages
- context-utilization
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-alce
evidence_basis: experimental_paper
justification: ../justification/retrieval-quality-bottleneck.md
canonical_concept: retrieval-quality-bottleneck
aliases:
- retrieval bottleneck
- retrieval recall upper bound
- 检索瓶颈
summary: ALCE 的检索分析 (retrieval-quality-bottleneck) 揭示检索质量是带引用生成的核心瓶颈。GTR top-5 在 ASQA 上仅覆盖 56.8% 答案（recall@5），而 recall@100 为 78.4%。即使使用 oracle 段落（匹配 recall@100），ChatGPT 正确性也仅从 40.4% 提升到 48.9%，说明 LLM 在上下文中存在利用率不足。更多段落对
  ChatGPT 无显著帮助（correctness 在 top-1 后即 plateau），但 GPT-4 展现出正比于段落数的持续提升。GTR 在所有指标上优于 DPR。
related:
- alce-benchmark-overview
- alce-prompting-strategies
- instruction-tuning-citation-ability
- llm-multi-document-synthesis-limitation
---
检索质量是 ALCE 系统性能的核心瓶颈。[^src-1]

GTR top-5 在 ASQA 上的 EM recall 仅为 56.8%，top-100 为 78.4%。ELI5 的 BM25 检索更弱：top-5 仅 9.6%，top-100 为 31.8%。这意味着在有限上下文窗口下，大量正确答案根本未被检索到。[^src-2]

即使使用 oracle 段落（5 篇黄金段落，recall 匹配 top-100），ChatGPT 正确性也仅从 40.4% 提升到 48.9%，说明 LLM 在上下文中利用正确信息的能力存在上限。[^src-3]

更多段落对 ChatGPT 的帮助有限：正确性在 top-1 后即趋于平台，引用质量在 top-3 后平台。ChatGPT-16K 即使放入 20 篇段落也未见提升（ASQA: 36.1% EM，反而低于 4K 的 40.4%）。[^src-4]

GPT-4 表现不同：从 5-psg 到 20-psg 正确性从 41.3% 升至 44.4%，citation recall 从 68.5% 升至 73.0%，呈现出更强的长上下文综合能力。[^src-5]

GTR 在 ASQA 上全面优于 DPR（recall@5: 56.8% vs 51.5%；模型正确性 40.4% vs 36.1%）。[^src-6]

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Experiments" -- "the retrieval quality is crucial to the final performance and has substantial room for improvement"
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "tables/retrieval_asqa.tex" -- "GTR R@5=56.8 R@100=78.4"; "tables/retrieval_eli5.tex" -- "BM25 R@5=9.6 R@100=31.8"
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Retrieval Analysis" -- "both models' correctness lags behind the corresponding retrieval recall...despite the presence of accurate answers in context, LLMs struggle to utilize them"
[^src-4]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Retrieval Analysis" -- "correctness plateaus at top-1 passage and citation quality plateaus at top-3"; "tables/asqa_different_llms.tex" -- ChatGPT-16K 20-psg: 36.1% EM
[^src-5]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "tables/asqa_different_llms.tex" -- "GPT-4 (5-psg) 41.3...GPT-4 (20-psg) 44.4"
[^src-6]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- "Retrieval Analysis" (Figure 4 right table) -- "DPR (5-psg): 36.1 EM, 65.0 Rec...GTR (5-psg): 40.4 EM, 73.6 Rec"

[^card-1]: alce-prompting-strategies
[^card-2]: alce-benchmark-overview
