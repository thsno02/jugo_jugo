---
id: graphrag-manipulation-only-attack-surface
title: GraphRAG 的"只改字、不加文"攻击面
status: accepted
card_type: concept
tags: [#graphrag, #security, #poisoning, #rag]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T10:05:00+08:00
edited_entity: llm
source_ids: [arxiv-graph-poisoning]
provenance_card: ../provenance/graphrag-manipulation-only-attack-surface.md
aliases: ["manipulation-only KPA", "graph poisoning without injection"]
related: [gragpoison-additive-vs-edit-attack, graphrag-pipeline-formalism, graphrag-text-defense-blind-spot, tkpa-graph-guided-targeted-poisoning, ukpa-coreference-disruption, graphrag-global-sensemaking-pipeline, graphrag-leiden-community-hierarchy, poisonedrag-knowledge-database-attack-surface]
---

GraphRAG 的安全文献此前主要研究"加内容"型攻击：在语料库里注入新的恶意 chunk，或在 chunk 内塞入提示词指令。Wen 等人指出，GraphRAG 还有一个被忽视的攻击面——**只修改语料中已有的少量字词，不加任何新文本，也能让构造出的知识图谱永久带毒**。这一面之所以被忽视，是因为图谱"先构图、再回答"的流水线把单字级改动的影响向下游放大了。

关键的威胁建模是 *gray-box / manipulation-only*：

- **攻击者知识**：知道 GraphRAG 会切 chunk、抽实体关系、做社区摘要，并以此为上下文回答；不需要看到最终图。
- **攻击者能力**：仅能改写受信源（如 Wikipedia 词条）中的少量词；不能注入新章节，不能拿模型参数。
- **隐蔽性**：不是显式目标，但因为修改极小（在论文实测里 0.03%–0.06% 的词量），与"加内容"相比几乎不可能在文本层被检出。

这把"投毒"从语料噪声问题重新定义为**对受信源的轻量编辑**问题：受害方不是放任未审阅的外部资料进来，而是日常依赖的 Wikipedia / 内部 wiki 被改了几个词。论文据此分两条线展开：TKPA 改一个查询的答案（precision），UKPA 让整个图断裂以广泛降级推理（breadth）。

边界与误区：

- 这套威胁针对 GraphRAG 这种"先把全部语料编译成图、再回答"的流水线；普通 chunk-RAG 因为没有持久结构，受影响方式不同。
- "只改字"不等于"加干扰词"——论文中的 Naive Swap 基线就是直接塞情感词，ASR 只有 16%；改字必须**配合图论或语言学结构**才有杀伤力。
- 不要把这套攻击混同为"提示注入"：注入的是事实层面的措辞，而非指令；LLM 不被劫持，被劫持的是它的知识源结构。

## References

- 论文 Abstract、Introduction 与 Attack Model 节明确将"editing the source corpus rather than injecting entirely new documents"立为新攻击面（`data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt`，第 157–230、284–296 行）。

## Footnotes

- `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` L197–199：*"An unexplored question is whether GraphRAG is also vulnerable when the adversary cannot add new text, but is only able to make small, subtle modifications to the existing corpus."*
- 同文件 L226–230：贡献列表标明 TKPA 改 48/94,496 词（<0.06%）即可 93.1% ASR；UKPA 改 60/134,072 词（<0.05%）即可让 QA 从 95% 跌到 50%。
