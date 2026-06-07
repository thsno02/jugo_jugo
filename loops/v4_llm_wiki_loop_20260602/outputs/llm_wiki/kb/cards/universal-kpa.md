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

通用知识投毒攻击（Universal Knowledge Poisoning Attack, UKPA）是 KPA 的第二种变体，其目标不是精确控制特定问答，而是大规模破坏 GraphRAG 系统的整体问答能力 [^src-1]。UKPA 利用语言学线索（linguistic cues）——特别是代词（pronouns）和依存关系（dependency relations）——来识别并篡改具有全局影响力的词汇，从而破坏生成图谱的结构完整性 [^src-2]。该攻击展现了极端的效率：仅修改全文不到 0.05% 的内容，就能将问答准确率从 95% 急剧下降到 50% [^src-3]。与 UKPA 的全局破坏策略形成对比，TKPA 则追求对特定问答结果的精确控制[^dist-1]。

## Footnotes

[^dist-1]: [定向知识投毒攻击（TKPA）](targeted-kpa.md) -- 本卡主张通过语言学线索大规模破坏整体问答能力（通用投毒，<0.05% 修改量使准确率从 95% 降至 50%），该卡主张通过图论分析精确控制特定问答结果（定向投毒，93.1% 成功率），区分点在于攻击目标粒度：全局破坏 vs 精确操控

[^src-1]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- Abstract -- "The second attack, named Universal KPA (UKPA), exploits linguistic cues such as pronouns and dependency relations to disrupt the structural integrity of the generated graph"
[^src-2]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- Abstract -- "exploits linguistic cues such as pronouns and dependency relations to disrupt the structural integrity of the generated graph by altering globally influential words"
[^src-3]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` -- Abstract -- "With fewer than 0.05% of full text modified, the QA accuracy collapses from 95% to 50%"
