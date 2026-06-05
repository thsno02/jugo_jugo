---
id: alce-citation-benchmark
title: ALCE：首个自动化 LLM 引用评估基准
status: accepted
card_type: concept
tags: [citation, benchmark, evaluation, LLM, reproducibility]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
justification: ../justification/alce-citation-benchmark.md
canonical_concept: alce-citation-benchmark
aliases: [ALCE, Automatic LLMs Citation Evaluation, LLM引用评估基准]
summary: >-
  alce-citation-benchmark（ALCE, Automatic LLMs Citation Evaluation）是首个可复现的 LLM 引用生成自动评估基准，要求端到端系统从语料库检索证据并生成带引用的回答，解决了此前依赖商业搜索引擎和人工评估难以复现对比的问题
related: [citation-quality-tri-dimension, nli-based-citation-verification]
---

ALCE（Automatic LLMs' Citation Evaluation）是首个可复现的 LLM 引用生成自动评估基准，由 Princeton 大学的 Tianyu Gao 等人于 EMNLP 2023 提出 [^src-1]。

此前的引用生成研究主要依赖商业搜索引擎（如 Bing Chat）和人工评估，导致不同建模方法之间难以复现和比较 [^src-2]。ALCE 通过以下设计解决这一问题：

1. **端到端任务定义**：给定一个自然语言问题 q 和文本段落语料库 D，系统需要返回由 n 个陈述组成的输出，每个陈述引用一组来自 D 的段落（最多 3 个引用）[^src-3]。
2. **多样化数据集**：收集三个覆盖不同问题类型的数据集——ASQA（歧义性事实问答，Wikipedia 语料 21M 段落）、QAMPARI（列表答案事实问答，Wikipedia）、ELI5（how/why/what 长文问答，Sphere 语料 899M 段落）[^src-4]。
3. **100 词段落粒度**：将语料库切分为 100 词段落，区别于商业系统引用整个网页，便于人类验证且允许更多段落放入 LLM 有限上下文中 [^src-5]。
4. **自动评估指标**：沿流畅度、正确性、引用质量三个维度设计自动指标，并通过人工评估验证与人类判断的强相关性 [^src-6]。

ALCE 仅提供评估数据（每个数据集 1000 个样本来自开发集），不提供训练数据，因为这些数据集中不存在引用标注的监督样本 [^src-7]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/intro.tex -- "We present ALCE, the first reproducible benchmark for automatically evaluating LLMs' generations with citations."
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- abstract -- "Existing work mainly relies on commercial search engines and human evaluation, making it challenging to reproduce and compare different modeling approaches."
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/benchmark.tex -- "the system is required to return an output S, which consists of n statements s_1, ..., s_n, and each statement s_i cites a list of passages C_i"
[^src-4]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/benchmark.tex -- "ASQA is a long-form factoid dataset...QAMPARI is a factoid QA dataset...ELI5 is a long-form QA dataset"
[^src-5]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/benchmark.tex -- "We take 100-word passages because it is easier for humans to verify, and allows for more retrieved passages to fit in LLMs' limited context."
[^src-6]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/intro.tex -- "We design automatic evaluation methods in three dimensions: fluency, correctness, and citation quality."
[^src-7]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/benchmark.tex -- "Our benchmark primarily assesses the citation capabilities of existing LLMs and does not provide training data"
