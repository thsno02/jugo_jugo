---
id: longmemeval-dataset-variants
title: LongMemEval 数据集三种规模变体
status: draft
card_type: dataset-design
tags: [dataset, long-context, scalability, evaluation]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-longmemeval]
evidence_basis: code_implementation
justification: ../justification/longmemeval-dataset-variants.md
canonical_concept: longmemeval-dataset-variants
aliases: [LongMemEval_S, LongMemEval_M, longmemeval_oracle, longmemeval_s, longmemeval_m]
summary: >-
  LongMemEval (longmemeval-dataset-variants) 提供三种规模变体:
  longmemeval_oracle (仅证据 session, oracle retrieval 上界),
  longmemeval_s / LongMemEval_S (~115k tokens, ~40 sessions, 适配 128k context),
  longmemeval_m / LongMemEval_M (~500 sessions, 超出 128k, 用于检索增强测试).
  支持属性控制管线编排任意长度历史以扩展难度.
related: [longmemeval-benchmark-overview, longmemeval-five-memory-abilities, longmemeval-retrieval-augmentation]
---

LongMemEval 提供三种不同规模的数据集变体，服务于不同评测场景。[^src-1]

**longmemeval_oracle**: 仅包含证据 session（evidence sessions），作为 oracle retrieval 的性能上界参考。history session 未按时间排序。[^src-1]

**longmemeval_s (LongMemEval_S)**: 拼接所有对话历史约消耗 115k tokens（基于 Llama 3 分词），包含约 40 个 history sessions。设计适配 128k context 窗口模型的 full-history 测试。[^src-1]

**longmemeval_m (LongMemEval_M)**: 每条对话历史包含约 500 个 sessions，超出 128k context 限制，专为测试检索增强系统设计，不适合直接作为 long-context 输入。[^src-2]

LongMemEval 还支持通过属性控制管线编排任意长度的自定义对话历史，混入来自 ShareGPT 和 UltraChat 的 filler sessions 以及基于用户背景模拟的 sessions，从而可在 LongMemEval_M 基础上进一步扩展难度。[^src-3]

[^src-1]: data/raw/github_repo/repo-longmemeval/repo/README.md -- "Dataset Format" P1 -- "longmemeval_s.json: ...roughly consumes 115k tokens (~40 history sessions) for Llama 3"
[^src-2]: data/raw/github_repo/repo-longmemeval/repo/README.md -- "Long-Context Generation" P1 -- "longmemeval_m.json is too long for long-context testing"
[^src-3]: data/raw/github_repo/repo-longmemeval/repo/README.md -- "Creating Custom Chat Histories" P1 -- "LongMemEval supports compiling a chat history of arbitrary length for a question instance"

[^card-1]: longmemeval-benchmark-overview -- 基准整体定位
[^card-2]: longmemeval-five-memory-abilities -- 五类记忆能力定义
