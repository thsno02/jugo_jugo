---
id: graphrag-text-defense-blind-spot
title: 现有文本侧防御为何对 GraphRAG 投毒近乎失明
status: accepted
card_type: source_claim
tags: [#graphrag, #security, #defense, #evaluation]
created_time: 2026-05-26T11:15:00+08:00
edited_time: 2026-05-27T10:09:00+08:00
edited_entity: llm
source_ids: [arxiv-graph-poisoning]
provenance_card: ../provenance/graphrag-text-defense-blind-spot.md
aliases: ["GraphRAG defense failure", "text-level defense bypass"]
related: [tkpa-graph-guided-targeted-poisoning, ukpa-coreference-disruption, gragpoison-additive-vs-edit-attack, graphrag-manipulation-only-attack-surface, ukpa-edit-distance-stealth-tradeoff, poisonedrag-existing-defenses-insufficient]
---

Wen 等人测试了三类被视为"代表性"的 RAG 投毒防御——Perplexity-based Filter (PF, GPT-2)、LLM-based Contamination Detector (LLMDet)、Semantic Closeness Checking (SCC)——结果对 TKPA / UKPA 几乎全部失效：F1 在 0.04 ~ 0.13 之间，最高的 LLMDet 对 TKPA 也只有 0.13。这一结果的解释超出"防御工具能力不足"，应当读作**对一类防御方法整体的结构性失明**。

为什么会全面失明，可以按攻击类型分别看：

- **对 TKPA**：改动由 LLM 在保留风格、流畅度、局部语义的前提下完成，PPL 没有异常升高（论文里 TKPA 的 PPL Ratio ≈ 1.15–1.21，对照 Naive Swap 的 5.12+），LLMDet 也只看 chunk 文本判断，看不到结构层面的"这段在图里成了枢纽"。
- **对 UKPA**：改动是把代词、指代换得稍模糊，每个句子仍然合法、可读、局部意义不变；要发现问题必须**跨 chunk 看共指 + 看构图后的拓扑差**，而所有被测防御都只在 chunk 局部判断，因此根本看不到长程裂解。
- **对 query-side 防御**（如 query paraphrasing）：论文明确指出无效——语料层的图已经被污染，无论怎么改写查询，最终都会落到被毒化的实体上。

这一观察的两个操作含义：

1. **防御要前移到构图阶段**。光靠文本扫描和 PPL 阈值无法捕捉"语义保留 + 结构破坏"的攻击。可能的方向是对比同一语料在多次构图下的 entity-relation 集合稳定性，或者比对"trusted snapshot"与新版图谱的 Jaccard 差。
2. **不应高估 LLM-based detector**。LLMDet 在 TKPA 上 F1 仅 0.13，说明把"判定是否被毒"再扔给 LLM 本身并不能替代结构层证据。

边界与误读：

- 论文没有说"所有防御都失效"，而是说**已有的代表性文本侧防御**失效。任何能直接看到 graph 构造前后 entity/relation 集合差的防御，原则上能捕捉到 UKPA；TKPA 留下的痕迹更小，但 social-graph anomaly detection 仍有空间。
- SCC 在 UKPA 上 F1 0.07：SCC 本应"专门用来抓 universal poisoning 的语义相近改写"，结果仍然失败，说明仅靠原文-改写句嵌入近似不够——需要看下游图差，而不是文本对差。

## References

- 防御失效表与解释见论文 §"Attack Stealthiness"（`data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt`，第 730–761 行）。
- query-side 防御无效的论证见同节末尾段（L738–740）。

## Footnotes

- L749–757：Table~\ref{tab:defense_evaluation}，TKPA × {PF, LLMDet} 与 UKPA × {SCC, PF, LLMDet} 的 Precision / Recall / F1。
- L734–736：*"the modified text is statistically and stylistically indistinguishable from clean text"*。
- L735–737：UKPA 防御失效解释——*"Breaking these signals leaves the sentence-level meaning intact but causes long-range fragmentation in the knowledge graph."*
- L738–740：query-side 防御无效——*"the poisoned corpus corrupts the knowledge graph itself, so any paraphrased query will ultimately retrieve compromised entities and poisoned context."*
