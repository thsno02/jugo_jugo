---
id: poisonedrag-attack-success-scaling
title: PoisonedRAG 攻击成功率与注入量的关系
status: accepted
card_type: experimental-finding
tags:
- poisonedrag
- asr
- scaling
- injection-count
- top-k
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-poisonedrag
evidence_basis: experimental_paper
justification: ../justification/poisonedrag-attack-success-scaling.md
canonical_concept: poisonedrag-attack-success-scaling
aliases:
- ASR vs N
- attack scaling
- 注入数量与攻击成功率
summary: 'PoisonedRAG 在百万级知识库中仅注入 N=5 条恶意文本(每目标问题)即可达约 90%+ ASR。ASR 随 N 增加而增加(N≤k 时), N>k 后趋于饱和。当 k=5 时 top-k 检索结果中含的恶意文本数量与 ASR 呈正相关: 1 条 ASR~0.4-0.5, 3 条 ASR~0.75-0.91, 5 条 ASR~0.94-1.0。该结果表明仅需少量注入(相对百万级库)即构成严重威胁。'
related:
- poisonedrag-dual-condition-framework
- poisonedrag-black-box-attack
- poisonedrag-cross-llm-transferability
- poisonedrag-defense-insufficiency
- poisonedrag-failure-modes
- poisonedrag-nontarget-question-impact
- poisonedrag-wikipedia-chatbot-attack
---
PoisonedRAG 攻击的一个核心实验发现是: 在百万级文本知识库中仅需注入极少量恶意文本即可实现高 ASR。

**N vs ASR 关系** (k=5 默认):
- N≤k 时 ASR 随 N 单调递增
- N>k 时 ASR 趋于饱和（因 top-k 中最多包含 k 条恶意文本）
- N=5 时: NQ 0.97, HotpotQA 0.99, MS-MARCO 0.91 (black-box)[^src-1]

**检索结果中恶意文本数量的影响** (k=5, 五条中分别有 1-5 条恶意):
- NQ black-box: 1条→0.48, 2条→0.76, 3条→0.84, 4条→0.90, 5条→1.00
- 规律: 当多数 (≥3/5) 检索文本为恶意时 ASR 显著升高[^src-2]

**绝对比例极低**: 5 条恶意文本相对 NQ 的 2,681,468 条总文本，注入比例仅约 0.0002%。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Evaluation / Main Results" -- "PoisonedRAG could achieve a 90% attack success rate when injecting five malicious texts"
[^src-2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "appendix / effectiveness when k retrieved texts contain different number of malicious ones" -- "1: 0.48, 2: 0.76, 3: 0.84, 4: 0.90, 5: 1.00"
[^src-3]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Evaluation / Main Results Table caption" -- "inject 5 malicious texts for each target question into a knowledge database with 2,681,468 clean texts"
[^card-1]: [poisonedrag-dual-condition-framework]
