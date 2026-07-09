---
id: poisonedrag-black-box-attack
title: PoisonedRAG 黑盒攻击
status: draft
card_type: attack-technique
tags: [poisonedrag, black-box, retrieval-condition, question-prepend]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-poisonedrag]
evidence_basis: experimental_paper
justification: ../justification/poisonedrag-black-box-attack.md
canonical_concept: poisonedrag-black-box-attack
aliases: [PoisonedRAG black-box, 黑盒知识腐蚀攻击, black-box knowledge corruption]
summary: >-
  PoisonedRAG 黑盒(black-box)设定下攻击者无法访问检索器参数且无法查询检索器。核心思路: 设 S=Q (目标问题本身), 因为问题与自身语义最相似, 从而 P=Q⊕I 能被各种检索器检索出。I 由攻击者控制的 LLM (如 GPT-4) 通过提示生成。该策略简单高效, 在 NQ 数据集上达到 97% ASR, 构造每条恶意文本运行时间低于微秒级别。
related: [poisonedrag-malicious-text-decomposition, poisonedrag-white-box-attack, poisonedrag-generation-subtext-crafting]
---

在黑盒设定下，攻击者对 retriever 零知识（不知参数、不能查询）。PoisonedRAG 利用一个关键洞察: **目标问题 Q 与自身的语义相似度最高**。因此设 S = Q，恶意文本 P = Q ⊕ I。[^src-1]

该策略的优势:
- 无需关于 retriever 的任何信息
- 对不同类型的 retriever（Contriever、ANCE 等）普遍有效
- 运行时间极短（~1.45×10⁻⁶ 秒/条），因为仅需简单拼接[^src-2]

实验结果: 在 NQ 上 ASR 达 0.97，HotpotQA 上 0.99，MS-MARCO 上 0.91（均使用 PaLM 2 作为 RAG 的 LLM）。F1-Score 普遍 ≥0.89，表明恶意文本确实被高概率检索。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Design / Black-box setting" -- "our key insight is that the target question Q is most similar to itself... we propose to set S=Q"
[^src-2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Evaluation / efficiency" -- "far less than 1 second for PoisonedRAG to optimize the malicious text in the black-box setting"
[^src-3]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Evaluation / Main Results" -- "NameTag could achieve 97% (on NQ), 99% (on HotpotQA), and 91% (on MS-MARCO) ASRs"
[^card-1]: [poisonedrag-malicious-text-decomposition]
