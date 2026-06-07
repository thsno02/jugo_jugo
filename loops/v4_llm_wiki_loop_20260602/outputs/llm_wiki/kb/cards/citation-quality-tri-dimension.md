---
id: citation-quality-tri-dimension
title: 引用评估三维度框架：流畅度-正确性-引用质量
status: accepted
card_type: mechanism
tags: [citation, evaluation, fluency, correctness, citation-quality, anti-gaming]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
justification: ../justification/citation-quality-tri-dimension.md
canonical_concept: citation-quality-tri-dimension
aliases: [三维度引用评估, fluency-correctness-citation-quality, ALCE三维评估]
summary: >-
  citation-quality-tri-dimension（三维度引用评估, fluency-correctness-citation-quality）ALCE 沿流畅度（MAUVE）、正确性（数据集特定指标）、引用质量（NLI 驱动的 recall/precision）三个维度评估，三者联合构成抗捷径的鲁棒评估
related: [alce-citation-benchmark, nli-based-citation-verification, rag-evaluation-tri-dimension, ragchecker-three-tier-metrics]
---

ALCE 基准沿三个正交维度评估系统回答质量，三者共同构成抗捷径（shortcut-resistant）的鲁棒评估框架 [^src-1]：

**流畅度（Fluency）**：使用 MAUVE 指标衡量输出的流畅性和连贯性 [^src-2]。由于大多数 LLM 都能生成流畅文本，MAUVE 主要作为基本健全性检查（sanity check）。MAUVE 对输出长度敏感，对 QAMPARI 不适用（只需列表格式）。

**正确性（Correctness）**：针对不同数据集设计不同指标 [^src-3]：
- ASQA：正确短答案的 exact match recall
- QAMPARI：与金标准答案列表的 precision/recall（recall-5：预测包含至少 5 个正确答案时视为 100%）
- ELI5：用 InstructGPT 生成 3 个子声明（sub-claims），再用 NLI 模型 TRUE 检查输出是否蕴含这些声明（claim recall）

**引用质量（Citation Quality）**：使用 NLI 模型 TRUE 衡量两个子维度 [^src-4]：
- Citation recall：被引段落是否能蕴含对应陈述
- Citation precision：是否存在无关引用

三维度联合的关键价值在于防止系统走捷径：直接使用 top-1 检索段落作为回答可以获得近乎完美的引用质量分数，但流畅度和正确性会大幅下降 [^src-5]。

RAGAS 提出的 RAG 评估三维度（检索质量、忠实性、生成质量）从管道组件角度分解评估[^card-1]，而 ALCE 的三维度（流畅度、正确性、引用质量）则从端到端输出质量角度分解。两者的"维度正交性"设计哲学一致，但切入视角互补：RAGAS 聚焦定位故障组件，ALCE 聚焦防止输出走捷径。

## Footnotes

[^card-1]: [RAG 评估三维度分解](rag-evaluation-tri-dimension.md) -- RAGAS 从管道组件角度分解评估（检索/忠实性/生成），与 ALCE 从输出质量角度分解（流畅度/正确性/引用质量）形成互补视角；共享"正交维度防止单一指标走捷径"的设计哲学
[^card-ragchecker-three-tier-metrics]: [RAGChecker 三层诊断指标体系](ragchecker-three-tier-metrics.md) -- ALCE 的三维度评估停留在系统输出层面（"引用质量好不好"），RAGChecker 的三层指标深入管道内部（"是检索不够还是生成器没用好上下文"）。RAGChecker 在 ALCE 的 citation recall/precision 之上增加了 6 个生成器诊断指标和 2 个检索器指标，提供从系统级到模块级的评估递进

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/evaluation.tex -- "Our benchmark measures the following three dimensions of system responses: Fluency...Correctness...Citation quality"
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/evaluation.tex -- "We use MAUVE to evaluate the fluency of the output...we mainly employ it as a sanity check as long as the MAUVE scores are high enough."
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/evaluation.tex -- "Our objective is to measure the informativeness and utility of the generation to the question."
[^src-4]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/evaluation.tex -- "We evaluate citation qualities using two metrics: (1) citation recall...and (2) citation precision"
[^src-5]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/evaluation.tex -- "Using the top-1 passages or first two sentences of the top-1 passages induces almost perfect citation quality, but fluency and correctness are dramatically lower."
