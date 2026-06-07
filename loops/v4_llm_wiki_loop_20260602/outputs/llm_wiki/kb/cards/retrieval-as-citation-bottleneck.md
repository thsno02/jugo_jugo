---
id: retrieval-as-citation-bottleneck
title: 检索质量是引用生成的根本瓶颈
status: accepted
card_type: source_claim
tags: [retrieval, bottleneck, GTR, DPR, context-utilization, oracle-gap]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
justification: ../justification/retrieval-as-citation-bottleneck.md
canonical_concept: retrieval-as-citation-bottleneck
aliases: [检索瓶颈, retrieval bottleneck for citation, 检索上界与模型利用差距]
summary: >-
  retrieval-as-citation-bottleneck（检索瓶颈, retrieval bottleneck for citation）检索 recall 构成模型正确性的上界；即使使用 oracle 段落，模型正确性仍低于检索 recall，表明 LLM 难以充分利用上下文中的正确答案；GTR 优于 DPR，更多段落在 ChatGPT 上收益饱和但 GPT-4 能持续受益
related: [citation-support-gap, context-window-degradation, context-utilization-as-performance-key]
---

ALCE 的检索分析揭示了检索质量在引用生成系统中的根本瓶颈作用，并发现即使检索完美也存在利用差距 [^src-1]。

**检索 recall 是正确性的上界**：随着检索段落数增加，检索 recall 稳步提升。ASQA 上 GTR 的 recall@5 为 56.8%，recall@100 为 78.4%。但模型的实际正确性远低于对应的检索 recall——即使提供 top-5 段落，ChatGPT 的 EM recall 仅 40.4% [^src-2]。

**Oracle 差距**：使用 5 个 oracle（金标准）段落时，ChatGPT 正确性提升至 48.9%（ASQA），但仍低于 recall@100 的 78.4%。这一差距表明 LLM 在上下文中有正确答案时仍难以充分利用它们 [^src-3]。

**检索器选择重要**：GTR 在正确性和引用质量上均优于 DPR（ASQA 上 EM 40.4% vs 36.1%，citation recall 73.6% vs 65.0%），强调了部署更好检索器的重要性 [^src-4]。

**更多段落的非线性收益**：违背直觉的是，在 ChatGPT（4K 窗口）中放入更多段落不会带来显著提升——正确性在 top-1 时即趋于饱和，引用质量在 top-3 时饱和。但 GPT-4 展示了随段落增加的持续提升趋势（ASQA EM：5-psg 41.3% → 20-psg 44.4%），表明 GPT-4 更擅长从长上下文中综合信息 [^src-5]。相反，ChatGPT-16K 在增加段落后反而性能下降 [^src-6]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/results.tex -- "The retrieval results play a crucial role to the correctness and the citation quality."
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/results.tex -- "both models' correctness lags behind the corresponding retrieval recall"
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/results.tex -- "despite the presence of accurate answers in context, LLMs struggle to utilize them in their outputs."
[^src-4]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/results.tex -- "GTR outperforms DPR in both correctness and citation quality, emphasizing the importance of deploying better retrievers."
[^src-5]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/results.tex -- "GPT-4 exhibits an increasing trend with more passages, but the improvement is not proportional to the retrieval performance."
[^src-6]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/results.tex -- "including more passages with ChatGPT-16K does not improve the results...suggesting that processing more passages is non-trivial and GPT-4 is better at synthesizing information from its long context than ChatGPT."
[^card-context-utilization-as-performance-key]: [上下文利用率是 RAG 性能的关键生成器指标](context-utilization-as-performance-key.md) -- RAGChecker 将本卡定性观察的"Oracle 差距"（模型无法充分利用上下文中的正确答案）量化为 context utilization 指标，并证明该指标在不同检索器间保持稳定（GPT-4 CU~60%），与本卡 GPT-4 能持续从更多段落中受益的发现相互印证
