---
id: poisonedrag-white-box-attack
title: PoisonedRAG 白盒攻击
status: accepted
card_type: attack-technique
tags:
- poisonedrag
- white-box
- adversarial-text
- hotflip
- textfooler
- retriever-optimization
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-poisonedrag
evidence_basis: experimental_paper
justification: ../justification/poisonedrag-white-box-attack.md
canonical_concept: poisonedrag-white-box-attack
aliases:
- PoisonedRAG white-box
- 白盒知识腐蚀攻击
- white-box knowledge corruption
summary: PoisonedRAG 白盒(white-box)设定下攻击者可访问检索器参数(如公开的 Contriever)。通过对抗文本生成方法(HotFlip/TextFooler)优化 S, 最大化 f_Q(Q) 与 f_T(S⊕I) 之间的相似度。白盒攻击 F1-Score 通常为 1.0 (所有恶意文本均被检索), 平均每条恶意文本优化耗时约 26 秒。HotFlip 和 TextFooler
  两种方法均有效, TextFooler 更隐蔽但计算开销更高。
related:
- poisonedrag-malicious-text-decomposition
- poisonedrag-black-box-attack
- poisonedrag-dual-condition-framework
- poisonedrag-retriever-robustness
- poisonedrag-threat-model
---
白盒设定假设攻击者能访问检索器的参数（如 Contriever 等公开模型）。PoisonedRAG 将 S 的构造形式化为优化问题:

S = argmax_{S'} Sim(f_Q(Q), f_T(S' ⊕ I))

即寻找使 P=S⊕I 与目标问题 Q 的 embedding 最相似的 S。[^src-1]

初始化 S=Q，然后使用对抗文本生成方法求解:
- **HotFlip** (默认): token 级替换，约 26 秒/条，F1-Score 达 1.0[^src-2]
- **TextFooler**: 同义词替换保留语义，约 64-77 秒/条，更隐蔽但开销更高[^src-3]

白盒攻击在 NQ 上 ASR 达 0.97，F1-Score 1.0，表明所有恶意文本均被成功检索。在某些情况下白盒反而略低于黑盒 ASR，据材料推测原因为 HotFlip 可能轻微影响恶意文本的语义。[^src-4]

白盒设定具有现实性: NVIDIA ChatRTX 默认使用公开可获取的 WhereIsAI/UAE-Large-V1 检索器。[^src-5]

[^src-1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Design / White-box setting" -- "S = argmax_{S'} Sim(f_Q(Q), f_T(S' ⊕ I))"
[^src-2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Evaluation / efficiency" -- "it takes less than 30 seconds to optimize each malicious text in the white-box setting"
[^src-3]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "appendix / Computational overhead" -- "HotFlip 26.12 ... TextFooler 63.76"
[^src-4]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Evaluation / Main Results" -- "HotFlip slightly influences the semantics of malicious texts in these cases"
[^src-5]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Threat Model" -- "ChatRTX... uses WhereIsAI/UAE-Large-V1 retriever, which is publicly available on Hugging Face"
[^card-1]: [poisonedrag-black-box-attack]
