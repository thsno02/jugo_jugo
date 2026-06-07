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

定向知识投毒攻击（Targeted Knowledge Poisoning Attack, TKPA）是 KPA 的第一种变体，其目标是精确控制 GraphRAG 系统对特定问题的回答结果 [^src-1]。TKPA 的机制分为两步：首先利用图论分析（graph-theoretic analysis）定位生成图谱中的脆弱节点（vulnerable nodes），然后使用 LLM 改写这些节点所对应的源文本叙述 [^src-2]。该攻击在实验中达到了 93.1% 的成功率，同时保持被投毒文本的流畅性和自然性，使其难以通过文本质量检测发现 [^src-3]。与 TKPA 的精确控制策略形成对比，UKPA 则选择大规模破坏整体问答能力而非针对单个问题[^dist-1]。

## Footnotes

[^dist-1]: [通用知识投毒攻击（UKPA）](universal-kpa.md) -- 本卡主张通过图论分析精确控制特定问答结果（定向投毒，93.1% 精确控制），该卡主张通过语言学线索大规模破坏整体问答能力（通用投毒，<0.05% 修改量使准确率从 95% 降至 50%），区分点在于攻击目标粒度：精确操控 vs 全局破坏

[^src-1]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- Abstract -- "The first attack, named Targeted KPA (TKPA), utilizes graph-theoretic analysis to locate vulnerable nodes in the generated graphs"
[^src-2]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- Abstract -- "rewrites the corresponding narratives with LLMs, achieving precise control over specific question-answering (QA) outcomes"
[^src-3]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- Abstract -- "with a success rate of 93.1%, while keeping the poisoned text fluent and natural"
