---
id: longmemeval-haystack-sampling-pipeline
title: LongMemEval Haystack Sampling 对话历史构建管道
status: draft
card_type: methodology
tags: [benchmark-construction, needle-in-haystack, chat-history, data-pipeline]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
evidence_basis: experimental_paper
justification: ../justification/longmemeval-haystack-sampling-pipeline.md
canonical_concept: longmemeval-haystack-sampling
aliases: [haystack sampling, evidence session construction, 对话历史编译管道]
summary: >-
  longmemeval-haystack-sampling 是 LongMemEval 构建可扩展对话历史的三阶段管道：session pool 构建（从 ShareGPT 25%、UltraChat 25%、模拟会话 50% 混合）、session sampling（随机抽样并与 evidence sessions 混洗）、timestamp resolution（基于 evidence session 预定义时间戳作为锚点分配时间或随机分配在 2023 年 5 月）。Evidence session 通过 self-chat 构建，指示用户 LLM 间接传达 evidence statement，约 70% 经人工编辑。类比 needle-in-a-haystack 测试但更具挑战性：需从多个扩展证据会话中检索和综合信息。
related: [longmemeval-benchmark-overview, longmemeval-five-core-memory-abilities]
---

LongMemEval 的对话历史构建类比 needle-in-a-haystack 测试，但更具挑战性——需从多个扩展证据会话（而非简单短句）中检索和综合信息。[^src-1]

**Evidence Session 构建**：
- 使用 Llama 3 70B Instruct 通过 self-chat 模拟，指示用户 LLM 间接传达 evidence statement
- 关键指令：(1) 间接提供 evidence statement (2) 消息简洁模拟真实用户风格
- 最多模拟 10 轮对话
- 约 70% 的 session 经人工编辑以确保质量[^src-2]

**历史编译三阶段管道**：
1. Session Pool 构建：从三个来源混合——ShareGPT 25%、UltraChat 25%、基于其他属性模拟的会话 50%
2. Session Sampling：随机抽样并与问题的 evidence sessions 混洗
3. Timestamp Resolution：以 evidence session 预定义时间戳为锚点确定范围，否则随机分配在 2023 年 5 月[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/3_benchmark.tex" -- "LongMemEval is more challenging and realistic as it involves retrieving and synthesizing information from multiple extended evidence sessions"
[^src-2]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/appendix.tex" Section "Evidence Session Construction" -- "roughly 70% of the sessions are human edited"
[^src-3]: `data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` -- "text/appendix.tex" Section "History Construction" -- "25% ShareGPT, 25% UltraChat, and 50% simulated sessions"
