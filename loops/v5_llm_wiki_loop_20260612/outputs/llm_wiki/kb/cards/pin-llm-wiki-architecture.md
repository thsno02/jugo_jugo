---
id: pin-llm-wiki-architecture
title: pin-llm-wiki 四层架构
status: accepted
card_type: system-architecture
tags:
- knowledge-base
- wiki-architecture
- raw-capture
- agent-memory
created_time: 2026-06-12 19:00:00+08:00
edited_time: 2026-06-12 19:00:00+08:00
edited_entity: llm
source_ids:
- repo-ndjordjevic-pin-llm-wiki
evidence_basis: code_implementation
justification: ../justification/pin-llm-wiki-architecture.md
canonical_concept: pin-llm-wiki-architecture
aliases:
- pin-llm-wiki structure
- pin-llm-wiki layers
- pin-llm-wiki 目录结构
summary: 'pin-llm-wiki 四层架构: raw/(不可变原始捕获 github/youtube/web), wiki/(摘要+wikilinks+引用回溯raw, 含 index.md/overview.md/log.md/sources/), AGENTS.md(agent行为规范), inbox.md(人/agent投递队列)。 结果为 repo-local memory layer,
  可 git 审查, agent 可查询。'
related:
- karpathy-llm-wiki-pattern-automation
- pin-llm-wiki-agent-consumption-protocol
---

pin-llm-wiki 将外部源转化为持久知识库，采用四层架构 [^src-1]：

1. **raw/**：不可变原始捕获层。按源类型分子目录（github/ youtube/ web/），保留源内容原貌以确保可溯源性。
2. **wiki/**：精炼知识层。包含 index.md（入口+全源列表）、overview.md（滚动跨源综合）、log.md（append-only 操作历史）、sources/（每源一页，含引用回溯 raw）、.archive/（软删除）。页面使用 `[[wikilinks]]` 交叉引用。
3. **AGENTS.md**：agent 操作手册。指导 AI agent 如何消费 wiki 内容。
4. **inbox.md**：源队列。人类或 agent 可将 URL 投入 `## Pending` 区，等待后续 ingest 处理。

整体产出为 repo-local memory layer：在 git 中可审查，agent 可查询，减少对单次 chat context 容量的依赖 [^src-2]。

[^src-1]: `data/raw/github_repo/repo-ndjordjevic-pin-llm-wiki/repo/README.md` -- "What gets created" P79-94 -- "inbox.md source queue; .pin-llm-wiki.yml config; AGENTS.md canonical instructions; wiki/ ... raw/"
[^src-2]: `data/raw/github_repo/repo-ndjordjevic-pin-llm-wiki/repo/README.md` -- "Why use it" P8-16 -- "The result is a repo-local memory layer: reviewable in git, queryable by agents, and less dependent on whatever context happens to fit in one chat."
