---
id: graphrag-defense-gap
title: GraphRAG 知识投毒防御空白
status: accepted
card_type: source_claim
tags: [graphrag, security, defense, open-problem, adversarial-robustness]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graph-poisoning]
justification: ../justification/graphrag-defense-gap.md
canonical_concept: graphrag-defense-gap
aliases: [GraphRAG 防御空白, GraphRAG defense gap, 知识投毒检测失败]
summary: >-
  graphrag-defense-gap（GraphRAG 防御空白, 知识投毒检测失败）现有最先进的防御方法无法检测针对 GraphRAG 的知识投毒攻击，该安全领域仍处于基本未探索状态
related: [graphrag-knowledge-poisoning-attack, text-perturbation-amplification]
---

截至该论文发表时（2025 年 8 月），现有最先进的防御方法（state-of-the-art defense methods）无法检测针对 GraphRAG 的知识投毒攻击 [^src-1]。论文明确指出，保护 GraphRAG 管道免受知识投毒攻击仍然是一个"基本未探索"（largely unexplored）的研究方向 [^src-2]。这一防御空白意味着当前部署的 GraphRAG 系统在面对精心设计的文本层面攻击时缺乏有效的检测和防护手段，尤其考虑到攻击所需的文本修改量极小（<0.05%）且修改后文本保持自然流畅 [^src-3]。eTAMP 论文的发现进一步表明，即使在 agent 记忆领域，更强大的模型也不必然更安全——能力与安全性脱钩是跨系统的普遍现象[^card-1]。

## Footnotes

[^card-1]: [模型能力与安全性的脱钩](model-capability-security-disconnect.md) -- GraphRAG 的防御空白（现有方法无法检测投毒）与 eTAMP 的能力-安全脱钩（更强模型不更安全）共同揭示 LLM 知识系统在安全防御方面的系统性不足

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graph-poisoning/text.txt` -- Abstract -- "experiments show that state-of-the-art defense methods fail to detect these attacks"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graph-poisoning/text.txt` -- Abstract -- "highlighting that securing GraphRAG pipelines against knowledge poisoning remains largely unexplored"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graph-poisoning/text.txt` -- Abstract -- "while keeping the poisoned text fluent and natural"
