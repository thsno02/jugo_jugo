---
id: ragchecker-generator-trilemma
title: RAG 生成器的三难：faithfulness × context utilization × noise sensitivity
status: draft
card_type: distinction
tags: [#rag, #evaluation, #ragchecker, #generator]
created_time: 2026-05-26T11:25:00+08:00
edited_time: 2026-05-26T11:25:00+08:00
edited_entity: llm
source_ids: [arxiv-ragchecker]
provenance_card: ../provenance/ragchecker-generator-trilemma.md
aliases: ["RAG generator metric trilemma", "RAG 生成端三角"]
related: [ragchecker-claim-entailment-decomposition]
---

RAGChecker 把生成器维度拆成 5 个 claim-级指标，其中三个互相牵制，构成"三难"：

- **faithfulness**：回答里的 claim 中，有多少能被某个被检索到的 chunk entail。"答案有几分来自语料"。
- **context utilization**：被检索到的 chunk 中包含的 ground-truth claim 中，有多少出现在最终回答里。"语料里相关的部分有多少被用上了"。
- **noise sensitivity**：回答里 incorrect 的 claim 中，有多少能被某个 chunk entail。再按 chunk 是否相关分成 **relevant noise sensitivity** 与 **irrelevant noise sensitivity**。"模型把语料里的杂质照搬下来的程度"。
- 此外还有两个补充：**hallucination**（错误 claim 既不在 ground-truth 也不在 chunk）与 **self-knowledge**（正确 claim 不在任何 chunk）。这两个反映"答非语料"的成分。

三难的核心：

1. 提高 faithfulness（让模型更紧贴上下文）通常意味着 context utilization 上升（语料里的事实被搬进答案）——这是好事。
2. 但**只要陪检索出来的相关 chunk 里掺了噪声，模型在更"听话"的同时也更可能照搬噪声**，于是 relevant noise sensitivity 同步上升。
3. 想用 prompt 显式要求"更 faithful、更 utilize、更不 noise-sensitive"时，论文实测：faithfulness 92.2→93.6，context utilization 59.2→63.7，noise sensitivity 35.4→38.1——三者无法同时优化。论文原话：*"the trilemma of context utilization, noise sensitivity, and faithfulness makes it difficult to improve all aspects simultaneously."*

操作含义：

- **RAG 调优要先选优先级，再写 prompt**。如果业务对幻觉零容忍（医疗、合规），就优先 faithfulness，并接受 utilization 不如 ChatGPT 直答；如果业务允许少量错误但要求覆盖面（写作助手、研究综述），优先 utilization。
- **不要把 faithfulness 当唯一的"好"指标**。论文里 Llama3-70B 的 faithfulness（93.2 / 95.9）反而高于 GPT-4（87.9 / 93.0），但这是因为 Llama3 对相关 chunk 几乎"照单全收"——high noise sensitivity 的代价。GPT-4 在 context utilization 与 noise sensitivity 上同时领先，整体反而更强。
- **三难也意味着模型选型与 prompt 设计要联合做**——闭源大模型在三角上的"前沿"位置不同于开源模型。论文给出的工程性结论：开源生成器普遍"faithful but blindly trust context"，需要补它们的判别力，而非进一步增强对 context 的依从。

边界与误读：

- 三难是经验观察，不是数学证明；不能把"提高 A 必降 B"当作不可逾越的硬约束。论文报告的曲线在 $k$ 与 chunk size 增大时会出现"saturation"，说明三个指标确实能同时缓慢改善——只是边际收益递减。
- noise sensitivity 在原始 §framework 中被进一步拆为 relevant 与 irrelevant 两类，工程上必须分开看；只报一个 noise sensitivity 平均值会掩盖"chunk-level faithfulness"现象（见相关卡）。

## References

- 五个 generator 指标的形式定义见 §"Fine-grained Evaluation with Claim Entailment"（`data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt`，第 892–907 行）与 appendix §"Generator Metrics"（L437–448）。
- 三难明示句见 §"Suggestions for Improvements"（同文件 L830）。
- 显式 prompt 实验的 92.2 / 59.2 / 35.4 → 93.6 / 63.7 / 38.1 数字见 §"Diagnosis"（L820–822）。
- Llama3-70B 与 GPT-4 在 faithfulness / utilization / noise sensitivity 上的对比来自被注释保留段（L800–805）。

## Footnotes

- L892–897：faithfulness 定义；relevant / irrelevant noise sensitivity 与 hallucination 的分类。
- L907–908：context utilization 与 self-knowledge 的定义；*"Generally a higher context utilization is preferred."*
- L820–822：prompt 显式要求实验的三组数字。
- L830：*"the trilemma of context utilization, noise sensitivity, and faithfulness makes it difficult to improve all aspects simultaneously."*
- L784：*"Open-Source Models are Worse at Distinguishing Accurate Information from Noise."*
