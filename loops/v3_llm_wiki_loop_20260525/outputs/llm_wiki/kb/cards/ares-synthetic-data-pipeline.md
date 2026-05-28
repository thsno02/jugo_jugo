---
id: ares-synthetic-data-pipeline
title: ARES 用合成 query–answer 训练小判官以替代人工标注
status: accepted
card_type: mechanism
tags: [#rag, #ares, #synthetic-data, #fine-tuning, #llm-judge]
created_time: 2026-05-26T11:05:00+08:00
edited_time: 2026-05-28T15:45:00+08:00
edited_entity: llm
source_ids: [arxiv-ares]
provenance_card: ../provenance/ares-synthetic-data-pipeline.md
aliases: ["ARES 合成数据生成", "weak/strong negative generation"]
related: [ares-three-judge-rag-evaluation, ares-ppi-confidence-bound, ares-gpt4-vs-human-annotation-tradeoff, ares-cross-domain-generalization-limits, ragas-wikieval-dataset, longmemeval-benchmark-construction-pipeline]
---

ARES 之所以能"少标注、不依赖外部 API、跑在 commercial GPU 上"，关键不是判官本身，而是它的合成数据生成路径——把"昂贵的人工标注 query/answer/标签"压成"少量 in-domain passage + 5 个 few-shot 样本"。流程：

1. **正例合成**：用 FLAN-T5-XXL，喂入"in-domain passage + 5 个 few-shot 'passage→query→answer' 样本"，让它给每条新 passage 生成一对合成 query/answer。再用一个 retriever 过滤：如果合成 query 拿不回原 passage，就丢弃。这条过滤规则来自 Promptagator/UDAPDR 一脉。
2. **Weak Negative**：从同语料里随机抽**不相关**的 passage（用于 C.R. 负例），或者从其它 passage 的合成 answer 里随机抽（用于 A.F. / A.R. 负例）。
3. **Strong Negative**：从同一篇文档里抽相邻 passage 作为 C.R. 强负例；如果文档只有单段，就用 BM25 取 top-10 相似 passage 抽样。对 A.F. / A.R. 强负例，则用 few-shot 提示让 FLAN-T5-XXL **故意生成与 passage 矛盾的 answer**。
4. **判官 fine-tune**：用 DeBERTa-v3-Large（304M）+ 单线性分类头 + dropout 0.1，loss 用 cross-entropy，学习率 5e-6，batch size 32，linear warmup+decay。判官选择标准是"在 human preference 验证集上 loss 三个 epoch 不改善就早停"。

之所以同时需要 weak 和 strong negative：weak negative 让判官学会"明显的相关 / 不相关"，strong negative 让判官学会"语料内相近但实际不命中"的微妙差异——这对应真实 RAG 系统里最容易让判官失手的那种 case。论文同时让 weak 和 strong 各占负例的一半（与正例数量平衡）。

操作含义 / 边界：

- 输入约束：需要"in-domain passage 集合 + 150–300 条标注 + 5 条以上 few-shot 样本"。低于 100–150 条 PPI 校准集时，ARES 已经无法把模拟 RAG 系统准确排序（见 `tab:ppi_count`）。
- 硬件门槛：FLAN-T5-XXL（11.3B）+ DeBERTa-v3-Large 需要 ~32GB GPU 才能跑通生成 + fine-tune，原文在 Limitations 里点名了这一点。
- 强 A.F. 负例靠"让 LLM 生成矛盾 answer"。在 KILT/SuperGLUE 缺乏真 hallucination 标签的数据集上，A.F. 评估被显式跳过——这是合成路径的一个真实局限。

## References

- 合成数据生成流程：`data/raw/arxiv/arxiv-ares/agent_source_bundle.txt`，`methods.tex` "LLM Generation of Synthetic Dataset" 子节（L698–721）。
- Negative 生成两策略：同文件 L710–719。
- Fine-tune 超参：`appendix.tex` "Fine-tuning Configuration for LLM Judges"（L298–303）。
- 数据效率与硬件门槛：`limitations.tex`（L666–678）。

## Footnotes

- `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` L713-719：`"Weak Negative Generation: For context relevance negatives, we randomly sample in-domain passages unrelated to a given synthetic query." / "Strong Negative Generation: For context relevance negatives, we randomly sample in-domain passages from the same document as the gold passage."` 以及"For answer faithfulness and answer relevance negatives, we prompt FLAN-T5 XXL ... to generate a contradictory answer"。
- 同文件 L302-303：`"linear warmup and linear decay ... with a 5e-6 learning rate and a 32 training batch size"`。
- 同文件 L672-674：DeBERTa-v3-Large (304M) 与 FLAN-T5-XXL (11.3B) 需 ~32GB GPU。
