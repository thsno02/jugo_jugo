---
id: ares-three-evaluation-dimensions
title: ARES 的三维度 RAG 评估标准
status: superseded
superseded_by: ares-three-dimensional-rag-evaluation
card_type: concept-decomposition
tags: [context-relevance, answer-faithfulness, answer-relevance, evaluation-criteria]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-stanford-ares]
evidence_basis: code_implementation
justification: ../justification/ares-three-evaluation-dimensions.md
canonical_concept: ares-three-evaluation-dimensions
aliases: [Context_Relevance_Label, Answer_Faithfulness_Label, Answer_Relevance_Label, context relevance, answer faithfulness, answer relevance]
summary: >-
  ARES 评估 RAG 系统的三个维度：context relevance（检索文档与查询的相关性）、answer faithfulness（答案是否忠实于检索上下文、无幻觉）、answer relevance（答案是否回答了用户查询）。每个维度独立打分，对应 label 列名为 Context_Relevance_Label / Answer_Faithfulness_Label / Answer_Relevance_Label，可单独或联合训练分类器。
related: [ares-rag-evaluation-framework, ares-ppi-statistical-calibration]
---

ARES 将 RAG 系统评估分解为三个独立维度：(1) Context Relevance — 检索到的文档/段落是否与用户查询相关；(2) Answer Faithfulness — 生成的答案是否忠实于所检索的上下文（即不包含幻觉内容）；(3) Answer Relevance — 生成的答案是否切实回答了用户的查询。[^card-1] 在代码实现中，这三个维度分别对应 label 列名 Context_Relevance_Label、Answer_Faithfulness_Label、Answer_Relevance_Label，可在 few-shot prompt 和分类器训练中单独或联合使用。UES/IDP 接口同时返回三个维度的分数。[^src-1]

[^card-1]: 参见 [ares-rag-evaluation-framework] 对框架整体设计的描述
[^src-1]: `data/raw/github_repo/repo-stanford-ares/repo/README.md` -- "Mini Q&A" P1 -- "ARES conducts a comprehensive evaluation of Retrieval-Augmented Generation (RAG) models, assessing the systems for context relevance, answer faithfulness, and answer relevance."
