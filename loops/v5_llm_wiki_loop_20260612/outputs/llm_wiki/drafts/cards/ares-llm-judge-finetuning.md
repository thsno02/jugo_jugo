---
id: ares-llm-judge-finetuning
title: ARES 轻量 LLM Judge 微调
status: draft
card_type: mechanism
tags: [llm-judge, deberta, contrastive-learning, finetuning, rag-evaluation]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ares]
evidence_basis: experimental_paper
justification: ../justification/ares-llm-judge-finetuning.md
canonical_concept: ares-llm-judge-finetuning
aliases: [ARES LLM judge, fine-tuned LLM judge, ARES judge training]
summary: >-
  ARES 使用 DeBERTa-v3-Large (304M) 作为 judge 基座，以对比学习目标在合成三元组上微调三个独立的二分类 judge，分别评估 context relevance、answer faithfulness、answer relevance。训练使用 cross-entropy loss + Adam、5e-6 学习率、batch size 32、early stopping（3 epoch 无改善）。设计目标是摆脱外部 API 依赖，可部署在商用 GPU 上。
related: []
---

ARES 选择 DeBERTa-v3-Large (304M 参数) 作为 judge 基座模型，目标是在商用 GPU 上独立部署而不依赖外部 API。[^src-1]

三个独立 judge 分别训练：(1) Context Relevance -- 检索段落是否与 query 相关；(2) Answer Faithfulness -- 生成答案是否忠实于检索段落；(3) Answer Relevance -- 答案是否与 query 和段落相关。[^src-2]

分类头使用单层线性层 + 0.1 dropout，输入为 [CLS] token 的 final hidden state。损失函数为 cross-entropy，优化器 Adam，学习率 5e-6，batch size 32，线性 warmup + 线性 decay，early stopping 于 3 epoch 无改善。[^src-3]

实验证明微调 DeBERTa judge + PPI 优于 few-shot GPT-3.5 judge，表明轻量级领域适配 judge 的有效性。[^src-4]

[^card-1]: [^ref→ares-automated-rag-evaluation-system] 三阶段流程之阶段 2
[^card-2]: [^ref→ares-synthetic-data-generation] 合成数据作为训练输入

[^src-1]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "experiments.tex" P512-513 -- "We selected DeBERTa-v3-Large for our fine-tuned LLM judge...without relying on external APIs"
[^src-2]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "methods.tex" P730-734 -- "Context Relevance...Answer Faithfulness...Answer Relevance"
[^src-3]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "appendix.tex" P298-303 -- "cross-entropy loss using Adam...5e-6 learning rate and a 32 training batch size"
[^src-4]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P824-826 -- "the fine-tuned LLM judge of ARES can more precisely distinguish between RAG systems"
