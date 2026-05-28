---
id: graphrag-text-defense-blind-spot
title: 现有文本侧防御为何对 GraphRAG 投毒近乎失明
status: accepted
card_type: source_claim
tags: [#graphrag, #security, #defense, #evaluation]
created_time: 2026-05-26T11:15:00+08:00
edited_time: 2026-05-28T15:32:00+08:00
edited_entity: llm
source_ids: [arxiv-graph-poisoning]
provenance_card: ../provenance/graphrag-text-defense-blind-spot.md
aliases: ["GraphRAG defense failure", "text-level defense bypass"]
related: [tkpa-graph-guided-targeted-poisoning, ukpa-coreference-disruption, gragpoison-additive-vs-edit-attack, graphrag-manipulation-only-attack-surface, ukpa-edit-distance-stealth-tradeoff, poisonedrag-existing-defenses-insufficient]
---

Wen 等人测试了三类被视为"代表性"的 RAG 投毒防御——Perplexity-based Filter (PF, GPT-2)、LLM-based Contamination Detector (LLMDet)、Semantic Closeness Checking (SCC)——结果对 TKPA / UKPA 几乎全部失效：F1 在 0.04 ~ 0.13 之间，最高的 LLMDet 对 TKPA 也只有 0.13[^src1]。这一结果的解释超出"防御工具能力不足"，应当读作**对一类防御方法整体的结构性失明**。同样的"现有 retrieval-side 防御对 RAG 投毒不够用"在 PoisonedRAG 的 paraphrasing / PPL / dedup / k-expansion 实测[^v3-1] 里有 chunk-RAG 一侧的对应数字。

为什么会全面失明，可以按攻击类型分别看：

- **对 TKPA**[^v3-2]：改动由 LLM 在保留风格、流畅度、局部语义的前提下完成，PPL 没有异常升高（论文里 TKPA 的 PPL Ratio ≈ 1.15–1.21，对照 Naive Swap 的 5.12+），LLMDet 也只看 chunk 文本判断，看不到结构层面的"这段在图里成了枢纽"[^src2]。
- **对 UKPA**[^v3-3]：改动是把代词、指代换得稍模糊，每个句子仍然合法、可读、局部意义不变；要发现问题必须**跨 chunk 看共指 + 看构图后的拓扑差**[^src3]，而所有被测防御都只在 chunk 局部判断，因此根本看不到长程裂解。
- **对 query-side 防御**（如 query paraphrasing）：论文明确指出无效——语料层的图已经被污染，无论怎么改写查询，最终都会落到被毒化的实体上[^src4]。

这一观察的两个操作含义：

1. **防御要前移到构图阶段**。光靠文本扫描和 PPL 阈值无法捕捉"语义保留 + 结构破坏"的攻击。可能的方向是对比同一语料在多次构图下的 entity-relation 集合稳定性，或者比对"trusted snapshot"与新版图谱的 Jaccard 差。
2. **不应高估 LLM-based detector**。LLMDet 在 TKPA 上 F1 仅 0.13，说明把"判定是否被毒"再扔给 LLM 本身并不能替代结构层证据。

边界与误读：

- 论文没有说"所有防御都失效"，而是说**已有的代表性文本侧防御**失效。任何能直接看到 graph 构造前后 entity/relation 集合差的防御，原则上能捕捉到 UKPA；TKPA 留下的痕迹更小，但 social-graph anomaly detection 仍有空间。
- SCC 在 UKPA 上 F1 0.07：SCC 本应"专门用来抓 universal poisoning 的语义相近改写"，结果仍然失败，说明仅靠原文-改写句嵌入近似不够——需要看下游图差，而不是文本对差。UKPA 也提供过自身的小编辑距离 ablation[^v3-4] 解释了为什么编辑距离这类文本级 proxy 不会留下可被 PPL 捕捉的信号。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` — 行 749-757 — Table tab:defense_evaluation：TKPA × {PF, LLMDet} 与 UKPA × {SCC, PF, LLMDet} 的 Precision / Recall / F1
[^src2]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` — 行 734-736 — "the modified text is statistically and stylistically indistinguishable from clean text"
[^src3]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` — 行 735-737 — UKPA 防御失效解释 "Breaking these signals leaves the sentence-level meaning intact but causes long-range fragmentation in the knowledge graph."
[^src4]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` — 行 738-740 — "the poisoned corpus corrupts the knowledge graph itself, so any paraphrased query will ultimately retrieve compromised entities and poisoned context."
[^v3-1]: [poisonedrag-existing-defenses-insufficient](poisonedrag-existing-defenses-insufficient.md) — chunk-RAG 一侧的"四类 retrieval-side 防御失效"对应实测
[^v3-2]: [tkpa-graph-guided-targeted-poisoning](tkpa-graph-guided-targeted-poisoning.md) — TKPA 的攻击机制（PPL 不异常的原因）
[^v3-3]: [ukpa-coreference-disruption](ukpa-coreference-disruption.md) — UKPA 的攻击机制（长程裂解的原因）
[^v3-4]: [ukpa-edit-distance-stealth-tradeoff](ukpa-edit-distance-stealth-tradeoff.md) — UKPA 编辑距离 ≤3 甜点解释 PPL signal 的缺席
