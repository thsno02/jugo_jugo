---
id: poisonedrag-failure-modes
title: PoisonedRAG 攻击失败模式
status: accepted
card_type: limitation-analysis
tags:
- poisonedrag
- failure-case
- parametric-bias
- retrieval-failure
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-poisonedrag
evidence_basis: experimental_paper
justification: ../justification/poisonedrag-failure-modes.md
canonical_concept: poisonedrag-failure-modes
aliases:
- PoisonedRAG failure cases
- attack failure analysis
- 攻击失败分析
summary: 'PoisonedRAG 未达 100% ASR 的两类失败模式: (1) 检索失败——部分恶意文本未被检索出, top-k 中混入干净文本导致 LLM 生成正确答案; (2) 参数偏置(parametric bias)——恶意文本自身包含正确答案, LLM 倾向于生成正确答案而非目标答案。第二类源暗示 LLM 存在对训练时记忆的事实的偏好。此外, 使用 "in an alternate
  universe" 等表述会被 GPT-4 识别为虚构。'
related:
- poisonedrag-attack-success-scaling
- poisonedrag-dual-condition-framework
---

PoisonedRAG 在部分情况下未能达到 100% ASR，论文分析了两类失败原因:

**失败模式 1: 检索失败**
- 某些恶意文本未能进入 top-k 检索结果
- top-k 中混入的干净文本包含正确答案，使 LLM 生成正确答案
- 例: 目标问题 "Who wrote the song what child is this?"，恶意文本未被全部检索，干净文本中含正确答案 "William Chatterton Dix"[^src-1]

**失败模式 2: 参数偏置 (parametric bias)**
- 恶意文本在构造过程中无意包含了正确答案
- 即使 k 条检索结果全为恶意文本，LLM 仍可能输出正确答案
- 例: 目标答案为 "sulfate ion"，但恶意文本中提及 "typically known as the acetate ion"，LLM 选择了正确的 "acetate ion"[^src-2]
- 该现象与已有研究中观察到的 parametric bias 一致 (Kortukov et al., 2024)

**额外发现**: 使用 "In an alternate universe" 等虚构框架表述时，GPT-4 能识别其为虚构，拒绝将虚构答案作为真实答案。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "appendix / Failure Case Analysis" -- "The top-k retrieved texts contain some clean ones"
[^src-2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "appendix / Failure Case Analysis" -- "the malicious texts themselves contain the correct answer"
[^src-3]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "appendix / Human Evaluation" -- "the answer says that the target answer is the answer in an alternate universe"
[^card-1]: [poisonedrag-attack-success-scaling]
