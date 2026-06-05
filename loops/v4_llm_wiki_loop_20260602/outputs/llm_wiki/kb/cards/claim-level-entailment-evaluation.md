---
id: claim-level-entailment-evaluation
title: 声明级蕴含检验评估方法
status: accepted
card_type: mechanism
tags: [rag, evaluation, claim-extraction, entailment, fine-grained]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ragchecker]
justification: ../justification/claim-level-entailment-evaluation.md
canonical_concept: claim-level-entailment-evaluation
aliases: [声明级蕴含检验, claim-level entailment checking, 细粒度声明评估, claim decomposition evaluation]
summary: >-
  claim-level-entailment-evaluation（声明级蕴含检验 / claim-level entailment checking / 细粒度声明评估）将文本分解为原子声明（claim），再逐一检查每个声明是否被参考文本蕴含；相比 response-level 评估（BLEU/ROUGE/BERTScore），该方法能捕捉长文本回答中正确与错误声明的混合分布，RAGChecker 在此基础上构建全部指标
related: [nli-based-citation-verification, rag-evaluation-meta-evaluation, ragchecker-three-tier-metrics, retrieval-snr-tradeoff, source-faithfulness-risk]
---

RAGChecker 提出的评估方法建立在两个核心组件之上：（1）文本到声明的提取器（text-to-claim extractor），将任意文本 T 分解为一组原子声明 {c_i}；（2）声明蕴含检查器（claim-entailment checker），判断给定声明 c 是否被参考文本 Ref 蕴含[^src-1]。

这种细粒度方法的动机在于：RAG 系统生成的回答通常是正确声明与错误声明的混合体，同时还可能遗漏标准答案中的某些声明。传统的 response-level 评估方法（如 n-gram 匹配的 BLEU/ROUGE、嵌入距离的 BERTScore、LLM 评分）对短答案有效，但无法识别长文本回答中的细微差异[^src-2]。

声明级蕴含检验的核心设计哲学是：给定任意待评估文本 T 和参考文本 Ref——二者可以是模型回答、标准答案或检索到的文本块——产出蕴含标签（蕴含/不蕴含）。通过改变 T 和 Ref 的角色，同一套机制可以衍生出所有评估指标[^src-3]。RAGChecker 使用 Llama3-70B-Instruct 同时作为声明提取器和蕴含检查器，实现了基于 RefChecker 框架的开源实现[^src-4]。相比 ALCE 基准使用的 NLI 模型 TRUE（T5-11B）进行二元蕴含判断，RAGChecker 的声明级方法提供了更细粒度的评估——能区分正确与错误声明的混合分布，而非仅判断整体蕴含[^card-nli-based-citation-verification]。

RAGChecker 在声明级蕴含检验之上构建了三层共 11 个诊断指标[^card-1]，元评估实验验证了这些指标与人类偏好的高度对齐[^card-2]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex, Fine-grained Evaluation with Claim Entailment" -- "we introduce two components: 1) a text-to-claim extractor that decomposes a given text T into a set of claims {c_i}, and 2) a claim-entailment checker to determine whether a given claim c is entailed in a reference text Ref or not"
[^src-2]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/introduction.tex, metric limitation" -- "typical measures such as n-gram-based (e.g., BLEU, ROUGE), embedding-based (e.g., BERTScore), and LLM-based methods perform well with concise answers but fail to detect finer distinctions in longer responses"
[^src-3]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/framework.tex, RAGChecker Metrics" -- "The design philosophy of all metrics is to obtain claim entailment labels given any to-evaluate text T and reference text Ref, where T and Ref can be model response, groundtruth answer, or retrieved chunks"
[^src-4]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/experiments.tex" -- "We employ Llama3-70B as both the claim extractor and checker models implemented by an open-sourced framework RefChecker"
[^card-1]: [RAGChecker 三层诊断指标体系](ragchecker-three-tier-metrics.md) -- 本卡描述声明级蕴含检验的基础方法，该卡描述在此基础上构建的三层（整体/检索器/生成器）11 个诊断指标
[^card-2]: [RAG 评估框架的元评估方法论](rag-evaluation-meta-evaluation.md) -- 本卡描述声明级蕴含检验方法，该卡通过元评估验证了基于此方法构建的 RAGChecker 指标与人类偏好的对齐度
[^card-nli-based-citation-verification]: [基于 NLI 模型的引用验证机制](nli-based-citation-verification.md) -- ALCE 使用 NLI 模型 TRUE 做整体蕴含判断（citation recall/precision），RAGChecker 的声明级分解方法可视为其演进，在长文本混合正误场景下提供更强的区分力
