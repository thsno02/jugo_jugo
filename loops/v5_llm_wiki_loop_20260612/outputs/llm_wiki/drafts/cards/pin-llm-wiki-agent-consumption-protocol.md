---
id: pin-llm-wiki-agent-consumption-protocol
title: pin-llm-wiki Agent 消费协议
status: draft
card_type: behavioral-protocol
tags: [agent-behavior, wiki-consumption, AGENTS.md, wikilinks]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-ndjordjevic-pin-llm-wiki]
evidence_basis: code_implementation
justification: ../justification/pin-llm-wiki-agent-consumption-protocol.md
canonical_concept: pin-llm-wiki-agent-consumption-protocol
aliases: [AGENTS.md protocol, agent wiki consumption, wiki agent behavior]
summary: >-
  pin-llm-wiki 生成的 AGENTS.md 定义 agent 消费协议: 回答前先读 wiki/index.md,
  沿 [[wikilinks]] 跳转相关源页, 答案中引用 wiki 页名, wiki 无答案时明说并在线获取,
  不自动 git commit/push。定位为可审查知识工作流(reviewable knowledge workflow),
  非无人值守发布系统, 大 fetch 有 token guard。
related: [pin-llm-wiki-architecture, karpathy-llm-wiki-pattern-automation]
---

pin-llm-wiki 生成的每个 wiki 均包含 AGENTS.md，定义 AI agent 与知识库交互的行为协议 [^src-1] [^card-1]：

1. **先查后答**：回答领域问题前必须先读 wiki/index.md
2. **链接导航**：沿 `[[wikilinks]]` 跳转至相关源页面获取细节
3. **引用标注**：答案中引用 wiki 页面名称作为出处
4. **诚实边界**：wiki 不包含答案时需明确告知用户，再在线获取当前信息
5. **操作克制**：不自动执行 `git commit` 或 `git push`，除非人类明确要求

该工具明确将自身定位为"可审查知识工作流"（reviewable knowledge workflow），而非无人值守发布系统 [^src-2]。生成页面需在 git diff 中人工审查，大型 fetch 设有 token guard，lint Phase 1 推迟矛盾检测与术语碰撞检查。

[^src-1]: `data/raw/github_repo/repo-ndjordjevic-pin-llm-wiki/repo/README.md` -- "Agent behavior" P116-123 -- "Read wiki/index.md before answering domain questions. Follow [[wikilinks]] into relevant source pages. Cite wiki page names in answers."
[^src-2]: `data/raw/github_repo/repo-ndjordjevic-pin-llm-wiki/repo/README.md` -- "Limits" P126-128 -- "This is a reviewable knowledge workflow, not an unattended publishing system."
[^card-1]: pin-llm-wiki-architecture
