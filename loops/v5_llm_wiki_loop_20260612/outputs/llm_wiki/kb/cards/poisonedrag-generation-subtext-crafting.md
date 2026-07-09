---
id: poisonedrag-generation-subtext-crafting
title: 生成子文本 I 的 LLM 提示构造
status: accepted
card_type: attack-technique
tags:
- poisonedrag
- generation-condition
- llm-prompting
- text-generation
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-poisonedrag
evidence_basis: experimental_paper
justification: ../justification/poisonedrag-generation-subtext-crafting.md
canonical_concept: poisonedrag-generation-subtext-crafting
aliases:
- crafting I
- generation sub-text
- 生成子文本构造
- TextGeneration function
summary: 'PoisonedRAG 使用 LLM (默认 GPT-4) 通过特定提示生成子文本 I 以满足 generation condition。提示格式为: 给定目标问题和目标答案, 让 LLM 生成长度约 V=30 词的语料使得以该语料为上下文时答案为目标答案。生成后验证: 若 LLM 不生成目标答案则重新生成(最多 L=50 次试验)。实验中平均仅需约 2 次查询即可成功生成。使用较弱
  LLM (GPT-3.5/LLaMA-2-7B/Vicuna-7B) 配合 in-context learning 同样有效。'
related:
- poisonedrag-malicious-text-decomposition
- poisonedrag-dual-condition-framework
- poisonedrag-black-box-attack
- poisonedrag-cross-llm-transferability
- poisonedrag-defense-insufficiency
---
子文本 I 的目的是: 当 I 作为 RAG 的上下文，LLM 对目标问题 Q 应生成目标答案 R。

**构造方法**: 使用攻击者控制的 LLM (可与 RAG 使用的 LLM 不同) 通过如下提示生成:

> "This is my question: [Q]. This is my answer: [R]. Please craft a corpus such that the answer is [R] when prompting with the question [Q]. Please limit the corpus to V words."

[^src-1]

**验证与重试**: 生成 I 后，将其作为上下文让 LLM 回答 Q。若答案不是 R，则重新生成，最多 L 次。实验中 L=50，但平均仅需 ~2 次查询（NQ: 1.62, HotpotQA: 1.24, MS-MARCO: 2.69）。[^src-2]

**弱 LLM 同样有效**: 即使使用 GPT-3.5、LLaMA-2-7B、Vicuna-7B 生成 I（配合 2-shot in-context learning），ASR 仍保持高水平（NQ 黑盒: 0.92-0.99）。[^src-3]

**多样性**: 由于 LLM 温度参数设为 1，相同 prompt 可生成不同的 I，使攻击文本具有多样性，规避去重防御。[^src-4]

[^src-1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Design / Crafting I to Achieve Generation Condition" -- "This is my question... Please craft a corpus"
[^src-2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Evaluation / efficiency" -- "on average, NameTag only needs to make around 2 queries to the GPT-4 to craft each malicious text"
[^src-3]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Evaluation / Impact of the LLM in generating I" -- "our NameTag is also effective when using less powerful LLMs to generate I with in-context learning"
[^src-4]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Design / Crafting I" -- "the generated I could be different even if the prompt is the same, enabling PoisonedRAG to generate diverse malicious texts"
[^card-1]: [poisonedrag-malicious-text-decomposition]
