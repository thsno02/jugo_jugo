---
id: poisonedrag-cross-llm-transferability
title: PoisonedRAG 跨 LLM 迁移性
status: accepted
card_type: experimental-finding
tags:
- poisonedrag
- transferability
- llm-agnostic
- gpt-4
- llama
- palm
- vicuna
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-poisonedrag
evidence_basis: experimental_paper
justification: ../justification/poisonedrag-cross-llm-transferability.md
canonical_concept: poisonedrag-cross-llm-transferability
aliases:
- cross-LLM transferability
- LLM-agnostic attack
- 跨模型迁移攻击
summary: 'PoisonedRAG 的恶意文本对 RAG 中使用的 LLM 种类不敏感, 攻击者无需知道目标 RAG 使用哪个 LLM。在 8 种 LLM (PaLM 2, GPT-4, GPT-3.5, LLaMA-2-7B/13B, Vicuna-7B/13B/33B) 上均保持高 ASR (NQ 黑盒: 0.88-0.97)。甚至攻击用弱 LLM 生成 I、目标 RAG 用强 LLM,
  攻击仍有效。LLM 温度参数设为 1.0 时攻击效果不受影响。'
related:
- poisonedrag-generation-subtext-crafting
- poisonedrag-attack-success-scaling
---

PoisonedRAG 一个重要发现是攻击不依赖于被攻击 RAG 系统中具体使用的 LLM。

**8 种 LLM 上的 ASR (NQ, black-box)**:
- PaLM 2: 0.97, GPT-3.5: 0.92, GPT-4: 0.97
- LLaMA-2-7B: 0.97, LLaMA-2-13B: 0.95
- Vicuna-7B: 0.88, Vicuna-13B: 0.95, Vicuna-33B: 0.91 [^src-1]

**跨 LLM 生成迁移**: 用 GPT-4 生成的 I 对 PaLM 2 / LLaMA-2 等目标 LLM 均有效。反之，用弱 LLM (如 LLaMA-2-7B) 生成 I 时配合 in-context learning，ASR 在 NQ 上仍达 0.91-0.99。[^src-2]

**温度鲁棒性**: 将 LLM 温度从 0.1 (默认) 升至 1.0，ASR 基本不变。[^src-3]

原因分析: 恶意文本本质是语义层面的误导性知识而非对抗性 token 序列，因此对不同 LLM 普遍有效。

[^src-1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Evaluation / Main Results Table" -- "PaLM 2 0.97 GPT-3.5 0.92 GPT-4 0.97 LLaMA-2-7B 0.97"
[^src-2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Evaluation / Impact of LLM in generating I" -- "effective when using less powerful LLMs"
[^src-3]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "appendix / temperature 1.0 results" -- "the effectiveness of PoisonedRAG is unaffected by the randomness in the decoding process"
[^card-1]: [poisonedrag-generation-subtext-crafting]
