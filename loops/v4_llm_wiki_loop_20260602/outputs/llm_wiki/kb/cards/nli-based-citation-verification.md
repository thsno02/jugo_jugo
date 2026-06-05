---
id: nli-based-citation-verification
title: 基于 NLI 模型的引用验证机制
status: accepted
card_type: mechanism
tags: [NLI, citation-recall, citation-precision, TRUE, AIS, entailment]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-alce]
justification: ../justification/nli-based-citation-verification.md
canonical_concept: nli-based-citation-verification
aliases: [NLI引用验证, citation recall/precision via NLI, AIS自动评估]
summary: >-
  nli-based-citation-verification（NLI引用验证, AIS自动评估）ALCE 使用 NLI 模型 TRUE（T5-11B）自动评估引用质量：citation recall 检查引用段落拼接后是否蕴含陈述，citation precision 检查去除某引用后支持是否不变；与人工评估 Cohen's kappa 达 0.698/0.525
related: [citation-partial-support-limitation, citation-quality-tri-dimension, claim-level-entailment-evaluation]
---

ALCE 使用自然语言推理（NLI）模型 TRUE 来自动化引用质量评估，该模型是基于 T5-11B 微调在多个 NLI 数据集上的蕴含判断模型 [^src-1]。其评估遵循 AIS（attributable to identified sources）框架 [^src-2]。

**Citation Recall 形式化定义**：对每个陈述 s_i 及其引用集合 C_i，citation recall 为 1 当且仅当 C_i 非空且 phi(concat(C_i), s_i) = 1，其中 phi 是 NLI 模型的蕴含判断函数。所有陈述的 recall 取平均 [^src-3]。直觉含义是：被引段落拼接后应能支持该陈述的全部事实声明。

**Citation Precision 形式化定义**：引用 c_{i,j} 被判定为"无关"当且仅当 (a) phi(c_{i,j}, s_i) = 0（该引用本身不支持陈述）且 (b) phi(concat(C_i \ {c_{i,j}}), s_i) = 1（移除该引用后其余引用仍支持陈述）。precision = 1 要求 recall = 1 且引用不是无关的 [^src-4]。这一设计允许冗余引用的存在——人类写作中也常引用多余来源以增强可信度。

**与人工评估的相关性**：人工评估验证了自动指标的有效性。Citation recall 的 Cohen's kappa 为 0.698（substantial agreement），citation precision 为 0.525（moderate agreement）。以人工标注为金标准，自动评估在 citation recall 上准确率 85.1%，citation precision 上 77.6% [^src-5]。

**已知局限**：该机制无法检测"部分支持"（partial support）的情况——当一个引用部分支持陈述但其他引用也覆盖了同样的信息时，该引用会被错误地判定为无关 [^src-6]。RAGChecker 提出的声明级蕴含检验方法在一定程度上缓解了这一局限——通过将文本分解为原子声明再逐一检查蕴含，能更精确地识别长文本中正确与错误声明的混合分布[^card-claim-level-entailment-evaluation]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/appendix.tex -- "We use the version of TRUE model from https://huggingface.co/google/t5_xxl_true_nli_mixture, which is trained on SNLI, MNLI, Fever, Scitail, PAWS, and VitaminC."
[^src-2]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/evaluation.tex -- "The NLI evaluation is in accordance with the attributable to identified sources (AIS) framework"
[^src-3]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/evaluation.tex -- "its citation recall is 1 if and only if there is at least one citation (C_i != empty) and phi(concat(C_i), s_i)=1"
[^src-4]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/evaluation.tex -- "c_{i,j} is irrelevant if and only if (a) phi(c_{i,j},s_i)=0, AND (b) phi(concat(C_i \ {c_{i,j}}), s_i)=1"
[^src-5]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/human_eval.tex -- "the Cohen's kappa coefficient between human and ALCE suggests substantial agreement for citation recall (0.698) and moderate agreement for citation precision (0.525)"
[^src-6]: `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` -- sections/evaluation.tex -- "Note that this algorithm overlooks the scenario when one citation partially supports the statement."
[^card-claim-level-entailment-evaluation]: [声明级蕴含检验评估方法](claim-level-entailment-evaluation.md) -- RAGChecker 将文本分解为原子声明再逐一检查蕴含，相比 ALCE 的整体 NLI 判断提供了更细粒度的评估能力，可部分缓解二元蕴含判断的局限
