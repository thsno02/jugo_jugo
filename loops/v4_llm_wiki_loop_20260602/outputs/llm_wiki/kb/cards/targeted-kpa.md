---
id: targeted-kpa
title: 定向知识投毒攻击（TKPA）
status: accepted
card_type: mechanism
tags: [graphrag, adversarial-attack, graph-theory, node-vulnerability, targeted-attack]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graph-poisoning]
justification: ../justification/targeted-kpa.md
canonical_concept: targeted-kpa
aliases: [TKPA, Targeted KPA, 定向知识投毒, targeted knowledge poisoning attack]
summary: >-
  targeted-kpa（TKPA, 定向知识投毒, Targeted KPA）利用图论分析定位知识图谱中的脆弱节点并用 LLM 改写对应叙述文本，以 93.1% 成功率精确控制特定问答结果且保持文本自然流畅
related: [graphrag-knowledge-poisoning-attack, universal-kpa]
---

定向知识投毒攻击（Targeted Knowledge Poisoning Attack, TKPA）是 KPA 的第一种变体，其目标是精确控制 GraphRAG 系统对特定问题的回答结果 [^src-1]。TKPA 的机制分为两步：首先利用图论分析（graph-theoretic analysis）定位生成图谱中的脆弱节点（vulnerable nodes），然后使用 LLM 改写这些节点所对应的源文本叙述 [^src-2]。该攻击在实验中达到了 93.1% 的成功率，同时保持被投毒文本的流畅性和自然性，使其难以通过文本质量检测发现 [^src-3]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graph-poisoning/text.txt` -- Abstract -- "The first attack, named Targeted KPA (TKPA), utilizes graph-theoretic analysis to locate vulnerable nodes in the generated graphs"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graph-poisoning/text.txt` -- Abstract -- "rewrites the corresponding narratives with LLMs, achieving precise control over specific question-answering (QA) outcomes"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graph-poisoning/text.txt` -- Abstract -- "with a success rate of 93.1%, while keeping the poisoned text fluent and natural"
