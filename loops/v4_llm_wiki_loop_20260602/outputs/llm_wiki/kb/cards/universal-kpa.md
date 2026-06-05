---
id: universal-kpa
title: 通用知识投毒攻击（UKPA）
status: accepted
card_type: mechanism
tags: [graphrag, adversarial-attack, linguistic-cues, pronouns, dependency-parsing, universal-attack]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graph-poisoning]
justification: ../justification/universal-kpa.md
canonical_concept: universal-kpa
aliases: [UKPA, Universal KPA, 通用知识投毒, universal knowledge poisoning attack]
summary: >-
  universal-kpa（UKPA, 通用知识投毒, Universal KPA）利用代词和依存关系等语言学线索篡改全局影响力词汇，仅修改不到 0.05% 的文本即可将 GraphRAG 问答准确率从 95% 降至 50%
related: [graphrag-knowledge-poisoning-attack, targeted-kpa, text-perturbation-amplification]
---

通用知识投毒攻击（Universal Knowledge Poisoning Attack, UKPA）是 KPA 的第二种变体，其目标不是精确控制特定问答，而是大规模破坏 GraphRAG 系统的整体问答能力 [^src-1]。UKPA 利用语言学线索（linguistic cues）——特别是代词（pronouns）和依存关系（dependency relations）——来识别并篡改具有全局影响力的词汇，从而破坏生成图谱的结构完整性 [^src-2]。该攻击展现了极端的效率：仅修改全文不到 0.05% 的内容，就能将问答准确率从 95% 急剧下降到 50% [^src-3]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graph-poisoning/text.txt` -- Abstract -- "The second attack, named Universal KPA (UKPA), exploits linguistic cues such as pronouns and dependency relations to disrupt the structural integrity of the generated graph"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graph-poisoning/text.txt` -- Abstract -- "exploits linguistic cues such as pronouns and dependency relations to disrupt the structural integrity of the generated graph by altering globally influential words"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graph-poisoning/text.txt` -- Abstract -- "With fewer than 0.05% of full text modified, the QA accuracy collapses from 95% to 50%"
