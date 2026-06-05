---
id: graphrag-knowledge-poisoning-attack
title: GraphRAG 知识投毒攻击
status: accepted
card_type: concept
tags: [graphrag, adversarial-attack, knowledge-graph, security, rag]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graph-poisoning]
justification: ../justification/graphrag-knowledge-poisoning-attack.md
canonical_concept: graphrag-knowledge-poisoning-attack
aliases: [知识投毒攻击, KPA, knowledge poisoning attack, GraphRAG poisoning]
summary: >-
  graphrag-knowledge-poisoning-attack（KPA, 知识投毒攻击, GraphRAG poisoning）GraphRAG 依赖 LLM 从原始文本提取知识构建图谱，攻击者仅需修改少量原文词语即可显著扭曲生成的知识图谱并误导下游推理
related: [graphrag-extraction-attack-surface, targeted-kpa, universal-kpa, graphrag-defense-gap]
---

知识投毒攻击（Knowledge Poisoning Attack, KPA）是一种针对 Graph-based Retrieval-Augmented Generation（GraphRAG）系统的对抗攻击范式 [^src-1]。GraphRAG 通过将原始文本转换为结构化知识图谱来增强大语言模型的准确性和可解释性，但其图谱构建过程依赖 LLM 从原始文本中提取知识，这一环节可被恶意操纵以植入误导性信息 [^src-2]。KPA 的核心特征是攻击的高效性——仅需修改源文本中极少量的词语，就能显著改变所构建的图谱结构，进而严重误导下游问答推理 [^src-3]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graph-poisoning/text.txt` -- Abstract -- "we propose two knowledge poisoning attacks (KPAs) and demonstrate that modifying only a few words in the source text can significantly change the constructed graph"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graph-poisoning/text.txt` -- Abstract -- "GraphRAG relies on LLMs to extract knowledge from raw text during graph construction, and this process can be maliciously manipulated to implant misleading information"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graph-poisoning/text.txt` -- Abstract -- "modifying only a few words in the source text can significantly change the constructed graph, poison the GraphRAG, and severely mislead downstream reasoning"
