---
id: text-perturbation-amplification
title: 文本微扰的图谱放大效应
status: accepted
card_type: mechanism
tags: [graphrag, adversarial-robustness, amplification, knowledge-graph-construction, fragility]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graph-poisoning]
justification: ../justification/text-perturbation-amplification.md
canonical_concept: text-perturbation-amplification
aliases: [微扰放大效应, perturbation amplification, 文本-图谱放大]
summary: >-
  text-perturbation-amplification（微扰放大效应, perturbation amplification）GraphRAG 图谱构建过程将极小的文本修改（<0.05%）放大为大规模图谱结构变化，暴露了 LLM 驱动的知识提取管道的内在脆弱性
related: [graphrag-defense-gap, graphrag-knowledge-poisoning-attack, universal-kpa]
---

GraphRAG 的图谱构建过程存在一种显著的微扰放大效应（perturbation amplification）：源文本中极小比例的修改会被 LLM 驱动的知识提取过程放大为知识图谱结构层面的大规模变化 [^src-1]。论文的两种攻击均利用了这一特性——TKPA 通过修改"少量词语"实现 93.1% 的定向攻击成功率 [^src-2]，UKPA 仅修改不到 0.05% 的文本即可将系统整体问答准确率从 95% 击溃至 50% [^src-3]。这种不对称性意味着 GraphRAG 管道中从文本到图谱的转换步骤是一个脆弱的放大器，微小的输入扰动会在图结构中产生不成比例的影响。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- Abstract -- "modifying only a few words in the source text can significantly change the constructed graph, poison the GraphRAG, and severely mislead downstream reasoning"
[^src-2]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- Abstract -- "achieving precise control over specific question-answering (QA) outcomes with a success rate of 93.1%"
[^src-3]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- Abstract -- "With fewer than 0.05% of full text modified, the QA accuracy collapses from 95% to 50%"
