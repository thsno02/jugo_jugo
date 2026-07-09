---
id: poisonedrag-malicious-text-decomposition
title: 恶意文本分解策略 P=S+I
status: accepted
card_type: attack-technique
tags:
- poisonedrag
- text-decomposition
- adversarial-text
- malicious-text-crafting
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-poisonedrag
evidence_basis: experimental_paper
justification: ../justification/poisonedrag-malicious-text-decomposition.md
canonical_concept: poisonedrag-malicious-text-decomposition
aliases:
- P=S+I decomposition
- malicious text decomposition
- 恶意文本双子文本拼接
summary: 'PoisonedRAG 将恶意文本 P 分解为两个子文本的拼接 P=S⊕I: S 负责满足检索条件(retrieval condition)使 P 被检索出, I 负责满足生成条件(generation condition)使 LLM 生成目标答案。先通过 LLM 生成 I, 再据攻击设定(black-box/white-box)构造 S, 拼接后双条件同时满足。实验证明 S⊕I
  完整体显著优于单独使用 S 或 I。'
related:
- poisonedrag-dual-condition-framework
- poisonedrag-black-box-attack
- poisonedrag-white-box-attack
- poisonedrag-generation-subtext-crafting
- rag-knowledge-corruption-attack-surface
---
为同时满足检索条件和生成条件这一对可能冲突的需求，PoisonedRAG 将恶意文本 P 分解为两个子文本:

- **S (retrieval sub-text)**: 使 P 的 embedding 与目标问题 Q 高度相似，确保被检索
- **I (generation sub-text)**: 作为上下文时能诱导 LLM 生成目标答案 R

构造顺序: 先生成 I → 再构造 S → 拼接 P = S ⊕ I。[^src-1]

实验验证了完整拼接 S⊕I 的必要性: 在 NQ 数据集上，black-box 设定下 S⊕I 的 ASR 为 0.97，而单用 S 仅 0.03（能被检索但无法误导 LLM），单用 I 为 0.69（能误导但不一定被检索）。[^src-2]

拼接顺序（S⊕I vs I⊕S）对攻击效果影响不大，两种顺序均保持高 ASR。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Design of PoisonedRAG / Crafting Malicious Texts" -- "decompose the malicious text P into two disjoint sub-texts S and I, where P = S ⊕ I"
[^src-2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "appendix.tex / PoisonedRAG outperforms its two variants" -- "S⊕I ... ASR 0.97 ... S ... ASR 0.03 ... I ... ASR 0.69"
[^src-3]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Evaluation / Impact of concatenation order" -- "NameTag is also effective when we change their order"
[^card-1]: [poisonedrag-dual-condition-framework]
