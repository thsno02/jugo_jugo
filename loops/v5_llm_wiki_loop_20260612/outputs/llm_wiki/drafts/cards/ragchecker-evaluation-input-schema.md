---
id: ragchecker-evaluation-input-schema
title: RAGChecker 评估输入数据格式规范
status: draft
card_type: data-schema
tags: [rag-evaluation, input-format, json-schema, ground-truth]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-amazon-ragchecker]
evidence_basis: code_implementation
justification: ../justification/ragchecker-evaluation-input-schema.md
canonical_concept: ragchecker-evaluation-input-schema
aliases: [RAGChecker input format, checking_inputs.json, RAGChecker data format]
summary: >-
  RAGChecker 评估输入为 JSON 格式，顶层 results 数组包含多个 query 对象，
  每个 query 包含 query_id query gt_answer response retrieved_context 字段，
  其中 gt_answer (ground truth answer) 是唯一必需的人工标注，retrieved_context
  为检索块列表含 doc_id 和 text。该格式要求使用者提供完整的 RAG pipeline
  输出（检索结果+生成回答）以及参考答案。
related: [ragchecker-claim-level-rag-evaluation-framework]
---

RAGChecker 的评估输入采用结构化 JSON 格式，要求使用者提供完整的 RAG pipeline 执行结果及参考答案：[^src-1] [^card-1]

每个评估单元包含以下字段：
- **query_id**: 查询标识符 (string)
- **query**: 输入查询 (string)
- **gt_answer**: ground truth answer (string) -- 唯一必需的人工标注
- **response**: RAG 生成器产生的回答 (string)
- **retrieved_context**: 检索器返回的文档块列表，每个块含 doc_id (string, optional) 和 text (string)

这一设计意味着 RAGChecker 是一个 post-hoc 评估工具：需要先运行完整的 RAG pipeline 得到检索结果和生成回答，再连同人工标注的参考答案一起提交评估。评估的最低门槛是准备 ground truth answer，检索结果和生成回答由待评估系统自动产生。[^src-2]

[^src-1]: `data/raw/github_repo/repo-amazon-ragchecker/repo/README.md` -- "Run the Checking Pipeline with CLI" P1 -- "The only required annotation for each query is the ground truth answer (gt_answer)."
[^src-2]: `data/raw/github_repo/repo-amazon-ragchecker/repo/README.md` -- "Run the Checking Pipeline with CLI" P1 -- "query_id... query... gt_answer... response... retrieved_context: [{ doc_id... text... }]"
[^card-1]: ragchecker-claim-level-rag-evaluation-framework
