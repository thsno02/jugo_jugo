---
id: closed-book-citation-paradox
title: 闭卷-引用悖论：无检索生成正确性更高但无法有效引用
status: accepted
card_type: distinction
tags: [closed-book, post-hoc-citation, correctness-citation-tradeoff, retrieval-distraction]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
justification: ../justification/closed-book-citation-paradox.md
canonical_concept: closed-book-citation-paradox
aliases: [闭卷引用悖论, ClosedBook+PostCite paradox, 正确性与引用质量脱耦]
summary: >-
  closed-book-citation-paradox（闭卷引用悖论, ClosedBook+PostCite paradox）ClosedBook 模式在 ELI5 上正确性（18.6 claim recall）超过 Vanilla（12.0），但 PostCite 后引用 recall 仅 15.5%，因为：(1) 开卷模型被无关段落干扰降低正确性；(2) 闭卷生成的正确文本与检索段落不相似，难以事后匹配引用
related: [citation-support-gap, retrieval-as-citation-bottleneck, rag-generator-self-knowledge]
---

ALCE 实验揭示了一个反直觉的"闭卷-引用悖论"：不使用任何检索段落的 ClosedBook 模式在某些数据集上反而实现了更高的正确性，但事后添加引用（PostCite）的效果极差 [^src-1]。

**实证数据**：在 ELI5 上，ClosedBook 的 claim recall 为 18.6%（所有策略中最高），而 Vanilla（使用 5 个检索段落）仅 12.0%。但 ClosedBook+PostCite 的 citation recall 仅 15.5%，远低于 Vanilla 的 51.1% [^src-2]。在 ASQA 上，ClosedBook 正确性 38.3% 仅比 Vanilla 的 40.4% 低 2%，但 citation recall 从 73.6% 骤降至 26.7% [^src-3]。

**原因分析**：作者通过人工检查模型输出，识别出两个关键原因 [^src-4]：

1. **检索段落的干扰效应**：open-book 模型容易被上下文中的无关段落分散注意力，生成正确性更低的回答。这与 Shi et al. 2023 的观察一致。
2. **生成-检索语义鸿沟**：ClosedBook 模式生成的文本虽然正确，但其表达方式与任何检索段落都不相似，使得事后通过语义匹配找到支持引用变得困难。

这一发现揭示了正确性和引用质量之间并非简单的正相关关系，对"先生成后引用"的系统设计范式提出了根本性质疑 [^src-5]。RAGChecker 后续将此类"正确但不可追溯到检索上下文"的声明操作化为 self-knowledge 指标，使闭卷悖论从定性观察演变为可量化的生成器行为维度[^card-rag-generator-self-knowledge]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/results.tex -- "ClosedBook+PostCite delivers strong correctness but poor citation quality."
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- tables/eli5.tex -- "ClosedBook: Claim 18.6, Citation Rec. 15.5; Vanilla: Claim 12.0, Citation Rec. 51.1"
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- tables/asqa.tex -- "ClosedBook: EM 38.3, Citation Rec. 26.7; Vanilla: EM 40.4, Citation Rec. 73.6"
[^src-4]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/results.tex -- "(1) open-book models are easily distracted by irrelevant passages...a phenomenon also observed by Shi et al.; (2) ClosedBook often generates texts that are correct but not similar to any retrieved passages, making it difficult to match a citation post-hoc."
[^src-5]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/results.tex -- "citation recall of ClosedBook+PostCite is lower than Vanilla by 47% on ASQA."
[^card-rag-generator-self-knowledge]: [RAG 生成器的自有知识指标](rag-generator-self-knowledge.md) -- RAGChecker 的 self-knowledge 指标量化了本卡所揭示的现象：生成器产出正确但不可追溯到检索上下文的声明。ALCE 定性发现闭卷模式正确性高但无法引用，RAGChecker 则将此行为定义为可度量的生成器指标，并证明检索质量提升时 self-knowledge 下降
