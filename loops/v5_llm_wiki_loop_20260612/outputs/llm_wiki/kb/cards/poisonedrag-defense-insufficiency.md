---
id: poisonedrag-defense-insufficiency
title: 现有防御对 PoisonedRAG 不充分
status: accepted
card_type: experimental-finding
tags:
- poisonedrag
- defense
- paraphrasing
- perplexity
- duplicate-filtering
- knowledge-expansion
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-poisonedrag
evidence_basis: experimental_paper
justification: ../justification/poisonedrag-defense-insufficiency.md
canonical_concept: poisonedrag-defense-insufficiency
aliases:
- defense against PoisonedRAG
- RAG defense evaluation
- 防御不充分性
summary: '论文评估四种防御均不足以抵御 PoisonedRAG: (1) Paraphrasing——改写目标问题后 ASR 仍达 79-93%; (2) Perplexity 检测——恶意文本 PPL 与正常文本无显著差异(因 I 由 GPT-4 生成质量高); (3) Duplicate filtering——因 I 每次生成不同，SHA-256 去重无效(ASR 不变); (4) Knowledge
  expansion (k=50)——ASR 仍达 41-43% 且增加 N 可进一步提升。四种防御均为事后策略, 论文呼吁开发新防御。'
related:
- poisonedrag-black-box-attack
- poisonedrag-generation-subtext-crafting
- poisonedrag-attack-success-scaling
- poisonedrag-advanced-rag-vulnerability
---
PoisonedRAG 论文系统评估了四种防御策略:

**1. Paraphrasing (问题改写)**
- 将目标问题用 GPT-4 改写 5 个版本后再检索
- ASR 下降有限: NQ BB 0.97→0.87, WB 0.97→0.93; HotpotQA BB 0.99→0.93
- 原因: 恶意文本与改写后的问题仍语义相关[^src-1]

**2. Perplexity (PPL) 检测**
- 用 PPL 区分恶意文本与正常文本
- ROC 分析: AUC 低，FPR 与 TPR 同步升高
- 原因: I 由 GPT-4 生成文本质量高；黑盒 S=Q 也是正常文本[^src-2]

**3. Duplicate text filtering (去重)**
- 用 SHA-256 去重
- 完全无效: ASR 不变
- 原因: 温度参数使每次生成的 I 不同[^src-3]

**4. Knowledge expansion (扩大 k)**
- 增加检索量 k=50 (比 N=5 大 10 倍)
- ASR 仍有 41% (HotpotQA BB)，且增加 N 即可反制[^src-4]

[^src-1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Defenses / Paraphrasing" -- "PoisonedRAG could still achieve high ASRs... paraphrasing defense cannot effectively defend"
[^src-2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Defenses / Perplexity-based Detection" -- "the perplexity values of malicious texts are not statistically higher than those of clean texts"
[^src-3]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Defenses / Duplicate Text Filtering" -- "the ASR is the same... duplicate text filtering cannot successfully filter"
[^src-4]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Defenses / Knowledge Expansion" -- "this defense still cannot completely defend... 41% ASR on HotpotQA when k=50"
[^card-1]: [poisonedrag-generation-subtext-crafting]
