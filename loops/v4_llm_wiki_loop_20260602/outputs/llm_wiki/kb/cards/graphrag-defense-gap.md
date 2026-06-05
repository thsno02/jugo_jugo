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
related: [graphrag-knowledge-poisoning-attack, model-capability-security-disconnect, rag-poisoning-defense-insufficiency, text-perturbation-amplification]
---

截至该论文发表时（2025 年 8 月），现有最先进的防御方法（state-of-the-art defense methods）无法检测针对 GraphRAG 的知识投毒攻击 [^src-1]。论文明确指出，保护 GraphRAG 管道免受知识投毒攻击仍然是一个"基本未探索"（largely unexplored）的研究方向 [^src-2]。这一防御空白意味着当前部署的 GraphRAG 系统在面对精心设计的文本层面攻击时缺乏有效的检测和防护手段，尤其考虑到攻击所需的文本修改量极小（<0.05%）且修改后文本保持自然流畅 [^src-3]。eTAMP 论文的发现进一步表明，即使在 agent 记忆领域，更强大的模型也不必然更安全——能力与安全性脱钩是跨系统的普遍现象[^card-1]。PoisonedRAG 对标准 RAG 的四种防御策略的系统性评估同样证实了防御不足的普遍性[^card-2]。

## Footnotes

[^card-1]: [模型能力与安全性的脱钩](model-capability-security-disconnect.md) -- GraphRAG 的防御空白（现有方法无法检测投毒）与 eTAMP 的能力-安全脱钩（更强模型不更安全）共同揭示 LLM 知识系统在安全防御方面的系统性不足
[^card-2]: [现有防御对 RAG 知识腐蚀攻击的不充分性](rag-poisoning-defense-insufficiency.md) -- 本卡聚焦 GraphRAG 系统完全缺乏有效防御，该卡聚焦标准 RAG 的四种具体防御策略（释义、困惑度、去重、知识扩展）均告失败

[^src-1]: `data/raw/arxiv/arxiv-graph-poisoning/text.txt` -- Abstract -- "experiments show that state-of-the-art defense methods fail to detect these attacks"
[^src-2]: `data/raw/arxiv/arxiv-graph-poisoning/text.txt` -- Abstract -- "highlighting that securing GraphRAG pipelines against knowledge poisoning remains largely unexplored"
[^src-3]: `data/raw/arxiv/arxiv-graph-poisoning/text.txt` -- Abstract -- "while keeping the poisoned text fluent and natural"
