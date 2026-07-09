---
id: poisonedrag-fact-verification-extension
title: PoisonedRAG 可扩展至事实验证任务
status: accepted
card_type: experimental-finding
tags:
- poisonedrag
- fact-verification
- fever
- broader-nlp-tasks
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-poisonedrag
evidence_basis: experimental_paper
justification: ../justification/poisonedrag-fact-verification-extension.md
canonical_concept: poisonedrag-fact-verification-extension
aliases:
- FEVER dataset attack
- fact verification attack
- 事实验证攻击
summary: PoisonedRAG 的设计原则(retrieval + generation conditions)可扩展至问答之外的 NLP 任务。在 FEVER 事实验证数据集上, 攻击者可使 RAG 输出错误的验证结果(SUPPORTS/REFUTES/NOT ENOUGH INFO)。黑盒 ASR 0.97, 白盒 ASR 0.88, F1-Score 0.98-0.99。该结果表明知识腐蚀攻击对知识密集型
  NLP 任务具有普遍威胁。
related:
- poisonedrag-dual-condition-framework
- poisonedrag-black-box-attack
---

论文将 PoisonedRAG 扩展至事实验证(fact verification)任务，证明攻击不限于 QA:

**FEVER 数据集实验**:
- 任务: 给定一个声明(claim)，判断检索到的文本 SUPPORTS、REFUTES 或 NOT ENOUGH INFO
- 攻击者目标: 使系统输出错误的验证结果

**结果** (100 个目标 claims):
- F1-Score: 黑盒 0.98, 白盒 0.99 (几乎所有恶意文本被检索)
- ASR: 黑盒 0.97, 白盒 0.88 [^src-1]

**意义**: PoisonedRAG 的双条件框架具有通用性——只要任务涉及从知识库检索上下文并据此生成输出，知识腐蚀攻击就可能有效。论文指出 RAG 主要为"knowledge-intensive tasks"设计，因此大多数 RAG 应用均在威胁范围内。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Discussion / Broad NLP tasks" -- "achieve a 0.97 and 0.88 ASR in the black-box and white-box settings"
[^src-2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "Discussion" -- "RAG is mainly designed for knowledge-intensive tasks"
[^card-1]: [poisonedrag-dual-condition-framework]
