---
id: longmemeval-five-memory-abilities
title: LongMemEval 五类核心长期记忆能力
status: accepted
card_type: taxonomy
tags:
- long-term-memory
- evaluation-taxonomy
- memory-abilities
created_time: 2026-06-12 19:00:00+08:00
edited_time: 2026-06-12 19:00:00+08:00
edited_entity: llm
source_ids:
- repo-longmemeval
evidence_basis: code_implementation
justification: ../justification/longmemeval-five-memory-abilities.md
canonical_concept: longmemeval-five-memory-abilities
aliases:
- five core long-term memory abilities
- 五种记忆能力
- question_type
summary: 'LongMemEval (longmemeval-five-memory-abilities) 定义五类核心长期记忆能力: Information Extraction (single-session-user/assistant/preference), Multi-Session Reasoning (multi-session), Knowledge Updates (knowledge-update),
  Temporal Reasoning (temporal-reasoning), Abstention (question_id 以 _abs 结尾). question_type 字段映射内部任务名到官方能力名.'
related:
- longmemeval-benchmark-overview
- longmemeval-dataset-variants
---
LongMemEval 定义了五种核心长期记忆能力，每种对应不同的 question_type 字段值。[^src-1]

**Information Extraction（信息抽取）**: 从单一会话中提取用户陈述的事实。对应 question_type: `single-session-user`（用户显式陈述）、`single-session-assistant`（助手先前信息）、`single-session-preference`（用户偏好）。[^src-2]

**Multi-Session Reasoning（多会话推理）**: 需要跨多个会话综合推理才能回答。对应 question_type: `multi-session`。内部任务名为 `two_hop` 和 `multi_session_synthesis`。[^src-3]

**Knowledge Updates（知识更新）**: 识别用户知识的更新，给出最新答案而非过时信息。对应 question_type: `knowledge-update`。[^src-2]

**Temporal Reasoning（时间推理）**: 需要理解事件时间关系才能回答。对应 question_type: `temporal-reasoning`。内部任务名为 `temp_reasoning_implicit` 和 `temp_reasoning_explicit`。[^src-3]

**Abstention（拒答）**: 问题涉及不存在于历史中的信息，系统应拒绝回答。识别方式为 question_id 以 `_abs` 结尾。评测时跳过这 30 个 abstention 实例的检索评估，因为它们没有 ground truth 答案位置。[^src-4]

[^src-1]: data/raw/github_repo/repo-longmemeval/repo/README.md -- "LongMemEval Overview" P2 -- "We release 500 high quality questions to test five core long-term memory abilities: Information Extraction, Multi-Session Reasoning, Knowledge Updates, Temporal Reasoning, Abstention"
[^src-2]: data/raw/github_repo/repo-longmemeval/repo/README.md -- "Dataset Format" P2 -- "question_type: one of single-session-user, single-session-assistant, single-session-preference, temporal-reasoning, knowledge-update, and multi-session"
[^src-3]: data/raw/github_repo/repo-longmemeval/repo/README.md -- "Creating Custom Chat Histories" P2 -- task name mapping table
[^src-4]: data/raw/github_repo/repo-longmemeval/repo/README.md -- "Baseline Retrieval" P2 -- "for evaluating the retrieval, we always skip the 30 abstention instances"

[^card-1]: longmemeval-benchmark-overview -- 基准整体定位与五类能力的上层描述
